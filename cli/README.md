# `aita`

**Usage**:

```console
$ aita [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `api`
* `reddit`
* `train`

## `aita api`

**Usage**:

```console
$ aita api [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `count`: Count number of AITA posts in database by...

### `aita api count`

Count number of AITA posts in database by label

**Usage**:

```console
$ aita api count [OPTIONS] HOST
```

**Options**:

* `--help`: Show this message and exit.

## `aita reddit`

**Usage**:

```console
$ aita reddit [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Add AITA reddit posts to database via api.

### `aita reddit add`

Add AITA reddit posts to database via api.
:param n_posts: how many posts to add to database
:param category: choose which filter to apply to subreddit

**Usage**:

```console
$ aita reddit add [OPTIONS] HOST N_POSTS
```

**Options**:

* `--category TEXT`
* `--help`: Show this message and exit.

## `aita train`

**Usage**:

```console
$ aita train [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `train`: Count number of AITA posts in database by...

### `aita train train`

Count number of AITA posts in database by label

**Usage**:

```console
$ aita train train [OPTIONS] HOST
```

**Options**:

* `--help`: Show this message and exit.
