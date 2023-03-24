# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

string=input("Enter the string: ")
length=len(string)
words=string.split()
global coded
coded=''
#To code
def code():
    coded=''    
    for word in words:
        if len(word)<3:
            coded+=word[::-1]+' '
        else:
            coded+='sdx'+word[1:]+word[0]+'dsg'+' '
    print("After coding: ", coded)

#To decode
def decode():
    rev=string[::-1]
    coded='sdx'+string[1:]+string[0]+'dsg'
    if length<3:
        after_decoding=rev[::-1]
        print('After decoding: ', after_decoding)
    else:
        after_decoding=coded[-4]+coded[3:(length+2)]   #sdxellohdsg   h
        print('After decoding: ', after_decoding)

#To take input
while True:
    what=input("Enter wheather you want to \n 1. Code \n 2. Decode \n 3. Exit \n ")
    if what =='1':
        code()
    elif what=='2':
        decode()
    else:
        break