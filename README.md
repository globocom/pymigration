Pymigration
===========

A generic tool for migrate in python.

Pymigration brings migrations to Python applications. Its main objectives are to provide a simple, stable and database-independent migration layer to prevent all the hassle schema changes over time bring to your applications.

We try to make Pymigration both as easy-to-use and intuitive as possible, by making it automate most of your schema-changing tasks, while at the same time providing a powerful set of tools for large or complex projects.


Install
=======

If you have easy_install  or pip available on your system, just type:

_easy_install pymigration_ or _pip install pymigration_

If you’ve already got an old version of pymigration, and want to upgrade, use:

_easy_install -U pymigration_ or _pip install --upgrade pymigration_

Test using the command with "pymigration -h"



Understanding how it works
==========================

The first thing you’ll need is a migration file. There are some example 
migration files in the “pymigrations” directory. The migration files 
have the following format::

    # -*- coding: utf-8 -*-
    #hello_world.py

    """
        migrate all the world of test
        greetings world
    """

    version = "0.0.1"

    def up():
        """ HeLo World and migrate the world """
        print "HeLo World and migrate the world"

    def down():
        """roolback the world"""
        print "Bye World and roolback the world"


Pymigration uses the _version_ information to track the migrations schema and to 
decide the order of execution of the scripts. Pymigration will go through all .py 
files in your directory and execute all of them in their creation (date) order.

Second, you have to configure access to your current version so Pymigration can execute DDL. 
Just create a file named “conf.py”, with the following content 
(there is also an example in the “pymigration” directory):

    # -*- coding: utf-8 -*-
    import settings

    folder = "{PATH_PYMIGRATION}/version.txt".format(**vars(settings))

    def get_current_version():
        with open("{folder}/version.txt".format(folder=folder))) as f:
            version = f.read()
        return version

    def set_current_version(version):
        with open("{folder}/version.txt".format(folder=folder)) as f:
            f.write(version)

You don’t need to create the methods get and set for current_version. Pymigration
will create it for you. 
If you don’t want to write methods get and set, you can specify its path instead. 
Note that this also makes it possible to use any database you like for the current version::

    # -*- coding: utf-8 -*-
    import settings

    folder = "{PATH_PYMIGRATION}/version.txt".format(**vars(settings))



Migrating to a specific version
===============================

If you want, you can migrate your database schema to a specific version by 
supplying the --to (or -t) parameter. The version id is the var identifier
used at the migration file:

    $ pymigration --to=00.00.01

If you don’t specify any version, use --up or --down, Pymigration will migrate 
the schema to the latest version available in the migrations directories 
specified in the config file.



Supported databases engines
===========================

You can use this project to run migrations on MySQL, Oracle, MS-SQL, redis, filesystem, solr, elasticsearch or any database server.


Getting involved !
==================

Pymigration's development may be viewed and followed on github::

    http://github.com/globocom/pymigration

Retrieve the source code using 'git'::

    $ git clone git@github.com:globocom/pymigration.git


Install package in 'development mode' and run tests with _run_::

    $ git clone git@github.com:globocom/pymigration.git
    $ cd pymigration
    $ ./run unit


[![Build Status](https://api.travis-ci.org/globocom/pymigration.png)](https://api.travis-ci.org/globocom/pymigration)
