jk_sql
======

Introduction
------------

This python module provides a uniform API to create, modify, read and write data to SQL tables in a database independent way.

**What this uniform interface is:** A simple way to interact with (in the long run: various) databases in a database independent way. The database schema is maintained separately and stored in a special model file. During runtime this information is available through a clean OOP interface: There are table objects and column objects that provide various information as well as data query and manipulation methods.

**What this uniform interface not is:** The API provided does NOT cover all microdetails of SQL. The design goal for this module is to provide a clean interface for the most common, typical database operations. So there are some limitations what you will be able to do with this API.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-sql)
* [pypi.python.org](https://pypi.python.org/pypi/jk_sql)

Please note that currently only SQLite is supported. In the long run more databases will be supported.

Please also note that this module is still in alpha stage. According to unit tests SQLite support works as intended. Nevertheless the API still must be considered as being unstable: A few changes might be in order until beta stage is reached. If you decide to make use of this module have in mind that a few changes to your program might be required later if this module reaches beta stage and you then perform an upgrade on that module.

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



