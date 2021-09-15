# Witalo Andrade - 2020/04/11
# This lambda will simply gerenerate a random number and will
# Publish as a value to cloud watch
import boto3
import random
cloudwatch = boto3.client('cloudwatch')
response = cloudwatch.put_metric_data(
MetricData = [
    {
        'MetricName': 'KPIs',
        'Dimensions': [
            {
                'Name': 'PURCHASE_SERVICE',
                'Value': 'CoolService'
            },
            {
                'Name': 'APP_VERSION',
                'Value': '1.0'
            },
        ],
        'Unit': 'None',
        'Value': random.randint(1,100)
    },
],
Namespace = 'CoolApp'
)
print (response)
