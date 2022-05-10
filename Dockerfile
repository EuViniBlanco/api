FROM python:3.10.4
WORKDIR /api
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY  . .
EXPOSE 8086