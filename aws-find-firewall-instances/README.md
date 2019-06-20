# Script to find all PANW firewall instances in an account

## Requirements
pip install argparse botocore boto3
    
    
## Input arguments
    
Mandatory --aws_secret_key XXXXX --aws_access_key XXXXX
Optional --aws_region eu-west-1

If --aws-region is not set the script will scan all regions. 


