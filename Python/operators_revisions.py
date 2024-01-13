
# what are operators ?
operators_explantion = """
  Operators: are basically special symbols which is use to perform special operations according to the symbol.
            For example if we are using * plus symbol so it will perform addition of two or more numbers.
    
    Major Types of operators are:

    1. Arithmetic Operators: are use to perform mathematical operations such as addition, substraction, multiplication,division, modulus, exponent etc.

    2. Assignment Operators: are use to assign right hand values to the left hand operand it called assignment operators.

    3. Logical Operators:    are use to perform logical operations such logical or, logical and , logical not it use perform operation based on multiple conditions.


    4. Comparision Operators: are use to compare two or more values in terms of less than, greater than, greater than or equal to,  equal to , not equal to  etc.

    5. Membership Operators: are use to check weather some particular element is belogn to given sequence(family) or not. for that we use in, not in.

    6. Identity Operators:   are use to check the identity in terms of checking it values, data-types, size etc for that we use is , is not.

    7. Bitwise Operators:    are use to perform opertions on bits by bits So it will first convert the given number into binary format and after it will perform the bitwise operation

 """

# artithmetic operators

num  = 12
num2 = 40

total_sum = num + num2

# lamda function for printing 
p = lambda data, msg=' ' : print(f'\n {msg} {data}')

# p(total_sum)
remainder = num2 % num # 40%12 = 
p(remainder)

# exponent

p(2**3)

p(num2//num, msg='Floor division')

# Assignment operator

name = "krishna"
full_name = ''
sir_name  = ' Yadav'
full_name += name + sir_name # concatenation then assignment 
p(msg='Full name', data=full_name)

marks = 78
attendence_marks = 10

marks += attendence_marks # addition then assignment like marks = 78:  marks += 10: marks = 78 + 10 = marks = 88
p(msg='Total marks', data=marks)

score   = 100

penalty = 4 # penalty of 4 numbers

score -= penalty # substraction then assignment  score -= penalty : score =  100 ,  score = 100-4


p(msg='Update Score', data=score)

# Logical Operators: use to perform logical operations such as logical and ,  logical or logical not

authenticated = False
is_admin         = False

# if user is authenticated and having admin permission then he can perform certains tasks

# if all conditions of are true then only logical and return true or body of logical and will be executed
if(authenticated and is_admin): # logical and we are saying if is_athenticated and is_admin both are true then only perform certain operation
    print('Yes you are authenticated and has admin permissions')

else:
    print('Sooory... You are not authenticated ')

# logical Or : it says if out of given contions if any one condition is true it return True
person_age  = 10
has_voter_id = True

if(person_age >= 18 or has_voter_id == True ): # logical or operator
    print('Yes you are eligible')
else:
    print('Soooooory you not eligible')
    


# logical Not operator: it work as reverse gate which means if input is true than it will return false, if input false than it will reutrn True

if not authenticated:
    print('Sooory... You are not authenticated ')

else:
    print('Yes... You are  authenticated ')



# Comparision  Operators : are use to compare two or more values in terms less than, greater than, equal to , not equal to etc.
    
if(num > num2): # if num > num2 : saying if 12 >40: if 12 is greater than 40 return true
    print(f'Yes {num} is greater than {num2}')

else:
    print(f'No {num} is not greater than {num2}')


# less than

if(num < num2): # 12 < 40 :true
    print(f'Yes {num} is less than {num2}')

else:
    print(f'No {num} is not less than {num2}')


    
    
# not equal
if(num != num2): # 12 != 40
    print(f'Yes {num} is not equal to {num2}')

else:
    print(f'No {num} both numbers equal {num2}')

    
# greater than or equal to
if(num2 >= 40): # 40 >= 40: means 40 is not greater but equal to 40 it will return true
    print(f'Yes {num2} is either greater or equal to 40')

else:
    print(f'No number: {num2} is neither equal nor greater than 40')


# membership operators

student_ids = [1,2,3,4,5,6.7,8,9,10]

roll = 22

# check weather roll exists in student-ids list or not

if(roll in student_ids):
    print(f'Yes roll: {roll} exist in students ids: {student_ids}')

else:
    print(f'No roll: {roll}  does not exist in students ids: {student_ids}')


python_dev_group_members = ['krishna', 'ankit', 'aman', 'nisha', 'aisha']

new_emp_name = 'Arjun'

# new employee want to know weather he is member of this dev group

if(new_emp_name in python_dev_group_members):
    print(f'Yes mr: {new_emp_name} you are a member of this group')

else:
    print(f'Sooory mr: {new_emp_name} you are not a member of this group')


if(new_emp_name not in python_dev_group_members):
    print(f'Sooory mr: {new_emp_name} you are not a member of this group')



# Identity operators

db_user_name = 'krishna7778'

client_user_name = 'krishna777'

# to we have to check weather both usernames are exactly same or not

if(client_user_name is db_user_name):
    print(f'Yes both usernames are exactly same')

else:
    print(f'Yes both usernames are not  same')

# password 

user_passsword = 'mypassword123'
db_password    = 'mypasssword123@'

# check password same or not
if user_passsword is not db_user_name:
    print('User password and database password is mis matched not same')



# Bitwise operators: are use to perform operations by bits by bits
num = 21
num2 = 48

# bitwise and operations

print(num & num2) # bitwise and &
print(num | num2) # bitwise or
print(num << 2)   # bitwise leff sift by 2**2 = 4*21 = 84
print(num2 >> 2 ) # bitwise right sift by 2**2 = 4: 48/4 = 12
print(~num)       # complement here
print(num^4)      # XOR here
print(bin(num))