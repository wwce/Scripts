import boto3
from botocore.exceptions import ClientError
def lambda_handler(event, context):
    client = boto3.client('ec2')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    #print(ec2_regions)
    for region in ec2_regions:
        ec2 = boto3.resource('ec2',region_name=region)
        #print(region)
        instances = ec2.instances.filter(Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']}
            ])
        #print("instances")
        #print(instances)
        #RunningInstances = [instance.id for instance in instances]
        #print("runninginstances")
        #print(RunningInstances)
        for i in instances:
            taglist = {}
            for tag in i.tags or []:
                taglist[tag['Key'].lower()] = tag['Value']
            #print("this is the tag list")
            #print(taglist)
            #print("this is the value of i before the if")
            #print(i)
            instanceid = [i.id]
            #print("instance.id")
            #print(i.id)
            if not 'donotstop' in taglist:
                #print("entering donotstop sequence")
                stoppingInstances = i.stop()
                print(f"stopping instances value {stoppingInstances}" )
                #print(stoppingInstances)
                #print("instance to stop, value of i within the if")
                #print(i)
                #print("instance name")
                instancename = " "
                for tag in i.tags or []:
                    if 'Name'in tag['Key']:
                        instancename = tag['Value']
                        #print(instancename)
                
                # Replace sender@example.com with your "From" address.
                # This address must be verified with Amazon SES.
                SENDER = "sender@email.com"

                # Replace recipient@example.com with a "To" address. 
                RECIPIENT = "recipient@email.com"

                # Specify a configuration set. If you do not want to use a configuration
                # set, comment the following variable, and the 
                # ConfigurationSetName=CONFIGURATION_SET argument below.
                #CONFIGURATION_SET = "ConfigSet"

                # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
                AWS_REGION = "us-west-2"

                # The subject line for the email.
                SUBJECT = f"{region} {instancename} Stopping Instance"

                # The email body for recipients with non-HTML email clients.
                BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                            "This email was sent with Amazon SES using the "
                            "AWS SDK for Python (Boto).\r\n"
                            f"stopped instance \n{i}\n"
                            f"stopped instance name \n{instancename}\n"
                            )
                            
                # The HTML body of the email.
                BODY_HTML = f"""<html>
                <head></head>
                <body>
                <h1>{region} {instancename} Stopping Instance</h1>
                <p>stopped instance {i} with name {instancename}</p>
                </body>
                </html>
                            """

                # The character encoding for the email.
                CHARSET = "UTF-8"

                # Create a new SES resource and specify a region.
                client = boto3.client('ses',region_name=AWS_REGION)

                # Try to send the email.
                try:
                    #Provide the contents of the email.
                    response = client.send_email(
                        Destination={
                            'ToAddresses': [
                                RECIPIENT,
                            ],
                        },
                        Message={
                            'Body': {
                                'Html': {
                                    'Charset': CHARSET,
                                    'Data': BODY_HTML,
                                },
                                'Text': {
                                    'Charset': CHARSET,
                                    'Data': BODY_TEXT,
                                },
                            },
                            'Subject': {
                                'Charset': CHARSET,
                                'Data': SUBJECT,
                            },
                        },
                        Source=SENDER,
                        # If you are not using a configuration set, comment or delete the
                        # following line
                        #ConfigurationSetName=CONFIGURATION_SET,
                    )
                # Display an error if something goes wrong.	
                except ClientError as e:
                    print(e.response['Error']['Message'])
                else:
                    resonsevar = response['MessageId']
                    print(f"Email sent! Message ID: {resonsevar}"),
                    #print(response['MessageId'])
