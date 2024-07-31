FROM python:3.9-slim

RUN pip install awscli boto3 

WORKDIR /app 

COPY copy_s3_data.py /app

CMD ["python","copy_s3_data.py"]