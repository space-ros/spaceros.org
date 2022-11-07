# Space ROS Website

This is the source code for the Space ROS website.

The site is implemented using the [Pelican static site generator](https://getpelican.com/) and uses the [pelican-fh5co-marble theme](https://github.com/claudio-walser/pelican-fh5co-marble) with the following plugins:

* [pelican_i18n_subsites](git@github.com:StevenMaude/pelican-i18n_subsites.git)
* [pelican_vimeo](git@github.com:kura/pelican_vimeo.git)
* [pelican_youtube](git@github.com:kura/pelican_youtube.git)
* [search](https://github.com/pelican-plugins/search)

## Installation

To build the site, first install the Pelican and Markdown packages if they are not already installed:

```
$ pip3 install "pelican[markdown]"
```

Then [install the Stork tool](https://stork-search.net/docs/install), which is used for indexing content.
For example,

```
michael@bluesalley:~/.local/bin$ wget https://files.stork-search.net/releases/v1.5.0/stork-ubuntu-20-04
michael@bluesalley:~/.local/bin$ chmod +x stork-ubuntu-20-04
michael@bluesalley:~/.local/bin$ ln -s stork-ubuntu-20-04 stork
```

Finally, get the source for the Space ROS website:

```
$ git clone --recurse-submodules git@github.com:space-ros/spaceros.org.git
```

## Building the Site

Traverse into the directory containing the website source code and run pelican to build the site:

```
$ cd spaceros.org/site
$ pelican
```

## Launching the site in development mode

Use the develop_server script to launch the site. For example, the following command will launch a development server on port 8081:

```
$ ./develop_server.sh start 8081
```

Open a browser window and navigate to *localhost:8081*

## Controlling the development server

The develop_server script has start, stop, and restart options that you can use to control the development server:

```
michael@bluenote:~/src/spaceros.org/site$ ./develop_server.sh --help

usage: ./develop_server.sh (stop) (start) (restart) [port]
This starts Pelican in debug and reload mode and then launches
an HTTP server to help site development. It doesn't read
your Pelican settings, so if you edit any paths in your Makefile
you will need to edit your settings as well.
```
