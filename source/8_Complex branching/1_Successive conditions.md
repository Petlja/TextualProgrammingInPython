# Successive conditions

There are tasks in which, when one condition is not fulfilled, another one should be checked, and if that condition is not valid either, then a third one is checked and so on. To avoid writting

```{code}

if first_condition:
    statement1
else:
    if second_condition:
        statement2
    else:
        if third_condition:
            statement3
        else:
            if fourth_condition:
                statement4
            else:
                    statement5
```

in Python we use the special word `elif`, which stands for *else:* and the indented *if* in the following line. So we get a more readable code:

```{code}

if first_condition:
    statement1
elif second_condition:
    statement2
elif third_condition:
    statement3
elif fourth_condition:
    statement4
else:
    statement5
```

Note 1: Any number of consecutive *elif* statements can be used this way.

Note 2: The part

```{code}

else:
    statement5
```

is optional and can be omitted if not needed.

## Examples and tasks

```{questionnote}

**Example - body mass index:**

The body mass index (abbreviated bmi) is used for quick orientation regarding the degree of obesity or weight loss. The formula for calculating body mass index is $bmi = {m \over {h \times h}}$, where *m* is the mass in kilograms and *h* is the height in meters. The *bmi* values are interpreted as follows:

- up to 18.5: malnourished person
- from 18.5 to 25: person of normal body weight
- from 25 to 30: overweight
- over 30: obese person

Write a program that takes a person's weight and height and then writes to which category that person belongs (limit values belong to a lower category).
```

One possible solution is given below. Consider why it is not necessary to use complex logical conditions (built with words *and*, *or*, *not*) in this solution.

```{py-code} 1

m = float(input('Body mass: '))
h = float(input('Body height: '))
bmi = m / (h*h)
if bmi <= 18.5:
    print('Malnourished.')
elif bmi <= 25:
    print('Normal body weight.')
elif bmi <= 30:
    print('Overweight.')
else:
    print('Obese.')


```

```{questionnote}

**Task - age groups of players:**

Young basketball players register at the beginning of the basketball season in one of the age categories (U10, U12, U14, U16, U18), according to how many years they turn in the calendar year in which the season begins. The registration rules are as follows:

- 9 and under - U10
- 10 or 11 years - U12
- 12 or 13 years - U14
- 14 or 15 years - U16
- 16 or 17 years - U18

Write a program that takes the age of a basketball player in the year they register and pritnts their age category.

For example, if age is 15, the program should print *U16*
```

```{py-code} 2

g = int(input("How old is player: "))
# finish the program


```

```{questionnote}

**Task - ordinal number:**

Write a program that loads an integer from 1 to 6 (including borders) and prints the appropriate ordinal number in letters. For example, if number 6 is loaded, the "sixth" (without quotation marks) should be printed.
```

```{py-code} 3

n = int(input("Enter a number from 1 to 6: "))
# finish the program
```