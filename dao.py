from connectdb import con , cur 
from models import Product

def insert (product: Product):
    sql = 'insert into Product(name,price,product_type) values (?,?,?)'
    rs = con.execute(sql,(product.name,product.price,product.product_type))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row
    else:
        return 0 
    
def update (product:Product):
    sql = 'UPDATE Product SET name = ? ,price = ?, product_type = ? WHERE id = ?'
    rs = con.execute(sql,(product.name,product.price,product.product_type,product.id))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row
    else:
        return 0 
def delete(id: int):
    sql = 'delete from Product where id = ?'
    rs = con.execute(sql,(id,))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row 
    else:
        return 0

def select():
    sql = 'select * from Product'
    rs = con.execute(sql)
    Products = rs.fetchall()
    if Products:
        data = []
        for Prod_tuple in Products:
            id,name,price,product_type = Prod_tuple
            data.append(Product(id=id,name=name,price=price,product_type=product_type))
        return data 
    else:
        return []
    

def select_by_Name(name :str):
    sql = 'select * from Product where name like ?'
    rs = con.execute(sql, ('%' + name + '%', ))
    results = rs.fetchall()
    if results:
        data = []
        for row in results:
            id,name,price,product_type = row
            data.append(Product(id=id,name=name,price=price,product_type=product_type))
        return data 
    else:
        return []
