import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

def s3_upload(bucketname, objectname, filename , region="us-east-1"):
    
    
    if objectname is None:
        objectname = os.path.basename(filename)
    
    s3 = boto3.client("s3")
    
    try:
        print(f"uploanding object{bucketname}")
        s3.upload_file(filename, bucketname, objectname)
        print("upload is successful")
        return True
    except FileNotFoundError:
        print("file not found")
        return False
    except NoCredentialsError:
        print("AWS credentials are not available")
        return False
    except ClientError as e:
        print(f"unexpected error --->>>> {e}")
        return False
    

def s3_object_delete(bucketname, objectname , region="us-east-1"):
    if not objectname:
        print("no object is available")
        objectname = os.path.basename(filename)
        
    s3 =boto3.client("s3")
        
    try:
        s3.delete_object(Bucket=bucketname, Key=objectname)
        print("successfully delete")
    except ClientError as e:
        print(e)
        return False
if __name__ == "__main__":
    filename = "1.jpeg"
    objectname = None
    bucketname = "gaosadoten"
    if s3_upload(bucketname, objectname, filename) is True:
        s3_object_delete(bucketname, objectname)