import json
def main(event, context):
    response = {'message': 'I am studying now.'}
    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(response)
    }

