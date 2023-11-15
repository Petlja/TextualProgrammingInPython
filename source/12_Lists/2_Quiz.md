# Quiz

```{questionnote}

**Example - sales**

At the beginning of the script, the values of several sales in one store are given. Extract the sales with a value greater than 1000 and less than or equal to 4000 into a list, then print the list elements out.
```

```{py-code} 9

sales = (241, 5372, 1278, 9335, 2438, 127, 529, 6027)
lower_bound = 1000
upper_bound = 4000
# complete the program
```

The problem is solved as follows:

```{py-code} 10

sales = (241, 5372, 1278, 9335, 2438, 127, 529, 6027)
lower_bound = 1000
upper_bound = 4000

requested_sales = []
for value in sales:
    if value > lower_bound and value <= upper_bound:
        requested_sales.append(value)

print('Requested sales:')
for value in requested_sales:
    print(value)

```

```{questionnote}

**Example - Leap changes**

A tuple of numbers is given. Extract numbers that differ from their predecessors at least by 10, then print them out.
```

```{py-code} 11

    numbers = (5, 7, 9, 11, 22, 18, 15, 13, 36, 31, 27, 14, 13, 20)
    # complete the program
```

One possible solution is:

```{py-code} 12

numbers = (5, 7, 9, 11, 22, 18, 15, 13, 36, 31, 27, 14, 13, 20)
leap_changes = []

for i in range(1, len(numbers)):
    if abs(numbers[i] - numbers[i-1]) >= 10:
        leap_changes.append(numbers[i])

print('Leap changes:')
for x in leap_changes:
    print(x)




```

```{questionnote}

**Task - even numbers**

A tuple of numbers is given. Extract the numbers that are even and then print them out.

Recall that the number ``x`` is even if ``x % 2 == 0``
```

```{py-code} 13

a = (35, 12, 32, 17, 64, 98, 77, 46, 9)
even = []
```

% commented out
%
% for x in a:
%     if x % 2 == 0:
%         even.append(x)
%
% print('Even numbers:')
% for x in even:
%     print(x)

```{questionnote}

**Task - every third word**

A tuple of strings is given. Extract strings **whose indices** are divisible by 3, then print them.
```

```{py-code} 14

    words = ('All', 'the', 'other', 'words', 'and', 'phrases', 'are', 'not', 'so', 'important')
    every_third = []
```

% commented out
%
% for i in range(len(words)):
%     if i % 3 == 0:
%         every_third.append(words[i])
%
% print('Every third word:')
% for rec in every_third:
%     print(rec)

```{questionnote}

**Task - below zero**

A tuple of numbers is given. Extract the numbers that are negative and their predecessors are positive, then print the extracted numbers.
```

```{py-code} 15

a = (1, -2, 3, 5, -4, -1, -3, 2, -7)
extracted = []
```

% commented out
%
% for i in range(1, len(a)):
%     if a[i] < 0 and a[i - 1] > 0:
%         extracted.append(a[i])
%
% for x in extracted:
%     print(x)
