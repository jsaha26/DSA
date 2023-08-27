# Weird Terminal
# Problem Statement : 
# (Asked in OnCampus Drive August, 2023)

# Here is a weird problem in Susan’s terminal. He can not write more than two words each line, if she writes more than two, it takes only 2 words and the rest are not taken. So she needs to use enter and put the rest in a new line. For a given paragraph, how many lines are needed to be written in Susan’s terminal?

# Input Format:
# A string as the text to input in the terminal

# Output Format:
# Number of lines written.

# Constraints:
# Number of words <=10^7

# Sample Input:
# How long do you have to sit dear ?

# Sample Output:
# 4

# Explanation:
# The writing will be:
# How long
# Do you
# Have to
# Sit dear ?

import string

def f(text1):
    text = ''.join([char for char in text1 if char not in string.punctuation])
    return len(text.split())//2

print(f("How long do you have to sit dear ?"))
