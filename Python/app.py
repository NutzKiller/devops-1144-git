# import boto3
# import json
# import os

# ec2_client=boto3.client("ec2")
# regions = ec2_client.describe_regions()['regions']
# for region in regions:
#   region_name = region['RegionName']
#   print(f"Instances in region: {region_name}")
#   ec2 = boto3.client('ec2', region_name=region_name)
#   instances = ec2.describe_instances()
#   for reservation in instances['Reservations']:
#     for instance in reservation['Instances']:
#       print(f"Instances ID: {instance['InstanceId']}")

#   s3=boto3.resource('s3')
#   for bucket in s3.buckets.all():
#     print(bucket.name)
#     print(instance)
#     print('------------------')
#     print('------------------')
#     print('------------------')


import boto3

def list_all_instances():
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    all_instances = []
    
    for region in regions:
        print(f"Checking region: {region}")
        regional_client = boto3.client('ec2', region_name=region)
        response = regional_client.describe_instances()
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_info = {
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'Type': instance['InstanceType'],
                    'Region': region,
                    'LaunchTime': instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S'),
                    'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                    'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A')
                }
                all_instances.append(instance_info)
    
    if all_instances:
        print("\nAWS EC2 Instances:")
        for instance in all_instances:
            print(f"- ID: {instance['InstanceId']} | State: {instance['State']} | "
                  f"Type: {instance['Type']} | Region: {instance['Region']} | "
                  f"LaunchTime: {instance['LaunchTime']} | PublicIP: {instance['PublicIpAddress']} | "
                  f"PrivateIP: {instance['PrivateIpAddress']}")
    else:
        print("No instances found in any region.")

if __name__ == "__main__":
    list_all_instances()
