def solution(structures):
    n = len(structures)
    
    def calculate_cost(is_ascending):
        # Determine the minimum starting height H
        # Target[i] = H + i (asc) or H - i (desc)
        # Requirement: H +/- i >= structures[i] => H >= structures[i] -/+ i
        h_start = 0
        for i in range(n):
            offset = i if is_ascending else -i
            h_start = max(h_start, structures[i] - offset)
        
        # Total cost = Sum(Target[i] - structures[i])
        total_cost = 0
        for i in range(n):
            offset = i if is_ascending else -i
            total_cost += (h_start + offset) - structures[i]
        return total_cost

    return min(calculate_cost(True), calculate_cost(False))

# Test Cases
# 1 & 2: Original Images
print(f"Original 1 ([1,4,3,2]): {solution([1, 4, 3, 2])}") # 4
print(f"Original 2 ([5,7,9,4,11]): {solution([5, 7, 9, 4, 11])}") # 9
# 3: Zero cost test
print(f"Test 3 (Already Stepwise): {solution([10, 11, 12, 13])}") # 0
# 4: Descending zero cost
print(f"Test 4 (Already Descending): {solution([5, 4, 3, 2])}") # 0
# 5: Large Scale
import random
large_structs = [random.randint(1, 1000) for _ in range(100000)]
print(f"Test 5 (100k structures): {solution(large_structs)}")