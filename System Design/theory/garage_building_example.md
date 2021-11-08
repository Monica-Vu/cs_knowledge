# Problem
Buid a parking garage.

# Steps
1. State assumptions / ask questions. 
**QUESTIONS:**
**Are there different types of parking spots (ex/ accessible, small, large)?** 
The parking spots will be compact, regular, and large .

**What are the costs of the parking spots?**  
Flat rate for time, but cost of intial parking spot will be vary. 

**ASSUMPTIONS:**
* Find a way to reserve a parking spot and get a ticket/reciepit when you reserve
- Find a way to pay for a parking spot
- The overall system needs high consistency so people don't reserve a spot at the same time
- This will likely be web application or mobile application

2. Define API or interface: explain the public and internal endpoints needed. 
* Note that these API's do not represent REST API's, they could represent other types (ex/ GraphQL, RPC)

**PUBLIC**
* Reserve parking slot (/reserve) 
params: garage_id, start_time, end_time
returns: reservation_id, spot_id

* Payment (will likely use a 3rd party like Stripe, Square, or might even build it in-house) (/payment)
param: reservation_id

* Cancel your reservation (/cancel)
params: reservation_id

**INTERNAL:**
* calculate_payment 
params: reservation_id (assuming reservation_id returns garage start time and the end time)   

* /free_spots
params: see all available spots 
Note: smaller vehicles could fit in larger spots but 

* /allocate_spot
params: spot_id

**OTHER ENDPOINTS (outside of problem)**:
* create an account 
* include options for Google or Facebook 
params: email, hashed password, first name, last name 

* login system
params: email, hashed password

3. Discuss about scalability.
**SCALABILITY**
- The average garage floor might have (at most) 2000 spots 
- There's not many garbage (so we have to design it to distributed systems)
- Focus: ensure there's no race conditions

4. Create your database (if applicable).
**DESIGNING THE DATABASE**
- Preference in relational database 
- Sharding: split your databases into smaller ones

Here are the tables you can create:
Reservation
- id (primary key)
- Allocated spots -> foreign key
- garage id -> foreign key
- start_time, end_time
- maybe if paid or not (depending if it'll be paid)

Garage
- id (primary key)
- zipcode 
- rate_compact
- rate_medium
- rate_large

Spot
- type of vehicle
- garage_id (foreign key, secondary key)
- specific status (reserved, available, unavailable for used)

Users
- id (primary_kkey)
- email 
- password (hashed - probably SHA_256)
- first name
- last name

Vehicle
- id
- user_id
- license
- vehicle_type (enum)

5. Discuss a high-level architecture 
- Frontend Application (Web or Mobile)
- Do we need middleware?
- Backend
- DB 

Consideration:
- We need to read more than write 

# Sources
https://youtu.be/NtMvNh0WFVM?t=1329