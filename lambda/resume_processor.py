import boto3
from uuid import uuid4

# DynamoDB Resource
dynamodb = boto3.resource('dynamodb')

# Your DynamoDB table
table = dynamodb.Table('my-website-resume-upload-db')

def lambda_handler(event, context):

    for record in event['Records']:

        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_size = record['s3']['object'].get('size', 0)

        table.put_item(
            Item={
                'unique': str(uuid4()),
                'file_name': object_key,
                'bucket_name': bucket_name,
                'file_size': file_size
            }
        )

    return {
        'statusCode': 200,
        'body': 'Successfully stored file metadata in DynamoDB'
    }
