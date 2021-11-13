# Problem
Design an application that allows users to log in through their Twitter accounts and view their analytics data (likes, retweets, etc) for the past day, week, month, or year.

# Thought Process
1. Understand goals and basic requirements
Questions:
1. Do we already have an endpoint of some kind to create accounts? Can we assume they only have an email, username, and password for now?
2. Do I have to handle security aspects? 
3. Do we have to develop the authentication system or encryption? Can we assume its built? 
4. Will we need to create the functionality to like, retweet, etc?
5. Can we eleborate of the meaning of analytics data? What kind of the data would the user want to see?

Assumptions:
1. A user can only login via username and password OR email and password they signed up with. 
2. We are designing a web application
3. When they view their analytics, can they viewing everything? (likes, retweets, mentions, direct messages)? Is it in a form of a graph? What information is it displaying (number of likes, who liked their tweet)?
4. Is the data bundle in that particular day? (so not past 24 hours; just that day). 

Goals:
1. The user needs to be able to login and the user needs to authenticate them properly.
2. The user needs to be able to see the following information:
- the number of retweets, likes, mentions, and direct messages 
- a chart or table of who retweeted, mentioned, direct messaged, or like your tweet (?)

2. Establish the scope 
(1) Make sure user can do the following:
- login
- like
- retweet
- mention
- direct message
- see interactions and amount of each
- see table of specific interactions (general timestamp)

3. Design at the right scale
Number of Users: 
- lots of users worldwide -> lots of requests 
- we may need to have servers on seperate computers to handle the amount of data 
- display the minimal amount of data at start and then allow for more details (?)

4. Start designing
External Endpoints:
(1) Login (POST /login) 
query params: username or email, password
- the endpoint will determine if it's an email or password
- make sure this one is secure via JWT (signed JSON) -> so server uses private key to make a signature to make a json packet and decode 
return: success or failure

(2) Like (POST /like) 
query: liker's username, origin username, tweet_id
- on the frontend side, the heart will be coloured to the user who liked it

(3) Retweet (POST /retweet)
query: username of retweeter, username of origin poster, tweet_id 
- on the frontend side (if successful), the tweet will be display on the retweeter 

(4) Mention (POST /mention)
query: user mentioning, user mentioned, tweet_id
- on frontend side, it will display the mentioner's db and the contents 

(5) Direct Message (POST /dm)
query: sender_username, receiver_username, message_id
- on the frontend side, we need to display the name of receiver and the sender's message

(6) Get Interactions and Number (GET /interactions)
query: start date, end date
- only the user can get their own data analytics

(7) Display specific interactions (frontend side)

Interal Endpoints:
- A way to count the different types of interactions

Frontend:
- Input fields with text for username or email AND password
- Assume a page displayed of overview and user can click on 
- A way for user to tweet (large textfield with buttons)
- Each tweet (block) has symbols for retweet and like (heart)
- When user does '@' with particular user, it will mention them
- Profile 
- Display tables and charts

Third-Party Libraries:
- Authentication / Verification
- One to display charts and tables 
- Component library 

Communication:
- could be REST or GraphQL (REST API is easier to setup but GraphQL can be more beneficial for long-run or if we want to add more items)

Database:
- relational databases are better for insertions, which we'll have to do a lot more as every action we take, we'll need to insert
- can get more organized data compared to non-relational (count interactions, get the users involved and context)

Tables:
(1) Users' info (id --> PK, username -> SK, email -> SK, password, display_image, display_name, num_followers, num_following)
(2) Tweets (id -> PK, account_id -> FK, content --> object)
(3) Interactions (id -> PK, TYPE -- Retweet, Like, Mention, Direct Message, tweet_id -> FK, performer_account id, receiver_ account id, timestamp)

5. Talk about common data structures or algorithms needed
- Class for each user (username, email, password, display_image, account_id, list of tweets)
- Class for each Tweet (id, num_retweets, num_likes, content as string). Methods include retweet and like. 

6. Talk about tradeoffs
- Which type of database?
- What technologies or frameworks for problems?
- What about caching? 
____
- ORMS --> can use for classes (can be used for interactions)