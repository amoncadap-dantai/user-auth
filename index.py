def handler(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "Hello from user-auth", "authenticated": true}'
    }