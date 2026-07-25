class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for d in range(0, 9):
            # y
            # x
            list_vertical = [l[d] for l in board if l[d] != '.']
            list_horizontal = [n for n in board[d] if n != '.']
            print(d)
            print(list_horizontal, list_horizontal)
            if (len(list_vertical) != len(list(set(list_vertical)))) or (len(list_horizontal) != len(list(set(list_horizontal)))):
                print("e")
                return False
        for lx in range(3):
            for ly in range(3):
                if not self.cube_list(lx, ly, board, 3):
                    return False
        
        return True
    
    def cube_list(self, x: int, y: int, board: list[str], n: int):
        acc = []
        first_x = x*n
        last_x = n*x + n
        for i in range(n):
            acc.extend(board[int(y*n+i)][first_x: last_x])
        acc = [num for num in acc if num != '.']
        return len(acc) == len(list(set(acc)))