class Buffalo:

    # contstructor
    def __init__(self, id, name, price):
    # attribute
        self.id = id
        self.name = name
        self.price = price


    # method
    def plowing(self):
        print(f"The buffalo named {self.name} is plowing.")
    
    def riding(self):
        print(f"The buffalo named {self.name} is been riding.")

    def selling(self):
        print(f"The buffalo named {self.name} is been selling at price {self.price}")

class RunningBuffalo(Buffalo):

    # constructor
    def __init__(self, id, name, price, speed):
        super().__init__(id, name, price)
        self.speed = speed

    # method
    def running(self):
        print(f"The buffalo {self.name} is running at speed {self.speed} km/hr")


# Instance
# normal buffalo
buffalo1 = Buffalo('K001','แดง', 20000)
buffalo2 = Buffalo('K002', 'เผือก', 15000)

print('id: ', buffalo1.id)
print('name: ', buffalo1.name)
print('price: ', buffalo1.price)

buffalo2.plowing()
buffalo2.riding()
buffalo2.selling()

print('id: ', buffalo2.id)
print('name: ', buffalo2.name)
print('price: ', buffalo2.price)

buffalo2.plowing()
buffalo2.riding()
buffalo2.selling()
# running buffal2
print("------------------------inheritance----------------------")
running_buffalo1 = RunningBuffalo('K001','ทุย', 20000, 20)
running_buffalo2 = RunningBuffalo('K002', 'กุด', 15000, 25)

print('id: ', running_buffalo1.id)
print('name: ', running_buffalo1.name)
print('price: ', running_buffalo1.price)

running_buffalo2.plowing()
running_buffalo2.riding()
running_buffalo2.selling()

print("-----------------------method inheritance-----------------------")

running_buffalo1.running()
running_buffalo2.running()
