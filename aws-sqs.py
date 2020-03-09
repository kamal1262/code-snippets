#### aws sqs , intro documentation 
*#url: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html*

###### published a message to sns or sqs 
# set the aws credentials in console 

import boto3
sns = boto3.client('sns', region_name='us-west-2')
# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:us-west-2:069150672205:qualityTopic',
    Message='Hello World',
)

# Print out the response
print(response)

#-----------------------------------------------
# send a message to your phone/email using sns
# Create an SNS client
# client = boto3.client(
#     "sns",
#     aws_access_key_id="YOUR ACCES KEY",
#     aws_secret_access_key="YOUR SECRET KEY",
#     region_name="us-east-1"
# )

# Send your sms message.
client.publish(
    PhoneNumber="+60163465607",
    Message="Hi Kamal, Hello to AWS world!"
)

#---------------------------------------------
# a full example 
"""Step 3: Do actual Pub-Sub
If you need to send messages to multiple recipients, it's worthwhile to read though Amazon's docs on sending to multiple phone numbers.

The SNS service implements the Publish-Subscribe pattern, and you can use it to send messages to a topic. Here are the steps to make this work:

- Create a named topic. This is just a commuication channel to which you can subscribe phone numbers.
- Subscibe your recipients to the topic.
- Publish a message on the topic.
The python code looks something like this:
"""

import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="YOUR ACCES KEY",
    aws_secret_access_key="YOUR SECRET KEY",
    region_name=us-east-1
)

# Create the topic if it doesn't exist (this is idempotent)
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

# Add SMS Subscribers
for number in some_list_of_contacts:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=number  # <-- number who'll receive an SMS message.
    )

# Publish a message.
client.publish(Message="Good news everyone!", TopicArn=topic_arn)

# credit url: https://bradmontgomery.net/blog/sending-sms-messages-amazon-sns-and-python/
