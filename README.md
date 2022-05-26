# gunicorn-subprocess-bug
Demonstration on bug if using subprocess.run in gunicorn

## Install deps

First of all, install `poetry` if it wasn't installed already:
```console
python3 -m pip install --user poetry
```

Then, install python requirements:
```console
poetry install
```

## Reproduce bug

Start the application:
```console
poetry run gunicorn app
```

And stop the application by `^C` and you will see the traceback of error.
