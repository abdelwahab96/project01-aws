# AWS Data Pipeline Project
**This project is a hands‑on implementation I built as part of my journey to getting the AWS Data Engineer certification**
**The goal was to design and deploy an end‑to‑end data pipeline using AWS services, starting from data ingestion all the way to querying and analysis.**

**project credit:** (https://www.youtube.com/watch?v=uqXX4fsUA64&list=PLRRQG4QYcyEXf2sq2XtpfvYmXMgyfWj2g&index=1)




# 📌 **Architecture Overview**
Data Ingestion

A demo form hosted on Amazon EC2 is used to collect data.

Submitted data is stored in Amazon DynamoDB.

ETL Trigger

An AWS Lambda function is triggered whenever new data is written to DynamoDB.

Lambda extracts the data and stores it in Amazon S3 (staging layer).

Data Processing

AWS Glue crawlers and jobs are used to process and combine the staged data.

Transformed data is written back to Amazon S3 (warehouse layer).

Monitoring

Amazon CloudWatch monitors Glue logs and provides visibility into processing.

Query and Analysis

Amazon Athena is used to query the processed data directly from S3 for analysis.





## ⚙️ Technologies & Services
- Amazon EC2 – Hosting the demo form

- Amazon DynamoDB – NoSQL database for form submissions

- AWS Lambda – Serverless trigger for data extraction

- Amazon S3 – Staging & warehouse layers

- AWS Glue – ETL and data transformation

- Amazon CloudWatch – Monitoring logs and changes

- Amazon Athena – Serverless SQL querying





### How to Run
⚠️ You will need an AWS account and proper IAM permissions for EC2, DynamoDB, cloudwatch, Lambda, S3, Glue, and Athena.

- Deploy the form on EC2

- Launch an EC2 instance and run your demo form app. using run.app

- Set up DynamoDB

- Create a table for form submissions.

- Configure Lambda

- Use the lambda/lambda_fnc.py code.

- Set DynamoDB Streams to trigger the Lambda.

- Prepare S3 buckets

- Create a bucket for staging and another for the warehouse layer.

- Set up Glue

- Create a crawler and job using glue_etl_v1.py.

- Run the job to process and combine data.

- Monitor with CloudWatch

- View Glue logs in CloudWatch for debugging.

- Query with Athena

- Point Athena to your processed data in S3 and start running SQL queries.




## 🌱 Why This Project
This project is a practical step to solidify the concepts I’ve been learning while preparing for the AWS Certified Data Engineer certification.
It demonstrates:

Event‑driven architecture with Lambda

Serverless data pipelines

Orchestration and monitoring on AWS



