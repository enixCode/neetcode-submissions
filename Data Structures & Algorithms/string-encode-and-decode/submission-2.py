class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            if s == '' or s == "":
                strs[i] = '<empty>'
        return '<>'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        s = s.split("<>")
        for i, sortie in enumerate(s):
            if sortie == '<empty>':
                s[i] = ''
        return s