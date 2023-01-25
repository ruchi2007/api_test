print(type('I AM ADIL MOM'))

print(type(12345))


def verify_status_code_200():
    print('I am from method')
    print('I am from method')
    print('I am from method')


print('I am outside')
verify_status_code_200()

# dict='hello',123,{'name':'test'}
#     for a in dict:
#     print(a)

# def test():
#     print('hello')
# def test1():
#     print('hello123')
# test()


# dict='hello',123,{'name':'test'}
#     for a in dict:
#     print(a)


name_list = ['iphone11', 'iphone13', 'iphone15']
filteriphone15 = []
for name in name_list:
    if name == 'iphone15':
        filteriphone15.append(name)
print(filteriphone15)

name_list = ['iphone11', 'iphone12', 'iphone13', 'iphone15', 'iphone17']
for name in name_list:
    if name == 'iphone13':
        print(name)

name = ['masum', 'ruchi', 'takia', 'atiqa', 'adil']
for x in name:
    # print(x)
    if x == 'takia':
        break
    print(x)

name = ['masum', 'ruchi', 'takia', 'atiqa', 'adil']
for x in name:
    # print(x)
    if x == 'takia':
        continue
    print(x)

name = ['masum', 'ruchi', 'takia', 'atiqa', 'adil']
for name in range(3):
    print(name)