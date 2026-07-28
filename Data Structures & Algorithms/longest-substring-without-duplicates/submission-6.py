class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buffer = []
        buffers = []
        output = 0
        for i, letter in enumerate(s):
            print('i', i, letter)
            buffers.append(len(buffer))
            buffer = [letter]
            for i2 in range(i+1, len(s)):
                if s[i2] not in buffer:
                    buffer.append(s[i2])
                    print('append', s[i2])
                else:
                    buffers.append(len(buffer))
                    print('end', buffer)
                    break
        buffers.append(len(buffer))
                

        return max(buffers) if len(buffers) > 0 else 0
