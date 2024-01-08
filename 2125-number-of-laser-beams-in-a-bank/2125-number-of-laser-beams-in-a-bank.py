class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, prev_row, current_row = 0, 0, 0
#         for row in bank:
#             row_proccess = row.split("0")
#             for split_row in row_proccess:
#                 if split_row != None:
#                     current_row += len(split_row)
            
#             if current_row==0:
#                 continue
#             if prev_row!=0:
#                 ans += prev_row*current_row
#             prev_row = current_row
#             current_row=0

#         return ans
        for row in bank:
            if '1' in row:
                current_row = row.count("1")
                if prev_row!=0:
                    ans += prev_row*current_row
                prev_row = current_row
                
        return ans