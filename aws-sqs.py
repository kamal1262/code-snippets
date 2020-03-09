

###### published a message to sns or sqs 

import boto3
sns = boto3.client('sns', region_name='us-west-2')
# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:us-west-2:069150672205:qualityTopic',
    Message='Hello World',
)

# Print out the response
print(response)
