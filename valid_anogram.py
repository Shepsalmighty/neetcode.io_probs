class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:    
                s_dict[letter] += 1

        t_dict = {}
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:    
                t_dict[letter] += 1

        return t_dict == s_dict
      
        # if t_dict == s_dict:
        #     return True
        # return False

#counting letters in both strings way too slow - 0(n^2)?
        # for letter in s:
        #     if s.count(letter) != t.count(letter):
        #         return False
        # return True
        
#counting each list also too slow - also 0(n^2) 
        # s_list = []
        # for letter in s:
        #     s_list.append(letter)
        
        # t_list = []
        # for letter in t:
        #     t_list.append(letter)

        # for letter in t_list:
        #     if t_list.count(letter) != s_list.count(letter):
        #         return False
        # return True
