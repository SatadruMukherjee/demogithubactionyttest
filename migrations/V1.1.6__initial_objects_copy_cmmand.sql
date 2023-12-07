create or replace table demoytcicd.public.sample_test (ChartIdentifier varchar(200) ,PdfFileName varchar(200) ,chase_dxclass varchar(1000));

--create the file format
create or replace file format demoytcicd.public.my_csv_format
type = csv field_delimiter = ',' skip_header = 1
field_optionally_enclosed_by = '"'
null_if = ('NULL', 'null') 
empty_field_as_null = true;

--create the external stage
create or replace stage demoytcicd.public.Snow_stage url="s3://normaldatapoint/" 
credentials=(aws_key_id='AKIA4ASLMUJLT4BUQD3B'
aws_secret_key='VDDcs71tVAjyqvcrE6cUJnf0Hfo/Ikis0KsPQ58y')
file_format = my_csv_format;

copy into demoytcicd.public.sample_test from 
@demoytcicd.PUBLIC.Snow_stage FILE_FORMAT=(FORMAT_NAME=my_csv_format);
