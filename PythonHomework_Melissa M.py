#!/usr/bin/env python
# coding: utf-8

# To complete the homework simply fill in your answers in this jupyter notebook!
# 
# Remember that there are many ways in which markup cells can be used and you can add useful things such as references and images to better explain your answers.
# 
# It is perfectly fine if you copy your answer from somewhere else in the internet as long as you understand the code you copied and cite the source. However, refrain from asking help for your colleagues (unless you're really struggling) as the ability to find information online is crucial for any tech role you might want to have in the future.
# 
# <h1> Question 1: Multiple prints</h1>
# Create 3 different variables of different types and print their values using a single print statement.

# In[89]:


first_variable = 1
second_variable = "weather"
third_variable = {
    "animal":"dog",
    "type":"mammal",
    "color":"black",
}


# In[90]:


print(first_variable)
print(second_variable)
print(third_variable)


# <h1> Question 2: Data structures</h1>
# Create two variables containing each a nested list and a nested dictionary and demonstrate how to access specific items of it.

# In[91]:


firstlist = ["lidl","asda","bm", "aldi"]
firstdict = {
    "article":"spoon",
    "shop":"sainsburys",
    "material":"steel",
    "price":"£5"
}


# In[155]:


first_variable=(firstlist,firstdict)


# In[108]:


#if we want to see specific elements, for example, those containing "a" 
new_firstlist = [x for x in firstlist if "a" in x]    #list comprehension
print(new_firstlist)


# In[109]:


new_firstdict = [x for x in firstdict if "e" in x] #list comprehension
print(new_firstdict)


# In[98]:


secondlist = [1,3,6,9] #odd numbers
seconddict = {
    "shop":"m&s",
    "material":"cotton",
    "price":"£20"
}


# In[101]:


second_variable =(secondlist,seconddict)


# In[110]:


for x in secondlist:                #for, if, else statements
    if x<9:
        print('in range')
    else:
        print('not in range')


# In[106]:


#if we want to list specific elements from our second dictionary, for example, those containing the letter "e":
newseconddict = [x for x in seconddict if "e" in x]  #List comprehension
print(newseconddict)


# In[ ]:


Reference: https://data-flair.training/blogs/python-list-comprehension/


# Now consider the following list,

# In[111]:


a_list = [1,2,3,4,5,6,7,8,9]
print(a_list)


# 1 - slice this list (by index) to contain only the numbers smaller than 5; <br>
# 2 - make a loop to create a new list containing only the EVEN numbers of this list (bonus point if you use a list comprehension!!);<br>
# 3 - make a loop to create a new list containing only the numbers that are multiples of 3;<br>
# Bonus - make a loop that will print every item on the list inside a sentence using a f-string.

# In[159]:


#1 - slice this list (by index) to contain only the numbers smaller than 5
print(a_list[:4])


# In[ ]:


#reference: https://www.programiz.com/python-programming/examples/list-slicing#:~:text=The%20format%20for%20list%20slicing,the%20range%20start%20to%20stop.


# In[160]:


#2 - make a loop to create a new list containing only the EVEN numbers of this list (bonus point if you use a list comprehension!!)

newlist=[x for x in a_list if x%2==0]
print(newlist)


# In[ ]:


#Reference: https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/


# In[133]:


# 3 - make a loop to create a new list containing only the numbers that are multiples of 3. Bonus - make a loop that will print every item on the list inside a sentence using a f-string.

mult_of_3 = [x for x in a_list if x%3==0]
print(mult_of_3)
f"In our list, the multiples of 3 are: {mult_of_3}"


# In[ ]:


# Reference: https://realpython.com/python-f-strings/


# <h1>Question 3: Creating functions</h1>
# 
# Create a function that takes a list of numbers and convert them into strings. (bonus point if you use a list comprehension!!)

# In[161]:


my_list =(1,4,7,10,13,16)


# In[147]:


mystring = [str(my_list) for x in my_list] #First method (not sure if this is a function, since does not have a "def" element)
print(mystring)


# In[186]:


def my_string(*args):          #Second method (it does use a "dev" element but I am not sure if syntax is correct)
    for i in args:
        print(i)

my_string(str(my_list))
    
#CORRECT METHOD#####################################################################################
def numberToString(the_list):
    another_list = []
    
    for item in the_list:
        converted_item = str(item)
        another_list.append(converted_item)
        
    return(another_list)

# In[ ]:


#reference: https://stackoverflow.com/questions/3590165/how-can-i-convert-each-item-in-the-list-to-string-for-the-purpose-of-joining-th


