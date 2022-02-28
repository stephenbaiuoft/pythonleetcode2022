import re


class Solution:
    # 2 pointers
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s)-1
        
        while (left < right):
            # CONTINUE to next comparison
            if (not (s[left].isalpha() or s[left].isdigit())):
                left +=1
                continue
            if (not (s[right].isalpha() or s[right].isdigit())):
                right -=1
                continue
                
            if (s[left] != s[right]):
                return False
            else:
                left +=1
                right -=1
        
        return True

    
    def isPalindromeUsingRegex(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]', '', s)
        print(s)
        return s == "".join(reversed(s))