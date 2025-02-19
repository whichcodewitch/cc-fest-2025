# here is the example without the use of a function
name = input("what is your name ?")
print("hello " + name)

# function solution
def greeting():
  name = input("what is your name ?")
  print("hello " + name)

greeting()

def greeting_w_argument(name):
  print("hello "+name)

greeting_w_argument(name)
