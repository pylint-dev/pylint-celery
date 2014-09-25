pylint-celery
=============

[![Build Status](https://travis-ci.org/landscapeio/pylint-celery.png?branch=master)](https://travis-ci.org/landscapeio/pylint-celery)
[![Code Quality](https://landscape.io/github/landscapeio/pylint-celery/master/landscape.png)](https://landscape.io/github/landscapeio/pylint-celery)
[![Coverage Status](https://coveralls.io/repos/landscapeio/pylint-celery/badge.png)](https://coveralls.io/r/landscapeio/pylint-celery)
[![Latest Version](https://pypip.in/v/pylint-celery/badge.png)](https://crate.io/packages/pylint-celery)
[![Downloads](https://pypip.in/d/pylint-celery/badge.png)](https://crate.io/packages/pylint-celery)

# About

`pylint-celery` is a [Pylint](http://pylint.org) plugin for improving code analysis for when analysing code using [Celery](http://celeryproject.org). It is also used by the [Prospector](https://github.com/landscapeio/prospector) tool.

## Usage

#### Pylint

Ensure `pylint-celery` is installed and on your path (`pip install pylint-celery`), and then run pylint:

```
pylint --load-plugins pylint_celery [..other options..]
```

#### Prospector

Ensure `pylint-celery` is installed and on your path (`pip install pylint-celery`), and then run prospector:

```
prospector --uses celery [..other options..]
```

# Features

* Fixes the warning 'celery.task' is not callable

# License

`pylint-celery` is available under the GPLv2 license.
