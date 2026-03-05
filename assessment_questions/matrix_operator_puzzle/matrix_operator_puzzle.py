def solve_matrix_puzzle(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    max_val = float('-inf')

    def evaluate(expression_list):
        if not expression_list or len(expression_list) % 2 == 0:
            return float('-inf')
        try:
            # Join list into string and evaluate
            res = int(expression_list[0])
            for i in range(1, len(expression_list), 2):
                op = expression_list[i]
                next_val = int(expression_list[i+1])
                if op == '+': res += next_val
                else: res -= next_val
            return res
        except:
            return float('-inf')

    for r in range(rows):
        for c in range(cols):
            if puzzle[r][c].isdigit():
                # Check Horizontal (Right)
                expr = []
                for k in range(c, cols):
                    expr.append(puzzle[r][k])
                    if len(expr) % 2 != 0: # Only evaluate if it ends in a digit
                        max_val = max(max_val, evaluate(expr))
                
                # Check Vertical (Down)
                expr = []
                for k in range(r, rows):
                    expr.append(puzzle[k][c])
                    if len(expr) % 2 != 0:
                        max_val = max(max_val, evaluate(expr))
    return max_val