# Advent of Code

Collection of my attempts at doing some Advent of Code challenges in Python.

## 2023 AOC

| Day   | Comment
|-------|---------
| 1     | Straightforward solution for part 1. For part 2, need to be careful with replacing since the correct decoding of e.g "nineight" is 98.
| 2     | The pattern for each row was nice to evaluate using regex.
| 3     | Interesting take here is to isolate the symbols in a dict, and use regex `finditer` to create adjacency masks for each number. The `&` operator isolates any adjacent symbol coordinates, and the group value is assigned to the symbol.
| 4     | Mostly about looping control. Initially did a regex solution but this was overkill.
| 5     | Learning the `reduce` function. Nice!
| 6     | Simple and straightforward!
| 7     | Used a nice `maketrans` trick here to allow lexicographic sorting. Made a function to calculate the hand type - lack of brains.
| 8     | Some graph traversals with a twist. Was stuck on part 2 but figured I should check for regularity in solution steps per node. After I confirmed regularity for all nodes in part 2 I initially implemented LCM manually at first - but the `math` module had my back all this time.. Full disclosure: least common multiple was new for me!
| 9     | I forgot to write a blurb about this one, and now I must admit the solution is a mouthful!
| 10    | Came back to tackle this in November 2024, and went for readability instead of concise code. Also played around with functions that "cleaned up" the pipe chart and colored the pipe elements and the enclosed parts of the grid.
| 11    | Much easier than day 10! The shortest path is just the sum of absolute difference in number of rows and columns between each point. By first evaluating which rows and columns are subject to spatial expansion, you can loop over the `range(min, max)` for rows/columns and sum 1 per "non-expanded" row/column and sum whatever expansion factor for the spatially challenged rows/columns - in part 1 that is 2, in part 2 that is 1 million.
| 12    | Brute forced part 1 but that was not possible for part 2. I looked at the subreddit for inspiration and struggled understanding this problem (I am not a developer after all!) until I found a [great writeup](https://advent-of-code.xavd.id/writeups/2023/day/12/) by [David Brownman](https://github.com/xavdid). This broke down the problem into understandable chunks - a lot of the solutions in the AOC megathreads are written "shorthand" and with some flair - so deciphering what happens is often difficult, so it's great to have found this resource for future reference!
| 13    | This problem was not that difficult. The most troublesome part was to get the generator that yielded mirror slices right. I rewrote a bit for part 2 to solve generally with X expected flaws - on the assumption that all tiles would have mirror locations changed, and that none of the part 1 values were correct.


## 2022 AOC 

| Day   | Comment 
|-------|---------
| 1     | Straightforward solutions for day 1.
| 2     | Using an approach with string indexing and integer division based on game score order.     
| 3     | First part in a one-liner (added a verbose solution too), second part using `set.intersection()` on an unpacked list of sets, on elf groupings of 3.  
| 4     | Very similar parts 1 (full overlap) and 2 (partial overlap). Made a simple line processing function with outputs depending on part 1 or part 2 requirements, and used this with `map` (and a `lambda` for part 2).
| 5     | Worst part was to wrangle the input data into something useable. List slicing galore!
| 6     | Regexed part 1, realized in part 2 that that was stupid. Implemented something more straightforward for part 2.
| 7     | Another day where parsing the input data properly is way more difficult than the actual parts 1 and 2!
| 8     | After solving, I refactored the code with some inspiration from other solutions that followed the same base logic. I avoided the crazy `numpy` solutions since I don't have time to get comfortable with `np` syntax at this point, but probably should do that sooner or later.
| 9     | This was easy enough, refactored part 1 after reading part 2 text to generalize snek length. List of neighbors threw me off, should make a utils that gives back coordinates for the different "types" of neighbor, e.g. yield neighbors for U/D/L/R, yield neighbors for diagonals, etc.
| 10    | Created generator that yielded cycle and register value. From there it was a party of modulo to get the correct outputs. Ugly but works!
| 11    | Figured out the common denominator trick to make part 2 work - but that doesn't help when I ran the code on processed monkeys from Part 1!
| 12    | Another task where I didn't read the task properly - took a while to understand that any elevation *drop* was acceptable. Part 2 was originally iterating the `climb` function for all `a`-nodes but I read a tip on Reddit that said if you had implemented a Dijkstra type algorithm, the easiest was to pass all `a`-nodes as live in the initial queue to get solve in one go.
| 13    | Lots of struggling to get the recursion right. Sorting all the signals would be easier if I hadn't created infinite `enumerate` loops by adding items to the same list.. 

## 2021 AOC 

| Day   | Comment 
|-------|---------
| 1     | Solved using simple list comprehensions.
| 2     | Using `if-elif` to handle submarine instructions.
| 3     | Some effort going in to handling data in a compact way. Could be more readable.
| 4     | Very fun problem where it makes sense to model the boards as a dict instead of nested lists.
| 5     | A bit messy to follow the logic, but more compact than evaluating each line for being either straight or diagonal.
| 6     | Avoid the temptation to store each fish as an element in a list...
| 7     | Simpler problem compared to the previous days, but the solution is not of closed form. Mean sometimes does not work, and it is also necessary to check the next position to find the true minimum.
| 8     | Fun implementation of `/u/4HbQ`s amazing `match` solution using lengths known digit masks from `"1"` and `"4"` to uniquely identify each display digit.
| 9     | Part 1 was fairly easy, but part 2 was my first foray ever into flooding algorithms and (programmatic) recursion, and was difficult to get right.
| 10    | Keep track of the order of opening brackets and popping that list vs. a dict of bracket pairs proved to be an efficient strategy. Could be written more concise, but is at least quite readable. 
| 11    | Same algorithm for both parts, but slightly different outputs. Learned some nice tricks related to `octopi.get` to only return "truthy neighbors" to avoid re-incrementing already flashed octopi.
| 12    | Had to refactor my initial solution after seeing `/u/4HbQ`s solution on Reddit. I find recursion hard and this was a great example for me to understand.
| 13    | Numpy is still difficult, but refactoring my old solutions from last year is helping.
| 14    | Interesting exercise with dictionary abuse. First time I did this last year I created new strings like in the cheeky example but hit a brick wall for part 2.. obviously..
