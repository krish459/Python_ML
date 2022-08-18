# print("Hello Krish")
# #for comments
# '''also
# this''' 

# str1 = 'this is me'
# #only starts with alpha and _ only

# age =  21
# weight = 75.41

# print("The value of 3+5 = ", 3+5)


# print("this "*50)


# Lists
# colleges = ['IIT','NIT','College']
# print(colleges[2])

# colleges[2]="COE"
# print(colleges[2])

# print(colleges)

# print(colleges[1:3])


# list2 = ["table","chair","fan","light","door","tap"]

# list2.append('microphone')

# print(list2)

# list2.insert(3,'bottle')
# print(list2)

# list2.remove('microphone')

# print(list2+["abc","def","ghi"])


# print(list2)
# print(len(list2))


# print(max(list2))
# print(min(list2))



# TUPLES cannot be edited

# tup1 = (1,2,3)
# # tup1[0] = 6
# print(tup1[0])

# list1= list(tup1)
# print(list1)

# Dictionary

# names = {'Harry':22,
#          "Krish": 20,
#          "Prachi":21,
#          "Sweety":45}

# print(names["Krish"])
# names["Prachi"]=100
# print(names["Prachi"])

# print(names.keys())
# print(names.values())


# number = int(input())
# print(number)

# for i in range(0,9):
#     print(i)

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# for item  in list1:
#     for i in item:
#         print(i)
    
    
# functions
# def average(num1,num2):
#     return (num1+num2)/2

# print(average(5,10))

# # Strings
# string = 'This is Krish'
# print(string[-2:])

# print(string.capitalize())
# print(string.find('This'))


# File IO
# file1 = open("krish.txt", "wb")
# print(file1.mode)
# file1.write(bytes("Write this to my file", "UTF-8"))
# file1.close()


# file1 = open('krish.txt', 'r+')

# text_to_read = file1.read()
# print(text_to_read)

# Object oriented programming

class Employee:
    __name = None
    __id = 0
    __salary = 0
    
    def set_name(self,name):
        self.__name= name
    
    def get_name(self):
        return self.__name
    
harry = Employee()
harry.set_name('harry')
print(harry.get_name())
# print(harry.__name)