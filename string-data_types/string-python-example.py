# link : https://pythonsandbox.com/code/pythonsandbox_u79070_sQX9WB73roLigWCh9Paq9IKT_v0.py
# here is the example without the use of a function
name = input("what is your name ?")
print("hello " + name)

# function solution
def greeting():
  name = input("what is your name ?")
  print("hello " + name)

greeting()

# passing variable by reference as an argument into a function
def greeting_w_argument(name):
  print("hello "+name)

greeting_w_argument(name)
