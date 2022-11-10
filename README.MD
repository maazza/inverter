# Exercise

Create a REST API with one endpoint /inverse expecting a JSON body containing a list of numbers and an integer N.
Return a JSON response containing the inverse of the input list (consider that this list could contain thousands of records), skipping multiples of N (leave them in place).
 
The project does not need to contain the whole setup to make it deployable. However, in addition to the code of the application, it should contain a test suite ensuring that those specifications are matched.
  
Below is a sample API request with the expected response (HTTP 200):
 
request:

POST /inverse
`{
"N": 3,
"Input": [1, 5, 7, 8, 6, 2, 9, 7]
}
`

response body:
`[7, 2, 8, 7, 6, 5, 9, 1]`

# Solution

run test

`docker compose run api pytest`

start server

`docker compose up`