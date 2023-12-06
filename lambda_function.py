import snowflake.connector as sf
import os

def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()

def lambda_handler(event, context):
    user=os.environ['user']
    password=os.environ['password']
    account=os.environ['account']
    database="RAMU"
    warehouse="COMPUTE_WH"
    schema="PUBLIC"
    role="ACCOUNTADMIN"
    conn=sf.connect(user=user,password=password,account=account);


    statement_1='use warehouse '+warehouse;
    statement3="use database "+database;
    statement4="use role "+role;
    run_query(conn,statement_1)
    run_query(conn,statement3)
    run_query(conn,statement4)
    sql_query_table_creation = "CREATE  TABLE if not exists test_table123(col1 integer, col2 string,col3 timestamp default current_timestamp())"
    run_query(conn, sql_query_table_creation);
    sql_query_data_ingestion="INSERT INTO test_table123(col1, col2) VALUES    (123, 'test string1'), (456, 'test string2')"
    run_query(conn, sql_query_data_ingestion);
