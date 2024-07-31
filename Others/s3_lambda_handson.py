import boto3 
import json 
import urllib.parse as url 

print("Lambda function triggerred") 

s3 = boto3.client("s3")

def lambda_handler(event,context):

    print(event)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = url.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding = 'utf-8')

    print(f'bucket name is {bucket_name}')
    print(f'key name is {key}')
    
    return {
        'bucket': bucket_name ,
        'key' : key
    }