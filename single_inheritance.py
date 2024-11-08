class saranya:
    def method1(self):
        print("parent Method")

class srini(saranya):
    def method2(self):
        print("child method")

child_obj=srini()
child_obj.method1()
child_obj.method2()