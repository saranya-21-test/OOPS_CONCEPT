class grandpa:
    def method1(self):
        print("parent method")

class father(grandpa):
    def method2(self):
        print("father method")

class mother:
    def method3(self):
        print("mother method")

class son(father,mother):
    def method4(self):
        print("son method")

obj=son()
obj.method1()
obj.method2()
obj.method3()
obj.method4()