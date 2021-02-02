# 		Project 0x12. Javascript - Warm up

## Resources:

* [Writing JavaScript Code](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg)
* [Variables](https://intranet.hbtn.io/rltoken/iE6zaLw7pybp648IfRmk5Q)
* [Data Types](https://intranet.hbtn.io/rltoken/4td1BbZAYn4Dldi6k0CY7A)
* [Operators](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg)
* [Operator Precedence](https://intranet.hbtn.io/rltoken/ALCoiVRvxmsjdqCUdWC_lg)
* [Controlling Program Flow](https://intranet.hbtn.io/rltoken/Nlfhdy6Thyu_WgtBSqoAUw)
* [Function](https://intranet.hbtn.io/rltoken/Ta66PZ6_16K3q99oELvjkQ)
* [Objects and Arrays](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ)
* [Intrinsic Objects](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ)
* [Module patterns](https://intranet.hbtn.io/rltoken/mduSK-WOoRe6WohU1p2zZQ)
* [var, let and const](https://intranet.hbtn.io/rltoken/kNWuHjyUvjr74wU2hBqd_A)
* [Javascript Tutorial](https://intranet.hbtn.io/rltoken/qkp1hdLiI8DJje88bxcL6w)
* [Modern JS](https://intranet.hbtn.io/rltoken/ieSajamJQ-Nv3XzcS_d5lA)



## General Learning Objectives:

### Why Javascript programming is amazing:
Javascript is the most popular language among developers, maybe because it is fun, interactive and dynamic, also intuitive and relatively easy to learn for beginners.  Being the language that browsers use, you don't have install a bunch of programs before you even begin. Having  a graphical UI thats fun and easy to manipulate. JavaScript has the largest and most active repository of library code in the world and that is a plus! 

### How to run a Javascript script:
In a browser you have two options. You can either put it inside a script element anywhere inside an HTML document, or put it inside an external JavaScript file (with a . js extension) and then reference that file inside the HTML document using an empty script element with a src attribute.

### How to create variables and constants:
- To create a variable in JavaScript, use the let keyword.
- To declare a constant (unchanging) variable, use const instead of let.

### What are differences between var, const and let:
var declarations are globally scoped or function scoped while let and const are block scoped. var variables can be updated and re-declared within its scope; let variables can be updated but not re-declared; const variables can neither be updated nor re-declared. They are all lifted up  to the top of their scope.

### What are all the data types available in Javascript:
There are six basic data types in JavaScript which can be divided into three main categories: primitive (or primary), composite (or reference), and special data types. String, Number, and Boolean are primitive data types. Object, Array, and Function (which are all types of objects) are composite data types.
- undefined : typeof instance === "undefined"
- Boolean : typeof instance === "boolean"
- Number : typeof instance === "number"
- String : typeof instance === "string"
- BigInt : typeof instance === "bigint"
- Symbol : typeof instance === "symbol"

### How to use the if, if ... else statements:
In JavaScript we have the following conditional statements:

- Use *if* to specify a block of code to be executed, if a specified condition is true
- Use *else* to specify a block of code to be executed, if the same condition is false
- Use *else* if to specify a new condition to test, if the first condition is false

### How to use comments:
To create a single line comment in JavaScript, you place two slashes "//" in front of the code or text you wish to have the JavaScript interpreter ignore. When you place these two slashes, all text to the right of them will be ignored, until the next line.

### How to affect values to variables:
You can assign a value to a variable using equal to (=) operator when you declare it or before using it.

### How to use while and for loops:
- while loops through a block of code once; then the condition is evaluated. If the condition is true, the statement is repeated as long as the specified condition is true. for  loops through a block of code until the counter reaches a specified number.

### How to use break and continue statements:
The continue statement (with or without a label reference) can only be used to skip one loop iteration. The break statement, without a label reference, can only be used to jump out of a loop or a switch.

### What is a function and how do you use functions:
A function is composed of a sequence of statements called the function body. Values can be passed to a function, and the function will return a value. In JavaScript, functions are first-class objects, because they can have properties and methods just like any other object.

### What does a function that does not use any return statement return:
A function without a return statement (or one that ends its execution without hitting one) will return *undefined.*

And if you use the unary negation operator twice on an undefined value, you will get *false.*

### Scope of variables:
The scope of a variable declared with *var* is its current execution context and closures thereof, which is either the enclosing function and functions declared within it, or, for variables declared outside any function, global

### What are the arithmetic operators and how to use them:
Arithmetic operators are the basic operators that we use to do sums in JavaScript:

*Operator*	*Name*                  	    *Purpose*	                                   *Example*
+	        Addition                            Adds two numbers together.	                   6 + 9
-	        Subtraction	                    Subtracts the right number from the left.      20 - 15
*	        Multiplication	                    Multiplies two numbers together.	           3 * 7
/	        Division	                    Divides the left number by the right           10 / 5
%	        Remainder (sometimes called modulo) Returns the remainder left over after          8 % 3 (returns 2, as three goes into 8 
                                                    you've divided the left number into a number   twice, leaving 2 left over).
                                                    of integer portions equal to the right number. 

**	       Exponent	                            Raises a base number to the exponent power, 
                                                    that is, the base number multiplied by itself, 
                                                    exponent times. It was first Introduced in 
                                                    EcmaScript 2016.	                            5 ** 2 (returns 25, which is the same                                                                                                     as 5 * 5).

### How to manipulate dictionary:
Dictionary object is used to store information in name/value pairs (referred to as key and item). The Dictionary object might seem similar to Arrays, however, the Dictionary object is a more desirable solution to manipulate related data.

Comparing Dictionaries and Arrays:

Keys are used to identify the items in a Dictionary object
You do not have to call ReDim to change the size of the Dictionary object
When deleting an item from a Dictionary, the remaining items will automatically shift up
Dictionaries cannot be multidimensional, Arrays can
Dictionaries have more built-in functions than Arrays
Dictionaries work better than arrays on accessing random elements frequently
Dictionaries work better than arrays on locating items by their content

### How to import a file:
To include an external JavaScript file, we can use the script tag with the attribute src . You've already used the src attribute when using images. The value for the src attribute should be the path to your JavaScript file. This script tag should be included between the <head> tags in your HTML document.

