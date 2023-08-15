FROM python:3.11-bullseye

WORKDIR /users_app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
