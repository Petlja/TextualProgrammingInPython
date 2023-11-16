# Quiz 

```{questionnote}

**Task - grocery prices**

Prices in one store are:

- Bread: 1 (per loaf - half kilogram)
- Milk: 0.8 (per liter)
- Egg: 0.08 (per piece)
- Chicken breast: 7.3 (per kilogram)
- Apples: 2.2 (per kilogram)
- Tomatoes: 1 (per kilogram)

Put this information in a dictionary and then complete the program by loading the name of a food and displaying the price of that food, or information that it is not available.
```

```{py-code} 4

```

```{questionnote}

**Task - absence**

The names of the students who were absent from the class were given in a tuple. Each appearance of one name represents absence from one class. Complete the program so that it calculates and prints out how many classes each student has missed.

To help you check your program, here is the expected result: for the data given in the tuple *absent*, you should get that James has 4 absences, Maya 3, Alexander 2, and Violet, Mark, Frankie, Peter, Ronnie and Oliver one absence each (not necessarily in that order).
```

```{py-code} 5

    absent = (
        'Maya', 'James', 'Violet', 'Alexander', 'James',
        'Mark', 'Maya', 'Frankie', 'James', 'Peter',
        'Ronnie', 'Oliver', 'Maya', 'Alexander', 'James')
```

% commented out
%
% absences = {}
% for name in absent:
%     absences[name] = absences.get(name, 0) + 1
% for name in absences:
%     print(name, absences[name])

```{questionnote}

**Task - stock status**

Purchases and sales of goods in the form of tuple of pairs are given. In each pair, the first element is the name of the goods, and the second is the change in stock status. For example, a pair *('cheese', -1.5)* means that the available quantity of cheese has decreased by 1.5 (that much cheese has been sold).

Complete the program that calculates and prints the state after these changes, based on the given state changes. Assume that there is no stock at the beginning.

Check the result: for the data given, you should get (in any order)

- cheese 18.5
- milk 297
- flour 985
- eggs 1988
- fish 47
```

In this task, the most important part of the program is traversing through all the pairs. For clarity, we immediately unpack each pair from the tuple *changes* to variables *good*, *change*.

```{py-code} 6

    changes = (
        ('cheese', 20), ('milk', 300), ('cheese', -1.5), ('flour', 1000),
        ('eggs', 2000), ('milk', -2), ('flour', -5), ('fish', 50),
        ('eggs', -12), ('milk', -1), ('flour', -10), ('fish', -3)
    )

    status = {}
    for good, change in changes:
        # complete

    for good in status:
        print(good, status[good])
```
