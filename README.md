[![Build Status](https://travis-ci.org/brianjbuck/noeval.svg?branch=master)](https://travis-ci.org/brianjbuck/noeval)

noeval
======

A pre-commit hook to warn against committing code with `eval()`

## Installation as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/brianjbuck/noeval
    rev: v1.0.0
    hooks:
    -   id: noeval
```

[0]: http://pre-commit.com/#pre-commit-configyaml---hooks
