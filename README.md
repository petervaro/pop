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
- [License](#license)



Dependencies
------------

- [Python](http://python.org) : 3.5.2+
- [Flask](http://flask.pocoo.org) : 0.11+
- [SQLAlchemy](http://www.sqlalchemy.org/) : 1.1.3+


Usage of the Server
-------------------

Running the server:

```
$ python server.py
```

Running in debug mode:

```
$ python server.py -D
$ python server.py --debug
```



Base URL
--------

http://<host>/pop/api/v1.0/artists



Parameters
----------

youngest=<int> (default:16 (in years))
oldest=<int> (default:74 (in years))
rate=<float> (default:10.00 (in pound))
gender=male|female|both (default:both)
longitude=<float> (default:-0.1802461 (in degrees))
latitude=<float> (default:51.5126064 (in degrees))
radius=<float> (default:1 (in miles))
sort=age|rate|gender|distance (default:rate)
order=ascending|descending (default:ascending)
count=all|<int> (default:all)
start=<int> (default:0)
force=true|false (default:false)



Errors
------

...



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
