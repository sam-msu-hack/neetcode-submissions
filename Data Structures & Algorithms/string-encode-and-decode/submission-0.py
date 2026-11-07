class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for element in strs:
            element_size = str(len(element))
            encoded_string += element_size
            encoded_string += '#'
            encoded_string += element
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            element = s[word_start:word_end]
            strs.append(element)
            i = word_end
        return strs


