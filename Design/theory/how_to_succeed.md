# How to Succeed in a System Design Interview
## General Tips 
* Think of the interview as more of a brainstorming session with [ano]other member(s)
* Familiarize yourself with different topics on how to approach them 
* Understand the best practices and common pitfalls of modern software systems 
* Be able to explore different directions
* Ask the right questions 
* Being knowledgable about common solutions to common problems (be honest if you haven't used it or if you just heard of it)

## Step-by-Step Approach 
1. Understand the goals and basic requirements 
- Clarify any ambiguity early in the interview and YOUR assumptions about the product 
ex/ If being asked to design a product like Twitter, Facebook, or Reddit. Make your assumptions. 
- Identify the system goals 
- Identify the identity, needs, and use cases of the system user
- Identify the inputs and outputs of the system 

2. Establish the Scope
- Describe the features to be created or that was taked 
- Try to define all features by importance. Make sure you and your interviewer agree on the product. 
- Should we discuss the end-to-end experience or just the API? 
- What clients do we want to support (mobile, web, desktop)?
- Do we require authentication? analytics? integration with other systems? 

3. Design at the right scale 
- Be aware if data can fit on one machine or if it'll need to be scaled (ex/ building a queue)
- How many requests will go through? 
- How much "reading" or "writing" will be involved?
- What is the expected response time?
- Whats the limit of data we allow users to provide

4. Start at high-level and drill-down.
- Start with end-to-end process based on goals establish ex/ different clients, APIs, backend service, offline processes, network architecture, data stores & how they all come together 
- Identify different system's entry points (user interactions, external API calls, offline processes) and see if there's potential bottlenecks 

5. Think of Data Structures and Algorithms and Common Techniques to Solve Common Issues
- Discuss tools and technologies you will need to build 
- Think about Data Structures you might need
- Think of common design patterns if applicable 
- Think about concurrency, redundancy

6. Talk about tradeoffs 
- What type of databases would you use and why?
- What are the caching solutions?
- What frameworks to pick? 

## Application 

# Resources
https://blog.pramp.com/how-to-succeed-in-a-system-design-interview-27b35de0df26
