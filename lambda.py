import json
import pandas as pd
import boto3
import mysql.connector
import os

s3 = boto3.client("s3")

def read_data_from_s3(event):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]
    response = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
    return response

def lambda_handler(event, context):
    response = read_data_from_s3(event)
    print(response)
    status = response['ResponseMetadata']['HTTPStatusCode']
    
    conn = mysql.connector.connect(
      host= os.environ['rds_endpoint'],
      user=os.environ['username'],
      password=os.environ['password'],
      database=os.environ['db_name']
    )
    
    if status == 200:
        test_df = pd.read_csv(response.get("Body"))
        
        for row in test_df.itertuples():
            conn.cursor().execute(os.environ['add_record'], (str(row.date), str(row.value), str(row.product), str(row.qtd)))
        conn.commit()
        
        return {
            'statusCode': status,
            'body': json.dumps("Successful S3 get_object response.")
        }
    else:
        return {
            'statusCode': status,
            'body': json.dumps("Unsuccessful S3 get_object response.")
        }
