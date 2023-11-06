def greeting(name):
  print("Hello, " + name)
  


def adding(a, b):
  sum = a + b
  print("The sum of the two numbers is " + str(sum))
    
def subtracting(a, b):
  difference = a - b
  print("The difference of the two numbers is " + str(difference))

    
def multiplication(a, b):
  product =  a * b
  print("The product of the two numbers is " + str(product))
    
def division(a, b):
  quotient = a / b
  print("The quotient of the two numbers is " + str(quotient))

def fibonacci(n):
    sum = 0
    num1 = 0
    num2 = 1
    for i in range(0, n):
        print(sum)
        num1 = num2 
        num2 = sum
        sum = num1 + num2
  
  
  