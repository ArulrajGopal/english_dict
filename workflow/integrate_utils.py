from Credentials import *
import boto3

def load_dyanmo_db(table_name,value):
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1', 
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    table = dynamodb.Table(table_name)

    response = table.put_item(Item=value)

    print(f"Write Successful into {table_name}")









