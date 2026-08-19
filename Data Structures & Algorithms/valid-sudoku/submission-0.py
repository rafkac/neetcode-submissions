class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        print(self.noRowDuplicates(board))
        print(self.noColumnDuplicates(board))
        print(self.noBoxDuplicates(board))


        return self.noRowDuplicates(board) and self.noBoxDuplicates(board) and self.noColumnDuplicates(board)


    def noColumnDuplicates(self, board: List[List[str]]) -> bool:
        columns = list(zip(*board))
        for c in columns:
            c = list(filter(lambda x: x.isdigit(), c))
            if len(c) != len(set(c)):
                return False

        return True


    def noRowDuplicates(self, board: List[List[str]]) -> bool: 
        for row in board:
            row = list(filter(lambda x: x.isdigit(), row))
            if len(row) != len(set(row)):
                return False

        return True
            

    def noBoxDuplicates(self, board: List[List[str]]) -> bool:
        boxes = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=[row[j:j+3] for row in board[i:i+3]]
                boxes.append(box)

        for b in boxes:
            flat = [x for row in b for x in row]
            digits = list(filter(lambda x: x.isdigit(), flat))
            if len(digits) != len(set(digits)):
                return False
        return True




        