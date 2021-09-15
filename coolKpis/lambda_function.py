import boto3
import random

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    value = random.randint(1, 100)
    print(value)
    response = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'KPIs',
                'Dimensions': [
                    {
                        'Name': 'PURCHASES_SERVICE',
                        'Value': 'CoolService'
                    },
                    {
                        'Name': 'APP_VERSION',
                        'Value': '2.0'
                    },
                ],
                'Unit': 'None',
                'Value': value
            },
        ],
        Namespace = 'CoolApp'
    )
    return value, response