
# what is a variable ? 
var_explaination = """ 
  Variable is just like a container which is use to store values into it So whenever we required that data set we can use it instead writting the same data again and again we can use variables.
  We can store once and use as manay times we want.

                    """

# data-typing ?

data_type = """It is way of classification or categorization of datasets into different categories
                So that we get know what are the differnt operations are applicable for particular data-set so we can perform according.

                For Example: if we have string we can perform oporations which are applicable for strings.
                             If we integer so we can perform operations which are applicable for integers

  """

# name differnt data-types in Python ?
"""
 Major data-types in Python are:

 String: is sequence of unicode characters which are written in single , double or in tripple quotes. It known as string

 Integer: all numbers including negative or positive numbers which does not contains any floating points. it known as integer

 Float: all numbers which contains some decimal points or floating points it known as float

 Booleans: are use to store True or False value at a time.

 Complex Number: complex numbers are imaginary number which contains some real number and imaginary numbers

 List: is use to store multiple elements into singl variable in ordered format.
       list are muttable so elements of the list can be manipulated after creating some list and square brackets use to create an list.
 
 Tuple: are immuttable by nature one we have define the tuple we can not update its data elements. it applicable for reading operations

 Dictionary: are use to store the data in key value pairs.
             Where each value is associated with some particular key and by using that key we access the data and update and delete as well.
             Keys are unique , we can't created same again and again.
 
 Sets: are use to store unique elements in random order. It does not store duplicate elements it muttable.

 Arrays: are use to store multiple elements of same types of data elements in variables, it only store homogeneous data elements which means every elements have same data-types.

"""


# string here

user_name = "krishna"
password  = 'mypassword123'

full_name = "Krishna Yadav"
profession= 'Software Developer'
role      = 'Django FullStack Developer'

# integer here

roll = 7778
product_quantity = 110
candidate_count  = 10


# float here

temprature  = 13.3
marks       = 90.7
students_percentage = 87.5


# list here

employees_id = [1,2,3,4,5,6,7,8,9,10]

expense_detail = ['mobile recharges', 'collage fee', 'food charges', 343,4,34,45,23,45]

expense_detail[0] = 'Travelling charges' # updating

expense_detail.pop(1)

expense_detail.insert(1, 'Krishna')

# tuples here are immuttable can't be updated after creation

stu_roll = (n for n in range(0, 100)) # tuple from 0 1 2 3 4 ... 99

# dictionary key values pairs

dev_details = {
    'name': 'krishna yadav',
    'role': 'Django Fullstack Developer',
    'skills': ['Python', 'Django', 'Rest-API', 'React', 'HTML', 'CSS', 'JS' 'more'],
    'university': 'Lovely Professional University',
    'city': 'Jalandhar Punjab'
}


# sets are use to store unique elements in random order
stu_email  = ('krishna@gmail.com', 'ayush@gmail.com', 'nisha@gmail.com', 'karan@gmail.com', 'ankita@gmail.com')
