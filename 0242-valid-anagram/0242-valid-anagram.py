class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq = {}

        if len(s) != len(t):
           return False

        for i in range(len(s)):
            current = s[i]

            if current in freq:
               freq[current] += 1
            else:
               freq[current] = 1

        for j in range(len(t)):
            current = t[j]

            if current in freq:
               freq[current] -= 1
            else:
               freq[current] = -1

        return all(value == 0 for value in freq.values())