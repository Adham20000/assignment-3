#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# In[1]:


#Write a Python program to find all the unique words and count the frequency ofoccurrence from a given list of strings.

def word_count(words):   #function
    word_set = set(words) #convert the list to set to get unique words
    word_counts = {}  # make an empty dict 
    for word in word_set: # a loop to itterate in the set
        word_counts[word] = words.count(word)  # counts the occurrences of the current word in list and takes the word as key in dict
    return word_counts

words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
print(word_count(words))


# In[8]:


# . Write a Python program that finds all pairs of elements in a list whose sum is equal to agiven value

lst = [1, 5, 3, 7, 9]
K = 12
result = []
seen = set()
 
for num in lst:
    complement = K - num
    if complement in seen:
        result.append((num, complement))
    seen.add(num)
        
print(seen)
print(result)


# In[ ]:


# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers
lst = [1, 5, 3, 7, 9]
result = []
for x in lst:
    


# In[13]:


# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
numbers = list(range(1, 21))
prime = []
non_prime = []

for num in numbers:
    if (num%num != 0):
        prime.append(num)
    elif (num%num == 0):
        non_prime.append(num)
    else:
        print("error")
        
print("prime : ",prime)
print("non prime: ",non_prime)
    


# In[14]:


# Write a Python function to print the even numbers from a given list.

numbers = list(range(1, 21))


even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# In[19]:


# Write a function that will take a given string and reverse the order of words.

def reversing(input):
    words = input.split()
    reverse = words[::-1]
    sdrow = " ".join(reverse)
    return sdrow


normal = "hello world"
print("reversed string : ", reversing(normal))


# In[27]:


# Given an integer x, return true if x is a palindrome, and false otherwise.
# Write a Python function that checks whether a passed string is a palindrome or not.

def checks(num):
    x = str(num)    # Convert the integer to a string
    y = x[::-1]     # Reverse the string
    
    if x == y:
        return True
    else:
        return False

integer = (input("Enter a number to check if it's a palindrome: "))
print("Palindrome =", checks(integer))


# In[31]:


# Write a Python function to create and print a list where the values are the squares of numbersbetween 1 and 30 (both included).

def square_list():
    squared = [num ** 2 for num in range(1,31)]
    return squared


squares = square_list()

print(squares)


# In[32]:


# Write a Python function to generate all permutations of a list.

from itertools import permutations

def per_generator(input):
    result = list(permutations(input))
    return result
    

the_list = [1 , 2 , 3]
print("the permutations : ", per_generator(the_list))


# In[33]:


# Write a Python program to access a function inside a function.

def outerfun():
    print("this is the outer function")
    
    def innerfun():
        print("this is the inner function")
        
    innerfun()
    
outerfun()    


# In[ ]:




