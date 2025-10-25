from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        sorted_str_hash = {}

        for str in strs:
            # print(str)

            sorted_str = sorted(str)
            sorted_str = "".join(sorted_str)
            
            if(sorted_str in sorted_str_hash):
                sorted_str_hash[sorted_str].append(str)
            else:
                sorted_str_hash[sorted_str] = [str]

        final_list = []
        for key,value in sorted_str_hash.items():
            final_list.append(value)

        return final_list


solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))