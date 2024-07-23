# cpp-transport-catalogue
Final Project: Transport Directory

The project is a database with bus routes, which provides information on:

Route names
Stop names
Type of route (circular/non-circular)
Road distance
Stop coordinates (for calculating geographical distance)
Bus speeds
Bus waiting times
Input data is received through cin. The database is then populated and serialized. The "output" data (i.e., information from queries to the database) is also received through cin, where the database file is deserialized and data is read from the database. The project is built using CMake. Asynchronous processing is applied.

Implemented functionalities include:

Retrieving information about stops/length/type for specific routes
Retrieving information about buses passing through a stop
Drawing the route map
Building the optimal route from stop A to B, considering transfers and waiting times
Example of a request to populate the database:
File: input_in.txt

Example of a data output request:
File: input_out.txt

Output:
File: answer_out.txt
  
