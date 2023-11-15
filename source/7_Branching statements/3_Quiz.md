# Quiz

## Logical expressions - questions

<!-- ```{eval-rst}
.. dragndrop:: console__branching_quiz_compare
    :feedback: Try again!
    :match_1: a <= b ||| a < b or a == b
    :match_2: a >= b ||| b <= a
    :match_3: not (a == b) ||| a < b or a > b
    :match_4: not (a != b) ||| a == b

    Match the equivalent expressions
``` -->

```{mchoice}
   :answer1: h < 7 and 11 <= h
   :answer2: h < 7 or 11 <= h
   :answer3: not(7 <= h) or not(h < 11)
   :answer4: h <= 7 or 11 < h
   :correct: 2, 3

   What are all conditions equal to **not (7 <= h and h <11)**?

```

<!-- ```{eval-rst}
.. dragndrop:: console__branching_quiz_abc_sign
    :feedback: Try again!
    :match_1: At least one of a, b, c is positive ||| a > 0 or b > 0 or c > 0
    :match_2: None of a, b, c is positive ||| a <= 0 and b <= 0 and c <= 0
    :match_3: a, b and c are not all positive ||| a <= 0 or b <= 0 or c <= 0
    :match_4: a, b and c are all positive ||| a > 0 and b > 0 and c > 0

    Match conditions and descriptions
``` -->

```{mchoice}
:answer1: (population <= 10000) or (population > 10000 and income <= 2000)
:answer2: population <= 10000 or income <= 2000
:answer3: population <= 10000 and income <= 2000
:answer4: (income <= 2000) or (income > 2000 and population <= 10000)
:correct: 1, 2, 4


The state government is offering assistance to build a sports center. Settlements with up to 10,000 residents are eligible to apply, as well as settlements with more than 10,000 residents and an average income of up to 2000. Which of the conditions correctly checks whether a settlement  can apply?
```

## Logical expression - tasks

```{questionnote}

**Task - numbers in order:**

Write a program that takes integers *a*, *b*, *c* and answers the question whether these numbers are given in order from smallest to largest.

```

```{py-code} 9

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
# finish the program

```

```{questionnote}

**Task - middle number:**

Write a program that takes integers *a*, *b*, *c* and answers the question whether *b* is medium in size.

```

```{py-code} 10

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    # finish the program

```

```{questionnote}

**Task - watching the dog:**

Anna and Mark live together and have a dog named Bobby. The two are scheduled to travel the same month, Anna from day *a1* to *a2*, and Mark from day *m1* to *m2*. They both leave in the morning and return in the evening. Since they don't want to leave Bobby alone, they wonder if their trips overlap.

Write a program that takes integers *a1*, *a2*, *m1* and *m2*, and answers the question of whether Anna's and Mark's travels overlap.
```

**Hint:** trips overlap if Mark leaves before Ana returns (the day of Mark's departure is less than or equal to the day of Ana's return) or vice versa - if Ana leaves before Mark returns.

```{py-code} 11

a1 = int(input("a1 = "))
a2 = int(input("a2 = "))
m1 = int(input("m1 = "))
m2 = int(input("m2 = "))
# finish the program

```