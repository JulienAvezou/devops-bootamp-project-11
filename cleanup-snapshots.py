import boto3
import schedule

from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")


def clean_up_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )['Volumes']

    for volume in volumes:
        snapshots = ec2_client.describe_snapshots(
            OwnerIds=['self'],
            Filters=[
                {
                    'Name': 'volume-id',
                    'Values': [volume['VolumeId']]
                }
            ]
        )['Snapshots']

        snapshots_sorted_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)

        for snap in snapshots_sorted_by_date[2:]:
            res = ec2_client.delete_snapshot(
                SnapshotId=snap['SnapshotId']
            )
            print(res)


schedule.every().day.do(clean_up_snapshots)

while True:
    schedule.run_pending()

