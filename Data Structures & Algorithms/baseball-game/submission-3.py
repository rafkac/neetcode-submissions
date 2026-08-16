class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                new_record = record[-1] + record[-2]
                record.append(new_record)
            elif op == "C":
                record.pop()
            elif op == "D":
                doubled = record[-1]
                record.append(doubled * 2)
            else:
                record.append(int(op))

        return sum(record)