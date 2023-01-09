# app/Dockerfile

FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

COPY ./src /app/src
COPY ./resources /app/resources
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["streamlit", "run", "src/index.py", "--server.port=8501", "--server.address=0.0.0.0"]
