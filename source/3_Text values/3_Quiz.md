# Quiz

Check your understanding of text values in Python by doing the next short quiz and tasks: 
<!--
```{eval-rst}
.. dragndrop:: console__text_quiz_format
    :feedback: Try again!
    :match_1: '12.34'|||format(12.34, '.2f')
    :match_2: '__12.34'|||format(12.34, '7.2f')
    :match_3: '_12.34'|||format(12.34, '6.2f')
    :match_4: '__12.3'|||format(12.34, '6.1f')
    :match_5: '12.3'|||format(12.34, '.1f')

    Match the *format* function calls with the results. The spaces are represented by '_' as they would not otherwise be visible.
```
-->

```{mchoice}
:answer1: s = 'a' + "b"
:answer2: s = 'ab"
:answer3: s = 'ab'
:correct: 2


Which of the statements is faulty?
```

```{mchoice}
:answer1: print('tra' + 2 * '-la')
:answer2: print('tra-' + 2 * 'la-')
:answer3: print('tra-' + 'la-' + 'la')
:answer4: print('tra-' + 'la-la')
:answer5: print('tra-la-' + '-la')
:correct: 1, 3, 4

Which statement prints `` tra-la-la ''? (Mark all correct answers)
```

<!-- ```{eval-rst}
.. dragndrop:: console__text_quiz_nanana
    :feedback: Try again!
    :match_1: 'NA' * 3 ||| 'NANANA'
    :match_2: 'N' + 3 * 'A' ||| 'NAAA'
    :match_3: 'N' * 3 + 'A' ||| 'NNNA'
    :match_4: 'N' * 3 + 3 * 'A' |||'NNNAAA'

    Match expressions with their values.
``` -->

```{fitb}
:answer: NANA

What the statement **print(('N' + 'A') * 2)** prints?\
|blank|

```

```{questionnote}

**Task - Profit Sharing**

The three friends agreed to divide the profits from the joint venture so that the first would get 2/7 of the earnings, the second 1/3, and the third the remaining sum. The total profit was 40000. Complete the program, which will print, in two decimal places, the earnings of each of the three friends.
```

```{py-code} 12

total_earnings = 40000
first = total_earnings * 2 / 7
second = 0 # fix the staement
third = total_earnings - first - second
# add statement(s) for printing
```
