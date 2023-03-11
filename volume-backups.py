import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-central-1")


def create_vol_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )['Volumes']
    for volume in volumes:
        new_snapshot = ec2_client.create_snapshot(
            volumeId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every().day.do(create_vol_snapshots)

while True:
    schedule.run_pending()