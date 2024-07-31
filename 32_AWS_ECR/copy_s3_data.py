import boto3

def copy_s3_files(source_bucket_name, destination_bucket_name):
  """Copies all files from a source S3 bucket to a destination S3 bucket.

  Args:
    source_bucket_name: The name of the source S3 bucket.
    destination_bucket_name: The name of the destination S3 bucket.
  """
  # Create an S3 client
  s3_client = boto3.client('s3')

  # Get objects (files) from the source bucket
  paginator = s3_client.get_paginator('list_objects_v2')
  for page in paginator.paginate(Bucket=source_bucket_name):
    for obj in page.get('Contents', []):
      # Construct the destination object key (filename)
      destination_object_key = obj['Key']

      # Copy the object from source to destination
      copy_source = {'Bucket': source_bucket_name, 'Key': obj['Key']}
      s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=destination_object_key)


if __name__ == "__main__":
    # Example usage
    source_bucket_name = "awsde-202405-src"
    destination_bucket_name = "awsde-202405-dest"
    copy_s3_files(source_bucket_name, destination_bucket_name)
    print("Files copied successfully!") 
