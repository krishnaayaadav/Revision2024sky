

# what is function 
function_explantion = """
  function: is basically group of statements tha is use to perform certain task.

  Basically the idea is put some common and repeatedly done tasks together make a function. 
  So instead of writting the same code again and again its better to make a function and use that function for different inputs

  And function increase code reausabilty. write once and use as many times we want

  So what we can do is we can create one function and then use that function to perform the given task for different inputs

   Advangets of using function:
              1. Write function once and use as many time you. This increase code resuability.
              2. Function save time and efforts.
              3. Large divide project into small modules, because of that code maintenance become easy.
              4. In function add/removing any function become easy because of modules
              5. Code debuggin become easy
            
        Note: Function does not call itself. We should have them manualy 
              Function return value at same place where called jaha se function ko call kiya gya hai.
            

 """




# normal function
def greet_msg(msg):
    print(f'\n Your message is: {msg}')
    return msg

print(greet_msg('Welcome to Python'))


# nested function

def calculator(num1, num2):

    def add_nums(*args):
        print('\n Performing here addition')

        total_sum = 0

        return total_sum
    
    return add_nums


add_nums = calculator(23, 43)

print(add_nums())

# lambda functions

make_double = lambda num: num*2 # 21*2=42
print(make_double(21))
