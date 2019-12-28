# Clearbit Autocomplete

[Clearbit-API](https://clearbit.com/docs) is a tool for data analyst and marketing experts to find information and online details about any business given only their company name.
As by 28th December 2019 the [native clearbit python integration](https://github.com/clearbit/clearbit-python) does however not support the "autocomplete" feature of the api, which returns possible but sometimes inaccurate business names and websites from a name-fragment or the full name. This repository aims at being a makeshift api for clearbit autocomplete by interfacing with the server via http.


## Dependencies
- **Urllib** is an http-library for python
- Python 3
