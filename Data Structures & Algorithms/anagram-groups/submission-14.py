class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        output_list = []
        for i, e in enumerate(strs):
            element = sorted(list(e))
            for index, sub_list in enumerate(output_list):
                if element in [sorted(sub_element) for sub_element in sub_list]:
                    output_list[index].append(e)
                    element = None
            if element != None:
                output_list.append([e])
        return output_list