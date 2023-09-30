# You need to accept a string from the user as input. 
# Whenever there is a sequence in the string where a '1' is followed by 'n' consecutive '0's and then followed by another '1,' you should keep track of the count of such sequences. 
# For instance, in the string "10100001001," the output should be 3. In the string "101ab01," the output should be 1.

import re
print(len(re.findall(r'(?=(10+1))', input())))
