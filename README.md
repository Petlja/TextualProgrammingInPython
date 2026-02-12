# Textual Programming in Python

This repository contains the source for the **Textual Programming in Python** course by [Petlja](https://petlja.org).

The course covers Python fundamentals: programs, text values, reading data, math functions, branching, scripts, data collections, lists, defining functions, and dictionaries.

- **Course on Petlja.org:** <https://petlja.org/en/course/12719/0>
- **GitHub Pages preview:** <https://petlja.github.io/TextualProgrammingInPython>

## Building

The source content is in the `source/` directory and can be converted to HTML using [Sphinx](https://www.sphinx-doc.org/) with the [PLCT](https://github.com/Petlja) toolchain.

### Prerequisites

- Have the [uv tool](https://docs.astral.sh/uv/) (version 0.10 or newer) installed

### Build HTML

```bash
uv run plct build
```

The output will be in the `build/` directory.

### Build and preview in browser

```bash
uv run plct preview
```

This starts a local server with live-reload at <http://127.0.0.1:8000>.

## License

This work by Fondacija Petlja is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

