a = input()
b = input()

num1 = int(a)
num2 =int(b)

c = num1 // num2
d = num1 / num2

print(int(c))
print(d)

print('--------------------------------')
a = 30
print('this is a number',a)
# 
set = {2,3,4,5}
print(set , sep='#',end="@")

print('--------------------------------')

x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))

x = 30
y = 50
print("the value if x{} and y {}".format(x,y))

print('--------------------------------')
fee = 4535
descount = 10
pay = (90 * fee ) / 100
print(pay)

km = 564.5
mile = km * 0.621317
print(mile)

print('--------------------------------')

a = 3 
if a>2:
    print(a)
print("nan")

a = int(input("Enter your score: "))
if a > 50:
    print("you pass the exam")
else :
    print("Sorry :( ")

print('--------------------------------')

number = float(input("Enter your namber :"))

if number  > 0 :
    print ("number is positve")
elif number == 0 :
    print ("the num is zero")
else :
    print("num is - ")
    
print('--------------------------------')
    
 
number = int(input())
num = number%2


if  num == 0 :
    print("not Weird")
elif num == 1 and number <= 5:
    print(" Weird")
elif num == 1 and number >= 6 and number <= 20:
    print("not Weird")
elif num == 1 and number >=20:
    print("Weird")
    
print('--------------------------------')

num = ['ddd', 'dddddd', 'rrrrr']
for a in num :
    print(a)


print('--------------------------------')

num = int(input())
for num in range(0 , num):
    print(num * num)
    
print('--------------------------------')
# 
# int = 1
# for int in range(0 ,100):
#     print(int+1 ,"+")
#  
# count = int(input("number :"))
# num = 1
#  
# while num <=10:
#     f = count * num
#     print(num , "X" ,count , " = ",f)
#     num = num+1
#     
#     
print('--------------------------------')

languages = ["python","java","swift","c#","C++"]

for var in languages :
    if var == 'swift' or var =='C++' :
        continue
    print(var)
print('--------------------------------')    

def sum(num1 , num2 ):
    """
    function to finde the sum
    """
    num = num1 + num2
    return num
    print(num1 ," + " ,num2 ," = ", num)
    
num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the secound num : "))

num = sum(num1 , num2)

print(num1 ," + " ,num2 ," = ", num)
print(sum.__doc__)

print('--------------------------------')

string = "computer"
"""
working with Slicing = [Start : end+1 : step ]

"""
print(string[2 : 6 : 2])

# cheking membership
string = "coumputer"
print(string)
print ("is C in String : ","c" in string)
print ("is T in string : ","t" not in string)


var = ["khan" , "Noori", "Tokhi"]
for index , item in enumerate (var):
    print(index , item )
    
#  finding the len
print("the length of String is = " , len(string))