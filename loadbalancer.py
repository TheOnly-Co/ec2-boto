import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)
client = boto3.client('elbv2', config=my_config)

response = client.create_load_balancer(
    LoadBalancerName='boto3',
    Listeners=[
        {
            'Protocol': 'http',
            'LoadBalancerPort': 8080,
            'InstanceProtocol': 'http',
            'InstancePort': 8080,
#            'SSLCertificateId': 'string'
        },
    ],
    AvailabilityZones=[
        'string',
    ],
    Subnets=[
        'string',
    ],
    SecurityGroups=[
        'string',
    ],
    Scheme='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
