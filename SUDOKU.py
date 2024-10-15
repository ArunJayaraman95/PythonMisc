from time import sleep

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# board = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2",".","8","5",".","7","9","1"],["7","1",".","9","2","4","8","5","6"],["9","6",".","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1",".","9"]]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKGREEN + "YUR" + bcolors.ENDC)

indices = []

def g(s):
    return bcolors.OKGREEN + s + bcolors.ENDC

def printBoard():
    print("===================")
    justIndices = [index[:2] for index in indices]

    for r in range(9):
        daRow = []
        for c in range(9):
            if [r,c] in justIndices:
                daRow.append(g(board[r][c]))
            else:
                daRow.append(board[r][c])
        print(' '.join(daRow))

    # for row in board:
    #     # print("ROW", row)
    #     print(' '.join(row))

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rowCheck() -> bool:
            for row in board:
                if len(set(row)) < 9:
                    return False
            return True

        def colCheck() -> bool:
            for col in range(9):
                if len(set([board[i][col] for i in range(9)])) < 9:
                    return False
            return True
        
        def boxCheck(offr = 0, offc = 0) -> bool:
            nums = []
            for r in range(3):
                for c in range(3):
                    nums.append(board[r + 3 * offr][c + 3 * offc])
            
            return len(set(nums)) == 9

        def allBoxCheck():
            for r in range(3):
                for c in range(3):
                    if not boxCheck(r, c):
                        return False
            
            return True


        
        for ri, row in enumerate(board):
            for ci, col in enumerate(row):
                if board[ri][ci] == '.':
                    indices.append([ri, ci])
                    # board[ri][ci] = '1'

        # INDEX REDUCTION
        for index in indices:
            candidates = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            # Row Check
            nums = []
            row = index[0]
            for c in range(9):
                curr = board[row][c]
                if curr != '.':
                    nums.append(curr)
            # Column Check
            col = index[1]
            for r in range(9):
                curr = board[r][col]
                if curr != '.':
                    nums.append(curr)

            #Box Check
            offr = row // 3
            offc = col // 3

            for r in range(3):
                for c in range(3):
                    curr = board[r + 3 * offr][c + 3 * offc]
                    if curr != '.':
                        nums.append(curr)

            nums = set(nums)
            for n in nums:
                candidates.remove(n)
            
            index.append(candidates)

        # Set all indices to first candiate
        for index in indices:
            board[index[0]][index[1]] = index[2][0]

        print(board, '\n')
        print(indices)

        print(rowCheck())
        print(colCheck())

        print("\n\n\n")

        def inc(index = 0):
            # sleep(3)
            # print(f"\nIncrementing index {index} {indices[index]}")

            row = indices[index][0]
            col = indices[index][1]
            candidates = indices[index][2]

            currNum = board[row][col]
            currIndex = candidates.index(currNum)
            if currIndex < len(candidates) - 1:
                board[row][col] = candidates[currIndex + 1]
                # printBoard()
            else:
                board[row][col] = candidates[0]
                # printBoard()
                inc(index + 1)

        printBoard()
        for index in indices:
            print(f"Index: {index[:2]}, Candidates: {index[2]}")
        
        x = input("\n Press Any Key to Continue: ")

        while (rowCheck() == False or colCheck() == False or allBoxCheck() == False):
            inc()
        printBoard()


printBoard()
print()

s = Solution()
s.solveSudoku(board)

print()
printBoard()