#dict={'name':'adil'}
#print(type(dict))
from pprint import pprint

dict={
  "email": "johne.doe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "username": "johne.doe",
  "userpassword": "john.doe",
  "billing": {
    "first_name": "John",
    "last_name": "Doe",
    "company": "",
    "address_1": "969 Market",
    "address_2": "",
    "city": "San Francisco",
    "state": "CA",
    "postcode": "94103",
    "country": "US",
    "email": "john.doe@example.com",
    "phone": "(555) 555-5555"
  },
  "shipping": {
    "first_name": "John",
    "last_name": "Doe",
    "company": "",
    "address_1": "969 Market",
    "address_2": "",
    "city": "San Francisco",
    "state": "CA",
    "postcode": "94103",
    "country": "US"
  }
}
#pprint(dict['billing']['address_1'])
dict='hello',123,{'name':'test'}
for a in dict:
    print(a)
