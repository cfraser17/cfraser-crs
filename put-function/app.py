import json
import boto3

#sets "dynamodb" variable to initialize the boto3 resource
dynamodb = boto3.resource('dynamodb')

#sets "table" variable to initialize the dynamodb variable from earler with the .Table method to access the crs-visitors table
table = dynamodb.Table('crs-visitors-v2')

def lambda_handler(event, context):
    #sets "response" variable to access 'crs-visitors' 
    response = table.get_item(Key={
            'ID':'0'
    })
    #sets variable 'record_count' to be the value of the variable 'repsonse'
    record_count = response['Item']['visitors']
    #sets 'record_count' to be itself + 1
    record_count = record_count + 1
    #prints value of 'record_count'
    print(record_count)
    #changes the variable 'response' to now put the value of 'record_count' into the visitors table
    response = table.put_item(Item={
            'ID':'0',
            'visitors': record_count
    })
    
    return {
        #return status code 200 "OKAY"
        'statusCode': 200,
        
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(str(record_count))
    }