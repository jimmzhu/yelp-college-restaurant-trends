# yelp-college-restaurant-trends

## Data

Raw Yelp JSON data lives in `data/raw`. Head over to the
[yelp dataset challenge site](https://www.yelp.com/dataset_challenge/dataset)
to obtain the data, and unpack the raw json files in data/raw.

Filtered JSON data lives in `data/businesses.zip`. Unpack this to get two input
data files:
- `data/businesses-train.json`
- `data/businesses-test.json`

From here you may run `src/parse_businesses.py` to generate test and training
CSV files:
```Shell
env/bin/python srcparse_businesses.py
```

Once we get to the point where we are able to do an initial classification on
our list of businesses, the classified businesses should be saved in the
appropriate directory:
  - `data/college/businesses.json`
  - `data/non-college/businesses.json`

## Feature Vectorization

All feature vectorizations should be implemented per business:
```Python
def get_categories(business, limit=5):
    """Return (5) categories of business (dict) represented as a vector of numbers"""
    return map(category_to_int, business['categories'])[:limit]

def category_to_int(category):
    """Convert category string into integer representation"""
    pass
```
Once this is done, register your feature transformation function in `src/parse_businesses.py`:
```
from name_of_file import get_categories
...Python
def business_to_row(business):
    return reduce(str_flatten, (
        ...,
        get_categories(business),  # 1x5
    ), ())
```
**NOTE:
Make sure that your feature vectorization function returns a fixed-length
vector. This is essential for making sure the CSV is properly formatted**

## Setup

Get Python pip (for package management)
```Shell
# Ubuntu
sudo apt-get install python-pip python-dev build-essential

# if you already have python (and therefore easy_install)
sudo easy_install pip
```

Install virtualenv, create a new virtual environment
```Shell
sudo pip install virtualenv
virtualenv env
```

Install dependencies
```Shell
env/bin/pip install -r requirements.txt
```

If you want to add new dependencies to the project, be sure to enter them into
`requirements.txt` and install using `env/bin/pip`, NOT `pip`. *If you're getting
"permission denied" errors, that's because you're not using* `env/bin/pip`.

See [this article](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)
for a description of why using pip for package management and isolating your
Python environment with virtualenv is a good idea.

## Dependencies
- [MSFTVC compiler](http://www.microsoft.com/en-us/download/details.aspx?id=44266)
- [python wheel](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
- [scikit-learn](http://scikit-learn.org/stable/documentation.html)

## Development

Code should be saved in the `src` directory, while data goes in the `data`
directory (mentioned above).

Please do not develop on the `master` branch. Check out your own branch as
follows:

```Shell
git pull
git checkout your-branch-name-here

# make some changes, then git add -A, git commit
git push -u origin your-branch-name
```

Then create a Pull Request (click button on GitHub), so it can be reviewed and
subsequently merged into the `master` branch.
