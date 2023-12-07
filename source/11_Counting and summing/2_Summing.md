# Summing

In one big group of practical problems, we come to the result by gradually building (accumulating) it as we go through the data. For example, if we need the sum of some numbers, we can get to it in this general way:

```
total = 0
for num in collection:
    total += num
print(total)
```

When we are computing the sum of all the elements of a collection, we get the same result by calling the *sum* function:

```
print(sum(collection))
```

We will use gradual formation of results when we need only some elements from the collection, that is, those that fulfill the given condition. In this case, the algorithm for calculating the sum would generally look like this:

```
total = 0
for num in collection:
    if (num meets the condition):
        total += num
print(total)
```

In order to obtain the mean of the data that fulfills a condition, it is necessary to count and add up such data, and then divide their sum by their number. In the general case it looks like this:

```
total = 0
counter = 0
for num in collection:
    if (num meets the condition):
        total += num
        counter += 1
print(total / counter)
```

Note that in Python, the sum and mean of the selected elements of the collection can be obtained in a shorter and more efficient way. We chose the above method because it looks almost the same as in other programming languages.

## Examples and tasks

```{questionnote}

**Example - Average IQ test result:**

The results of an IQ test for a group of people are given. A score of -1 means that the person did not take the test. Complete the program by printing the mean obtained on the test.
```

```{py-code} 10
:opt-in-ai:

iq_results = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)
```

We can write the program like this:

```{py-code} 11
:opt-in-ai:

iq_results = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)
num_tested = 0
iq_sum = 0

for result in iq_results:
    if result != -1:
        iq_sum += result
        num_tested += 1

if num_tested > 0:
    mean_iq = iq_sum / num_tested
    print('Mean IQ is', mean_iq)
else:
    print('No one was tested.')

```

```{questionnote}

**Task - on duty:**

In Company X, all employees occasionally remain on-call. The norm for the previous period is 20 hours on-call. Every extra hour (over 20 hours) on-call is additionally paid. The number of on-call hours for each employee is given, and the manager wants to know the total number of on-call hours **over the norm**.

Complete the program by computing and printing the total number of overtime hours on-call.
```

If you solve the task correctly, you should get a score of 25 for the data given, since $(21-20)+(23-20)+(34-20)+(25-20)+(22-20)=25$.

```{py-code} 12
:opt-in-ai:

norm = 20
hours_on_duty = (21, 23, 19, 34, 25, 22, 17)
total_overtime = 0
# complete the program

print('Total overtime on call is', total_overtime)
```

% commented out
%
% norma = 20
% hours_on_duty = (21, 23, 19, 34, 25, 22, 17)
% total_overtime = 0
% for hours in hours_on_duty:
%     if hours > norm:
%         total_overtime += (hours - norm)
% print('Total overtime on duty is', total_overtime)

```{questionnote}

**Task - average yield:**

In one orchard after the third year, plum yield per tree is monitored. Trees with yields below 3 kilograms are considered damaged or diseased and will be taken out.

The yield of all the trees in the orchard is given. Complete the program by calculating and printing the average yield of healthy trees (with yields of 3 kilograms or more).

```

You should get a result of approximately 14.757 for the given data.

```{py-code} 13
:opt-in-ai:

yield_per_plant = (11.3, 15.8, 9.5, 2.6, 21.1, 13.4, 17.9, 0.7, 14.3)

# complete the program
```
