import boto3
import os
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

endpoint_url = os.getenv('S3_ENDPOINT')
s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

print(f"Using endpoint: {endpoint_url}")

def delete_all_files(bucket_name):
    try:
        paginator = s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get('Contents', []):
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted {obj['Key']}")
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == "__main__":
    local_directory = os.getenv('LOCAL_DIRECTORY')
    bucket_name = os.getenv('BUCKET_NAME')
    delete_all_files(bucket_name)  # This line will delete all files in the bucket
