# Passgen

A simple service for generating passwords with guaranteed presence of uppercase and lowercase letters, numbers and special characters.

[![Build Status](https://travis-ci.org/toolen/passgen.svg?branch=master)](https://travis-ci.org/toolen/passgen)
[![Coverage Status](https://coveralls.io/repos/github/toolen/passgen/badge.svg?branch=master)](https://coveralls.io/github/toolen/passgen?branch=master)
[![Documentation Status](https://readthedocs.org/projects/passgen/badge/?version=master)](http://passgen.readthedocs.io/en/master/?badge=master)
[![License](https://img.shields.io/github/license/toolen/passgen.svg)](https://github.com/toolen/passgen/blob/master/LICENSE)
[![Docker Image](https://images.microbadger.com/badges/image/toolen/passgen.svg)](https://microbadger.com/images/toolen/passgen)

## Try

[Demo](https://toolen.github.io/passgen/#try)

## Usage

You can use AJAX to call the passgen API and will receive a randomly generated password in return.

```
https://passgen.zakharov.cc/api/v1/passwords
```

### Results

The API will provide you with a JSON object that you can parse and apply to your application.

```
{"password": "6;HgyR"}
```

### API errors

If API service experiencing server issues, we'll return a simple JSON object with an error.

```
{"title": "Invalid parameter", "description": "The \"length\" parameter is invalid. Less than the minimum length 4."}
```

### Specifying a length

You can specify a length of generated password by adding the "length" parameter to your request. Valid values for the parameter from 4 to 254. If parameter not specified default values is 6.

```
https://passgen.zakharov.cc/api/v1/passwords?length=6
```

## Settings

### CORS

You can disable CORS by environment variable.

```
PASSGEN_CORS_ENABLED=False
```

### Gunicorn

Gunicorn settings can be specified by using environment variable GUNICORN_CMD_ARGS. All available command line arguments can be used. For example, to specify the bind address and number of workers:

```
GUNICORN_CMD_ARGS="--bind=127.0.0.1:8080 --workers=3"
```

## Deploy

### Docker

```
docker run -d -p 80:8080 --restart always toolen/passgen:2.0.0
```
