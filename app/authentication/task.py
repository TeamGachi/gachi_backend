from celery import Celery
from rest_framework.request import Request
from django.core.mail import EmailMessage

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def send_email(email: str) -> None:
    subject = "축하합니다!"
    to = [email]
    from_email = "limjung99@gmail.com"
    message = "축하합니다 회원가입에 성공하셨습니다."
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
