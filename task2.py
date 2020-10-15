#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
joshList = []

a = input("Word")
b = input("Word")
c = input("Word")
d = input("Word")
e = input("Word")

joshList.append(a)
joshList.append(b)
joshList.append(c)
joshList.append(d)
joshList.append(e)

print(joshList)
