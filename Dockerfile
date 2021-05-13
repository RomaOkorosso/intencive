FROM python:3.9

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn main:app --reload  --port 8001 --host 0.0.0.0