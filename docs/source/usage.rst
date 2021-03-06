.. _usage:

Usage
==========

You can use AJAX to call the passgen API and will receive a randomly generated password in return::

    https://passgen.zakharov.cc/api/v1/passwords


Results
-----------------

The API will provide you with a JSON object that you can parse and apply to your application::

    {"password": "6;HgyR"}


API errors
-----------------

If API service experiencing server issues, we'll return a simple JSON object with an error::

    {"title": "Invalid parameter", "description": "The \"length\" parameter is invalid. Less than the minimum length 4."}


Specifying a length
-------------------

You can specify a length of generated password by adding the "length" parameter to your request. Valid values for the parameter from 4 to 254. If parameter not specified default values is 6::

    https://passgen.zakharov.cc/api/v1/passwords?length=6
