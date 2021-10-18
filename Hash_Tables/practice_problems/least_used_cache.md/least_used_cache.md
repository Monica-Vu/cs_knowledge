# Problem
Describe an implementation of a least-frequently-used cache, and big-O notation of it.

# Description of DTS
A least-frequently-used (LFU) cache is an algorithm in which the least frequently used item in the cache is removed via an eviction algorithm once the cache's capacity limit is reached. This is done by keeping tracking of how much each item is used. 

# Advantages
* Efficient in cases where access patterns of cached objects do not change often 

# Use Cases
* Caching an image of a frequently visisted website  on a Content Delievery Network to decrease amount of loading 
* Removing assets (ex/ images) that will only be accessed for a limited amount of time. These assets' usage will decrease and eventually get deleted automatically. Think of a new product released or news.

# Implementation
## Data Structures
* Two doubly linked list
(1) Frequency List that contains the frequency of each item and pointer to ancestor of frequency 
* **Hash Table:** stores all items with a key that is processed via a hash function with the value as the item

## How it Works
Everytime an item in the list is accessed, it gets moved to the tail of the next parent frequency pointer.

## Components 
```
class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {} # represents {key: cache_node}
        self.capacity = capacity
        self.freq_link_head = None
    
    # When you get the key, it'll return the key (moving forward as needed) or return -1
    def get(self, key):
        if key in self.cache:
            cache_node = self.cache[key]
            freq_node = cache_node.freq_node 
            value = cache_node.value

            self.move_forward(cache_node, freq_node)
            return value 
        else:
            return -1
    
    # when you set a new key, it moves a new value and the cache_node gets move forward
    def set(self, key, value):
        if self.capacity <= 0:
            return -1
        
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.dump_cache()
            
            self.create_cache(key, value)

        else: 
            cache_node = self.cache[key]
            freq_node = cache_node.freq_node
            cache_node.value = value

            self.move_forward(cache_node, freq_node)

class CacheNode(object):
    """
    doubly linked list
    """
    def __init__(self, key, value, freq_node, pre, nxt):
        self.key = key
        self.value = value
        self.freq_node = freq_node
        self.pre = pre # previous CacheNode
        self.nxt = nxt # next CacheNode

    def free_myself(self):
        if self.freq_node.cache_head == self.freq_node.cache_tail:
            self.freq_node.cache_head = self.freq_node.cache_tail = None
        elif self.freq_node.cache_head == self:
            self.nxt.pre = None
            self.freq_node.cache_head = self.nxt
        elif self.freq_node.cache_tail == self:
            self.pre.nxt = None
            self.freq_node.cache_tail = self.pre
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre

        self.pre = None
        self.nxt = None
        self.freq_node = None

class FreqNode(object):
    """
    doubly linked list
    """
    def __init__(self, freq, pre, nxt):
        self.freq = freq
        self.pre = pre # previous FreqNode
        self.nxt = nxt # next FreqNode
        self.cache_head = None # CacheNode head under this FreqNode
        self.cache_tail = None # CacheNode tail under this FreqNode

    def count_caches(self):
        if self.cache_head is None and self.cache_tail is None:
            return 0
        elif self.cache_head == self.cache_tail:
            return 1
        else:
            return '2+'

    def remove(self):
        if self.pre is not None:
            self.pre.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.pre = self.pre

        pre = self.pre
        nxt = self.nxt
        self.pre = self.nxt = self.cache_head = self.cache_tail = None

        return (pre, nxt)

    def pop_head_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return None
        elif self.cache_head == self.cache_tail:
            cache_head = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_head
        else:
            cache_head = self.cache_head
            self.cache_head.nxt.pre = None
            self.cache_head = self.cache_head.nxt
            return cache_head

    def append_cache_to_tail(self, cache_node):
        cache_node.freq_node = self

        if self.cache_head is None and self.cache_tail is None:
            self.cache_head = self.cache_tail = cache_node
        else:
            cache_node.pre = self.cache_tail
            cache_node.nxt = None
            self.cache_tail.nxt = cache_node
            self.cache_tail = cache_node

    def insert_after_me(self, freq_node):
        freq_node.pre = self
        freq_node.nxt = self.nxt

        if self.nxt is not None:
            self.nxt.pre = freq_node
        
        self.nxt = freq_node

    def insert_before_me(self, freq_node):
        if self.pre is not None:
            self.pre.nxt = freq_node
        
        freq_node.pre = self.pre
        freq_node.nxt = self
        self.pre = freq_node
```

## Description Implemention 


## Operations
* Most are O(1)

# Misc Terminology
**Content Delievery Network**: A group of geographically distributed servers that allow web content to be delievered more quickly, typically via global use caching in data centers. 

# Source
https://ieftimov.com/post/when-why-least-frequently-used-cache-implementation-golang/

https://www.akamai.com/our-thinking/cdn/what-is-a-cdn#:~:text=A%20content%20delivery%20network%20(CDN,closer%20to%20where%20users%20are.&text=CDNs%20cache%20content%20like%20web,near%20to%20your%20physical%20location.

https://medium.com/@epicshane/a-python-implementation-of-lfu-least-frequently-used-cache-with-o-1-time-complexity-e16b34a3c49b

TODO -- read this: https://www.tutorialspoint.com/lfu-cache-in-python