FROM python:3.6-alpine
WORKDIR /app
COPY . /app 
CMD ["python", "./actual_game.py"]

