FROM python:3.9

RUN mkdir -p /usr/src/intencive

WORKDIR /usr/src/intencive

COPY . /usr/src/intencive
RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn main:app --reload --host 0.0.0.0 --port ${PORT}