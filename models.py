class Product:
    def __init__(
        self, 
        id : int,
        name : str,
        price : int,
        product_type: str):
     self.id = id
     self.name = name
     self.price = price
     self.product_type = product_type   


    def __repr__(self):
       return f' <Product: {self.model}>'