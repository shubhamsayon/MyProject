text = "This is a string!"
print(text)
# So this right here is a variable that stores a string
# Now let's use single quotes and find if that makes any difference.
text = 'This is a string!'
print(text)
# No changes! That means both of these syntaxes work in the same way.
# What about multiline strings? Here's how you can define a multi-line string using triple quotes -
paragraph = """Let's begin with the first sentence.
This is the second sentence.
Finally, we have the last sentence."""
print(paragraph)
# there we go we have successfully defined the multiline string!

# There's another way of displaying the string in multiple lines, and you can do that in a single line of code itself.
# Simply, use the new-line character "\n" whenever you want to display text in a new line. Here's how to do it:

paragraph = """Let's begin with the first sentence.\nThis is the second sentence.\nFinally, we have the last sentence."""
print(paragraph)
# There we go! We have a complete paragraph with three different sentences printed on new lines.
# since "\n" is an escape sequence, so it won't be displayed on the standard output screen rather it tells the standard output to print a new line character.

# Well! What if you want to keep the special character "\n" and use it as a normal string. Is that possible?
# Yes! you can definitely do that. Let's say you want to print the text -
# "\n represents the new-line character!"
# So as usual let's use single quotes and place the text within it
text = '\n represents the new-line character!'
print(text)
# But this prints the text after "\n" in a new line instead of printing the entire text as a string on the same line.
# There are different ways of dealing with this. One of the ways is to use
# another backslash before the escape character to tell Python that you want to treat it as a normal string.
# Here's how to do it:
text = '\\n represents the new-line character!'
print(text)
# Yet another way is to use the prefix 'r' before your string.
# The r means that the string is to be treated as a raw string,
# which means all escape codes will be ignored.
text = r'\n represents the new-line character!'
print(text)
# ============= Narrator's Note: Open slide 2 of Working with strings in Python.pptx to start explaining string indexing=============





