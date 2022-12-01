import config
import boto3

session = boto3.Session(
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECREY_KEY,
)

s3 = session.resource('s3')
source_dir = config.bucket_dir
destination_dir = config.dest_dir
bucket = s3.Bucket(config.bucket_name)
file = config.filename

list_of_files = []
with open('%s' %file) as list:
    for l in list:
        list_of_files.append(l.strip(',\n'))
        
for l in list_of_files:
    print('Downloading file - ', l)
    bucket.download_file(source_dir + l, destination_dir + l)
print('Done')