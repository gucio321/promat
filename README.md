# Promat website

This is source code of the new Promat's website.

## How To Build

To build this project locally, you need to install [python3](https://python.org).
Then, download this repository and `cd` into its folder.
Then run:
```sh
# python3 -m pip install virtualenv
python3 -m pip virtualenv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Now to rebuild html code and serve the website locally run `make serve`

## Dev tips

- in articles section, set the following article's date to disable displaying article info:

```
Date: 1000-01-01 00:00
```
