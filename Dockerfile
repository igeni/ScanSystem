# syntax=docker/dockerfile:1
FROM python:3.8.3
WORKDIR /code
COPY req.txt req.txt
RUN pip install -r req.txt
#EXPOSE 8000
COPY . .
CMD ["python3", "main.py"]