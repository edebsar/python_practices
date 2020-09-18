###1. Write a python program to find the sum of first 10 natural numbers.
# def sumNatural(n):
#     sum  = 0
#     while n > 0:
#         sum += n
#         n -= 1
#     return sum
    
# int_ = int(input("Please mention the natural number to add up to: "))
# print(f"The sum of first {int_} natural numbers is {sumNatural(int_)}")

###2. Write a program in python to display n terms of natural number and their sum.
# class naturalSum:
#     def __init__(self,num_):
#         self.num_ = num_
#         self.sum_ = 0
    
#     def termsList(self):
#         print(f"Natural numbers up to {self.num_} are: ")
#         for i in range(1,(self.num_+1)):
#             print(i)
    
#     def numSum(self):
#         for i in range(1,(self.num_+1)):
#             self.sum_ += i
#         print(f"Sum of {self.num_} natural numbers is: {self.sum_}.")

# int_ = int(input("please input the natural numbers up to which u want the sum: "))
# a = naturalSum(int_)
# a.termsList()
# a.numSum()

###3. Write a program in python to input 10 numbers from keyboard and find their sum and average. 
# class naturalSum:
#     def __init__(self, args_):
#         self.args_ = args_
#         self.numLen = len(args_)
#         print(f"Sum of {self.args_} numbers is: {self.numSum()}.")
#         print(f"Average of natural numbers up to is: {self.numAvg()}")
    
#     def numSum(self):
#         sum_ = 0
#         for i in range(0,self.numLen):
#             sum_ += int(self.args_[i])        
#         return sum_

#     def numAvg(self):
#         return (self.numSum()/self.numLen)

# inputInt_ = [] 
# print("please input 10 numbers for which u want the sum & average with comma separated: ")
# for i in range(10):
#     inputInt_.append(int(input(f"number {i+1}: ")))
# naturalSum(inputInt_)

###5. Write a program in python to display the n terms of odd natural number and their sum.
# class natOddSum:
#     def __init__(self,num_):
#         self.num_ = num_
#         print(f"{self.num_} terms of odd Natural numbers are: ")
#         print(*self.termsList())
#         print(f"Sum of {self.num_} odd natural numbers is: {self.numSum()}.")
    
#     def termsList(self):
#         oddList = []
#         for i in range(0,(self.num_)):
#             oddList.append((2*i + 1))
#         return oddList
    
#     def numSum(self):
#         sum_ = 0
#         for i in (self.termsList()):
#             sum_ += i
#         return sum_
        

# int_ = int(input("please input the natural numbers up to which u want the sum: "))
# natOddSum(int_)

### 6. Write a program in python to display the n terms of square natural number and their sum. 1 4 9 16 ... n Terms
# class natOddSum:
#     def __init__(self,num_):
#         self.num_ = num_
#         print(f"{self.num_} terms of square Natural numbers are: ")
#         print(*self.termsList())
#         print(f"Sum of {self.num_} terms square natural numbers is: {self.numSum()}.")
    
#     def termsList(self):
#         oddList = []
#         for i in range(1,(self.num_ + 1)):
#             oddList.append((i*i))
#         return oddList
    
#     def numSum(self):
#         sum_ = 0
#         for i in (self.termsList()):
#             sum_ += i
#         return sum_
        

# int_ = int(input("please input the natural numbers up to which u want the sum: "))
# natOddSum(int_)

###7. Write a program in python to find the number and sum of all integer between 100 and 200 which are divisible by 9.
# class NumSum:
#     def __init__(self, firstInt, secondInt):
#         self.num1 = firstInt
#         self.num2 = secondInt
    
#     def run(self):
#         print(f"Numbers between {self.num1} and {self.num2}, that are divisible by nine, are: ")
#         print(*self.numsList())
#         print(f"And sum of these numbers is: {self.numSum()}.")
    
#     def numsList(self):
#         nums = []
#         for i in range(self.num1,(self.num2+1)):
#             if (i % 9) == 0:
#                 nums.append((i))
#         return nums
    
