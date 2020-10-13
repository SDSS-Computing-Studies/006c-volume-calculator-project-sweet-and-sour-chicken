## SDSS Computing Studies Python Assignment
### Assignment #6c Global and Local Variables (Total Marks 5)

Objectives:
* Understand what is meant by variable scope
* Create and work with local variables
* Define a global variable from within a function

Think about some of the math words that you may have used when 
solving a problem: variable, area, length, perimeter, hypotenuse
Now consider the following math problem.

Find the area of a circle with a radius of 10cm.
Since the formula to calculate the area of a circle is A = pi * r^2
we might need to know a value for pi, a value for r and then calculate A.
However, we don't need to know the perimeter, or hypotenuse or many other
math words, so we don't even consider them.  In fact, if we were to create
a function that helped us calculate the area of a circle, we would only
assign variables for A, pi and r, and when we go leave the problem to go
back to our assignents, we might forget all about those variables we
just created.

This is the concept of a LOCAL variable.  When you create a variable
INSIDE a function, it is a local variable, and does not exist outside
of the variable.  This is good because then we can save on memory (the
variable is created when the function starts and then destroyed when the 
function is finished) but also keeps us from having variables that are
floating around in the background that might mess up some of our
other functions.

The takeaway message here is: variables should only be created where they
are needed, and then destroyed. It's kind of like the concept of
"put away your toys when you are finished playing with them".

In Python, if you declare a variable OUTSIDE of a function, it is considered
a GLOBAL variable, and can be used in every function.  It is persistent in 
memory as long as the entire program is running.

Variable SCOPE refers to whether a variable is a local variable or a global variable.
Consider the code in the file example1.py


### XX Tasks

##### Task 1
(x points) 

