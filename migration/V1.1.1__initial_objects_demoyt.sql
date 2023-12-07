CREATE  TABLE if not exists demoytcicd.public.test_table123(col1 integer, col2 string,col3 timestamp default current_timestamp());
INSERT INTO demoytcicd.public.test_table123(col1, col2) VALUES    (123, 'test string1'), (456, 'test string2');
