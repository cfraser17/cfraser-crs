import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crs-visitors-v2')

def lambda_handler(event, context):
    #defines "response" to be the output of the method "get_item"
    response = table.get_item(Key={
       'ID':'0'
    })
    #returns the "response" value of the row "record_count"
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(str(response['Item']['visitors']))
    }