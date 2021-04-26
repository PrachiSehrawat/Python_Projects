#### Finding a word whether its a palindrome or not ####

# usr = input("Enter a Word: ")
# X = reversed(usr)
#
# if list(usr) == list(X):
#     print("Its a Palindrome")
# else:
#     print("Its not a palindrome")



#### HCF of Two Numbers ####

# n1 = int(input("Enter the first no.:"))
# n2 = int(input("Enter the second no.:"))
#
# def hcf(n1, n2):
#     if n1 > n2:
#         smaller = n2
#     else:
#         smaller = n1
#     for i in range(1, smaller + 1):
#         if (n1 % i == 0) and (n2 % i == 0):
#             factor = i
#     return factor
#
# print(f'hcf = {hcf(n1, n2)}')



#### LCM of Two Numbers ####

# n1 = int(input("Enter the first no.:"))
# n2 = int(input("Enter the second no.:"))
#
# def lcm(n1, n2):
#     if n1 > n2:
#         greater = n1
#     else:
#         greater = n2
#     while True:
#         if (greater % n1 == 0) and (greater % n2 == 0):
#             break
#         greater += 1
#     return greater
#
# print(f'lcm = {lcm(n1, n2)}')



#### Reverse of a given number ####

# num = int(input("Enter a no.: "))
#
# def rev_num(num):
#     rev = 0
#     while num > 0:
#         remainder = num % 10
#         rev = (rev * 10) + remainder
#         num = num // 10
#     return rev
#
# print(f'Reverse of the given number is {rev_num(num)}')



#### Checking For Prime Number ####

# num = int(input("Enter The No.:"))
# if num < 1:
#     print("Its not a prime number.")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Its not a prime number.")
#             break
#     else:
#         print("Its a prime number.")










