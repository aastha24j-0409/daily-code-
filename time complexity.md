# Day 7 - Time Complexity Practice

## Q1

```python
x = nums[5]
```

Answer: O(1)

Reason:
Accessing an element by index takes constant time.

---

## Q2

```python
for i in range(n):
    print(i)
```

Answer: O(n)

Reason:
The loop runs n times.

---

## Q3

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Answer: O(n²)

Reason:
Two nested loops.

n × n = n²

---

## Q4

```python
for i in range(n):
    for j in range(100):
        print(i, j)
```

Answer: O(n)

Reason:
100 is a constant.

100n → O(n)

---

## Q5

```python
i = 1

while i < n:
    i *= 2
```

Answer: O(log n)

Reason:

1 → 2 → 4 → 8 → 16 ...

The value doubles every iteration.

---

## Q6

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Answer: O(n)

Reason:

O(n) + O(n)

= O(2n)

= O(n)

---

## Q7

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

Answer: O(n²)

Reason:

0 + 1 + 2 + ... + (n-1)

= n(n-1)/2

= O(n²)

---

## Q8

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

Answer: O(n³)

Reason:

n × n × n

= O(n³)

---

## Q9

```python
arr = [1, 2, 3, 4, 5]

if 5 in arr:
    print("Found")
```

Answer: O(n)

Reason:
List search may scan all elements.

---

## Q10

```python
s = set([1, 2, 3, 4, 5])

if 5 in s:
    print("Found")
```

Answer: O(1)

Reason:
Set lookup uses hashing.

---

# What I Learned Today

- List lookup → O(n)
- Set lookup → O(1)
- One loop → O(n)
- Nested loops → O(n²)
- Triple nested loops → O(n³)
- Divide by 2 repeatedly → O(log n)

# Quick Cheat Sheet

O(1)  -> Index access, Set lookup

O(n)  -> One loop, List search

O(log n) -> Halving or doubling

O(n²) -> Two nested loops

O(n³) -> Three nested loops
