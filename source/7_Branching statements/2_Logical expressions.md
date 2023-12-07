# Logical expressions

In some tasks we need to express conditions that are more complex than simply comparing two values. The words **and**, **or** and **not** are used to connect the simpler terms, and Python uses exactly the same words for that. Here is how to evaluate such complex contidions. If *a* and *b* are any conditions, then:

- condition `a and b` is fulfilled if both conditions *a* and *b* are fulfilled;
- condition `a or b` is fulfilled if at least one of conditions *a* and *b* is fulfilled;
- condition `not a` is fulfilled if condition *a* is not fulfilled (which we have already mentioned in the lessons on Karel);

These conditions can be further combined into even more complex ones according to the needs of the task. In complex conditions, we can use parentheses to influence the order in which the conditions are calculated (also when we are not sure which is the default order), and to make the program clearer to other people reading it. If there are no parentheses in the complex condition, *not* is applied first, then *and*, and finally *or*.

## Logical expressions - examples

```{questionnote}

**Example - leap year:**

Write a program that prints whether a given year (between the 1800 and the 2200, including borders) is leap or simple.

According to the Gregorian calendar, the following rules are used to determine whether a year is simple or leap:

- years that are not divisible by 4 (e.g., 1923, 1070, 2017) are simple;
- years that are divisible by 100 and not by 400 (e.g. 1700, 1800, 1900, 2100, 2200) are also simple;
- all other years (eg 1984, 2000, 2012) are leap. These are years that are divisible by 4 and not by 100, or are divisible by 400.
```

Writing down these rules in the form of logical conditions, we get:

```{py-code} 5
:opt-in-ai:

year = int(input())
if (year % 4 > 0) or (year % 100 == 0 and year % 400 > 0):
    print("Year", year, "is simple.")
else:
    print("Year", year, "is leap.")
```

We get an equally good solution if we use the description for leap years given in rule 3 (verify by thinking through it and by trying both programs that we get the same result):
 
```{py-code} 6
:opt-in-ai:

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Year", year, "is leap.")
else:
    print("Year", year, "is simple.")

```

```{questionnote}

**Example - office hours:**

The opening hours of one souvenir shop are from 7 to 11 in the morning and from 17 to 22 in the evening (to be considered that it works at 7:00 and at 17:00 sharp and does not work at 11:00 and at 22:00). Peter came across the store at *H* hours and *M* minutes. Write a program that takes the number *H* (from 0 to 23) and answers whether Peter came across the store during office hours.
```

```{py-code} 7
:opt-in-ai:

h = int(input())
if (7 <= h and h < 11) or (17 <= h and h < 22):
    print("Peter came across during office hours.")
else:
    print("Peter came across out of business hours.")
```

We can also come to a solution by gradually computing logical values, using logical variables:

```{py-code} 8
:opt-in-ai:

h = int(input())
at_morning_office_hours  = 7 <= h and h < 11
at_evening_office_hours = 17 <= h and h < 22
at_office_hours = at_morning_office_hours or at_evening_office_hours
if at_office_hours:
    print("Peter came across during office hours.")
else:
    print("Peter came across out of business hours.")
```

In this solution, only *h* is an integer variable, and all others (*at_morning_office_hours*, *at_evening_office_hours*, *at_office_hours*) are logical, which means that they will get values *True* or *False* when executing the program.