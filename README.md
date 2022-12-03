# Advent of Code

Collection of my attempts at doing some Advent of Code challenges in Python.

## Code structure

For each task there is a function that cleans the Puzzle data, and one function per part A and B that takes the same cleaned input data.

For each task there is a corresponding test that uses the sample data and answer provided per Puzzle.

# Solved Tasks

## 2022 AOC

| Day   | Stars         | Comment 
|-------|---------------|---------
| 1     | :star::star:  | Straightforward solutions for day 1.
| 2     | :star::star:  | Using an approach with string indexing and integer division based on game score order.     
| 3     | :star::star:  | First part in a one-liner (added a verbose solution too), second part using `set.intersection()` on an unpacked list of sets, on elf groupings of 3.  

## 2021 AOC (Incomplete)

| Day   | Stars         | Comment 
|-------|---------------|---------
| 1     | :star::star:  | Solved using simple list comprehensions.
| 2     | :star::star:  | Using `if-elif` to handle submarine instructions.
| 3     | :star::star:  | Some effort going in to handling data in a compact way. Could be more readable.
| 4     | :star::star:  | Very fun problem where it makes sense to model the boards as a dict instead of nested lists.
| 5     | :star::star:  | A bit messy to follow the logic, but more compact than evaluating each line for being either straight or diagonal.
| 6     | :star::star:  | Avoid the temptation to store each fish as an element in a list...
| 7     | :star::star:  | Simpler problem compared to the previous days, but the solution is not of closed form. Mean sometimes does not work, and it is also necessary to check the next position to find the true minimum.
| 8     | :star::star:  | Fun implementation of `/u/4HbQ`s amazing `match` solution using lengths known digit masks from `"1"` and `"4"` to uniquely identify each display digit.
