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

If you are new to ROS 2, a good place to start is the `ROS 2 documentation site <https://docs.ros.org/en/humble/>`_.
This site has installation instructions for ROS, tutorials, how-to guides, and more.

In addition, there are two sites that can be helpful as you learn and use ROS 2:

ROS Answers
^^^^^^^^^^^

`ROS Answers <https://answers.ros.org/questions/>`_  is a website that has questions and answers from the ROS community.
If you encounter an issue, it is very likely that someone else has faced the same problem before, and that it’s covered among the more than 10,000 questions at ROS Answers.
Start by searching for questions similar to yours; if your question isn’t already asked, post a new one.
Be sure to check the guidelines on how to prepare your question before posting.

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

Review the Space ROS Documentation
----------------------------------

The `Space ROS documentation <https://space-ros.github.io/docs/rolling/index.html>`_ describes the differences between Space ROS and the standard ROS 2 Humble distribution.


View the Space ROS github organization
--------------------------------------

The `Space ROS github organization <https://github.com/space-ros>`_ has several repositories that contain various parts of the Space ROS work , including Docker images, work on requirements tools and processes, and sample applications.

Build the Space ROS Docker image
--------------------------------

The `Space ROS docker repository <https://github.com/space-ros/docker>`_ has several Docker scripts for building Space ROS, MoveIt2 on SpaceROS, and demonstration applications.

First, clone the docker repository

.. code-block:: bash

    git clone git@github.com:space-ros/docker.git

Then follow the instructions in spaceros/README to build and run the base image.
The image contains the Space ROS packages and the additional static analysis tools used by Space ROS.
