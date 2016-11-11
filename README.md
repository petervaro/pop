[![[license: GPLv3]][1]][2]
[![[python: 3.5]][3]][4]

- - -

POP Server API Documentation
============================

- [Dependencies](#dependencies)
- [Usage of the Server](#usage-of-the-server)
- [Base URL](#base-url)
- [Parameters](#parameters)
- [Errors](#errors)
- [Run Tests](#run-tests)
- [License](#license)



Dependencies
------------

- [Python](http://python.org) : 3.5.2+
- [Flask](http://flask.pocoo.org) : 0.11+
- [SQLAlchemy](http://www.sqlalchemy.org/) : 1.1.3+


Usage of the Server
-------------------

Running server for the first time:

```
$ python server.py --populate
```

Running server once its database has been populated:

```
$ python server.py
```

For debug mode use the `-D` or the `--debug` flags, like:

```
$ python server.py --debug
```



Base URL
--------

The `GET` API uses the following base URL:

```
http://<host>/pop/api/v1.0/artists
```

This request will return the result of a query that is using the default values
only. To refine the search criterias, one should use the
[parameters](#parameters).

On each successful request a list of dictionaries will be returned, containing
the following keys and their values:

- `'uuid'`
- `'gender'`
- `'rate'`
- `'age'`
- `'longitude'`
- `'latitude'`
- `'distance'`

If the search criteria is too strict and no results can satisfy it, an empty
list will be returned. On any error, an [error object](#errors) will be
returned.



Parameters
----------

The following parameters and their values are available to refine the search:

- `youngest`: integer, age in years, default: `16`
- `oldest`: integer, age in years, default: `74`
- `rate`: float, salary in pounds between &pound;10.00 and &pound;39.97,
  default: `24`
- `gender`: string, either `'male'`, `'female'` or `'both'`, default: `'both'`
- `longitude`: float, longitudinal coordinate value in degree, default: `-0.1802461`
- `latitude`: float, latitudinal coordinate value in degree, default: `51.5126064`
- `radius`: float, distance from a given coordinate in miles, default: `1`
- `sort`: list, comma separated keys and their weights, their weight is a float,
  between `0.0` and `1.0`, default: `age*0.1,rate*0.7,gender*0.1,distance*0.1`:
    - `age`
    - `rate`
    - `gender`
    - `distance`
- `order`: string, either `'ascending'` or `'descending'`, default: `'ascending'`
- `count`: integer or string, limiting number of results, default: `'all'`
- `start`: integer, offset from the beginning of the results, default: `0`
- `force`: string, either `'true'` or `'false'`, if true, the request is forced
  to deal with invalid data, that is, it will use values which are close enough
  to the given invalid parameter or the default ones, default: `'false'`



Errors
------

On each unsuccessful request, that is, request contains invalid parameter names
or values, will return a dictionary, which has a single key, called `'error'`.
The value of this key is another dictionary, the error object, which contains 3
keys:

- `'code'`: integer error code, which can be:
    - `1` on type error -- expected different type for the given parameter
    - `2` on value error -- expected different value for the given parameter
    - `3` on numeric value if it is out of range, lesser than expected
    - `4` on numeric value if it is out of range, greater than expected
- `'name'`: string, the name of the parameter where the error occured
- `'text'`: string, detailed explanation and hint why the error occured



Run Tests
---------

Running server for testing puposes the first time:

```
$ python server.py --populate --dummy
```

Running server once its database has been populated:

```
$ python server.py --dummy
```

Once the server is up and running, one should run the tests:

```
$ python tests/tests.py
```



License
-------

Copyright &copy; 2016 **Peter Varo**

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program, most likely a file in the root directory, called 'LICENSE'.
If not, see <http://www.gnu.org/licenses>.



<!-- -->

[1]: https://img.shields.io/badge/license-GNU_General_Public_License_v3.0-blue.svg
[2]: http://www.gnu.org/licenses/gpl.html
[3]: https://img.shields.io/badge/python-3.5-lightgrey.svg
[4]: https://docs.python.org/3
