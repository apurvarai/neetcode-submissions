class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for i in strs:
            sorteS=''.join(sorted(i))
            mp[sorteS].append(i)
        # print(mp)
        return list(mp.values())
        