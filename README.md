# Advent of Code

Collection of my attempts at doing some Advent of Code challenges in Python.

## Code structure

For each task there is a function that cleans the Puzzle data (unless the input data is just one long string, ref. 2022, day 6), and one function per part A and B that takes the same cleaned input data, with some minor variation for puzzles where part B requires some input from part A (ref. 2021, day 9).

For each task there is a corresponding test that unit tests the data cleaning functions and parts 1 and 2 using both the provided sample data for each question and with the final answer provided per Puzzle. This is to allow for (slightly) easier refactoring of the code at a later stage.

# Solved Tasks

## 2022 AOC

| Day   | Stars         | Comment 
|-------|---------------|---------
| 1     | :star::star:  | Straightforward solutions for day 1.
| 2     | :star::star:  | Using an approach with string indexing and integer division based on game score order.     
| 3     | :star::star:  | First part in a one-liner (added a verbose solution too), second part using `set.intersection()` on an unpacked list of sets, on elf groupings of 3.  
| 4     | :star::star:  | Very similar parts 1 (full overlap) and 2 (partial overlap). Made a simple line processing function with outputs depending on part 1 or part 2 requirements, and used this with `map` (and a `lambda` for part 2).
| 5     | :star::star:  | Worst part was to wrangle the input data into something useable. List slicing galore!
| 6     | :star::star:  | Regexed part 1, realized in part 2 that that was stupid. Implemented something more straightforward for part 2.
| 7     | :star::star:  | Another day where parsing the input data properly is way more difficult than the actual parts 1 and 2!

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
| 9     | :star::star:  | Part 1 was fairly easy, but part 2 was my first foray ever into flooding algorithms and (programmatic) recursion, and was difficult to get right.
