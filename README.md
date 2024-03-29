# Advent of Code

Collection of my attempts at doing some Advent of Code challenges in Python.

## Code structure

For each task there is a function that cleans the Puzzle data (unless the input data is just one long string, ref. 2022, day 6), and one function per part A and B that takes the same cleaned input data, with some minor variation for puzzles where part B requires some input from part A (ref. 2021, day 9).

For each task there is a corresponding test that unit tests the data cleaning functions and parts 1 and 2 using both the provided sample data for each question and with the final answer provided per Puzzle. This is to allow for (slightly) easier refactoring of the code at a later stage.

# Solved Tasks

## 2023 AOC

| Day   | Stars         | Comment
|-------|---------------|---------
| 1     | :star::star:  | Straightforward solution for part 1. For part 2, need to be careful with replacing since the correct decoding of e.g "nineight" is 98.
| 2     | :star::star:  | The pattern for each row was nice to evaluate using regex.
| 3     | :star::star:  | Interesting take here is to isolate the symbols in a dict, and use regex `finditer` to create adjacency masks for each number. The `&` operator isolates any adjacent symbol coordinates, and the group value is assigned to the symbol.
| 4     | :star::star:  | Mostly about looping control. Initially did a regex solution but this was overkill.
| 5     | :star::star:  | Learning the `reduce` function. Nice!
| 6     | :star::star:  | Simple and straightforward!
| 7     | :star::star:  | Used a nice `maketrans` trick here to allow lexicographic sorting. Made a function to calculate the hand type - lack of brains.
| 8     | :star::star:  | Some graph traversals with a twist. Was stuck on part 2 but figured I should check for regularity in solution steps per node. After I confirmed regularity for all nodes in part 2 I initially implemented LCM manually at first - but the `math` module had my back all this time.. Full disclosure: least common multiple was new for me!


## 2022 AOC (Incomplete)

| Day   | Stars         | Comment 
|-------|---------------|---------
| 1     | :star::star:  | Straightforward solutions for day 1.
| 2     | :star::star:  | Using an approach with string indexing and integer division based on game score order.     
| 3     | :star::star:  | First part in a one-liner (added a verbose solution too), second part using `set.intersection()` on an unpacked list of sets, on elf groupings of 3.  
| 4     | :star::star:  | Very similar parts 1 (full overlap) and 2 (partial overlap). Made a simple line processing function with outputs depending on part 1 or part 2 requirements, and used this with `map` (and a `lambda` for part 2).
| 5     | :star::star:  | Worst part was to wrangle the input data into something useable. List slicing galore!
| 6     | :star::star:  | Regexed part 1, realized in part 2 that that was stupid. Implemented something more straightforward for part 2.
| 7     | :star::star:  | Another day where parsing the input data properly is way more difficult than the actual parts 1 and 2!
| 8     | :star::star:  | After solving, I refactored the code with some inspiration from other solutions that followed the same base logic. I avoided the crazy `numpy` solutions since I don't have time to get comfortable with `np` syntax at this point, but probably should do that sooner or later.
| 9     | :star::star:  | This was easy enough, refactored part 1 after reading part 2 text to generalize snek length. List of neighbors threw me off, should make a utils that gives back coordinates for the different "types" of neighbor, e.g. yield neighbors for U/D/L/R, yield neighbors for diagonals, etc.
| 10    | :star::star:  | Created generator that yielded cycle and register value. From there it was a party of modulo to get the correct outputs. Ugly but works!
| 11    | :star::star:  | Figured out the common denominator trick to make part 2 work - but that doesn't help when I ran the code on processed monkeys from Part 1!
| 12    | :star::star:  | Another task where I didn't read the task properly - took a while to understand that any elevation *drop* was acceptable. Part 2 was originally iterating the `climb` function for all `a`-nodes but I read a tip on Reddit that said if you had implemented a Dijkstra type algorithm, the easiest was to pass all `a`-nodes as live in the initial queue to get solve in one go.
| 13    | :star::star:  | Lots of struggling to get the recursion right. Sorting all the signals would be easier if I hadn't created infinite `enumerate` loops by adding items to the same list.. 

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
| 10    | :star::star:  | Keep track of the order of opening brackets and popping that list vs. a dict of bracket pairs proved to be an efficient strategy. Could be written more concise, but is at least quite readable. 
| 11    | :star::star:  | Same algorithm for both parts, but slightly different outputs. Learned some nice tricks related to `octopi.get` to only return "truthy neighbors" to avoid re-incrementing already flashed octopi.
| 12    | :star::star:  | Had to refactor my initial solution after seeing `/u/4HbQ`s solution on Reddit. I find recursion hard and this was a great example for me to understand.
| 13    | :star::star:  | Numpy is still difficult, but refactoring my old solutions from last year is helping.
| 14    | :star::star:  | Interesting exercise with dictionary abuse. First time I did this last year I created new strings like in the cheeky example but hit a brick wall for part 2.. obviously..
