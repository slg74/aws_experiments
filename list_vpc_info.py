import boto3
import csv
from pathlib import Path


def get_short_term_credentials() -> tuple:

    path = Path.home() / "Downloads" / "admin_user_pulumi_accessKeys.csv"

    with open(f"{path}") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            access_key_id = row[0]
            secret_access_key = row[1]

    return access_key_id, secret_access_key


def get_vpc_info():
    session = boto3.Session(region_name="us-east-2")
    ec2_client = session.client("ec2")

    # Get all VPCs
    vpcs = ec2_client.describe_vpcs()["Vpcs"]

    # Print VPC information
    for vpc in vpcs:
        vpc_id = vpc["VpcId"]
        cidr_block = vpc["CidrBlock"]
        is_default = vpc["IsDefault"]
        instance_tenancy = vpc["InstanceTenancy"]
        state = vpc["State"]

        print(f"VPC ID: {vpc_id}")
        print(f"CIDR Block: {cidr_block}")
        print(f"Is Default VPC: {is_default}")
        print(f"Instance Tenancy: {instance_tenancy}")
        print(f"State: {state}")
        print("---")


def main():
    print(get_short_term_credentials())
    get_vpc_info()


if __name__ == "__main__":
    main()
