# Kevin Deldycke's blog

Source and content to generate my static [blog](https://kevin.deldycke.com),
which is powered by [Pelican](https://getpelican.com) (engine) and
[Plumage](https://github.com/kdeldycke/plumage) (theme).

## Installation

- Fetch a copy of the repository:

  ```shell-session
  $ git clone https://github.com/kdeldycke/kevin-deldycke-blog.git blog
  $ cd ./blog
  ```

- Install Python:

  ```shell-session
  $ brew install python
  $ python --version
  Python 3.12.4
  ```

- Install `uv`:

  ```shell-session
  $ python -m pip install uv
  ```

- Install this blog's dependencies:

  ```shell-session
  $ uv venv
  $ source .venv/bin/activate
  $ uv pip install --all-extras --requirement ./pyproject.toml
  ```

## Development

- In one terminal, run:

  ```shell-session
  $ uv run pelican --verbose ./content
  ```

- And in another:

  ```shell-session
  $ uv run pelican --verbose --listen
  (...)
  Serving site at: 127.0.0.1:8000 - Tap CTRL-C to stop
  ```

- Then go to [http://localhost:8000](http://localhost:8000).

## TODO

### Content

- Use ML to produce article's summaries.
- Renders disqus comments as static content for SEO? => https://github.com/getpelican/pelican-plugins/tree/maste-disqus_static
- https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags
- https://github.com/getpelican/pelican-plugins/tree/master/post_stats
- https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git
- https://elegant.oncrashreboot.com/amazon-bestazon
- https://elegant.oncrashreboot.com/amazon-onelink
- dark theme? https://github.com/alexandrevicenzi/Flex/blob/bbf47fe35473774d8a41478523cf4d3b21268e35/templates/base.html#L31-L44

### Plugins

- clean_summary
- https://github.com/getpelican/pelican-plugins/tree/master/representative_image
- https://github.com/jhshi/pelican.plugins.post_revision

### Theme

- Re-use previous artworks from Maomium ?
- Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201
- Use https://github.com/getpelican/pelican-plugins/tree/master/footer_insert
  to add generation time / git SHA / github action workflow debug info to
  each HTML file?

## Dependencies

```mermaid docs/assets/dependencies.mmd
```

## License

The content of this repository is copyrighted (c) 2004-2020 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](license).
