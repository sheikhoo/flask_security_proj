FROM python:3.6

EXPOSE 5000

ADD . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD python app.py