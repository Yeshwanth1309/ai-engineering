print("---Reference Example ---")
a=[1,2,3,4]
b=a
print(a)
print(b)
b.append(5)
print(a)
print(b)

print("\n=== Shallow Copy Example ===")
a=[1,2,3]
b=a.copy()
print(a)
print(b)

from copy import deepcopy
print("\n=== Deep Copy Example ===")
a = [[1, 2], [3, 4]]
b=deepcopy(a)
b[0].append(99)
print(a)
print(b)
