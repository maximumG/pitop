Pitop
=====

Pitop is a Python module for interaction with the Itop REST API.

For now only a read-only method is available meaning you can only request from the API but not currently pushed to the
API.

Links
=====

You can browse the Itop REST API documentation at https://wiki.openitop.org/doku.php?id=advancedtopics:rest_json

Dependencies
============

- Python >= 2.6
- requests

Usage
=====

Request
-------

The request/search operation is done trough the *request* function available in the pitop module. The function returns a list
of dynamic objects created from the JSON returned from the REST API. You can use it as the following example.

.. code-block:: python

	import pitop
	objects = pitop.request("http://url/rest.api", "user", "password", object="ItopObject")
	print type(objects)
	print objects[0]


You need to tell the *request* function:

- The Itop REST API URL
- Your credentials (username & password)
- The Itop object type you are requesting

A more advanced example is using the optional argument of the *request* function.

.. code-block:: python

	import pitop
	objects = pitop.request("http://url/rest.api", "user", "password", object="ItopObject", filter="my filter", output_fields=["field1", "field2"])
	print type(objects)
	print objects[0]

The *filter* argument is used to filter out the results from Itop API call.
The *output_fields* argument is a list of the object's attribute you want Itop to return - by default all object's attribute are returned.

CSV parsing
-----------

pitop module is also able to parse the CSV file exported from Itop. The function returns a list of dynamic objects created
from the CSV file.

.. code-block:: python

	import pitop
	objects = pitop.csv("filepath", object="itopObject")
	print type(objects)
	print objects[0]

You need to tell the *csv* function:

- The path to the CSV file
- The Itop object type you are trying to create