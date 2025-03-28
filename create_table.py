from connectdb import con

sql = '''
 create table product(
 id integer primary key autoincrement,
 name text not null,
 price integer not null,
 product_type text not null);

'''
con.execute(sql)