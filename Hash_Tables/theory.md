# About
A data structure that stores key-value pairs where the key is sent to a hash function that performs arithemetic operations to generate a hash value, which is the index of the key-value pair

## Visualization

## Components
* Hash function
* Array/List

## Time Complexity
| Operation | Average | Worst | 
| ------------- | ------------- | ------------- |
| Search | O(1) | O(n) | 
| Insertion | O(1) | O(n) |
| Deletion | O(1) | O(n) |

## Advantages
* All operations are around O(1) assuming the hash table is built properly 

## Disadvantages 
* Can be memory intensive 
* Need to design properly

## Uses
* 

# Important Terminology/Concepts 
## Hash function
* A function that determines the index of the key-value pair
* An efficient hash function is the root of creating a good hash table

### Properties of a Good Hash Function
* Fast computation
* Minimize colissions/duplicate values -> allows for nearly constant time access
* One way: you're unable to identify the key given the value 

## Hash Collision: 
* Two keys get mapped to the same index 
* You can choose to either have only one key-value pair per bucket or allow the bucket to have multiple key-value pairs 
* Regardless of how "good" your hash function, this is evitable 

### Methods to Minimize Collisions
#### Liner Probing
If a pair generates a hash value that already exists/is occupied, search linearly for the next free slot in the table

#### Quadratic Probing
If a pair generates a hash value that already exists/is occupied, search quadratic (n) for the next free slot in the table. This means that we search for the i^2th slot. This means we try all positions at (hash(x + 1*1)) and if full, then we search for (hash(x + 2*2)) % S where S represents the size and so on until an empty slot is found. This costs O(N * L) but takes no space.

```
def hashing(table, tsize, arr, N):
     
    # Iterating through the array
    for i in range(N):
         
        # Computing the hash value
        hv = arr[i] % tsize
 
        # Insert in the table if there
        # is no collision
        if (table[hv] == -1):
            table[hv] = arr[i]
             
        else:
             
            # If there is a collision
            # iterating through all
            # possible quadratic values
            for j in range(tsize):
                 
                # Computing the new hash value
                t = (hv + j * j) % tsize
                 
                if (table[t] == -1):
                     
                    # Break the loop after
                    # inserting the value
                    # in the table
                    table[t] = arr[i]
                    break

```

#### Chaning
The hash table will be a linked list (or just a list) and we just add the value to the end of that bucket

#### Resizing
* You can increase the size of the hash table 
* You may need to rehash after a threshold (i.e load factor) reaches a certain point 
    * The most common value is 0.75. This means that once 70% of the space is occupied, the size of the hash table will be doubled. Note that this can be eventually intensive. 

# Sources
https://www.youtube.com/watch?v=S5NY1fqisSY&list=WL&index=1

https://www.educative.io/edpresso/what-is-a-hash-table

https://en.wikipedia.org/wiki/Hash_function

https://www.geeksforgeeks.org/quadratic-probing-in-hashing/