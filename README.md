
# DocumentCloud User Uploads Graph

This repository contains an Add-On for DocumentCloud which will create a graph
(image of a graph) that has the number of uploads over time for a given username.

## Files


Example invocation:
```
python main.py --data '{"name": "xxxx-yyyy-1234"}'
```

### main.py

This is the file implements the user graph of upload frequency specific functionality.  

### config.yaml

This is a YAML file which defines the data your Add-On expects to receive.
DocumentCloud will use it to show a corresponding form with the proper fields.
It uses the [JSON Schema](https://json-schema.org/) format, but allows you to
use YAML for convenience.  You may read more about JSON Schema, but here are
the basics to get started:

```yaml
# The title is the title of your Add-On
title: Hello World
# The description will be shown above the form when activating the Add-On
description: This is an updated simple test add-on
# Type should always be object
type: object
# Properties are the fields for your form
properties:
  # the key is the name of the variable that will be returned to your code
  name:
    # the title is what will be shown as the form label
    title: Name
    # a string is text
    type: string
```

At the top level you have the following properties:

* `title` - The title for your Add-On
* `description` - a description for your Add-On - will be displayed above the
  form when someone runs the add-on
* `type` - This should always be set to `object`
* `properties` - This is an object describing the data fields your add-on accepts
    * The name will be the name of the variable the data is returned in
    * `title` - The label shown on the form for this field
    * `type` - This may be `string`, `number` or `boolean`

### requirements.txt

This is a standard `pip` `requirements.txt` file.  It allows you to specify
python packages to be installed before running the Add-On.  You may add any
dependencies your Add-On has here.  By default we install the
`python-documentcloud` API library and the `requests` HTTP request package.
You may upgrade the `python-documentcloud` version when new releases come out
in order to take advantage of new features.

### LICENSE

The license this code is provided under, the 3-Clause BSD License

## Reference

### Full parameter reference

This is a reference of all of the data passed in to the Add-On.  A single JSON
object is passed in to `main.py` as a quoted string.  The `init` function
parses this out and converts it to useful python objects for your `main`
function to use.  The following are the top level keys in the object.

* `token` - An access token which will be valid for 5 minutes, giving you API
  access authorized as the user who activated the add-on.  The `init` function
  uses this value to configure the DocumentCloud client object.

* `refresh_token` - A refresh token which will be valid for 1 day, giving you
  API access to new refresh tokens when they expire.  The `init` function uses
  this value to configure the DocumentCloud client object.

* `base_uri` - This can be used to point the API server to other instances,
  such as our internal staging server.  It should not be used unless you are
  running your own instance of DocumentCloud.  It is also used in the
  initialization of the DocumentCloud client.

* `auth_uri` - The corresponding `auth_uri` if a `base_uri` is specified.

*  `documents` - This is the list of Document IDs which is passed in to `main`

*  `query` - This is the search query which is passed in to `main`

*  `data` - This is the Add-On specific data, as defined when registering the
   Add-On with DocumentCloud.  It is passed in to `main` in the `params`
   dictionary under the key `data`

* `user` and `organization` - The user ID and organiation ID of the user who
  activated the Add-On.  They are also passed in to `main` through the `params`
  dictionary under the keys `user` and `organization` respectively.

* `id` - A UUID to uniquely identify this Add-On run.  It allows DocumentCloud
  to identify the run, as well as allowing the run to send back progress,
  status message and file updates.
