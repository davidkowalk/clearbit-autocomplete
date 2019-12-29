# Documentation Clearbit Autocomplete
Author: David J. Kowalk

## Contents:
1. Import
2. Functions
  - autocomplete

## Importing Clearbit Autocomplete
In order to use the clearbit-autocomplete api for python you must first download the source-code from its [GitHub repository](http://www.github.com/davidkowalk/clearbit-autocomplete).

```
git clone git@github.com:davidkowalk/clearbit-autocomplete.git
```
or via https
```
git clone https://github.com/davidkowalk/clearbit-autocomplete.git
```

You may now find the sourcecode to the api in the folder ``/src/``. Copy the file ``clearbit-autocomplete.py`` into your project source folder and import the api as follows:

```
from clearbit-autocomplete import autocomplete as cb-autocomplete
```
## Function(s)

Once you imported the api into your project you can use the api in your project.
### autocomplete()
Company Autocomplete is an API that lets you auto-complete company names and retreive logo and domain information in json-format.

| Parameters | Description | Required |
|------------|-------------|----------|
| name       | Cleartext name of the company as a string. | yes |

Usage:

```
json-data = cb-autocomplete("segments")
print(json-data)
```

Output:
```
[
  {
    "name": "Segment",
    "domain": "segment.com",
    "logo": "https://logo.clearbit.com/segment.com"
  },
  {
    "name": "Segmentify",
    "domain": "segmentify.com",
    "logo": "https://logo.clearbit.com/segmentify.com"
  }
]
```

Note: Json formatting in the output may vary.
