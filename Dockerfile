FROM python:3.11-alpine
WORKDIR /usr/src/app

COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "flask", "--app", "./app/main.py", "run", "--host=0.0.0.0", "-p 5001" ]
EXPOSE 5001
