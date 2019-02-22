""" SLICING A STRING """

# Python differs supper and lower case
# When using """ on print python respect word wrap.
print("""teste de print
com aspas
duplas""")

# all charactrs in a string has an index (like a list), starting in 0.
frase = 'Curso em Vídeo Python'
# print the character in index 2
print(frase[2])
# print the characters from 4(inclusive) to 10(exclusive)
print(frase[4:10])
# print the characters from start until 8
print(frase[:8])
# print the characters from 3 til the end
print(frase[3:])
# print characters from 1to 18 in a step by 3
print(frase[1:18:3])
print(frase[::2])

""" ANALISYS """

# LEN
# Returns the lenght (how much longer is it). In this case 21 characters
print(len(frase))
# Returns how much a character (or string) repeats in the string
print(frase.count('o'))
# start and finish of a slice
print(frase.count('o', 0, 13))

# FIND
# It ruturns the position (index) that the sequence you want starts.
print(frase.find('deo'))
# When i doesn't find anything, it returns -1
print(frase.find('android'))

# IN
# Returns if the sequnce you want exists in a string
print('Python' in frase)
print('teste' in frase)

""" TRANSFORMATION """

# REPLACE
# It replaces a character or a sequence of it on a string.
frase2 = frase.replace('Python', 'Android')
print(frase2)

# UPPER
print(frase2.upper())
# LOWER
print(frase2.lower())
# CAPTALIZE - make only the firs letter of the first word upper
print(frase2.capitalize())
# TITLE - Make only the first letter of all words upper
print(frase2.title())
# STRIP - Removes all blank spaces in the end and begining of string
frase3 = '   aprenda Python   '
print(frase3.strip())
# RSTRIP - remove blank spaces at RIGHT
print(frase3.rstrip())
# LSTRIP - Same as above but at left
print(frase3.lstrip())

""" DIVISION """

# SPLIT
# It splits the string (blank spaces by default or a character/string you want) creating a list with all the words
print(frase.split())
print(frase.split('e'))
print(frase.split('a'))  # Here there's no split.

""" JOIN """

# It makes the contrair of slpit. It joins the sentences
frase4 = '-'.join(frase.split())
print(frase4)
frase5 = ' '.join(frase.split())
print(frase5)
frase6 = ''.join(frase.split())
print(frase6)
