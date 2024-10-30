import boto3
import os

region = 'us-east-2'
instance = ['i-0f3e2beca56dc6fd9']
ec2 = boto3.client('ec2', region_name=region)
# status = bool(os.environ["STATUS"])

def lambda_handler(event, context):

    status = eval(event["status"])

    if status:
        print('start your instances: ' + str(instance))
        ec2.start_instances(InstanceIds=instance)
    else:
        print('stopped your instances: ' + str(instance))
        ec2.stop_instances(InstanceIds=instances)