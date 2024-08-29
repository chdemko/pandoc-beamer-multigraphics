Usage
=====

To apply the filter, use the following option with pandoc:

.. code-block:: shell-session

    $ pandoc --filter pandoc-beamer-multigraphics

Explanation
-----------

In the metadata block, specific set of classes can be defined to
change ``image`` elements to become multi-images using the ``\multiinclude``
command of beamer.

The metadata block add information using the ``pandoc-beamer-multigraphics``
entry by a list of definitions:

.. code-block:: yaml

   pandoc-beamer-multigraphics:
     - classes: [multigraphics]
       format: pdf
       width: 10cm

The metadata block above is used to use multi-images ability for image elements
which have ``multigraphics`` class. The format used will be ``pdf`` and the
width will be ``\textwidth``.

Each entry of ``pandoc-beamer-multigraphics`` is a YAML dictionary
containing:

-  ``classes``: the set of classes of the ``image``\ s to which the
   transformation will be applied. This parameter is mandatory.
-  ``format``: the image format
-  ``width``: the image width
-  ``height``: the image height
-  ``start``: the starting number (0 by default)
-  ``end``: the ending number (infinity by default)

It's also possible to set the paramters for each image using the pandoc
attribute notation.

Example
-------

Demonstration: Using
:download:`pandoc-beamer-multigraphics-sample.txt
<images/pandoc-beamer-multigraphics-sample.txt>`
as input gives and image output file in
:download:`pdf <images/pandoc-beamer-multigraphics-sample.pdf>`.

Image files used:

- :download:`Tux_junior-0.pdf <images/Tux_junior-0.pdf>`
- :download:`Tux_junior-1.pdf <images/Tux_junior-1.pdf>`
- :download:`Tux_junior-2.pdf <images/Tux_junior-2.pdf>`
- :download:`Tux_junior-3.pdf <images/Tux_junior-3.pdf>`
- :download:`Tux_junior-4.pdf <images/Tux_junior-4.pdf>`
- :download:`Tux_junior-5.pdf <images/Tux_junior-5.pdf>`
- :download:`Tux_junior-6.pdf <images/Tux_junior-6.pdf>`
- :download:`Tux_junior-7.pdf <images/Tux_junior-7.pdf>`
- :download:`Tux_junior-8.pdf <images/Tux_junior-8.pdf>`
- :download:`Tux_junior-9.pdf <images/Tux_junior-9.pdf>`
- :download:`Tux_junior-10.pdf <images/Tux_junior-10.pdf>`

The
`Tux junior image <https://opengameart.org/content/tux-junior-walking-sample>`_
has been created by
`Stephen Groundwater <https://opengameart.org/users/groundwater>`_ under the
`CC BY-SA 3.0 <http://creativecommons.org/licenses/by-sa/3.0/>`_ licence.


.. code-block:: shell-session

    $ pandoc \
        -t beamer \
        -V theme:Warsaw \
        --filter pandoc-beamer-multigraphics \
        -o docs/images/pandoc-beamer-multigraphics-sample.pdf \
        docs/images/pandoc-beamer-multigraphics-sample.txt


