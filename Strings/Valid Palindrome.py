class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+','',s.lower())
        if (s[::-1]==s):
            return True
        else:
            return False
