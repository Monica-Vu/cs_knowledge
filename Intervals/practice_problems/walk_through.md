# Problem
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
**Example 1:**
Input: intervals = [[1,3],[2,6],[8,10],[15,18]] 
Output: [[1,6],[8,10],[15,18]] 
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

**Example 2:**
Input: intervals = [[1,4],[4,5]] 
Output: [[1,5]] 
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
**Constraints:**
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

# Steps
0. Re-read question and take notes of what you feel like is the most important. Put these into your own words to the interviewer as needed. 

1. Ask questions and clarify anything. Make assumptions as needed.
**Input:** A list of 2-item list 
**Output:** A list of 2-item list where there are no intersections or intervals

**Questions**
* Will the intervals be in order? (based on examples) 
Let's assume not and that we will have to consider it ourselves.

**Assumptions**
* Inputs are always valid 

2. Brainstorm ideas. Say everything even if you're 100% you're correct. Ideally, your interviewer will be helpful. 
**Brainstorm**
* We're unsure if the list is sorted. What would we have to do if it was not sorted? If it's not sorted, we would have to iterate through the rest of the list and find the lowest start value and then compare it against our current merged interval. If it was sorted, we just need to check the next item.
* If it was sorted, we can take the first item as the input, get the start value of the item. If that start value is greater than the end value of the last item in our current output, then we know it's seperate and just append it. Otherwise, we get the bigger end value.

3. Write a clear algorithm
**Algorithm**
* [If required] return list if its length is 1 or less (no need to even sort)
* Sort the input (feel free to store it in a seperate interval)
* Put the first item in the output list
* Iterate through the rest of the list
    * Get the last ending value of the last item in our output list 
    * If the last ending value is greater than the start value, it indicates that there's an intersection. The ending value should be the greater of the two.  
    * Otherwise, we can append it
* Return the output list

4. Write your code. Ideally, this should be pretty straightforward if you are familiar with your language. 
**Solution#1 -- Using Python Indexing**
```
def merge(intervals):
    if len(intervals) <= 1:
        return intervals 
    
    # alternative: sorted_intervals = sorted(intervals, key=lambda i: (i[0], i[1]))
    sorted_intervals = sorted(intervals)
    output = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_ending_value = output[-1][1]

        if start <= last_ending_value:
            output[-1][1] = max(last_ending_value, end)
        else:
            output.append([start, end])
    return output
```
**Solution#1 -- Using Python Indexing**
5. Develop your test cases. 
* Two Intervals 
* More than two intervals with non-overlapping
* More than four intervals with two or more non-overlapping
* More than four intervals with two or more non-overlapping (and one case must completely overlap another)
* Duplicate intervals  

6. Analyze your code
**Time Complexity: O(n * log N)** --> need to iterate through array and sort it (can cost up to O(n) as well)
**Space Complexity: O(n)** --> worst case scenario is that none of the intervals overlap but we may need to store the sorted result if we don't want to overlap the result

7. At the minimum, discuss possible improvements

# Sources
https://youtu.be/44H3cEC2fFM
https://youtu.be/qKczfGUrFY4