def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y==0:
    return "error: can't divide by zero"
  else:
    return x/y 
print("-----calculator-----")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for dividion")


while True:
  choice= input("enter yiur choice(1,2,3,4) or q for quit ")
 
  if choice.lower()=='q':
    break

  if choice in('1','2','3','4'):
    try:
        x= float(input("enter the first number "))
        y= float(input("enter the second number "))
    except ValueError:
      print("enter the valid value")

    if choice=='1':
       print(f'{x} + {y}= {add(x,y)}')
    elif choice=='2':
       print(f'{x} - {y} = {subtract(x,y)}')
    elif choice =='3':
       print(f'{x} * {y} = {multiply(x,y)}')
    elif choice=='4':
       print(f'{x} / {y} = {divide(x,y)}')
  else :
       print("invalid input")
  




