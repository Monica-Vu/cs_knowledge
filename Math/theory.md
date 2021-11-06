# Tips 
* If the code involves division or modulo, check for the `0` case 
* When a question involves `a multiple of a number`, modulo might be useful ex/ FizzBuzz
* **For strongly typed languages**, consider overflow or underflow 
**Overflow:** When assign a variable more than the maximum permissible value
**Underflow:** When assign a variable more than the maximum permissible value
    * Ask your interviewer if you actually need to handle this
* Floating point numbers might have rounding mistakes so consider using epsilon comparisons rather **ex/ `abs(x - y) <= 10e7` rather than `x == y`**

# Common Formulas
* Sum of 1 to N = ((n + 1) * n) / 2
* Sum of Geometric Series  = 2^0 + 2^1 + 2^2 + 2^3 + ... 2^n = 2^n+1 - 1
* Permutations of N = N! (N - K)! where `K` is the number of objects chosen 
* Combinations of N = N! (K! *(N - K)!) where `K` is the number of objects chosen 

# Typical Test Cases 
* Negative numbers
* Zero
* Integers 
* Floating point numbers 