class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in mapping:
                mapping[sorted_string].append(string)
            else:
                mapping[sorted_string] = [string]
        
        return mapping.values()