import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def manage_route(app):
  @app.get("/test/numpy")
  def test1():
    print(np.array([1,2,3]))

    return {
      'message': 200,
      'statusCode': 'ok',
      'data': 'test1'
    }
  
  @app.get("/test/pandas")
  def test2():
    print(pd.Series([1,2,3],index=list('abc')))

    return {
      'message': 200,
      'statusCode': 'ok',
      'data': 'test2'
    }
  
  @app.get("/test/matplotlib")
  def test3():
    plt.plot([1,2,3],[10,20,30])
    plt.show()

    return {
      'message': 200,
      'statusCode': 'ok',
      'data': 'test3'
    }