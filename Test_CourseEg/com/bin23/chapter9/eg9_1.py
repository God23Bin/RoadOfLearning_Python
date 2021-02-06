class Product:
    id = 0
    def __init__(self,name,color,price,weight):
        Product.id = Product.id + 1
        self.name = name
        self.color = color
        self.price = price
        self.weight = weight
        print('一产品已经被生产，其ID是' + str(Product.id))

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

class Computer(Product):
    def __init__(self,name,color,price,weight,memory,disk,processor):
        super(Computer, self).__init__(name,color,price,weight)
        self.memory = memory
        self.disk = disk
        self.processor = processor
        print('一电脑已被生产，其名字为', name)

class MobilePhone(Product):
    def __init__(self,name,color,price,weight,generation,networkstandard):
        super(MobilePhone, self).__init__(name,color,price,weight)
        self.generation = generation
        self.networkstandard = networkstandard
        print('一移动手机已被生产，其名字为', name)

def main():
    c = Computer("宏碁笔记本电脑", "黑色", 5800, "2kg", '8192K', '500G', 'Intel')
    m = MobilePhone("Honor", '蓝色', 1998, '0.3kg', '4G', 'TD')
    print("产品名称：" + c.name + "，产品价格：" + str(c.getPrice()))
    print("产品名称：" + m.name + "，产品价格：" + str(m.getPrice()))

if __name__ == '__main__':
    main()