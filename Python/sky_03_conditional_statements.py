# response body
response = {
    'name': "krishna",
    "age": 23,
    "address": "Punjab",
    "status": 200
}


print(response['name'])
print(response['age'])
print(response['address'])


# lambda function
print_function = lambda msg=None, data=None: print(f'\n Message: {msg} Data: {data}')

# conditional statement
if response['status'] == 200: # it valid response

    # perform data extractions
    data_extraction = print_function
    data_extraction(msg='Perform Data Extraction', data=[340,34,34,34,34])

    # data simplification
    simplification = print_function

    # storing into database
    db_handler    = print_function

    # we are using into our application
    data_render  = print_function

# nested conditional statements
response_keys = response.keys()

if 'name' in response_keys: # if name exists

    if('age' in response_keys):
        print('yes name and age both exists in response body')


# nested conditions
if('address' in response_keys):

    if('email' in response_keys):
        print('\n Yes Address and Email both exists')
    
    else:
        print('Sooory Email does not exists in response body')

    