# yelp-college-restaurant-trends

Raw Yelp JSON data lives in data/raw

For testing purposes, save classified (college or non-college) JSON samples into
the respective directory in data/

For example, `data/college/businesses.json` should contain JSON samples of
college-oriented restaurants.

## Development

Please do not develop on the `master` branch. Check out your own branch as
follows:

```Shell
git pull
git checkout your-branch-name-here

# make some changes, then git add -A, git commit
git push -u origin your-branch-name
```

Then create a Pull Request (click button on github), so it can be reviewed and
subsequently merged into the `master` branch.
