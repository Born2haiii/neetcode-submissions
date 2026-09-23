
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)

        if Counter(slist) == Counter(tlist):
            return True
        else:
            return False
                


        