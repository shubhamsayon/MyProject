text = "Hello World!"
# Let's see what happens when we do not specify the end index
print(text[6:])
# ====== run the code ======
# So, this means - "Using this syntax you can get the characters
# starting from index 6 all the way until the end of the string.

# What about leaving out the start index? Let's see -
print(text[:5])
# ====== run the code ======
# It is evident from the output that all the characters starting from the first character
# until the character at the stop index -1. i.e., the character at the index 4
# will be included in this case.

# Now we also have something known as a step size. Though the step size is optional
# while slicing a string, yet it has several applications and advantages.
# If step size is not specified then the increment between the indices
# within the specified range is considered to be 1.
# This means, all the indices within the specified range/slice of a given string
# will be taken into account and the entire substring will be generated as output without skipping
# any element in between. However, if you want to slice the given string in such a way that the value
# in between the indexes is incremented by any value other than 1 then you can use
# the step-size to specify such increments. In simple words, the step size can be used to skip indices
# within the specified slice.

# Let us consider an example to understand how we can define a step-size to
# generate the desired output. Consider the following string-
text = "mPaYsTtHeOrN"
# How will you extract all the characters that lie at odd indices? This is how -
print(text[1::2])
# What we essentially did here is - we started from the first odd index which is 1 all the way
# up to the last character of the given string. But, we also used a step size of 2 in order to ensure
# that every character at the odd indices gets included in the substring.
# This also means, we skipped every even character from the given string.
# So, let's run our code and visualize the output.
# ============== Run the code===============

# Before we wrap up this lesson, let's look at a classic example that uses a negative step size.
# Yes! You heard me right. Just like indices, step size can also be negative.
# Therefore, you can slice through a sequence or a string in the reverse direction using
# negative step size. This can be instrumental in operations like reversing a string.

# For example, let's say we have the following string -
text = "Desserts"
# You can reverse this string in a single line of code using a negative step size -
print(text[::-1])
# Here, the absence of start and stop index means that the entire string will be considered
# while the -ve step size will ensure that the string is traversed in the reverse direction.
# Now, let's run the code and see the output for ourselves-
# ================ Run the code========

# Wonderful!
# That was it for this lesson. Grab a cup of coffee and feel free to join me in the next lecture
# where you will learn about "String Formatting!"
# Cya soon!