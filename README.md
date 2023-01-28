# get the buildroot stats

In the buildroot topdir run the following command:

```
support/scripts/pkg-stats  --json stats.json
```

Copy the stats.json to the toplevel directory of buildroot-stats

# import stats from buildroots stats.json output

```
./import import -i stats.json
```


# start the flask app

```
export FLASK_APP=buildroot-stats.py
flask run
```
