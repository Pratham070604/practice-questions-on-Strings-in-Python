'''Write a program to reverse a string using slicing.

a = "Python Programming"
print(a[::-1])
'''

''' Check if the string "madam" is a palindrome.
a = "madams"
if a == a[::-1]:
    print(True)
else:
    print(False)
'''

''' Write a program to remove all vowels from a string.
a = "Python is easy to learn"
vowels = 'aeiouAEIOU'
result = ''

for i in a:
    if i not in vowels:
        result += i

print(result)
'''

'''Write a function that counts the number of words in a given sentence.
a = "Python is easy to learn"

def count_words(s):
    b = s.split()
    print(len(b))

count_words(a)
'''


'''Write a function to find the longest word in a string.
a = "Python is easy to learn"

def Longest_word(s):
    b = s.split()
    c= " "
    for i in b:
        if len(i) >= len(c):
            c=i
    print(c)

Longest_word(a)
'''

''' Remove duplicate characters from a string.

a = "Python is easy is  to learn. I am Smooth"

def Duplicate_word(s):
    b = s.lower().split()
    c=[]

    for char in b:
        if char not in c:
            c.append(char)
    
    print(' '.join(c).capitalize())

Duplicate_word(a)
'''