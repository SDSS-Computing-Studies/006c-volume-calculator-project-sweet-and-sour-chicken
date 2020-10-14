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


### 1 Assignment 

Create a program that will have the user enter in important measurements for a geometric
shape and then calculate the volume of that shape.  This will be an assignment done in groups
of up to 3 people MAXIMUM. ( You can work individually or in pairs if you wish)

When you create your assignment, you will be asked to join or create a team.  You will need
to make sure your team name is correct because you will not be able to join a different
team if you spell it incorrectly.

You should divide up the work so that each of you is working on different parts of the program.
Some basic assignment functions have been included in the file:

assignment.py

Criteria:
* The program should have a title screen
* The program should have the option to show instructions or provide help
* The program should repeat when completed unless the user chooses to quit
* The program should provide clear options for available commands when required
* Each function should be documented
* There should be some external documentation included about what the program does and how it works. (Like a user manual)
* Your documentation may be a text file, or may be created in word and drag/dropped into your Github folder
* The function for each shape (to determine volume) should not have any inputs or print statements. It is JUST for calculations
* There should only be 1 function that asks the user to input data. It will ask the appropriate number of questions and generate a list of appropriate data



