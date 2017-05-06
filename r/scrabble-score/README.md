# Scrabble Score

Given a word, compute the scrabble score for that word.

## Letter Values

You'll need these:

```plain
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

## Examples
"cabbage" should be scored as worth 14 points:

- 3 points for C
- 1 point for A, twice
- 3 points for B, twice
- 2 points for G
- 1 point for E

And to total:

- `3 + 2*1 + 2*3 + 2 + 1`
- = `3 + 2 + 6 + 3`
- = `5 + 9`
- = 14

## Extensions
- You can play a double or a triple letter.
- You can play a double or a triple word.

## Installation
See [this guide](https://github.com/exercism/xr/blob/master/docs/INSTALLATION.md) for instructions on how to setup your local R environment.

## How to implement your solution
In each problem folder, there is a file named `<exercise_name>.R` containing a function that returns a `NULL` value. Place your implementation inside the body of the function.

## How to run tests
Inside of RStudio, simply execute the `test_<exercise_name>.R` script. On the command-line, you can also run `Rscript test_<exercise_name>.R`.

## Source

Inspired by the Extreme Startup game [https://github.com/rchatley/extreme_startup](https://github.com/rchatley/extreme_startup)

## Submitting Incomplete Problems
It's possible to submit an incomplete solution so you can see how others have completed the exercise.

