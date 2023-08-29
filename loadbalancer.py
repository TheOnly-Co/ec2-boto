import boto3
lb_east = boto3.client('elbv2', region_name='us-east-1')
client = boto3.client('elbv2')

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
