def check_csv_file_existence(bucket_name, key):
    # Initialize S3 client with credentials
    s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', region_name='')

    try:
        # Check if the file exists in S3
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except:
        return False


import boto3
import csv 
import os
# call s3 bucket
BUCKET_NAME='tredenceset'
example_prefix = 'test_s3_working_part2'
s3 = boto3.resource('s3',aws_access_key_id='', aws_secret_access_key='', region_name='us-east-1')
bucket = s3.Bucket(BUCKET_NAME) # Enter your bucket name, e.g 'Data'
current_date = datetime.utcnow().strftime("%Y-%m-%d")
# key path, e.g.'customer_profile/Reddit_Historical_Data.csv'
key = f"{example_prefix}/{current_date}/data5.csv"

def append_or_create_csv(file_path, header, row):
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header if the file is created now or doesn't exist
        if not file_exists:
            writer.writerow(header)

        # Write the row to the CSV file
        writer.writerow(row)


def lambda_handler():
    # download s3 csv file to lambda tmp folder
    local_file_name = '/tmp/test.csv' #
    check_file=check_csv_file_existence(BUCKET_NAME, key)
    if (check_file):
      s3.Bucket(BUCKET_NAME).download_file(key,local_file_name)
    # list you want to append
    listdata = ['Hola',123,321,31,'Bhola']
    header=['A','B','C','D','E']
    append_or_create_csv(local_file_name, header, listdata)
    bucket.upload_file('/tmp/test.csv', key)
    os.remove(local_file_name)
    return {
        'message': 'success!!'
    }

lambda_handler()