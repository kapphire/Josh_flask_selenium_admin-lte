a = ['hello','world','1','2']

my_dict = {}
for index, item in enumerate(a):
    if index % 2 == 0:
        my_dict[item] = a[index+1]

print(my_dict[1])