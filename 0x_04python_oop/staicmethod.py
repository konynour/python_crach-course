class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def PI():
        return 3.14

x = Math.add(5, 10)  
y = Math.add5(x)     
z = Math.add10(y)    

print(x, y, z)  
