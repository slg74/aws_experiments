import boto3
import csv
import os

from pathlib import Path


def get_iam_credentials() -> tuple:

    path = Path.home() / "Downloads" / "admin_user_pulumi_accessKeys.csv"

    with open(f"{path}") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            access_key_id = row[0]
            secret_access_key = row[1]

    return access_key_id, secret_access_key


def set_iam_credentials():
    session = boto3.Session(region_name="us-east-2")
    iam_client = session.client("iam")
    access_key_id, secret_access_key = get_iam_credentials()
    os.environ["AWS_ACCESS_KEY_ID"] = access_key_id
    os.environ["AWS_SECRET_ACCESS_KEY"] = secret_access_key


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


def get_subnet_info():
    session = boto3.Session(region_name="us-east-2")
    ec2_client = session.client("ec2")

    # Get all subnets
    subnets = ec2_client.describe_subnets()["Subnets"]

    # Print subnet information
    for subnet in subnets:
        subnet_id = subnet["SubnetId"]
        vpc_id = subnet["VpcId"]
        cidr_block = subnet["CidrBlock"]
        availability_zone = subnet["AvailabilityZone"]
        state = subnet["State"]

        print(f"Subnet ID: {subnet_id}")
        print(f"VPC ID: {vpc_id}")
        print(f"CIDR Block: {cidr_block}")
        print(f"Availability Zone: {availability_zone}")
        print(f"State: {state}")
        print("---")


def main():
    get_iam_credentials()
    set_iam_credentials()
    get_vpc_info()
    get_subnet_info()


if __name__ == "__main__":
    main()
