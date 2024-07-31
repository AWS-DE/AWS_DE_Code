import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the batch get request
response = dynamodb.batch_get_item(
    RequestItems={
        'user': {
            'Keys': [
                {'user_id': {'S': 'john_123'}} 
            ]
        }
    }
)


# Process the response
for item in response['Responses']['user']:
    print(item)
