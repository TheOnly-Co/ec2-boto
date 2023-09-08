import boto3

client = boto3.client('elbv2')

response = client.create_load_balancer(
    Name='my-load',
    Listeners=[
        {
            'Protocol': 'https',
            'LoadBalancerPort': 8080,
            'InstanceProtocol': 'string',
            'InstancePort': 8080,
            'SSLCertificateId': 'string'
        },
    ],
    AvailabilityZones=[
        'us-east-1b',
    ],
    Subnets=[
        'subnet-065dbdb78e460f4f2',
    ],
    SecurityGroups=[
        'sg-03a9b6d9353ccb94d',
    ]
)
