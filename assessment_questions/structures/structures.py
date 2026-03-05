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