#     def numSum(self):
#         sumT = 0
#         for i in (self.numsList()):
#             sumT += i
#         return sumT
        

# firstInt = int(input("please input the 1st integer from which u want the sum: "))
# secondInt = int(input("please input the 2nd integer from which u want the sum: "))
# a = NumSum(firstInt, secondInt)
# a.run()

###8. Write a program in python to count total number of alphabets, digits and special characters in a string.
# a_count = 0
# d_count = 0
# s_count = 0
# def check_char(i):
#     a = int(ord(i))
#     if a >= 65 and a <= 90 \
#         or \
#             a >= 97 and a <= 122:
#             global a_count 
#             a_count += 1
#             print(f"{i} is alphabet.")
#     elif a >= 48 and a <= 57:
#         global d_count 
#         d_count += 1
#         print(f"{inputChar} is digit.")
#     else:
#         global s_count 
#         s_count += 1
#         print(f"{inputChar} is special character.")

# ###the below three lines are an alternative to define global variable like above in the function
# #globals()["a_count"]
# #globals()["d_count"]
# #globals()["s_count"]
# if __name__ == "__main__":
#     inputChar = input(f"Please input a string: ")
#     for i in inputChar:
#         check_char(i)
#     print(a_count, d_count, s_count)

###9. Write a program in python to count total number of vowel or consonant in a string.
# def check_char(Char):
#     v_flag = False
#     c_flag = False
#     vowels = "aeiouAEIOU"
#     a = int(ord(Char))
#     if (a >= 65 and a <= 90) or (a >= 97 and a <= 122):
#         if Char in vowels:
#             print(f"{Char} is vowel.")
#             v_flag = True
#         else:
#             print(f"{Char} is consonant.")
#             c_flag = True
#     else:
#         print(f"{Char} is not an alphabet.")
#     return (v_flag, c_flag)

# v_count = 0 
# c_count = 0
# inputChar = input(f"Please input a string: ")
# for i in inputChar:
#     a = check_char(i)
#     print(a)
#     if a[0] == True and a[1] == False:
#         v_count += 1
#     elif a[0] == False and a[1] == True:
#         c_count += 1
#     else:
#         pass

# print(f"{inputChar} has total {v_count} vowels and {c_count} consonants.")

###10. Write program in python to check a list is empty or not.
# def listCheck(lumb):
#     if not lumb:
#         print(f"{lumb} is empty")
#     else:
#         print(f"{lumb} is not empty")

# lumb = []
# inputstr = ""
# while inputstr.lower() != "stop":
#     inputstr = input("please insert the elements of a list: ")
#     if inputstr.lower() != "stop":
#         lumb.append(inputstr)

# listCheck(lumb)

###11. Write a program in python to sum all the items in a list. 
# class ListSum:
#     def __init__(self):
#         self.lumb = []
#         self.inputstr = ""
#         self.sumTotal_int = 0
#         self.sumTotal_str = ""
    
#     def intSum(self, lumb):
#         for i in lumb:
#             i = int(i)
#             print(i, type(i))
#             self.sumTotal_int += i
#         return self.sumTotal_int


#     def strSum(self, lumb):
#         for i in lumb:
#             self.sumTotal_str += i
#         return self.sumTotal_str


#     def run(self):
#         intVal = 0
#         strVal = ""
#         print("It will add a list of numbers or concatenate a list of strings.")    
#         while self.inputstr.lower() != "stop":
#             self.inputstr = input("please insert the elements of a list: ")
#             if self.inputstr.lower() != "stop":
#                 self.lumb.append(self.inputstr)
#         if not self.lumb:
#             print(f"{self.lumb} is empty")
#         else:
#             print(f"{self.lumb} is not empty")
#             try:
#                 intVal = int(self.lumb[0])
#                 print("hit int")
#                 print(f"The sum of items in {self.lumb} is {self.intSum(self.lumb)}")
#             except ValueError:
#                 try:
#                     isinstance(self.lumb[0], str)
#                     print("hit str")
#                     print(f"The sum of items in {self.lumb} is {self.strSum(self.lumb)}")
#                 except ValueError:
#                     print("hit none")
#                     print(f"{self.lumb}'s first item is neither string nor integer, so stopped operation.")


