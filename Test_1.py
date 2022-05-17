class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):  # 简易版
        return f'{self.name}${self.price}'
        # return self.name + '$' + str(self.price)


    def __repr__(self):  # representation
        return f'<Product({self.name},{self.price})>'

    def __add__(self, other):
        if isinstance(other, str):
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        result = []
        if isinstance(other, int):
            for i in range(other):
                result.append(self)
        return result
    def print_name(self):
        print(self.name)




class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]



if __name__=='__main__':
    p1 = Product('珍珠奶茶', 60)
    # p+'黑糖'
    p2 = Product('意大利面', 220)
    # print(p1 + p2)
    # print(p1 * 5)
    s = ShoppingCart([p1, p2])
    print(s[0])