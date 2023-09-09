# syntax=docker/dockerfile:1

FROM python3:latest
RUN mkdir app 
WORKDIR /app

# requirements 배포 
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

