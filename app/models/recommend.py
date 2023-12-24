import pandas as pd
import numpy as np
import os

def create_user_profile(dict_rating, df_sim):
    df = pd.DataFrame(index=[0], columns=df_sim.columns)
    for key, value in dict_rating.items():
        df[key] = value

    df = df.T.fillna(0)
    df.rename(columns={0: "rating"}, inplace=True)

    return df

def recommend_games(df_new_user, df_sim):
    # Convert df_similarity and df_new_user to numpy arrays
    df_similarity_array = df_sim.to_numpy()
    df_new_user_array = df_new_user.to_numpy()

    # Calculate the dot product (weighted ratings)
    weighted_ratings = np.dot(df_similarity_array, df_new_user_array)

    # Normalize the ratings by dividing by the sum of similarities for each item
    sum_of_similarities = df_sim.sum(axis=1).values
    normalized_ratings = weighted_ratings / sum_of_similarities[:, np.newaxis]

    # Min-max scaling to a 0-10 range
    min_score = np.min(normalized_ratings)
    max_score = np.max(normalized_ratings)
    normalized_ratings = 10 * (normalized_ratings - min_score) / (max_score - min_score)

    # Convert the result to a DataFrame
    recommended_games_df = pd.DataFrame(
        normalized_ratings, index=df_sim.index, columns=["score"]
    )

    # Sort the recommended games in descending order
    top_recommendations = recommended_games_df.loc[df_new_user.index].sort_values(
        by="score", ascending=False
    )

    # Return the top recommendations as a DataFrame
    return top_recommendations


def get_top_recommendations(dict_rating, df_sim):
    df = pd.DataFrame(list(dict_rating.items()), columns=["name", "rating"])
    mean_value = df["rating"].mean()

    dict_rating = dict(zip(df["name"], df["rating"]))
    df_new_user = create_user_profile(dict_rating, df_sim)

    condition = (
        (df_new_user["rating"] < mean_value)
        & (df_new_user["rating"] != 0)
        & (df_new_user["rating"] < 5)
    )
    df_new_user.loc[condition, "rating"] -= mean_value

    df_recommeds = recommend_games(df_new_user, df_sim)
    rec_games = df_recommeds.loc[
        df_new_user[df_new_user.values == 0].index
    ].sort_values(by="score", ascending=False)

    return rec_games


df_sim = pd.read_csv(os.path.abspath(os.path.join("static", "boardgames_sim.csv")))
df_sim = df_sim.set_index("name")


def service_recommend(body):
    return get_top_recommendations(body, df_sim)