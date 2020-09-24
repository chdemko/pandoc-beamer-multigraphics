# This Python file uses the following encoding: utf-8

from unittest import TestCase

from panflute import convert_text, Para, Image

import pandoc_beamer_multigraphics


class MultiGraphicsTest(TestCase):
    @classmethod
    def conversion(cls, markdown, fmt="markdown"):
        doc = convert_text(markdown, standalone=True)
        doc.format = fmt
        pandoc_beamer_multigraphics.main(doc)
        return doc

    def test_simple(self):
        doc = MultiGraphicsTest.conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
---
![](myimage){.multigraphics}
            """,
            "beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\multiinclude[graphics={},format=pdf]{myimage}",
        )

    def test_complete(self):
        doc = MultiGraphicsTest.conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
---
![](myimage){.multigraphics start=1 end=3}
            """,
            "beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\multiinclude[graphics={},start=1,end=3,format=pdf]{myimage}",
        )

    def test_meta1(self):
        doc = MultiGraphicsTest.conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
    format: png
    height: 20cm
---
![](myimage){.multigraphics}
            """,
            "beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\multiinclude[graphics={height=20cm,width=\textwidth},format=png]"
            r"{myimage}",
        )

    def test_meta2(self):
        doc = MultiGraphicsTest.conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
    format: png
    width: 20cm
---
![](myimage){.multigraphics}
            """,
            "beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\multiinclude[graphics={height=\textheight,width=20cm},format=png]"
            r"{myimage}",
        )
