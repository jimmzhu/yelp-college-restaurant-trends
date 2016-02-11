# yelp-college-restaurant-trends

## Data

Raw Yelp JSON data lives in data/raw. Head over to the
[yelp dataset challenge site](https://www.yelp.com/dataset_challenge/dataset)
to obtain the data, and unpack the raw json files in data/raw.

For testing purposes, save JSON samples into their respective directory based on
the `city` in which the business is located (this should be done first before we
can do college vs. non-college classification).

For example, `data/cities/Las Vegas/businesses.json` should only contain JSON
samples for businesses located in Las Vegas.

Once we get to the point where we are able to do an initial classification on
our list of businesses, the classified businesses should be saved in the
appropriate directory:
  - `data/college/businesses.json`
  - `data/non-college/businesses.json`

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
