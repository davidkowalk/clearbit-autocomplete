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

After unpacking the zip you will now find the sourcecode to the api in the folder ``/src/``. Copy the file ``clearbit-autocomplete.py`` into your project source folder and import the api as follows:

```python
import clearbit_autocomplete as clearbit
```

Alternatively you can also import the package via pip. Make sure to link to the folder with the file ``setup.py``:

```
pip install ~/Path/To/Package/Folder/
```
In Python:
```python
import clearbit_autocomplete as clearbit
```

## Functions

### autocomplete()
Company Autocomplete is an API that lets you auto-complete company names and retreive logo and domain information in json-format.

| Parameters | Description | Required |
|------------|-------------|----------|
| name       | Cleartext name of the company as a string. | yes |

Usage:

```python
json_data = clearbit.autocomplete("GitHub")
print(json.dumps(json_data, indent=4))
```

Output:
```json
[
    {
        "name": "GitHub",
        "domain": "github.com",
        "logo": "https://logo.clearbit.com/github.com"
    },
    {
        "name": "GitHub Support",
        "domain": "github.community",
        "logo": "https://logo.clearbit.com/github.community"
    },
    {
        "name": "GitHub",
        "domain": "github.blog",
        "logo": "https://logo.clearbit.com/github.blog"
    },
    {
        "name": "GitHub Status",
        "domain": "githubstatus.com",
        "logo": "https://logo.clearbit.com/githubstatus.com"
    },
    {
        "name": "GitHub",
        "domain": "github.co.jp",
        "logo": "https://logo.clearbit.com/github.co.jp"
    }
]
```

Note: Json formatting in the output may vary.
