class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        res=[]
        for i in strs:
            mp["".join(sorted(i))].append(i)
        print(mp)
        for i,j in mp.items():
            res.append(j)
        return res