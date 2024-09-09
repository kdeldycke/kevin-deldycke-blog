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
  $ uv sync --all-extras --dev
  ```

## Build and browse website

- To build the content, in one terminal, run:

  ```shell-session
  $ uv run -- pelican
  ```

- And to serve the website, in another terminal:

  ```shell-session
  $ uv run -- pelican --listen
  (...)
  Serving site at: 127.0.0.1:8000 - Tap CTRL-C to stop
  ```

- Then go to [http://localhost:8000](http://localhost:8000).

## Theme development

The section above is enough to add and modify the website content.

Now if you need to work both on the content and the theme you need to:

- Get a local copy of the theme outside your `./blog` virtualenv:

  ```shell-session
  $ cd ..
  $ git clone https://github.com/kdeldycke/plumage.git
  $ cd ./blog
  ```

- Change `plumage` dependency in the Blog's `pyproject.toml` from:

  ```toml
  dependencies = [
      ...
      "plumage <anything>",
      ...
  ]
  ```

  To:

  ```toml
  dependencies = [
      ...
      "plumage",
      ...
  ]
  ```

- Also add this new section in the same `pyproject.toml`, to [force `uv` to pick up the latest local copy](https://github.com/astral-sh/uv/issues/2844#issuecomment-2241196371):

  ```toml
  [tool.uv.sources]
  plumage = { path = "../plumage", editable = true }
  ```

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
- Use https://github.com/getpelican/pelican-plugins/tree/master/footer_insert
  to add generation time / git SHA / github action workflow debug info to
  each HTML file?

## Dependencies

```mermaid docs/assets/dependencies.mmd
```

## License

The content of this repository is copyrighted © 2004-2024 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](license).
