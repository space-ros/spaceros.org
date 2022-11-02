Getting Started
###############

:order: 2
:date: 2018-01-25 08:46
:icon: icon-github
:summary: How to install this theme
:lang: en
:slug: getting_started
:use_disqus: true

How to get started with Space ROS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Learn ROS 2
-----------

If you are new to ROS 2, a good place to start is the `ROS 2 documentation site <https://docs.ros.org/en/humble/>`_. This site has installation instructions for ROS, tutorials, how-to guides, and more.

In addition, there are two sites that can be helpful as you learn and use ROS 2:

ROS Answers
^^^^^^^^^^^

`ROS Answers <https://answers.ros.org/questions/>`_  is a website that has questions and answers from the ROS community. If you encounter an issue, it is very likely that someone else has faced the same problem before, and that it’s covered among the more than 10,000 questions at ROS Answers. Start by searching for questions similar to yours; if your question isn’t already asked, post a new one. Be sure to check the guidelines on how to prepare your question before posting.

ROS Discourse Forums
^^^^^^^^^^^^^^^^^^^^

To stay up-to-date on the latest developments within the ROS community, you can join the `ROS Discourse <https://discourse.ros.org/>`_ forums, which is the place for announcements, news, and discussions of general interest.

Watch Background Presentations on Space ROS
-------------------------------------------

The following presentations give some background infomation about Space ROS.

The ROSWorld 2021 keynote presentation by Kim Hambuchen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

.. vimeo:: 649649866

The Amazon re:MARS 2022 presentation by Michael Jeronimo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

.. youtube:: GxTdhhCwETQ
  :class: youtube-16x9
  :allowfullscreen: yes
  :seamless: yes


Get the Code
------------

By path in your pelicanconf.py

.. code-block:: python
    
    THEME = '/path/to/theme/pelican-fh5co-marble'


Install it using pelican-theme
------------------------------

Of course you can install it using the pelican-themes cli tool, which is maybe more convinient for you.

.. code-block:: bash
    
    pelican-themes -i /path/to/theme/pelican-fh5co-marble

Afterwards you can use it by just configuring its name in pelicanconf.py

.. code-block:: python
    
    THEME = 'pelican-fh5co-marble'
