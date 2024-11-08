class saranya:
    def method1(self):
        print("parent method")

class sandy(saranya):
    def method2(self):
        print("child1 method")

class tarun(saranya):
    def method3(self):
        print("child2 method")


obj=sandy()
obj.method1()
obj.method2()

obj1=tarun()
obj1.method1()
obj1.method3()