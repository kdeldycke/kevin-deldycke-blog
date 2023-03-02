# Kevin Deldycke's blog

Source and content to generate my static [blog](https://kevin.deldycke.com),
which is powered by [Pelican](https://getpelican.com) (engine) and
[Plumage](https://github.com/kdeldycke/plumage) (theme).

## Installation

Fetch a copy of the repository:

```shell-session
$ git clone --recursive https://github.com/kdeldycke/kevin-deldycke-blog.git blog
$ cd ./blog
```

To fetch and/or reset submodules to their committed reference:

```shell-session
$ git submodule update --init --recursive
```

Install Python 3.11 and upgrade all its utilities:

```shell-session
$ brew install python
$ python --version
Python 3.11.0
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade poetry
```

Install this blog's dependencies:

```shell-session
$ poetry install
```

## Development

Update to latest submodules:

```shell-session
$ git submodule init
$ git submodule update --remote --merge
```

In one terminal, run:

```shell-session
$ poetry run pelican --verbose --debug ./content
```

And in another:

```shell-session
$ poetry run pelican --verbose --listen
(...)
Serving site at: 127.0.0.1:8000 - Tap CTRL-C to stop
```

Then go to [http://localhost:8000](http://localhost:8000).


## TODO

### Content

  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Reuse edit link logic from https://github.com/pmclanahan/pelican-edit-url ?

### Theme

  * Re-use previous artworks from Maomium ?
  * Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201

## License

The content of this repository is copyrighted (c) 2004-2020 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](LICENSE).
