from distutils.core import setup
import os

def README():
    return open("README.md").read()

setup(name='cbautocomplete',
    version = '0.0.1',
    description = 'Interface for the clearbit autocomplete api',
    author = 'David J. Kowalk',
    author_email = 'david.kowalk@gmail.com',
    url = 'https://github.com/davidkowalk/clearbit-autocomplete',

    license = "MIT",
    keywords = "clearbit autocomplete data",

    long_description = README(),
    long_description_content_type='text/markdown',

    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    package_dir = {'':'src'},

    python_requires = ">=3.5",
    install_requires=['urllib3'],

    project_urls={
        'Bug Reports': 'https://github.com/davidkowalk/clearbit_autocomplete/issues',
        'Funding': 'https://paypal.me/davidkowalk',
        'Source': 'https://github.com/davidkowalk/clearbit_autocomplete/',
    }

)
