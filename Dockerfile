FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Set environment variables from .env during build
ARG ENV_FILE
ENV ENV_FILE=${ENV_FILE:-.env}
RUN cat $ENV_FILE | xargs -n 1 | sed 's/=.*//' | xargs -I {} sh -c 'echo export {}=\"\$"{}\" >> /etc/environment'

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV PYTHONUNBUFFERED 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