# Create a small calculator. The function should pick two numbers and perform one of four mathematical operations with it (sum/subtraction, division, multiplication, exponents). The desired operation should be an option (hint: what IF the user wants to do a sum?)
# 
# Bonus: Make a function that can pick ANY number of numbers.

# In[ ]:


value1 = float(input("Enter first number: "))
op = input("Enter operator: ")
value2 = float(input("Enter second number: "))
result = float(value1) + float(value2)

if op == "+":
    print(value1 + value2)
elif op == "-":
    print(value1 - value2)
elif op == "*":
    print(value1 * value2)
elif op == "/":
    print(value1 / value2)
else:
    print("Invalid operation")


# In[ ]:


#reference: https://www.youtube.com/watch?v=62Rbtc5gpsw


# Create a function that check if a number is within a list of numbers.

# In[3]:


list = [4,8,12,16,20,24,30]
for i in list:
    if (i == 24):
        print("the number is within the list of numbers")
    else:
        print("the number is not within the list of numbers")
            


# Bonus: similar to the item above, create a function that checks if a string contains a given substring, e.g. 'I have a cat' contains the string sequence 'cat' or 'ave'.

# In[7]:


my_string = 'I have a cat'
for i in my_string:
    if (i=="cat"):
        print("the string contains the sequence Cat")
    elif (i=="ave"):
        print("the string contains the sequence ave")


# In[ ]:


#reference: https://stackoverflow.com/questions/5143769/how-do-i-check-if-a-given-python-string-is-a-substring-of-another-one


# Bonus: create a function that given the initial speed of a projectile that is thrown at 90 degrees will calculate how much time the projectile will take to get back to the initial altitude. (yes you're expected to disregard air resistence)

# In[ ]:


initial_speed=120


# In[ ]:


initial_altitude=60


# In[ ]:


gravity=10


# In[4]:


def time(x,y):    
    result = -initial_speed/gravity
    print(abs(result))


# <h1>solve these questions...or ELSE</h1>
# 
# Why the nested if statement below doesn't only produce the first print? Can you modify it so it produces the desired output?

# In[9]:


food = 'Pizza'
drinks = 'Beer'                           #deleted "else" statement

if food == 'Pizza' and drinks == 'Beer':
    print('Yeeeey!')
if food == 'Pizza' and drinks != 'Beer':
    print('Yey.')
if food != 'Pizza' and drinks == 'Beer':
    print('Yey!')


# <h1> Debugging </h1>
# None of the blocks of code below work. Your task is to make them work (if possible!) and add markup cells (or comments) explaining why they don't work.

# print("Is this working?")

# In[1]:


#print("does this work?")


# In[11]:


print("does this work?")


# In[13]:


print("about now?')


# In[14]:


print("about now?")        #changed single quote for double quote after the word "now"


# In[16]:


text_variable = "Today on a scale from 1 to 10 I am feeling..."
my_mood = 10
print(text_variable my_mood)


# In[20]:


print(text_variable, str(my_mood)) #I converted the variable "my_mood" into a string variable, then added a comma between the two variables
                                         


# In[5]:


text_variable = "Today on a scale from 1 to 10 I am feeling..."
my_mood = 10
print(text_variable+my_mood) #Yep there are ways to make it work with a + operator too!


# In[22]:


print(text_variable+str(my_mood)) #same as above, I converted the "my_mood" variable into a string variable


# In[7]:


a_dictionary = {item1: 'Value 1',
                item2: 'value 2',}


# In[25]:


a_dictionary = {"item1": 'Value 1',    #I added quotes to item1 and item2 
                "item2": 'value 2',}
print(a_dictionary)


# In[10]:


1 = 1 # Should return True


# In[26]:


1==1     #I added an additional equal sign


# In[27]:


# Why isn't the outcome 'Clap your hands?'  
mood = 'happy'
if mood == 'Happy':
    print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')


# In[28]:


# Answer: Because in the first line happy is written with lowercase h, and in the second is with uppercase H 
mood = 'happy'
if mood == 'happy':
    print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')


# In[30]:


def printerfunction(x,y):   # I added an indentation to the second line of code
    print(x,y)

printerfunction("a word", "another word")


# In[ ]:


# bonus/annoying round, why is this crashing?
mood = 'happy'
if mood == 'Happy':
   print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')


# In[33]:


#ANSWER: because again in the first line happy was written with lowercase h, while in the second line was with uppercase H. I wrote 'happy' with lowercase in the second line and it works
mood = 'happy'   
if mood == 'happy':
   print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')

