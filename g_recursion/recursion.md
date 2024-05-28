## Recursion

### Overview

Recursion occurs when a function calls itself repeatedly until it reaches a **specified stopping condition**.
Such a function is called a **recursive function**.

### Why use Recursion ?
1. Recursive code is generally shorter and easier to write than iterative code.
2. Recursion is the most useful for tasks that can be defined in terms of similar subtasks.

### Format of a Recursive Function

#### Base Case
The base case is where all further calls to the same function stop, meaning that it does not make any subsequent recursive calls.
#### Recursive Case
The recursive case is where the function calls itself repeatedly until it reaches the base case.


### Syntax of a Recursive Function
```plain
def RecursiveFunction() :
  # Base Case
  if <baseCaseCondition> :
    <return some base case value>

  # Recursive Case
  else :
    <return(recursive call and any other task)>
```

### Use Where Appropriate

#### Problem Breaks Down Into Smaller Similar Subproblems
The most obvious indication that you should use recursion is when that problem can be broken down into smaller subproblems. It is likely that a problem can be solved using recursion when you observe a pattern of that problem breaking down into similar subproblems.

#### Problem Requires an Arbitrary Number of Nested Loops
> If you know the number of loops that need to be nested, use the iterative approach. If you do not know the number of loops that need to be nested, use the recursive method.

To solve some problems, you might have to nest an arbitrary number of loops. However, since we do not know the number of loops, the solution will get complicated. Such problems can be more easily solved using recursion.
