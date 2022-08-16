# What is REST API?
* One of the most common types of web services 
* Allows applications to communicate with a server via REST API 
* usually called over HTTP 
* a set of architectural constraints

# Uses
* Give a network client (ex/ single-page app, mobile app) access to your data 
* Give end users or services ability to access data

# Rules
* **Use JSON** for requests payloads and responses for the following reasons:
    * Almost every network technology can use it
    * JavaScript has built-in methods to encode and decode JSON (likewise for server-side technologies) and is easy to manipulate on the client-side 
    * Set application type to `Content-Type` in response header to `application/json` to ensure REST API app responds with JSON that clients interpret it as such UNLESS files are being sent & received between client & server. 

* Use **nouns** that represent the **entity** instead of verbs in endpoint paths 
    * Our HTTP request already has a verb, which makes it redundant 
    * See: [common HTTP methods](#common-http-methods), [examples with common HTTP metods](##express-example), and [Naming](#naming)

* If an object can contain another object, group those that contain associated  information (up to 2-3 depths) to minimize attackers getting unnecessary info. See `/articles/:articleId/comments` endpoint from [this example](##express-example)
    * Consider returning the URI as part of the response. See: [Endpoint-Depth-Example](##Nested-Endpoint-Example)

* Handle errors gracefully and return standard error codes to minimize confusions

* Allow for filtering, sorting, and pagination as databases for the following reasoing:
    * An excessive amount of large data can slow down (or even break) systems
    * Increase performance by getting 

* Follow [Security Practices](#Security-Practices)

* Follow semantic versions
    * Phase out old endpoints (rather than force users to move to new API immediately). We would label `/v1/`, `/v2/` and so forth after the main url.

* Cache data to improve performance 
    * Use local memory cache when possible rather than querying data 
        * Redis allows for in-memory caching 
        * Express has apicache middleware to cache application

# Common HTTP Methods 
| Method        | Operation   | Example |        
| ------------- |-------------| --------- |
| GET    | get resources | **GET /posts/** gets new post |
| POST      | submit new data to server|  **POST /posts/** adds new post |  
| PUT | update existing data | **PUT /posts/:id** updates post of that given id 
| DELETE | remove data | **DELETE /posts/:id** removes a post of the given id |

## Express Example
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// parse payload to json
app.use(bodyParser.json());

app.get('/posts', (req, res) => {
    // code to get posts 

    // sets header and sends data over 
    // calls JSON.stringify for you on top of sending
    res.json(articles)
}) 

app.post('/posts', (req, res) => {
    // code to add new posts 

    res.json(articles)
})

app.put('/posts/:id', (req, res) => {
    // object destructing in JavaScript
    const { id } = req.params

    // code to add new posts 
});

app.delete('/posts/:id', (req, res) => {
    const { id } = req.params

    // code to add new posts 
});

// a GET method to get comments of a particular article (child resource)
app.get('/posts/:postId/comments', (req, res) => {
    const { postId } = req.params;
    const comments = [];

    // code to add get comments

    res.json(comments);
});

app.listen(3000, () => console.log('server started'));
```

## Nested Endpoint Example 
If you want to return a commentor of a particular article, return the URI for the particular user instead (`"author": "/users/:userId"`), rather than `/articles/:articleId/comments/:commentId/commentor`

# Common HTTP Status Codes
| Value        | Name   | Meaning |        
| ------------- |-------------| --------- |
| 400 | Bad Request | Client-side input failed validation | 
| 401 | Unauthorized | User is not authorized to access a resource (usually because they're not authenticated) | 
| 403 | Forbidden | User is authenticated, but not authorized to access a resource | 
| 404 | Not Found | A resource is not found.
| 500 | Internal server error | Generic Error: don't throw explicitly. | 
| 502 | Bad Gateway | Invalid response from an upstream server |
| 503 | Service Unavailable | Something unexpected happened on server side ex/ some parts of system failed, server overload | 

## Example 
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// sample response
const users = [
  { email: 'abc@foo.com' }
]

app.use(bodyParser.json());

app.post('/users', (req, res) => {
    const { email } = req.body;
    const userExists = user.find(u => u.email === email); 

    if (userExists) {
        return res.status(400).json({ error: 'User already exists'})
    }

    res.json(req.body);
})

app.listen(3000, () => console.log('server started'));
```

# Filtering, Pagination & Sorting Example 
## Filter by Results
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// employees data in a database
const employees = [
  { firstName: 'Jane', lastName: 'Smith', age: 20 },
  //...
  { firstName: 'John', lastName: 'Smith', age: 30 },
  { firstName: 'Mary', lastName: 'Green', age: 50 },
]

app.use(bodyParser.json());

/*
The following is a request to get employees.
You can pass in keys such as: `firstName`, `lastName`, and `age` with specific params to get specific values.

*/
app.get('/employees), (req, res) => {
    const { firstName, lastName, age } = req.query; 
    let result = [...employees];

    // if firstName is not null, find employee(s) with first name passed in
    if (firstName) {
        results = results.filter(r => r.firstName === firstName)
    }

    // if not null, find employee(s) with last name passed in
    if (lastName) {
        results = results.filter(r => r.lastName === lastName)
    }
}
```
If the URL was `/employees?lastName=Smith&age=30`, then the page would only display employees with the last name Smith and age of 30. 

## Pagination
You can include a `page` query paramter and return a group of entries. **Example:** (page - 1) * 20 to page * 20

You can also see a "limit" and a pagination with the cursor.

## Sorting
You can add a query parameter called `sort` and specify which fields to sort where `+` means ascending and `-` means descending. **Example:** http://example.com/articles?sort=+author,-datepublished

# Security Practices
* Use SSl/TLS certificate (i.e `HTTPS`) to make sure communication between client and server is private and encrypted (don't let your message interpret your information)

* Ensure people are not able to access info that requested by performing role checks (Principle of Least Privilege) via single, grouped, or granular roles (make sure adminstrator can add or remove features from users) ex/ a normal user should not be able to access info from another user or have administrative powers

* Create access token to prevent abuse or malicious intents ex/ only authors or editors should be able to edit a blog post 

* Use UAuth2 (framework for authorization) for SSO (allows user to verify themselves with a trusted 3rd party application ex/ Google, Microsoft, Azure, AWS as a way of token exchange) and get their email
    * Reduce user data -> less problematic with data breach
    * Don't need to implement multi-factor authentication 
    * Users don't need a new account or new password 

* Use API keys for existing user (and make sure it's hidden) with different permissions. These permissions can then be stored in the database with 'read" and "write" at the start and a middleware request to fetch user and permissions.

* Good secrets management

* Choose when to enforce authorization with request-level authorization: look at an incoming request and see if user has access to resource or not 

* Outside of the above, use authorization logic in application code

* Use good libraries or third party tools ex/ Oso, Okta 

# Naming
* Represent collections via plural and singular items via an id with the pluralized version
* Ensure URI are consistent 
* Name based on what it is ex/ Store, Procedure
* Use forward slash (`/`) to indicate hierarchical relationships ex/ `http://api.example.com/device-management/managed-devices/{id}/scripts/{id}`
* Do not use trailing forward slash in url
* Use hyphen (`-`) to seperate words when naming and do not use underscores to increase readability, especially in long path segments
* Use lowercases in URIs 
* Do not use file extensions 
* Query parameters are used for filtering, limitations, or sorting

## Examples
Make a endpoint to get posts of a particular user: 
`/users/:userId/posts` 

Make an endpoint to get employees between ages 18 to 30. One possible endpoint is `/employees?minAge=18&maxAge=30`

# Terminology
* **API:** application programming interface that conforms to specific architectural constraints (ex/ stateless communication and cacheable data)

**Resource:**
* a mapping to a set of entities (not the entity itself) ex/ weather info
* can be a singleton or collection ex/ `authors` is a collection resource, `author` is a singleton resource. This translate to `/author` to get a `author` collection and `/author/{authorId}` to get a specific author
* can have sub-collections ex/ `authors` can have `posts`, which can be defined as `/author/{authorId}/posts` 

**URI:** uniformed resource identifiers to address resources

**Document Resource:** singular concept similiar to object instance or database record (has fields and values) ex/ an author can be represented as `/author/:id`

**Collection:** server-managed directory of resources ex/ a bunch of authors (plural) ex/ `/authors`, `http://api.example.com/device-management/managed-devices`, `http://api.example.com/user-management/users`, `http://api.example.com/user-management/users/{id}/accounts`

**Store:** A client-managed resource repo that allows an API client to put resources in, get them back out and decide when to delete them (each has a URI chosen by client)
ex/ `http://api.example.com/song-management/users/{id}/playlists`

**Controller:** procedural concepts (executable actions) that are presented by verbs 
ex/ `http://api.example.com/cart-management/users/{id}/cart/checkout`

# Sources
[Best practices for REST API design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

https://stackoverflow.blog/2021/10/06/best-practices-for-authentication-and-authorization-for-rest-apis/

https://restfulapi.net/resource-naming/