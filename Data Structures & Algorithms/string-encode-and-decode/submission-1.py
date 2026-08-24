class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = ""

        for string in strs:
            encoded_str+=str(len(string))
            encoded_str+="#"
            encoded_str+=string
            
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs = []
        i=0
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            strs.append(s[j+1 : j+1+num])
            i = j + 1 + num
        return strs
