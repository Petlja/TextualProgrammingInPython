# Tasks with loading data

## Example

```{questionnote}

**Example - paintwork**

Philip is preparing to paint the ceiling in one room. In order to know how much paint to buy, he needs to know the dimensions of the room and how many square meters one kilogram of paint covers. Write a program that loads the length of the room, the width of the room, an area that can be covered by one kilogram of paint, and prints the required number of kilograms of paint.
```

Solution:

```{py-code} 7

length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
area_per_kg = float(input("Enter the area covered by 1 kg of paint: "))
needed_kg = length * width / area_per_kg
print(needed_kg, "kg of paint is required.")
```

## Practice tasks

```{questionnote}

**Task - rabits**

The rabbit population on one island is being doubled every year. Write a program that loads the current number of rabbits on the island and the number of years, and prints how many rabbits would be on the island in a given number of years if they continue to reproduce at the same pace.
```

```{py-code} 8

# insert your code here

```

```{questionnote}

**Task - Buying a car**

John buys the car in installments. Write a program that sequentially loads the contract price, the amount of one installment and the number of installments, and prints how much more John will pay in total over the price stated in contract.
```

```{py-code} 9

# insert your code here
```
