
import math

def check_complexity(complexity, n):
    limit = 10**8

    if complexity == "O(1)":
        operations = 1
    elif complexity == "O(log n)":
        operations = math.log2(n)
    elif complexity == "O(n)":
        operations = n
    elif complexity == "O(n log n)":
        operations = n * math.log2(n)
    elif complexity == "O(n^2)":
        operations = n ** 2
    else:
        return "Unsupported complexity"

    if operations <= limit:
        return "PASS"
    else:
        return "FAIL"


print(check_complexity("O(n)", 100000))
print(check_complexity("O(n^2)", 100000))
print(check_complexity("O(log n)", 1000000))
