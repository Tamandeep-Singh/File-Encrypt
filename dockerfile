FROM python:3.8

WORKDIR /file-encrypt

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . . 

