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
