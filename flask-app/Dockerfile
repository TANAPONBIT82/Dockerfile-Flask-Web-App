FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install Flask=version

RUN pip install requests

CMD python app.py