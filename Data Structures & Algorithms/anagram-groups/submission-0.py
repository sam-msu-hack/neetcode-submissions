class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = []
        my_dict = defaultdict(list)
        for word in strs:
            code = [0]*26
            for char in word:
                code[ord("a")-ord(char)] +=1
            my_dict[tuple(code)].append(word)
        return list(my_dict.values())

            