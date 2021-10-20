FROM python:3.8.5

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY ./backend .
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
