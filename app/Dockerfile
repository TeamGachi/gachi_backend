FROM python
MAINTAINER your_name "limjung99@g.hongik.ac.kr"
RUN apt-get update -y
RUN apt-get install -y pip
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:8000"]