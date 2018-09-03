# AWS SAM sample - create API Gateway & Lambda
I study AWS SAM.
NOW I use AWS SAM and create AWS Resources(API Gateway & Lambda)

# WHY
I wanted to use AWS SAM.
This time I study and use AWS SAM.
First step, Lambda returns HTML and I can watch the browser.

# STRUCTURE
[Client Brower] ->(HTTP)-> [API Gateway] -> [Lambda] >(return '<html><body>I am studying now.</body></html>) -> [API Gateway] ->(HTTP)-> [Client Browser]

# OPERATION CONFIRM
When you operate this program, you need to change the configuration files.

(1) AWSSAM-Parent.yml Line:16 "<<S3 BucketName>>"
    You must create S3 Bucket.
    And you replace BucketName.

(2) AWSSAM-Parent.yml Line:84 "x.x.x.x/32"
    If you want to limit the IP Address, you must to replace "x.x.x.x/32".
    If you don't want to limit the IP Address, you delete the word "Condition:  IpAddress: aws:SourceIp:  - "x.x.x.x/32".

(3) AWSSAM-Child.yml Line:9 "mailaddress"
    You must replace the your e-mail address.

## AWS Resource
- API Gateway
- AWS Lambda
- Amazon SNS
- IAM Policy
- IAM Role
