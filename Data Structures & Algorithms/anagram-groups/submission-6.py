class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        output_list = []
        for e in strs:
            is_in = False
            element = sorted(list(e))
            for index, sub_list in enumerate(output_list):
                if element in [sorted(sub_element) for sub_element in sub_list]:
                    output_list[index].append(e)
                    is_in = True
            if not is_in:
                output_list.append([e])
        return output_list