import boto3



response = s3.list_objects_v2(Bucket='awsde-202405')
for obj in response.get('Contents', []):
    print(obj['Key'])
