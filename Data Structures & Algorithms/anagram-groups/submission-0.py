class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in store:
                store[sortedString].append(s)
            else:
                store[sortedString] = [s]
        return list(store.values())