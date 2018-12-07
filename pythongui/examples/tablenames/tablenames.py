import sqlite3 as s3


connection = s3.connect('toolhouse.db')
result = connection.execute('PRAGMA table_info(product)')
for row in result:
    print (row)

# another way

result = connection. execute('select * from product')
column_names = [name[0] for name in result.description]

## bingo baby

print (column_names)
print(column_names[0])