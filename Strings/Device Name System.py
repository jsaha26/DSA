#https://prepinsta.com/bny-mellon-coding-questions-and-answers/

from collections import defaultdict

frequency = defaultdict(int)
output = []

for _ in range(int(input())):
    element = input()
    frequency[element] += 1
    output.append((element, frequency[element]))
  
print()

for element, count in output:
    if count == 1:
        print(element)
    else:
        print(f"{element}{count - 1}")
