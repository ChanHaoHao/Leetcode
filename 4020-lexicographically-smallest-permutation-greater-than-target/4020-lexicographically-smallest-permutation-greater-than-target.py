import collections

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # get what we have in s
        s_counts = collections.Counter(s)
        
        best_solution = ""
        # count the used chars in target, from 0 to i
        prefix_counts = collections.Counter()
        
        # use every index as a pivot
        for i in range(n):
            # Determine counts available for the suffix and pivot
            available_counts = s_counts - prefix_counts
            
            # Find the smallest char > target[i] to use as the pivot
            for code in range(ord(target[i]) + 1, ord('z') + 1):
                pivot_char = chr(code)
                if available_counts[pivot_char] > 0:
                    # Found a valid pivot character
                    available_counts[pivot_char] -= 1
                    
                    current_prefix = target[:i]
                    
                    # Build the smallest possible suffix from remaining characters
                    suffix_parts = []
                    for k_code in range(ord('a'), ord('z') + 1):
                        k_char = chr(k_code)
                        if available_counts[k_char] > 0:
                            suffix_parts.append(k_char * available_counts[k_char])
                    suffix = "".join(suffix_parts)
                    
                    candidate = current_prefix + pivot_char + suffix
                    if best_solution == "" or candidate < best_solution:
                        best_solution = candidate
                    
                    # Since we want the smallest pivot_char, break after finding one
                    break
            
            # Update prefix_counts for the next iteration
            target_char = target[i]
            prefix_counts[target_char] += 1
            if prefix_counts[target_char] > s_counts[target_char]:
                # We can't match the target's prefix any further, so stop.
                break
                
        return best_solution