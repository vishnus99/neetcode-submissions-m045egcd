from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        remaining = len(students)
        print(counter)
        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                remaining -= 1
                counter[sandwich] -= 1
            else:
                break

        return remaining