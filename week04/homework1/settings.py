# Database configs
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 3306
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'

# Statements one
STATEMENTS_ONE = {
    '1': 'SELECT * FROM data;',
    '2': 'SELECT * FROM data LIMIT 10;',
    '3': 'SELECT id FROM data;',
    '4': 'SELECT COUNT(id) FROM data;',
    '5': 'SELECT * FROM data WHERE id<1000 AND age>30;',
}

# Statement two
STATEMENTS_TWO = {
    '6': 'SELECT id,COUNT(DISTINCT order_id) FROM data1 GROUP BY id;',
    '7': 'SELECT * FROM data1 d1 INNER JOIN data2 d2 ON d1.id = d2.id;',
    '8': 'SELECT * FROM data1 UNION SELECT * FROM data2;',
    '9': 'DELETE FROM data1 WHERE id=\"CA001\";',
    '10': 'ALTER TABLE data1 DROP COLUMN column_name;'
}