# Dynamic Programming
**Definition:** Break down an optimization problem into simplier sub-problems and store the solutions of these sub-problems 

**Memoization:** A method that involves storing the results of previous function calls to speed up future calculations.

## Example Problems
* Asking for a maximum or minimum given certain constraints 

# Process 
1. Identify the sub-problems via words. Figure out how you can identify which sub-problem is needed to solve the problem. 

2. Write the sub-problem as a recurring mathmatical decision (mathemtical recurrence). 

Think about what decision you need to make at every step. If your algorithm is at step i, what information do you need to decided what to do at step i + 1? What information did step i need to do in step i -1? For example, we could decide to add an item to our potential maximum subarray or omit it. 

If you find it hard to write code with the mathematical formula, you may be using the wrong formula. 

3. Solve the problem using what you did in steps 1 and 2.

4. Determine the size of the memoization list and the direction it should be filled. This usually equals to the number and size of variables that the problem requires. 

5. Code your solution. Most of the information should be discovered from Steps 2 to 4 and we just need to add the base case.


# Sources
https://www.freecodecamp.org/news/demystifying-dynamic-programming-3efafb8d4296/