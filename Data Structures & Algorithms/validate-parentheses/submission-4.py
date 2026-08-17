class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            "()": 0,
            "{}": 0,
            "[]": 0
        }
        last_open = ''
        for carac in s:
            for item in p.items():
                if carac in item[0]:
                    p[item[0]] += -1 if carac == item[0][0] else +1
                    if carac == item[0][0]:
                        last_open = item[0][0]
                    else:
                        if last_open not in item[0] and last_open != 0:
                            return False
                        else:
                            last_open = ''
                    if any([val > 0 for e, val in p.items()]):
                        return False
        return all([val == 0 for e, val in p.items()])