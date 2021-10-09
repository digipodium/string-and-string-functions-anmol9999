# 1) CREATING A STRING

from typing import List


name = 'doctor strange'
destination = 'holy sanctrum'

print(f'{name} resides at {destination} ')

# 2) Take a string input and print it's length.

content ='dr strange is my favourate marvel character'
print(len(content))

# 3) Print the last word of the string (Python is great) using slices.

content = 'Python is great'
print(content[-5:])

# 4) Print the each word in different line of string (python is everywhere).

string = 'python is everywhere'
print('python\nis\n everywhere')


# 5) Print the string  ( Hello World!) in reverse.

string = 'Hello World!'
print(string[::-1])

# 6) Convert the string (How are you?) in uppercase.

string = 'How are you?'
ustring = string.upper()
print(ustring)

# 7) Convert the string (How Is It Going?) in lowercase.

string = 'How IS IT GOING?'
lstring = string.lower()
print(lstring)

# 8) Join the following list by spaces( ) and print the result,
# words = ['Python', 'is', 'easy', 'to', 'learn']

words = ['Python', 'is', 'easy', 'to', 'learn']
jwords = " ".join(words)
print(jwords)

# 9)Print a multiline string using a single print.
words = '''Doctor Strange is a practicing magician who
draws his powers from mystical entities such as Agamotto,
Cyttorak, Ikonn, Oshtur, Raggadorr, and Watoomb, who lend their energies for spells. Strange also wields mystical artifacts
including the Cloak of Levitation which enables him to fly; the Eye of Agamotto,
an amulet whose light is used to negate evil magic; the Book of the Vishanti,
a grimoire which contains vast knowledge of white magic;  and the Orb of Agamotto, 
a crystal ball which is used for clairvoyance.'''
print(words)

# 10) Print this string (to move to newline '\n' is used). (results should look exactly like the provided string).

string = "to move to newline '\\n' is used"
print(string)

# 11) Print a variable with some text using a single print function, output should look like following.
#     the variable is 15

variable = 'the variable is'
v2 = 15
print(variable,v2)


# 12) Concatenate the following strings and print the result
#s1 = 'python '
#s2 = 'is '
#s3 = 'great.'

s1 = 'python '
s2 = 'is '
s3 = 'great.'

str = s1+s2+s3
print(str)


# 13) Print # 20 times without using a loop.

a = '#'*20
print(a)


# 14) Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
#1.
#2.
#3.

print("1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.")


# 15) Ask user to input a sentence and print each word on a different line.

msg = input("Enter a sentence : ")
words = msg.split(" ")
for i in words:
    print(i)


# 16) Ask user to input a string and check if the string ends with '?'

msg = input('enter a string: ')
if msg[-1] == '?':
    print('sentence ends with "?"')
else:
    print('sentence does not ends with "?"') 


# 17) Ask user to input a string and print how many times e appeared in the string.

msg = input('enter a string: ')
num_of_e = msg.count("e")
print(f'e occurs {num_of_e} times')

# 18) Check if the user input is a number.

msg = input(" ")
ans = msg.isnumeric()
if ans == True:
    print('user input is a number')
else:
    print('user input is not a number')


# 19) Remove the extra spaces in beginning and in the end of the following string-
 #    text = '   this is not a good string           '

text = '   this is not a good string           '
clr_text = text.strip()
print(clr_text)


# 20) Ask user to input string, print found if any of the character is upper case.

msg = 'enter a string: '
flag=0
for character in msg:
    if character.isupper()==True:
        flag=1

if flag==1:
    print('found')


# 21) Extract names from the following string and store them in a list.
#     names = 'Joe, David, Mark, Tom, Chris, Robert'

names = 'Joe, David, Mark, Tom, Chris, Robert'
List=names.split(", ")

x=[]
for i in words:
    x.append(i)
print(x)

# 22) In the following string, add aye in the end of every word and print the results.
#    text = 'this is some text'

text = 'this is some text'
add_text = text.replace(" ","aye")
print('add_text',end="aye")


# 23) Ask user to enter a string and check if the string contains fyi.

str = input("Enter a sentence : ")
idx=str.find("fyi")
if idx==-1:
    print("The sentence does not contains 'fyi'")
else:
    print("The sentence contains 'fyi'")


# 24) Remove all the special characters and numbers from the following string
 #     text = '%p34@y!*-*!t68h#&on404'

text = '%p34@y!*-*!t68h#&on404'
new_text=""
for character in text:
    if character.isalpha():
        new_text+=character

print(new_text) 

# 25) calculate the average word length of the following paragraph.
#      this is a paragraph which is written just for the purpose of providing content to
#       let the average word length be calculated

para = "this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated"
words = para.split(" ")
sum_of_words=0
for ch in words:
    num=len(ch)
    sum_of_words+=num
avg = sum_of_words/len(words)
print(avg)