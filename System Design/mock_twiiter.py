"""
Design an application that allows users to log in through their Twitter accounts 
and view their analytics data (likes, retweets, etc.) for the past day, week, month, or year.
"""

"""
Tasks:
- Allow user to login

Questions:
1. Do users already have an account? 

2. If they sign up, for the purpose of this program, can we assume that their email is unique? 

Assumptions:
1. Don't worry about security (ex/ password should be hidden)

Plan:
1. Create a Twitter class that takes a user as objects. Let the email and password be part of the dictionary. For now, we should be able to add users. 
- In a real life system, we want to make sure nobody can just grab the password. We should use a private getter. 

2. Create a user class that can be added in twitter.com

3. Add additional functions to allow different users (including self) to like, retweet, or mention in relation to self or another user. This would require 
a POST object. 
=========
HOW TO APPROACH
1. Need to create the frontend, backed, and a data model that we need (likes, retweets) as well as dates 
2. Ask more about requirements (ex/ is there already a sign-up system). Figure how exact features in MVP and approximate deadline (reduce or keep features). Do we have to worry about security?
3. If we're asked for a frontend for web application, desktop, and mobile, they'll be different systems. 
4. For each system, we need to figure out platform ex/ web application might allow you to have admin-mode or more intensive mode, mobile might be limited to liking other posts or viewing your or others feed 
5. Once we figure out the features we need, we need to figure out the database that is needed.  
6. Consider the site traffic (ex/ middleware for caching) and if a lot of people tweet/like (think about scalability) -- maybe we have to build a message queue to ensure the system doesn't get overwhelm. 
7. Once we have an idea of what our data looks like, we have to think about the scalability of the product. Then we get into more details about the architecture ex/ communication channel between frontend and backend (ex/ GraphQL, REST, etc). 
Look at pro's and con's of the technologies. Likewise for frontend and backend. 
8. Once these are determined, we can start writing intial steps to write out the application. 
9. Once we have a base applicaton, we have to deploy it. 
10. To figure out how to deploy, we need to figure which cloud and pipeline you want to setup. Then subsequently, we have deployment pipeline -- we need to figure out analytics for product. 
11. Launch product and assess how users are using. 

"""
import datetime

ID = 0

class Twitter: 
    def __init__(self):
        self.users = {}

    def create_account(self, email, password):
        new_user = User(email, password)
        users[new_user.email] = new_user.password
    
    def verify_user(self, email):
        if email not in self.users:
            return "Invalid email or password"

class User: 
    def __init__(self, email, password): 
        self.email = email
        self.password = password

class Post: 
    # for date, we probably should do the current date but for now, let'spretend 
    def __init__(self, content, creator, date):
        self.id = ID 
        self.content = content
        self.num_likes = 0
        self.num_retweets = 0

        ID += 1
    
    def like_post(self,id):
        self.num_likes += 1 

def main(): 
    MockTwitter = Twitter()



main()