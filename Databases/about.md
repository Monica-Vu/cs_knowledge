# What is a database? 
* An **organized collection of structured information/data** that is typically stored in a computer system and is typically controlled by a dtabase management system (DBMS) 
* DBMS + database = database system (shortened to just database)
* modelled as a series of rows and columns to make processing and querying data efficiently to allow data to be easily accessed, managed, modified, updated, controlled, and organized

# Types
## Relational Databases (Management System)
* Defines database relationships in forms of tables with rows and columns (AKA relations) with keys
* Most efficient way to access structured info
* Does not support many-to-many relationships well
* Usually have predefined data that can be supported
Data is ACID (atomity, consistency, durability, isolation) 
* Most popular

### Advantages
* Structured data
* Ability to establish relationship
* Easy to navigate data (consistent)
* Prevents records from being deleted without deleting PK (need to cascade)
* More secure data transactions
* More data integrity
* Limitless indexing for faster query

### Disadvantages
* Unable to store complex or very large images, numbers, design, or multimedia
* Costs a lot to maintain and create new servers 

### Use Cases
* Strong transactional functionality: stop & go; request/reply that's ordered or interactive apps
* Data mining
* Complex reporting


**Examples:** mySQL, Oracle, PostGreSQL (more of object-oriented database)

## Nonrelational Databases (Management System)
* Allows unstructured and semistructured data to be stored and manipulated (does not be have to defined)
* Popularity grew as web application become more complex
* Good for scalability & flexible (rapid application development), which is suitable for AGILE
* Strong when paired with cloud, non-relational databases as it can save companies a lot of money

### Advantages
* Good for data that is not structured (don't have to make new columns)
* Data can be dynamic and allow for variant inputs (easy to update schema & fields)
* Less transformation for data (MongoDB is ritten in JavaScript)

### Disadvantages 
* Less support: noSQL databases are usually open-source
* Need more technical skills for setup
* noSQL is still growing and has many features to implement

**Examples:** MongoDB, Apache Cassandra, Redis

### Types
#### Document 
* Stores data in JSON, BSON or XML
* Items are nested 
* Most wiely used data
* Flexible as data becomes like code 

ex/ MongoDB

#### Key-value
* Each element in database is stored as a key paired with an attributename e
ex/ shopping carts, user preferences, user profiles 

#### Column Store
* A type of database that is organized as a set of columns

##### Advantages
* Good for analytics: don't need to read row-by-row, reducing memory 
* Can easily aggregate values

##### Disadvantages
* Writing data to columns requires multiple events with the disk

## Graph Databases
* A database where each element is stored as a node and form connections via links or relationships. These links are first-class elements and are stored directly. 
* Often runs w/ more traditional databases

### Use Cases
* Social networks
* Fraud detection
* Knowledge graphs

# Sources
https://www.oracle.com/ca-en/database/what-is-database/

https://en.wikipedia.org/wiki/Rapid_application_development

https://medium.com/@zhenwu93/relational-vs-non-relational-databases-8336870da8bc

https://aloa.co/blog/relational-vs-non-relational-database-pros-cons