FROM python:3.8.20

WORKDIR /app

COPY ./requirement.txt /app/requirement.txt

RUN pip install --no-cache-dir -r /app/requirement.txt

COPY ./App /app/App

COPY ./Model /app/Model

EXPOSE 8000

CMD [ "uvicorn", "App.server:app", "--host", "0.0.0.0", "--port", "8000" ]