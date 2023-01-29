# buildroot-packages

buildroot-packages is a flask based web application to display the
buildroot packages. The source of the data is the output of the buildroot
script `support/scripts/pkg-stats`.

# Requirements

## Debian

```
apt install python3-venv python3-pip
```

# Setup

## Get the buildroot stats

In the buildroot topdir run the following command to get the data in
json format.

```
support/scripts/pkg-stats  --json stats.json
```

Copy the stats.json to the toplevel directory of buildroot-packages.
```
cp stats.json <SRCDIR>
```

## Prepare venv

Create and run the app in a python virtual environment (venv).
```
cd <SRCDIR>
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Import/Update stats from buildroots stats.json output

```
./import import -i stats.json
```

# Run the app

## Development

```
cd <SRCDIR>
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export FLASK_APP=buildroot-stats.py
flask run
```

## Lighttpd as proxy for gunicorn

The app is running under gunicorn as python WSGI HTTP server. An example
systemd unit file shows how to start the app.

lighttpd is configured as proxy for the gunicorn server.

The implentation is based on the example show on:

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04

Download the sources to `/var/lib/`.

```
git clone https://github.com/hthiery/buildroot-stats
```

Install the systemd unit file to `/etc/systemd/system`.
```
cd /var/lib/buildroot-packages/
sudo cp contrib/buildroot-packages.service /etc/systemd/sytem
```

Install the lighttpd config file to `/etc/lighttpd/conf-available`.
```
sudo cp contrib/99-buildroot-packages.conf /etc/lighttpd/conf-availabe
```

Make sure the module mod_proxy is enabled in the lighttpd config.

Start the systemd unit and Restart lighttpd.
