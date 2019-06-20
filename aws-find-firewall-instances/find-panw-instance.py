from __future__ import print_function
import boto3
import argparse
from botocore.exceptions import ClientError

PANW_DESCRIPTION = 'Palo Alto Networks NGFW'

def main(access_key, secret_key, aws_region):

    client = boto3.client('ec2')
    panw_instances = []
    region_list= [] #
    aws_region_list = [] # All aws regions from ec2.describe_regions
    """:type : pyboto3.ec2"""
    aws_regions = client.describe_regions()

    for aws_region_name in aws_regions['Regions']:
        aws_region_list.append(aws_region_name['RegionName'])

    #
    # Gather the regions to use.  If no region specified then we assume all regions
    # else we will check that the region in the input parameters exists and use that one.
    #

    if aws_region in aws_region_list:
            region_list.append(aws_region)

    else:
        aws_region == 'all'
        region_list.extend(aws_region_list)

    #
    # Scan the regions in the region list for ami images that match the PANW description
    #
    for region in region_list:
        print('Scanning region {}'.format(region))
        client = boto3.client('ec2', region_name = region)

        try:
            panw_images =  client.describe_images(Filters=[
                {
                    'Name': 'description',
                    'Values': [
                        PANW_DESCRIPTION
                    ]
                },
            ])
        except ClientError as error:
            print(f'error is {error}')

        ami_list = []

        for image in panw_images['Images']:
            ami_list.append(image['ImageId'])
            # print (image['ImageId'])

        try:
            for image in ami_list:
                response = client.describe_instances(Filters=[{
                    'Name': 'image-id',
                    'Values':
                        [image]

                    },
                ])
                if len(response['Reservations']) > 0 :
                    panw_instances.extend(response['Reservations'])
        except ClientError as error:
            print(error)
        except Exception as e:
            print(e)

    if len(panw_instances) > 0 :
        print('\n*** Found PANW Instances ***\n')
        print('Instance InstanceId: \t\t Availability Zone:')
        for panw_instance in panw_instances:
            dict_data = panw_instance['Instances'][0]
            print ('{} \t\t {}'.format(dict_data['InstanceId'],dict_data['Placement']['AvailabilityZone']))
    else:
        print ('No Palo Alto Networks VM Series instances found in this account')

if __name__ == '__main__':

    """
    requirements

    pip install argparse botocore boto3

    Input arguments
    Mandatory --aws_secret_key XXXXX --aws_access_key XXXXX
    Optional --aws_region eu-west-1
    """
    parser = argparse.ArgumentParser(description='Get Parameters')
    parser.add_argument('-r', '--aws_region', help='Select aws_region', default='all')
    parser.add_argument('-k', '--aws_access_key', help='AWS Key', required=True)
    parser.add_argument('-s', '--aws_secret_key', help='AWS Secret', required=True)

    args = parser.parse_args()

    access_key = args.aws_access_key
    secret_key = args.aws_secret_key
    aws_region = args.aws_region

    main(access_key, secret_key, aws_region)




