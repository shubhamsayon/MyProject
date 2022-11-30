# Consider the following string
my_string = "abcXdirYafgNhiaMjeQaRu"
# How will you count the total number of characters in the given string?
# you can also think of this as counting the entire length of the string. And if you remember, we have
# already learned the built-in method that helps us to find the length of a given sequence.
# It's the len() method. SO, let's use it here -
print(len(my_string))

# Wonderful! Now let's say that you want to find the index of the letter "g" in the given string.
# Is there a way to do that? Well! There are more than one way to do so. You can use a couple of methods
# that will help you find the index of "g"
# The first method is known as index() which searches the string for a specified value
# and returns the position of where it was found. Note that index() returns the position of the first
# occurrence of the value. Let's use it to solve the problem -
print(my_string.index('g'))
# The second method that solves the purpose is known as find(). It is quite similar to index() method
# However,  find() method returns -1 if the value is not found whereas index() method will raise an exception
print(my_string.find('g'))
print(my_string.find('k'))  # returns -1
# print(my_string.index('k')) # raises a ValueError

# Okay! Now, let's say that you want to find out the number of times
# the character "a" appears in the given string.
# For this you have a method known as count() that returns the number of times a specified value
# appears in the string. The value you want to count can either be a single character or a substring.
# If no match is found then the value returned will be 0.
print(my_string.count('a'))
print(my_string.count('k'))  # returns 0

# What if you want to convert all the characters of the given string to lowercase?
# The method that allows you to do so is known as lower(). Here's how to use it-
print(my_string.lower())
# Similarly, to convert all the characters to uppercase you can use the upper() method -
print(my_string.upper())

# Your next task is to find whether the given string starts with "abc" or not
# To solve this, use Python's startswith() method which returns True
# if the string starts with the specified value, otherwise False.
print(my_string.startswith('abc'))  # returns True

# Similarly, you can use the endswith() method to check if a given string ends with a specified value.
# The output returned is True if the condition is satisfied otherwise the False.
# Let's check if the given string ends with "axy" or not.
print(my_string.endswith('axy'))  # returns False
# Now let's check if it ends with aRu
print(my_string.endswith('aRu'))  # returns True

# Next in the list of commonly used string method is the strip() method
# which is insanely useful in many occasions.
# The strip() method removes any leading characters i.e. at the beginning
# and trailing characters or the characters at the end. If you do not specify the characters
# to be removed then the strip() method trims whitespaces are from the front and end of the string by default.
# Consider that you have the following string
txt = "###Learning Python*****"
# You can get rid of all the # and * characters from this string using the strip method. Here's how-
print(txt.strip('#*'))
# Wohoo! Now, what if you only want to get rid of the # characters? It is evident that
# all the '#' characters appear at the beginning or the left end of the string. This can be done using
# the lstrip() method. Here's how to do it-
print(txt.lstrip('#'))
# Similarly, the method rstrip() removes any trailing character, i.e. characters at the end of the string.
# Let's remove all the "*" characters from the string.
print(txt.rstrip('*'))
# Let's consider another string that looks like this -
txt_2 = "   Hello World!   "
# let's use strip() on this and visualize the output.
print(txt_2.strip())
# So, it is clear from the output that by default strip will eliminate all the leading and trailing spaces.

# Let's consider another string-
txt_1 = "Programming is Fun!"
# Can you replace the sub-string Programming with another string - "Python"
# So, instead of "Programming is Fun!" we should have "Python is Fun!"
# when we display the given string txt_1
# This can be done using the replace() method which replaces a specified string with another specified string.
# Let's see how to use it -
print(txt_1.replace('Programming', 'Python'))
# So, the first parameter is the old substring while the second parameter is the new sub-string
# Let's execute this now.
# There we go! We have replaced the two strings successfully.

# Now consider the following string:
languages = 'Python,Java,C,C#,C++,Golang'
# Can you separately store each programming language in the given string as a separate item?
# This can be done if you can manage to separate out each programming language and then store them
# as individual items in a Python list. For now, you can think of lists as
# data structures used to store multiple items in a single variable.
# It can be seen that each programming language is separated by a comma in the given string.
# So, the comma is our delimiter.
# We can use this delimiter along with the split method to split and store each language as an
# individual item in a list. Simply put, the split() method allows ou to split a string into a list
# based on a specified delimiter. So, lets see this in action-
print(languages.split(","))

# The final method that you will be learning in this lesson goes by the name join().
# The join() method allows you to capture all items present in a given iterable and join them into
# a single string using a specified separator.
# Let's use an example to understand this. Consider that you have the following list-
ip = ['192', '168', '255', '255']  # Here each string is an individual item.
# Let's join all the strings into a single string by introducing a "." (dot) between each integer
print('.'.join(ip))
# here the first "." is the separator, and then we have the join() method which takes the given list as an input
# Let's execute this
# Eureka! We did it.

# With that we come to the end of this section. Please feel free to expand your horizons by
# exploring other methods used with strings in Python from the official Python documentation.


