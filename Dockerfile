FROM python:3.8

WORKDIR /app/backend

ENV PYTHONPATH=/app/

COPY . .

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["waitress-serve", "--call", "app:create_app"]
