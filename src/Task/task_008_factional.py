# num = int(input("Enter a number which fact you want to get!"))
# # 5
# fact = 1
#
# if num < 0:
#     print("Fact is not defined!")
#
# if num == 0:
#     print("FACT = ", fact)
# else:
#     for i in range(1, num + 1):
#         fact = fact * i
#
# print("Factorial of : ", fact)

def recursion_fib(n):
    if n<=1:
        return n
    else:
        return  recursion_fib(n-1)+recursion_fib(n-2)
num = int(input("Enter how many terms :"))
if num<0:
    print("-ve value")
for i in range(num+1):
    print(recursion_fib(i))
