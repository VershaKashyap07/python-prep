input_str = "hi how are you"
l =[]
def upperstr(str):
    for i in str.split():
        l.append(i.capitalize())
    #print(l)
    str1 = " ".join(l)
    print(str1)

upperstr(input_str)

# print(input_str.capitalize())
# print(input_str.title())


#############################
#reverse a number 
#palindrome number

n = 123
temp = n
rev = 0
while n !=0:
    rev = (rev*10)+(n%10) # to get last digit
    n= n //10  # to remove last digit
    
print("reverse is ", rev)

########################
#to check for palindrome means a number and its reverse should be so we can read from left or write it should be same
########################
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")


########################
#3) count number of digit in given number
#121 is apalindrome number
number = 123456
count =0
while number!=0:
    count+=1
    number//=10

print(count)

#4)Find GCD/HCF of two numbers by using iterative method
num1 = 10
num2 = 5

def gcdIter(num1,num2):
    gcd = 1
    if num1<num2:
        min =num1
    else:
        min =num2

    for i in range(1, min+1):
        if num1%i==0 and num2%i==0:
            gcd = i
    return gcd



#4)Find GCD/HCF of two numbers by using recursive Euclidean’s theorem

def gcdRec(a,b):
    if b==0:
        return a
    else:
        return gcdRec(b,a%b)
    
#print(gcdRec(15,3))

#5)Check if a number is Armstrong Number or not
#Armstrong means (abc) = a^n +b^n+c^n where n is len or order of the number, 153 is armstrong number

def armStrong(num):
    order = len(str(num))
    temp = num
    sum =0
    while num>0:
        digit  = num%10
        sum += digit**order
        num//=10

    if temp == sum:
        return True
    else:
        return False
    
print(armStrong(0))

#6)Print all Divisors of a given Number
def divisiors(num):
    l =[]
    for i in range(1,num+1):
        if num%i ==0:
            l.append(i)
    return l

print(divisiors(10))

# we can use sqrt method here to get sqrt of a number , 1/2 means root 2 so use0.5 or 1/2
from math import sqrt
def divisorsSqrt(num):
    l=[]
    for i in range(1, int(num**(1/2))+1):
        if num%i==0:
            l.append(i)
            if(num//i!=i):
                l.append(num//i)

    return l

print(divisorsSqrt(25))

#7)Check if a number is prime or not

def prime(num):
    cnt =0
    for i in range(2,num): # not num+1 because we need to exclude that num
        if num%i==0:
            cnt+=1
    
    if cnt==2:
        return True
    else:
        return False

print(prime(10))


#####optimal way
def primeOptimal(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i==0:
            cnt+=1

            if i!= num//i:
                cnt+=1

    if cnt==2:
        return True
    else:
        return False

#print(primeOptimal(10))

########prime no upto certain number

n =50
for i in range(2,n+1):
    if(primeOptimal(i)):
        print(i)

#8)Sum of first N Natural Numbers

def sumofNatural(n):
    if n==0:
        return n
    return n + sumofNatural(n-1)

ans = sumofNatural(3)
print(ans)

#9)factorial of a Number : Recursive
def factRec(num):
    if num ==1:
        return num
    
    return num * factRec(num-1)

print(factRec(5))


#9)factorial of a Number : Iterative
def factIter(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact *i
    return fact

print(factIter(4))


#10)Reverse a given list 

#or simply 
'''
for i in range(len(arr)-1,-1,-1):
    print(arr)
'''


arr =[5,4,2]
def reverseListIter(l):
    a = 0
    b = len(l)-1
    while a<b:
        arr[a], arr[b] = arr[b],arr[a]
        a+=1
        b-=1
    return arr
print("rverse arr is ",reverseListIter(arr))


##10)Reverse a given list recusively
a = 0
b = len(l)-1
def reverseListRec(l,a,b):
    if a<b:
        arr[a], arr[b] = arr[b],arr[a]
        reverseListRec(arr,a+1,b-1)
    return arr
#print("rverse arr is ",reverseListRec(arr,a,b))


#Print Fibonacci Series up to Nth term
def Fibonacci(n):
    last = 0
    curr = 1
    fib  = [0,1]
    for i in range(2, n):
        next  = curr+last
        fib.append(next)
        last = curr
        curr = next
    return fib, curr

print(Fibonacci(3))

fibonacci_list, last_fibonacci_number = Fibonacci(3)
print(fibonacci_list)  # This will print the list of Fibonacci numbers: [0, 1, 1, 2]
print(last_fibonacci_number)  # This will print the last Fibonacci number: 2


#Remove Duplicates in-place from Sorted Array


def remove_duplicates(nums):
    if not nums:
        return 0  # If the array is empty, no duplicates to remove

    # Initialize two pointers: one for the current element and one for the next distinct element
    i = 0

    # Iterate through the array
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            # Found a distinct element, so move it to the next position
            i += 1
            nums[i] = nums[j]

    # i points to the last distinct element, so the length of the modified array is i+1
    return i + 1

# Example usage:
sorted_array = [1, 1, 2, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(sorted_array)
print(sorted_array[:new_length])  # Print the modified array with duplicates removed


#########################################
# String question
#########################################

#Reverse string

#1) Reverse order of words in a given string/sentence
str1 = "hi how are you"
out = "you are how hi"

str2 = str1.split()
str3 = (" ".join(str2[::-1]))
print(str3)

#2) reversing each word by keeping the same order in a given string/sentence
def reverse_words(input_string):
    words = input_string.split()  # Split the input string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)  # Join the reversed words back into a string
    return reversed_string

# Example usage
input_string = "Hello World! OpenAI is amazing."
output_string = reverse_words(input_string)
print(output_string)


#3) reversing each word by not keeping the same order in a given string/sentence
def reverse_words_with_reverse_order(input_string):
    words = input_string.split()  # Split the input string into words
    words = words[::-1]# order reversed
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)  # Join the reversed words back into a string
    return reversed_string

# Example usage
input_string = "Hello World"
output_string = reverse_words_with_reverse_order(input_string)
print(output_string)

#4Check if the given String is Palindrome or not
def stringPalindrome(str,pos):
    if pos > len(str)/2:
        return True
    if str[pos]!= str[len(str)-pos-1]: #base cond
        return False
    return stringPalindrome(str, pos+1)

print(stringPalindrome("silent",0))


#5)Check if two Strings are anagrams of each other
first_Str = "silente"
sec_Str = "listen"

def Anagrams(str1,str2):

    dict1 = {}
    if len(str1) != len(str2):
        return False
    
    for i in str1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1

    for j in str2:
        if j in dict1:
            dict1[j]-= 1
        else:
            return False
        
    for count in dict1.values():
        if count!=0:
            return False
    return True

print(Anagrams(first_Str,sec_Str))

#6)Write a function to count the occurrence of each character in a string and return the counts in a dictionary.


def count_occur(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict


print(count_occur("hi"))

from collections import defaultdict 
  
def isAnagram(s,t):
        count = defaultdict(int)
        print(count)
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
        print(count)
        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))






    














    










