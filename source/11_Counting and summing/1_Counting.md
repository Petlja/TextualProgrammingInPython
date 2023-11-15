# Counting


It is a very common case that we are only interested in some of the data from a collection. Here we will practice how to count and, if necessary, sum numbers that are of interest to us, or that fulfill some condition.. The general form of a program (algorithm) by which we count the elements of a collection that meet a given condition looks like this:

```python
num = 0
for x in collection:
    if (x meets the condition):
        num += 1
print(num)
```

```{infonote}

The statement ``x += a`` increases the value of the variable *x* by *a*. This is actually an abbreviated form of the statement :code:`x = x + a`, which assigns the value *x + a* to the variable *x*.

The statement ``x -= a`` decreases the value of the variable *x* by *a*. This is an abbreviated form of the statement :code:`x = x - a`, which assigns the value *x - a* to the variable *x*.
```

In our example, the statement *num += 1* increases the value of the variable *br* by 1.

## Examples and tasks

```{questionnote}

**Example - meeting:**

The team leader has offered two options for the time of the meeting to be held tomorrow. Each team member wrote in a table which term would be more appropriate for him/her (1 for the first term, 2 for the second). This information was transferred to the first line of the following program.

Complete the program - script, so that given the data on voting of team members, it prints how many voted for the first and how many for the second term.
```

```{py-code} 1

terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)
```

For example, we can count the number of team members who voted for the first term, and calculate the rest at the end.

```{py-code} 2

terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

num_first_term = 0
for t in terms:
    if t == 1:
        num_first_term += 1

num_second_term = len(terms) - num_first_term

print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')
```

Another way is to count the votes for both the first term and the second term.

```{py-code} 3

terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

num_first_term = 0
num_second_term = 0
for t in terms:
    if t == 1:
        num_first_term += 1
    if t == 2:
        num_second_term += 1
print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')
```

or, assuming the data is "clean", that is, there are no values other than 1 and 2:

```{py-code} 4

terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

num_first_term = 0
num_second_term = 0
for t in terms:
    if t == 1:
        num_first_term += 1
    else:
        num_second_term += 1

print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')
```

In case the information is not known in advance but should be entered, we could write a program like this:

```{py-code} 5

n = int(input("How many team members voted: "))
num_first_term = 0
for i in range(n):
    t = int(input("Enter one vote: "))
    if t == 1:
        num_first_term += 1

num_second_term = n - num_first_term
print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')
```

At the beginning of this program, we load the number of votes *n*, then use the *for* loop to repeat loading and counting one vote *n* times.

```{questionnote}

**Task - written test:**

Several people took the traffic proficiency test, which is a prerequisite for taking the practical part of the exam. A test is considered passed if the number of incorrect answers is less than or equal to 3.

At the beginning of the script are given the test results of one group of candidates (number of incorrect answers for each person who took the test). Complete the script by listing how many candidates have passed the test.
```

```{py-code} 6

num_incorrect = (2, 5, 1, 0, 4, 2, 7, 1)
passed = 0

# add the missing statements here

print(passed)
```

% commented out
%
% passed = 0
% for x in num_incorrect:
%     if x <= 3:
%         passed += 1
% print(passed)

```{questionnote}

**Task - swimming pool**

A visit to the pool is being prepared for a group of children. Anyone lower than 160 centimeters can only go into the smaller pool. The organizer is interested in how many children are below 160 centimeters in order to plan the groups.

Children's heights are given at the beginning of the program. Complete the program to print the number of children lower than 160 centimeters.
```

```{py-code} 7

heights = (160, 161, 174, 149, 153, 160, 158, 182, 144)

```

```{questionnote}

**Task - humidity**

In a botanical garden, soil moisture is measured once a day for rare and sensitive species. Humidity is expressed in numbers from 0 to 1, and conditions for the development of plants are considered to be good when the humidity is between 0.3 and 0.7 (including boundaries).

Values of humidity (measured over a period of time) are given at the beginning of the script. Complete the script by printing the number of days when the humidity was not good.
```

```{py-code} 8

humidity = (0.2, 0.5, 0.61, 0.40, 0.72, 0.51, 0.43, 0.35, 0.28)


```