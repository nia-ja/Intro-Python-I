"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('src/foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.close()
    print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newFile = open('src/bar.txt', "w")

text = "First.\nSecond.\nThird.\nFourth"
# OTHER SOLUTION:
# lines = ['First line.\n',
#          'Second line.\n',
#          'Third line\n',
#          'I hate writing texts.']
# for i in lines:
#     newFile.write(i)
newFile.write(text)

newFile.close()
print(newFile.closed)

with open('src/bar.txt') as b:
    read_data = b.read()
    print(read_data)
    b.close()
    print(b.closed)