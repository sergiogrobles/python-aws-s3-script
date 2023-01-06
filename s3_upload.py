def s3_buckets(file_name):
    # import AWS packages to connect to your account
    import boto3
    from botocore.exceptions import ClientError
    # import os to obtain environment variables
    import os
    
    # declare variable parameters for the boto3 client 
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    error = False

    '''
    's3': the  AWS service we want to use, you could change this if you desire a different service
    
    region_name: put the region name your bucket is located in, perferably, as close to your users as possible, to reduce latency
    
    aws_access_key_id: AWS access key id, obtained by creating an IAM user
    
    aws_secret_access_key: AWS secret access key, obtained by creating an IAM user
    
    
    It is advised to store your AWS keys in your environent variables, outside your application code, as a security measure
    '''
    try: 
        client = boto3.client('s3', region_name = 'us-east-1',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        
    # error to True, to prevent any errors and uploading of undesired files
    except ClientError:
        error = True
    
    if error == False:
        bucket_name = os.environ.get('S3_BUCKET') # grab the name of your bucket from your environment variables
        object_name = file_name

        return client.upload_file(file_name, bucket_name, object_name)