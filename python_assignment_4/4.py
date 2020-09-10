class A:
    def feature1(self):
        print("Deep")
        print(super())
        
class B(A):
    def feature2(self):
        print("Hello ")
        super().feature1()
        
x=B()
x.feature2()