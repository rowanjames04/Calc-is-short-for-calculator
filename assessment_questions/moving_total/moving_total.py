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