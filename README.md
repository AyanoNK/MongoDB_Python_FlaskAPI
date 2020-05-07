# A Flask API that communicates with a MongoDB database to add, delete, and update into it.
Simple Flask API to manipulate data from a simple MongoDB database.
To execute the API
1. Start by creating a Mongo database.
   * The default name on the API is *colegio*.
   * Consider that the MongoURI is set to localhost. If you plan it to use it on a Docker network, change `localhost` to your configuration.
2. Name your collection students.
   1. Default fields on the API are *_id*, *name* and *age*.
3. Execute the API! Start it using `python3 api.py` on a console located on the directory of the API.

I left a Dockerfile in case you want to create an image with the API. 
