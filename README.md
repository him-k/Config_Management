                              A FastAPI application to manage a Configuration Management system for onboarding Organisations from each country.

**Key Features:**<br>
CRUD (Create, Read, Update, Delete) operations for managing configurations.

**Build With:**
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic

**API Description**
* POST /create_configuration/  - Create a new configuration for a country with specified requirements.
  Request:
  {
  "country_code": "RUS",
  "configuration": {
      "business_name": "Russia Business Name",
      "P": "ABCDE12",
      "G": "22AAAAA"
}

Response body:
{
  "country_code": "RUS",
  "configuration": {
    "business_name": "Russia Business Name",
    "P": "ABCDE12",
    "G": "22AAAAA"
  }
}
200	OK: Successful Response
400 Bad Request: If there are validation errors in the request body.

* GET /get_configuration/{country_code}-Retrieve the configuration requirements for a specific country.
  Response
{
  "country_code": "IN",
  "configuration": {
    "business_name": "My Business Name",
    "PAN": "ABCDE1234F",
    "GSTIN": "22AAAAA0000A1Z5"
  }
}
200 OK: Successful response.
404 Not Found: If the specified country_code does not exist.
{
  "detail": "Configuration not found"
}

*POST /update_configuration/- Update the configuration requirements for a specific country.
 Request:
 {
  "country_code": "IN",
  "configuration": {
    "business_name": "Updated Business Name",
    "PAN": "ABCDE5678G",
    "GSTIN": "22AAAAA0000A1Z6"
  }
}
Response
{
  "country_code": "IN",
  "configuration": {
    "business_name": "Updated Business Name",
    "PAN": "ABCDE5678G",
    "GSTIN": "22AAAAA0000A1Z6"
  }
}
200 OK: Successful Response
404 Not Found: If the specified country_code does not exist- Configuration does not exist


* DELETE /delete_configuration/
  Request:
  In parameters, give the country code
  
  Response
    true
  200 OK: Configuration successfully deleted.
  404 : Configuration not found, if configuration does not exist
  
  


  

