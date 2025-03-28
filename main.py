import sys
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from models import Product
from dao import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('product.ui',self)

        self.showProduct()

     #signal & slot 
        self.btnInsert.clicked.connect(self.insertProduct)
        self.TBproduct.cellClicked.connect(self.selectedRow)
        self.btnUpdate.clicked.connect(self.updateProduct)
        self.btnDelete.clicked.connect(self.deleteProduct)
        self.btnSearch.clicked.connect(self.searchProduct)


    def searchProduct(self):
        search = self.txtSearch.text()
        products = select_by_Name(search)
        self.add_product_to_table(products)

    def add_product_to_table(self, products):
        if len(products)>0:
          self.TBproduct.setRowCount(len(products))
          row = 0 
          for product in products:
             self.TBproduct.setItem(row,0, QTableWidgetItem(str(product.id)))
             self.TBproduct.setItem(row,1, QTableWidgetItem(str(product.name)))
             self.TBproduct.setItem(row,2, QTableWidgetItem(str(product.price)))
             self.TBproduct.setItem(row,3, QTableWidgetItem(str(product.product_type)))

             row += 1

        else:
         self.TBproduct.removeRow(0)

    def showProduct(self):
      products = select()
      if len(products)>0:
          self.TBproduct.setRowCount(len(products))
          row = 0 
          for product in products:
             self.TBproduct.setItem(row,0, QTableWidgetItem(str(product.id)))
             self.TBproduct.setItem(row,1, QTableWidgetItem(str(product.name)))
             self.TBproduct.setItem(row,2, QTableWidgetItem(str(product.price)))
             self.TBproduct.setItem(row,3, QTableWidgetItem(str(product.product_type)))

             row += 1

      else:
        self.TBproduct.removeRow(0)
       #self.TBproduct.setRowCount(0)

    def deleteProduct(self):
        id = int(self.txtID.text())
        row = delete(id)
        if row>0:
            QMessageBox.information(self,'Information','Delete Product successful')
        else:
            QMessageBox.waring(self,'Warning','Unable to delete Product')

        self.showProduct()
        self.txtName.clear()      
        self.txtPrice.clear()     
        self.txtType.clear()   




    def insertProduct(self):
        name = self.txtName.text()
        price = int(self.txtPrice.text())
        product_type = self.txtType.text()

    
        product = Product( id=0,name=name, price=price, product_type=product_type)
        row = insert(product)
        if row>0:
            QMessageBox.information(self, 'Information', 'Insert Product successful')
            self.showProduct()
        else:
            QMessageBox.warning(self, 'Waring', 'Unable Insert Product')


        self.txtName.clear()      # เคลียร์ข้อความในช่องกรอกชื่อ
        self.txtPrice.clear()     # เคลียร์ข้อความในช่องกรอกราคา
        self.txtType.clear()      # เคลียร์ข้อความในช่องกรอกประเภทสินค้า
   
    def selectedRow(self):
       row =  self.TBproduct.currentRow()
       id = self.TBproduct.item(row, 0).text()
       name = self.TBproduct.item(row, 1).text()
       price = self.TBproduct.item(row, 2).text()
       type = self.TBproduct.item(row, 3).text()

       self.txtID.setText(id)
       self.txtName.setText(name)
       self.txtPrice.setText(price)
       self.txtType.setText(type)

       self.btnInsert.setEnabled(False)
       self.btnUpdate.setEnabled(True)
       self.btnDelete.setEnabled(True)


  

    def updateProduct(self):
        id = int(self.txtID.text())
        name = self.txtName.text()
        price = int(self.txtPrice.text())
        product_type = self.txtType.text()

     
        product = Product( id=id,name=name, price=price, product_type=product_type)
        row = update(product)

        if row>0:
            QMessageBox.information(self, 'Information', 'Update Product successful')
            self.showProduct() # รีเฟรชแสดงข้อมูลใหม่
            self.txtID.clear()  # เคลียร์ช่องกรอกข้อมูล
            self.txtName.clear()
            self.txtPrice.clear()
            self.txtType.clear()
        
        # เปิดใช้งานปุ่ม Insert หลังจากการอัพเดต
            self.btnInsert.setEnabled(True)
            self.btnUpdate.setEnabled(False)
            self.btnDelete.setEnabled(False)
        else:
            QMessageBox.warning(self, 'Waring', 'Unable to Update Product')
        self.txtName.clear()      
        self.txtPrice.clear()     
        self.txtType.clear()      
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
