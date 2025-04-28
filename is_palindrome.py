
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for letter in s.lower():
            if letter.isalnum():
                a += letter      
        return a == a[::-1]
# 0(n^2)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         a = ""
#         b = ""
#         for letter in s.lower():
#             if letter.isalnum():
#                 a += letter
                
#         for letter in a:
#             if letter.isalnum():
#                 b += letter
#         print(b)        
#         return a == b[::-1]
