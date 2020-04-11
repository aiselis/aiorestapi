Rapid rest resources for aiohttp
================================

[![Latest PyPI package version](https://badge.fury.io/py/aiorestapi.svg)](https://pypi.org/project/aiorestapi)

Key Features
------------

-   Supports both client and server side of HTTP protocol.

Getting started
---------------

`aiorestapi` allows you to quickly create a rest resource in a few steps. It automatically creates the resource routes on the collections or individual items; it's simply to specify the suffix '_collection' or '_item' on the methods.
The serialization / deserialization of results / requests occurs transparently using  python dictionaries.

An example creating a simple rest resource
```python
from aiohttp import web
from aiorestapi import RestView, routes

@routes.resource("/views")
class RestResource(RestView):

    # example call: GET to <server>/views?start=10
    async def on_get_collection(self, start=0) -> list:
        return [
            {"id": int(start)+1, "value": 1},
            {"id": int(start)+2, "value": 2},
        ]

    # example call: GET <server>/views/80
    async def on_get_item(self, id: str) -> dict:
        return self.key

    # example call: POST to <server>/views
    async def on_post_collection(self, body: dict) -> dict:
        return body


app = web.Application()
app.add_routes(routes)
app['key'] = [1, 2, 4, 5]

if __name__ == '__main__':
    web.run_app(app)
```

Installation
------------
It's very simple to install aiorestapi:
```sh
pip install aiorestapi
```

Notes
-----

- @routes.resource decorator the decorator automatically adds the routes to '<server>/myresources' and '<server>/myresources/{id}'
- From the RestView object it is possible to access the aiohttp request with self.request
- The query parameters are automatically converted into parameters of the view method.
- If requests have a body it is necessary to specify in the method a parameter called 'body'
- If requests are to the single item it is necessary to specify a parameter called 'id'
- The items stored as 'app[<key>]' are accessible into view as properties 'self.<key>'

To Do
-----

- Tests!!
- Documentation
- Configurable custom serializers/deserializers

Requirements
------------

-   Python \>= 3.6
-   [aiohttp](https://pypi.python.org/pypi/aiohttp)

License
-------

`aiorestapi` is offered under the Apache 2 license.

Source code
-----------

The latest developer version is available in a GitHub repository:
<https://github.com/aiselis/aiorestapi>
