                              A FastAPI application to manage a Configuration Management system for onboarding Organisations from each country.

**Key Features:**<br>
CRUD (Create, Read, Update, Delete) operations for managing configurations.

**Build With:**
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic

**API Description**
* POST /create_configuration/  - Create a new configuration for a country with specified requirements.<br>
  Request:<br />
  {<br />
     $~$$~$"country_code": "RUS",<br>
     $~$$~$"configuration": {<br>
      $~$$~$$~$"business_name": "Russia Business Name",<br>
      $~$$~$$~$"P": "ABCDE12",<br>
      $~$$~$$~$"G": "22AAAAA"<br>
 }<br>

  Response body:<br>
  {<br>
   $~$$~$ "country_code": "RUS",<br>
    $~$$~$"configuration": {<br>
     $~$$~$$~$ "business_name": "Russia Business Name",<br>
     $~$$~$$~$ "P": "ABCDE12",<br>
      $~$$~$$~$"G": "22AAAAA"<br>
    }<br>
  }<br>
  200	OK: Successful Response<br>
  400 Bad Request: If there are validation errors in the request body.<br>

* GET /get_configuration/{country_code}-Retrieve the configuration requirements for a specific country.<br>
  Response<br>
  {<br>
  $~$$~$"country_code": "IN",<br>
  $~$$~$"configuration": {<br>
   $~$$~$$~$ "business_name": "My Business Name",<br>
    $~$$~$$~$"P": "ABCDE1234F",<br>
    $~$$~$$~$"G": "22AAAAA0000A1Z5"<br>
  }<br>
}<br>
200 OK: Successful response.<br>
404 Not Found: If the specified country_code does not exist.<br>
{<br>
  "detail": "Configuration not found"<br>
}<br>

* POST /update_configuration/- Update the configuration requirements for a specific country.<br>
  Request:<br>
  {<br>
  $~$$~$"country_code": "IN",<br>
  $~$$~$"configuration": {<br>
   $~$$~$$~$ "business_name": "Updated Business Name",<br>
   $~$$~$$~$ "P": "ABCDE5678G",<br>
   $~$$~$$~$ "G": "22AAAAA0000A1Z6"<br>
   }<br>
 }<br>
 Response<br>
 {<br>
  $~$$~$"country_code": "IN",<br>
  $~$$~$"configuration": {<br>
   $~$$~$$~$ "business_name": "Updated Business Name",<br>
   $~$$~$$~$ "P": "ABCDE5678G",<br>
   $~$$~$$~$ "G": "22AAAAA0000A1Z6"<br>
   }<br>
 }<br>
 200 OK: Successful Response<br>
 404 Not Found: If the specified country_code does not exist- Configuration does not exist<br>


* DELETE /delete_configuration/<br>
  Request:<br>
  In parameters, give the country code<br>
  
  Response<br>
   $~$$~$ true<br>
  200 OK: Configuration successfully deleted.<br>
  404 : Configuration not found, if configuration does not exist<br>
  
  


  

