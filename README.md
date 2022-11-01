# Space ROS Website

This is the source code for the Space ROS website.

The site is implemented using the [Pelican static site generator](https://getpelican.com/) and uses the [pelican-fh5co-marble theme](https://github.com/claudio-walser/pelican-fh5co-marble) with the following plugins:

* [pelican_i18n_subsites](git@github.com:StevenMaude/pelican-i18n_subsites.git)
* [pelican_vimeo](git@github.com:kura/pelican_vimeo.git)
* [pelican_youtube]( git@github.com:kura/pelican_youtube.git)

## Installation

To build the site, first get the source:

```
$ git clone --recurse-submodules git@github.com:mjeronimo/spaceros.org.git
```

Then, install Pelican and Markdown:

```
$ pip3 install "pelican[markdown]"
```

## Building the Site

```
$ cd spaceros.org/site
$ pelican
```

## Launching the site in development mode

```
$ ./develop_server.sh start 8081
```

Open a browser window and navigate to *localhost:8081*
