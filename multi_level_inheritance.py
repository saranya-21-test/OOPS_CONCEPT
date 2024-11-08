class granpa:
    def method1(self):
        print("parent method")

class father(granpa):
    def method2(self):
        print("child method")

class son(father):
    def method3(self):
        print("sub child method")

obj=son()
obj.method1()
obj.method2()
obj.method3()