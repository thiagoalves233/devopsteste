# Dockerfile
FROM python:3.9

WORKDIR /app

COPY monitor_process.py .

RUN pip install psutil

ENTRYPOINT ["python", "monitor_process.py"]
