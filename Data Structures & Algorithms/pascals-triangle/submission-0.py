class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []


        for i in range(numRows):
            match i:
                case 0:
                   rows.append([1])
                case 1:
                    rows.append([1,1])
                case _:
                    middle = []
                    prev_row = rows[i-1]
                    for j in range (i-1):
                        n = prev_row[j] + prev_row[j+1]
                        middle.append(n)

                    rows.append([1] + middle + [1])

        return rows

            

        