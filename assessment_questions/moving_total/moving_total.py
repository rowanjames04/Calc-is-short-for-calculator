class MovingTotal:
    def __init__(self):
        self.container = []
        self.totals = set()

    def append(self, numbers):
        for num in numbers:
            self.container.append(num)
            # If we have at least 3 elements, calculate the latest triplet sum
            if len(self.container) >= 3:
                new_total = sum(self.container[-3:])
                self.totals.add(new_total)

    def contains(self, total):
        return total in self.totals
    

# Test Cases
mt = MovingTotal()
# 1-4: Original requirements
mt.append([1, 2, 3, 4])
print(f"Original 1 (6): {mt.contains(6)}")   # True
print(f"Original 2 (9): {mt.contains(9)}")   # True
print(f"Original 3 (12): {mt.contains(12)}") # False
print(f"Original 4 (7): {mt.contains(7)}")   # False
# 5: Continued original
mt.append([5])
print(f"Original 5 (12 after 5): {mt.contains(12)}") # True
# 6: Large Scale (10,000 items)
import random
large_data = [random.randint(1, 100) for _ in range(10000)]
mt.append(large_data)
print(f"Large Test 6 (Last sum): {mt.contains(sum(large_data[-3:]))}")
# 7: Non-existent high value
print(f"Test 7 (High value): {mt.contains(99999)}") # False