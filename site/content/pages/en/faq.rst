FAQ
###

:order: 1
:date: 2018-01-25 08:46
:icon: icon-zoom-in2
:summary: Frequently asked questions about Space ROS
:lang: en
:slug: faq
:use_disqus: false

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~

What are robotic and autonomous space systems?
==============================================

A robotic space system is a robot that operates in the space environment.
Example system types include humanoids, manipulators, mobile robotic platforms such as rovers, and multi-robot systems.
Autonomous space systems are space systems with robotic qualities such as agency, and include robotic satellites, space vehicles and lunar landers.

The most relevant near-terms space environments are local to our Solar System at operational distances range from low-earth orbit to deep space.
The conditions of space are very different than those of Earth.
The strength of gravity varies from microgravity (e.g. orbital freefall), low-gravitational fields (e.g. proximal to asteroids) and gravitational wells such as the Lunar and Martian surfaces.
There are tremendous temperature and pressure differences, hazardous radiation conditions and local factors such as dust.

What is the Space Robot Operating System?
=========================================

Space ROS is a reusable software framework based on ROS2 for robotics and autonomous space systems.
Space ROS modifies ROS2 with the intent of aligning its software to aerospace mission and safety assurance standards.

Why Space ROS?
==============

Reusable software frameworks such as core Flight System (cFS) exist for spacecraft flight software.
The value of cFS is measured by is use on many missions.
There does not, however, currently exist a reusable and accessible flight software framework for robotic space systems.
Space ROS is intended to fill this niche.

There is a recognized desire to leverage the reusability, modularity and accessibility of open-source ROS in robotic and autonomous space systems.
NASA has used ROS in its Robonaut 2 and Astrobee robots on the International Space Station, and will use ROS2 at the ground node of the VIPER (Volatiles Investigating Polar Exploration Rover) mission.
The Space ROS team therefore decided to begin with ROS2 at its foundation software framework on which to improve to it to align it to mission and safety assurance standards.

Building a robot for space is different than, and in many ways more challenging than, building terrestrial robots.
Mission and safety assurance are critical to space operations.
Therefore, robotic software must be flight qualifiable.
This means it must subscribe to standards such as NASA NRP7150.2 Software Engineering Requirements.
Latency must be accounted for in space robotic operations, which means the command and control.

Is Space ROS Open Source?
=========================

The core of Space ROS is open source and available via GitHub.

What license does Space ROS use?
================================

Like ROS, the core of Space ROS is licensed under the standard three-clause BSD license.
This is a very permissive open license which allows for reuse in commercial and closed source products.
You can find more about the BSD license here:

http://opensource.org/licenses/BSD-3-Clause

http://en.wikipedia.org/wiki/BSD_licenses

While the core parts of Space ROS are licensed under the BSD license, other licenses are commonly used in the community packages, such as the Apache 2.0 license, the GPL license, the MIT license, and even proprietary licenses.
Each package in the Space ROS ecosystem is required to specify a license, so that it is easy to quickly identify if a package will meet your licensing needs.

What missions will robotic space systems perform?
=================================================

What are some safety and mission assured features of Space ROS?

* Realtime and determinism
* Strict memory management
* Exception handling
* Cyber security
* Communication middleware including DDS, AMS etc.

.. What is Continuous Qualification?
.. =================================

How do I protect intellectual property if I used Space ROS?
===========================================================

Users of Space ROS are free to branch Space ROS and any of its open-source applications for private or commercial use.
Users are responsible for protecting their own intellectual property and ensuring export compliance.
No intellectual property or export controlled software shall exist in the open source Space ROS repository.
You are responsible for licensing your software, as stated in What license is Space ROS under?

How do I qualify Space ROS for flight?
======================================

Space ROS is intended to provide a partial solution to mission and safety assurance.
Its continuous qualification system will provide robust software and artifacts to support the flight qualification process.
It is the responsibility of users of Space ROS to ensure that any flight software matured from Space ROS satisfies the requirements of the mission.

.. What verification and validation tools does Space ROS continuous qualification assume?
.. ======================================================================================

How can I contribute?
=====================

The success of Space ROS depends on active participation of the open source and user community.
There are several ways to contribute, including identifying issues, fixing issues, and managing an application-level framework.

What programming language(s) is Space ROS written in?
=====================================================

Because verification and validation tools for aerospace, and space specifically, Space ROS assumes C++ 14.

Is there a Space ROS roadmap?
=============================

The Space ROS team released a Request for Information (RFI) to solicit feedback from the space and open source community.
The RFI is collecting information on upcoming missions and use cases, requested features and requested applications.
The Space ROS team will analyze the feedback and assign a preference ordering.
This will constitute the initial roadmap and provide the information to the Space ROS community about opportunities to contribute.

What is the Space ROS governance model?
=======================================

Space ROS will have a Technical Steering Committee (TSC) to oversee the maturation of Space ROS and prioritize the Space ROS roadmap.
The TSC will also organize Working Groups comprising members of the Space ROS community to focus on key topics.

.. Will Space ROS allow real-time operations?
.. ==========================================

.. What processing platforms will Space ROS target?
.. ================================================
