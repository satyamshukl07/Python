# str = "satyams shukla"
# ch = str[2]
# print(ch)

#conctination
# str1 = "satyam"
# len1 = len(str1)
# print(len1)
# str2 = "shukla"
# len2 = len(str2)
# print(len2)
# final_str = (str1+" "+str2)
# print(final_str)
# print(len(final_str))

#indexing

# str = "satyams shukla"
# # ch = str[0]
# # print(ch)
# print(str[3])


#slicing


#str = "satyam shukla"
#print(str[0:6])

#negative index
#print(str[-6:-1])


#string_funtion

#str = "satyam shukla"
#print(str.endswith("la"))
#print(str.capitalize())
#print(str.replace("shukla" ,"pandit"))
#print(str.find("shukla"))
#print(str.count("a"))


#practice
 #WAP to input user first name and print its lenght

# str = "satyam shukla"
# print(len(str))

#WAP to find the occersnce of $ in a string

# str = "satyam $hukla"
# print(str.find("$"))



#conditional statement if-elif-else(syntax)

# age = 32
# if(age>=18):
#     print("you are eligible for votes")
# else:
#     print("You are not eligible")

# light = "yellow"
# if(light == "green"):
#     print("you can go")
# elif(light == "yellow"):
#     print("Look front of yours")
# elif(light == "red"):
#     print("Stop")
# else:
#     print("Wrong Output")



# age = 16
# if(age>=18):
#     print("you are eligble for vote")
# else:
#     print("Why are u always gives wrong output That is incoreect")



#grade student based on there marks

# marks =40
# if(marks>=90):
#     print("A+")
# elif(marks>=80):
#     print("B+")
# elif(marks>=70):
#     print("C+")
# elif(marks>=60):
#     print("D+")
# else:
#     print("E")


#wap to check if number entererd by user is odd or even

# n =23
# if (n%2==0):
#     print("number is even")
# else:
#     print("number is odd")



    #find the greatest of 3 number enterd by the user
# a= int(input("Enter your first value"))
# b= int(input("Enter your second value"))
# c= int(input("Enter your third value"))
# if(a>=b and a>=c):
#     print("a is greater")
# elif(b>=a and b>=c):
#     print("b is greater")
# elif(c>=a and c>=b):
#     print("c is greter")




    #WAP to check if a number is a multiple of 7 or not

# a= int(input("Enter Your Number"))
# if(a%7==0):
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")



#greter in 4 number which is greater


a = int(input("Enter your 1st number"))
b = int(input("Enter your 2st number"))
c = int(input("Enter your 3st number"))
d = int(input("Enter your 4st number"))
if(a>=b and a>=c and a>=d):
    print("A is greater")
if(b>=a and b>=c and b>=d):
    print("B is greater")
if(c>=a and c>=b and a>=d):
    print("C is greater")
if(d>=a and d>=b and d>=c):
    print("D is greater")
else:
    print("The code is end here")