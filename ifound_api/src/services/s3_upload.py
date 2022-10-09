import boto3
from sqlalchemy.orm import Session
from fastapi import UploadFile, File
import re
import os


def post_file_on_s3(bucket_name, bucket_path, path, filename):
    #aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
    #aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    s3 = boto3.resource('s3') #, aws_access_key_id, aws_secret_access_key)
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object(bucket_path) 

    with open(path, 'rb') as data:
	    obj.upload_fileobj(data, ExtraArgs={'ACL':'public-read'})


    for object_summary in bucket.objects.filter(Prefix="courses/"):
        if filename in object_summary.key:
            url_content = 'https://stm-public.s3.amazonaws.com/'+object_summary.key
            return url_content