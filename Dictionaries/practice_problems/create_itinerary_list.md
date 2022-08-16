# Problem
Given a list of objects in the form of "source : destination", each representing a leg of a trip, give the output of the trip itinerary. 

**Example:**
Input: [ "YVR:SFO", "YYZ:NYC", "SFO:YYZ" ] 
Output: [YVR, SFO, YYZ, NYC]

# Thought Process 
1. Questions / Assumptions
- Will the input be not empty and always valid (only strings of places seperated by a colon)

Input: list of strings of source to destination seperated by a comma, our starting place

Output: A list of the trip iternary, representing where we been

2. Brainstorm + Algorithm
2.1 Convert to a Dictionary 
- Intialize an empty dictionary called trip 
- Iterate through each item and split it by comma
- The result of the above would be a list of two elements. The first one is our source and the second one is our destination.
- As we iterate through, we create key-value pairs for our dictionary. First item = key, second item = value
- Return that at the start

2.2 Convert to List
- Intialize empty list
- Put start 
- while the trip dictionary is not empty:
   - set the destination as the value when we get trip of source --> seperate function
   - append the destination
   - delete the key-pair with the source 
   - source as destination

3. Code solutions.

4. Create test cases: 
* Empty List
* Start is None
* One item
* >= 2 items
* Long list of items 
* Maybe elements of a different type from expected 

5. State complexity.
**Time Complexity:** O(n) -> We need to iterate through the object 
**Space complexity**: O(n) -> We store all the objects as keys

6. Discuss improvements (and implement if time permitted).