class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            mapping[sorted_string].append(string)
        
        return mapping.values()