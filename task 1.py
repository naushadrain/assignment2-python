import random 

print("Lisr of password \n")
print("------------------------------------------")
a = int(input("enter the number of password:"))
if 1<=a<=20:
    for i in range(a):
        list1 = ["apaya","Peach","Rose","Pomegranate","Pineapple","Rambutan"]
        list2 = ["Beetroot","Carrot","Turnip","Radish","Daikon","Celeriac"]
        list3 = ["lion","dog","cat","monkey","elephant","fox"]
        list4 = ["coconut","mango","ginkgo","white oak","papaya","banyan"]
        password = random.choice(list1)+random.choice(list2)+random.choice(list3)+random.choice(list4)
    print("password generators = ",password)
else:
    print("please enter a suitable number")
