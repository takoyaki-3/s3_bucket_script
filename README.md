S3 Bucket File Deletion Script

## Project Description
This project is a Python script designed to delete all files from a specified Amazon S3 bucket. The script uses the boto3 library to interact with the S3 service and relies on environment variables for configuration. This approach ensures that sensitive information, such as AWS credentials, is not hardcoded into the script.

## Features
- Delete All Files in S3 Bucket: The script lists and deletes all files in a specified S3 bucket.
- Environment Variable Configuration: Configuration details, such as AWS credentials and S3 endpoint, are loaded from an .env file.
- Error Handling: The script includes basic error handling to manage missing credentials.

## Prerequisites
- Python 3.6 or higher
- boto3 library
- python-dotenv library
- AWS credentials with appropriate permissions to delete objects in the specified S3 bucket

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

Install required libraries:

```bash
pip install boto3 python-dotenv
```

Create a .env file:

In the root directory of the project, create a .env file and add the following environment variables:

```env
S3_ENDPOINT=<your-s3-endpoint>
AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
BUCKET_NAME=<your-bucket-name>
LOCAL_DIRECTORY=<your-local-directory>
```

Run the script:

```bash
python script.py
```

## Usage
The script will delete all files in the S3 bucket specified by the BUCKET_NAME environment variable.
Ensure you have the necessary permissions to delete objects in the S3 bucket.
The script prints the endpoint being used and the names of deleted files to the console.

## Error Handling
If AWS credentials are not available, the script will print an error message: "Credentials not available".

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
This script uses the boto3 library for AWS interactions and python-dotenv for loading environment variables.
For any issues or questions, please open an issue in the repository or contact the project maintainer.