# ListSum().run()


###12. Write a program in python to get the largest number from a list.

# class LargeNum:
#     def __init__(self):
#         self.lumb = []
#         self.inputstr = ""
    
#     def intLarge(self, lumb):
#         lumb.sort()
#         return lumb[len(lumb)-1]


#     def run(self):
#         intVal = 0
#         print("It will find the largest from a list of numbers.")    
#         while self.inputstr.lower() != "stop":
#             self.inputstr = input("please insert the elements of a list: ")
#             if self.inputstr.lower() != "stop":
#                 self.lumb.append(self.inputstr)
#         if not self.lumb:
#             print(f"{self.lumb} is empty")
#         else:
#             print(f"{self.lumb} is not empty")
#             try:
#                 intVal = int(self.lumb[0])
#                 print("hit int")
#                 print(f"The largest of items in {self.lumb} is {self.intLarge(self.lumb)}")
#             except ValueError:
#                 print(f"{self.lumb}'s first item is not an integer, so stopped operation.")


# LargeNum().run()

###13. Write a program in python to print the numbers of a specified list after removing even numbers from it.
# class LargeNum:
#     def __init__(self):
#         self.lumb = []
#         self.inputstr = ""
    
#     def intLarge(self, lumb):
#         result = []
#         for i in lumb:
#             i = int(i)
#             if i % 2 != 0:
#                 result.append(i)
#         return result




#     def run(self):
#         intVal = 0
#         print("It will find the largest from a list of numbers.")    
#         while self.inputstr.lower() != "stop":
#             self.inputstr = input("please insert the elements of a list: ")
#             if self.inputstr.lower() != "stop":
#                 self.lumb.append(self.inputstr)
#         if not self.lumb:
#             print(f"{self.lumb} is empty")
#         else:
#             print(f"{self.lumb} is not empty")
#             try:
#                 intVal = int(self.lumb[0])
#                 print("hit int")
#                 print(f"The list {self.lumb} without even numbers is \n {self.intLarge(self.lumb)}")
#             except ValueError:
#                 print(f"{self.lumb}'s first item is not an integer, so stopped operation.")


# LargeNum().run()

###14. Write a program in python to convert a list of characters into a string.
# class Char2String:
#     def __init__(self):
#         self.lumb = []
#         self.inputstr = ""

    
#     def intLarge(self, lumb):
#         result = ""
#         for i in lumb:
#             result += i
#         return result




#     def run(self):
#         intVal = 0
#         print("It will find the largest from a list of numbers.")    
#         while self.inputstr.lower() != "stop":
#             self.inputstr = input("please insert the elements of a list: ")
#             if self.inputstr.lower() != "stop":
#                 self.lumb.append(self.inputstr)
#         if not self.lumb:
#             print(f"{self.lumb} is empty")
#         else:
#             print(f"{self.lumb} is not empty")
#             print(f"the final string is {self.intLarge(self.lumb)}")




# Char2String().run()


###15. Write a program in python to convert a list of multiple integers into a single integer. 
   ### Sample list: [2, 54, 6, 1000]
    ### Expected Output: 25461000

# class Intone:
#     def __init__(self):
#         self.lumb = []
#         self.inputstr = ""
#         self.lumb2 = []

    
#     def intLarge(self, lumb):
#         resultstr = ""
#         for i in lumb:
#             i = str(i)
#             resultstr += i
#         return resultstr

#     def run(self):
#         print("It will create one integer from a list of integers.")    
#         while self.inputstr.lower() != "stop":
#             self.inputstr = input("please insert the elements of a list: ")
#             if self.inputstr.lower() != "stop":
#                 self.lumb.append(self.inputstr)
#         if not self.lumb:
#             print(f"{self.lumb} is empty")
#         else:
#             print(f"{self.lumb} is not empty")
#         for i in self.lumb:
#             self.lumb2 = [int(i) for i in self.lumb]
#         print(self.intLarge(self.lumb2))

# Intone().run()
