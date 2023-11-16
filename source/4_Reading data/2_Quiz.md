# Quiz

Check your understanding of data reading in Python by doing the following short quiz:

```{mchoice}
:answer1: The program will print 5
:answer2: The program will print 23
:answer3: An error will occur when trying to add a string and a number
:correct: 3

What happens when we run the next program and enter ``2``?
```python
a = input()
print(a+3)
```

```{mchoice}
:answer1: The program will print 5
:answer2: The program will print 23
:answer3: An error will occur when trying to add a string and a number
:correct: 2

What happens when we run the next program and enter ``2``?

```{code}
a = input()
print(a+'3')
```


<!-- ```{eval-rst}
.. dragndrop:: console__text_quiz_4
    :feedback: Try again!
    :match_1: '2.11'|||str(2.1) + '1'
    :match_2: 3.1|||float('2.1') + 1
    :match_3: error in computation|||float('2.1') + '1'
    :match_4: 2.11|||float('2.1') + 1/100
    :match_5: '3.1'|||str(2.1 + int('1'))

    Match the expressions with the calculation results.

``` -->

```{mchoice}
:answer1: When the first decimal place of a is greater than or equal to 5
:answer2: When the number a is negative
:answer3: When the number a is positive
:answer4: When the number a is single-digit
:answer5: When the difference between a and int(a) is greater than 0.5
:correct: 2


When is the integer *int(a)* greater than the real number a?
```
