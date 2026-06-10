class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        length  = int(len(s)/2)
        for i in range(length):
            if not s[i].lower() == s[len(s) - 1 - i].lower():
                return False
        return True