class  basic_calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def sum(self):
        print(self.a+self.b)
        
    def sub(self):
        print(self.a-self.b)
        
    def prod(self):
        print(self.a*self.b)
        
    def divide(self):
        print(self.a/self.b)
        
num1=int(input("Enter the first Number:"))  
num2=int(input("Enter the second Number:"))
p=basic_calc(num1,num2)

print("The sum of Two Number is : ")
p.sum()

print("The difference of Two Number is : ")
p.sub()

print("The product of Two Number is : ")
p.prod()

print("The division of Two Number is : ")
p.divide()
