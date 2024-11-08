class saranya:
    def method1(self):
        print("parent1 method")

class sandy:
    def method2(self):
        print("parent2 method")

class tarun(saranya,sandy):
    def method3(self):
        print("child method")

obj=tarun()
obj.method1()
obj.method2()
obj.method3()