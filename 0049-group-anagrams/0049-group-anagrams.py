class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anag={}
        for s in strs:
            key=''.join(sorted(s))
            if key in anag:
                anag[key].append(s)
            else:
                anag[key]=[s]  
        return list(anag.values())          
        