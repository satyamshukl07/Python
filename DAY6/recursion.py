# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(100) 

 
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(9))


# write a recursive function to calculate the sum of first n natural numbers.
def cal_sum(n):
    if(n==0):
        return 0 
    print(n)
sum = calc_sum(n-1)+n

calc_sum(5) 
print(sum)

# ques 2 == write a recursive funcction to print all element in a list

 