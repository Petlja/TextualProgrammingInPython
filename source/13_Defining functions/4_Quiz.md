# Quiz 2

```{questionnote}

**Task - discount:**

One manufacturer offers goods at a price of 10 euros a piece, and for orders of 50 or more pieces a 10% discount is granted. Several buyers announced that they were coming to buy a certain number of pieces. The customer names and quantities requested are given at the beginning of the program.

Write a function which prints how much the certain customer should pay for the given name of the customer and the quantity of goods .
```

The customer name is passed to the function here for print purposes only. The price of goods is calculated on the basis of quantity, which is passed on to the function as a second argument.

```{py-code} 7

# define the function print_price

customers = ('Oliver', 'Freddie', 'Sophia', 'Lucas')
quantities = (70, 28, 150, 6)
n = len(customers)
for i in range(n):
    print_price(customers[i], quantities[i])

```

```{questionnote}

**Task - text underlining:**

Write the *underline(text)* function, which shows the given text underlined.

```

**Hint:** The *underline* function should consist of only two *print* statements. The first statement should print the given text, and the second one should print the line. You can get a string containing a line by multiplying the string `'-'` by the length of the given string.

```{py-code} 8

# define the function 'underline'

underline("From Celsius to Fahrenheit:")
for c in range(15, 46, 5):
    print(c, '°C =', round(c * 9 / 5 + 32, 1), '°F.')
print()

underline("From Fahrenheit to Celsius:")
for f in range(50, 111, 10):
    print(f, '°F =', round((f-32) * 5 / 9, 1), '°C.')
```

% commented out
%
% def underline(text):
%     print(text)
%     print('-' * len(text))