'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    count = {}
    for c in text:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    for c, f in count.items():
        print(c,f)
        

def count_char_insensitive(text):
    text_lower = text.lower()
    count = {}
    for c in text_lower:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    for c, f in count.items():
        print(c,f)

# bonus task:
def count_char_ordered(text):
    text_lower = text.lower()
    count = {}
    for c in text_lower:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    for letter in sorted(count, key=lambda l: count[l], reverse=True):
        print(letter, count[letter])


text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

