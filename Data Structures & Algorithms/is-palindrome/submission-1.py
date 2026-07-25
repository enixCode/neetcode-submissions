class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        s = [val for val in s if val in 'abcdefghijklmnopyghijklmnopqrstuvwxyzAQWZSXEDCRFVTGBYHNUJIKOLPM0123456789']
        print(''.join(s).lower())
        print(''.join(list(reversed(s))).lower())
        return ''.join(s).lower() == ''.join(list(reversed(s))).lower()