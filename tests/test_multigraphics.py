"""Test module."""
from unittest import TestCase

from panflute import convert_text

import pandoc_beamer_multigraphics


class MultiGraphicsTest(TestCase):
    def verify_conversion(
        self,
        text,
        expected,
        transform,
        input_format="markdown",
        output_format="latex",
        standalone=False,  # noqa: FBT002
    ) -> None:
        """
        Verify the conversion.

        Parameters
        ----------
        text
            input text
        expected
            expected text
        transform
            filter function
        input_format
            input format
        output_format
            output format
        standalone
            is the output format standalone ?
        """
        doc = convert_text(text, input_format=input_format, standalone=True)
        doc.format = output_format
        doc = transform(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format=output_format,
            extra_args=["--wrap=none"],
            standalone=standalone,
        )
        self.assertEqual(converted.strip(), expected.strip())  # noqa: PT009

    def test_simple(self):
        self.verify_conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
---
![](myimage){.multigraphics}
            """,
            """
\\begin{frame}
\\multiinclude[graphics={},format=pdf]{myimage}
\\end{frame}
            """,
            pandoc_beamer_multigraphics.main,
            output_format="beamer",
        )

    def test_complete(self):
        self.verify_conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
---
![](myimage){.multigraphics start=1 end=3}
            """,
            """
\\begin{frame}
\\multiinclude[graphics={},start=1,end=3,format=pdf]{myimage}
\\end{frame}
            """,
            pandoc_beamer_multigraphics.main,
            output_format="beamer",
        )

    def test_meta1(self):
        self.verify_conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
    format: png
    height: 20cm
---
![](myimage){.multigraphics}
            """,
            """
\\begin{frame}
\\multiinclude[graphics={height=20cm},format=png]{myimage}
\\end{frame}
            """,
            pandoc_beamer_multigraphics.main,
            output_format="beamer",
        )

    def test_meta2(self):
        self.verify_conversion(
            """
---
pandoc-beamer-multigraphics:
  - classes: [multigraphics]
    format: png
    width: 20cm
---
![](myimage){.multigraphics}
            """,
            """
\\begin{frame}
\\multiinclude[graphics={width=20cm},format=png]{myimage}
\\end{frame}
            """,
            pandoc_beamer_multigraphics.main,
            output_format="beamer",
        )
