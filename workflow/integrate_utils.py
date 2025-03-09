import boto3

def load_dyanmo_db(table_name,primary_key,value):
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1', 
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    table = dynamodb.Table(table_name)

    response = table.put_item(Item=value)

    record_id = value[primary_key]

    print(f"{record_id} record written into {table_name} successfully!!!")









