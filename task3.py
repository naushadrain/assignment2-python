import re
import random
try:
    file1 = open("first file.txt",'r')
    file2 = open("second file.txt","w+")
    p = []
    a = file.readlines()
    for lines in w:
        mail = ""
        id = lines[:9]
        a = lines[9:]
        b = a.split(" , ")
        for i in p[1]:
            if i.lower():
                mail += i + "."
        email = (mail + b[0] + str(random.randint(500,2000)) + "@poppleton.ac.uk").isupper()
        std = re.sub(" "," ", email)
        file2.write(id+" "+std+"\n")
    file1.close()
    file2.close()

except FileNotFoundError as found:
    print(found)


    

