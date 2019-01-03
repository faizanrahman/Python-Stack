class Product:
    def __init__(self,price,item_name,weight,brand):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status="For sale"
        
    def sell(self):
        self.status = "Sold"
        return self
    
    def addTax(self,tax):
        self.tax=tax
        return self.price + self.price * tax
        
    def returnItem(self,reason_for_return):
        self.reason_for_return = reason_for_return
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "For sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price * 0.80
        return self
        
    def displayInfo(self):
        print(self.price)
        print(self.item_name)
        print(self.weight)
        print(self.brand)
        print(self.status)
        return self
        

p1=Product(100,"iphone","1 lbs","Apple")

#print(p1.price)
#print(p1.item_name)
#print(p1.weight)
#print(p1.brand)
#print(p1.status)

#print(p1.addTax(0.15))
#p1.sell()
#print(p1.status)

#print(p1.returnItem("defective"))
#print(p1.returnItem("like_new"))
#print(p1.returnItem("opened"))



p1.displayInfo()
        