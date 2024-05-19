**ORION**

Orion is a custom, statically typed programming language that mixes features from different languages such as Python, Java, and Assembly

## Features

- Statically typed
- Procedural
- Uses code blocks and labels

## Example

see `example.txt`

## How to run

1. In the terminal navigate to this directory and run `python3 orion.py <filename>`

## Syntax

- Lines are terminated by a semicolon with the exception of labels, which are terminated by a colon

- - `label:`
- - `function();`

- Comments are denoted by a `#` and are ignored by the interpreter

- - `function(); # This is a comment`

- Whitespace is ignored by the interpreter

- - `       function();         ` is the same as `function();`

- Functions are called by the function name followed by parentheses containing the arguments

- - `function(arg1, arg2);`

- Variables are declared with the data type followed by the variable name

- - `int x;`

- The assignment operator is `=`
 
- - `x = 5;`

- Labels and jumps control the flow of the program - jump around the code by using the `jump()` function to jump to a label

- - `jump(label);`

- If statement blocks are controlled by the inbuilt `jumpif(condition, label)` function

- - `jumpif(x == 5, label);`
- - condition can be any boolean expression

- Labels do NOT interfere with the regular program flow, they are simply markers to jump to

- The `out(string)` function is used to output to the console

- - `out("Hello, World!");`

- The `in()` function is used to get input from the user

- - `int x = in();`




