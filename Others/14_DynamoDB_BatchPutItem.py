import boto3
import time
import random

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the items to write
items_to_write = [
    {'user_id': {'S': 'abe_123'}, 'name': {'S': 'Abhi'}, 'Age': {'N': '30'}},
    {'user_id': {'S': 'hanvi_256'}, 'name': {'S': 'Hanvi'}, 'content': {'S': '20'}}
]


item = {
                    'user': [
                        {
                            'PutRequest': {
                                'Item': item
                            }
                        } for item in items_to_write
                    ]
                }

print("***********************************")
print(item)
print("***********************************")

def batch_write_with_backoff(items):
    max_retries = 5
    base_delay = 1  # seconds

    for attempt in range(max_retries):
        try:
            # Create batch write request
            response = dynamodb.batch_write_item(
                RequestItems={
                    'user': [
                        {
                            'PutRequest': {
                                'Item': item
                            }
                        } for item in items
                    ]
                }
            )
            
            # Check for unprocessed items
            if 'UnprocessedItems' in response and response['UnprocessedItems']:
                print("Unprocessed items found, retrying...")
                items = response['UnprocessedItems']['user']
                raise Exception("Unprocessed items, retrying...")
            
            # If no unprocessed items, break the loop
            break
        
        except Exception as e:
            wait_time = base_delay * (2 ** attempt)
            print(e)
            wait_time_with_jitter = wait_time + random.uniform(0, base_delay)
            print(f"Attempt {attempt + 1} failed, retrying in {wait_time_with_jitter:.2f} seconds...")
            time.sleep(wait_time_with_jitter)

# Execute the batch write with exponential backoff
batch_write_with_backoff(items_to_write)