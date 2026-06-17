# aws-serverless-resume-processing-system

# Event-Driven Resume Processing Pipeline on AWS

## Project Overview

This project demonstrates an event-driven serverless architecture on AWS.

When a user uploads a PDF resume to Amazon S3, an AWS Lambda function is automatically triggered through S3 Event Notifications. The Lambda function extracts file metadata, stores it in Amazon DynamoDB, publishes notifications to Amazon SNS, and logs execution details in Amazon CloudWatch.

## Architecture Diagram

<img width="912" height="589" alt="image" src="https://github.com/user-attachments/assets/2bf37eb1-ed44-49fc-b698-edc5a2e9f6be" />

---

## Workflow

1. User uploads PDF resume to Amazon S3
2. Amazon S3 generates Event Notification
3. AWS Lambda executes automatically
4. Lambda extracts file metadata
5. Metadata stored in DynamoDB
6. Notification published to SNS
7. Email delivered to subscriber
8. Execution logs stored in CloudWatch

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- AWS IAM

---

## Key Features

- Event-driven architecture
- Serverless computing
- NoSQL data storage
- Email notifications
- Monitoring and logging
- Secure IAM-based access

---

## Technologies

Python, Boto3, AWS

---

## Author

Rahul Shirode
