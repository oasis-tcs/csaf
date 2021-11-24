Instructions - to accompany Committee Note markdown templates.

This file: should be cn-template-README-v0.4.txt (or similar)
Questions or suggestions for improvement: please contact Paul Knight or Chet Ensign (OASIS TC Administration).

The template package (.zip) contains the following files and directories:
-- a markdown file (.md) ... this is the main template, customized with titles and other elements for this Work Product
-- an HTML version generated from the markdown (using the process described below) - for reference
-- a directory "styles" containing an HTML style sheet (.css)
-- a directory "images" containing an example image file

Structure:

OASIS currently supports the "github-flavored markdown" (gfm) variant of markdown.
- This allows URIs to be automatically hyperlinked in the resulting HTML, without extra format elements
- Allows section headers to use "#" markings only in front of section titles (not both sides)
- Allows generation of Table of Contents (TOC) in HTML via "pandoc"
- documentation is at https://github.github.com/gfm/

The accompanying markdown template provides the basic "skeleton" of an OASIS-styled document, and contains examples which demonstrate markdown syntax for many typical document components, including:

- Section numbering (maximum five levels)
- text
- text highlighting including bold, italics, and monospaced code blocks
- lists using several levels of bullets
- numbered lists
- tables
- images
- linkable captions for tables and images
- references to other documents
- internal cross-references to references, captions of images and tables, and numbered sections of the document

Usage:

OASIS publication rules require that both HTML and PDF versions of a Work Product must be published along with the "editable source" (markdown).

OASIS staff will usually prepare the HTML and PDF after the TC has approved the publication. However, the TC contributors and editors are responsible for the correct formatting and structure of the markdown source for the Work Product body.

In order to check that the markdown source will be rendered into HTML with the expected result, the TC should generate HTML and review it before approving the Work Product for publication.

How to use pandoc to generate the HTML from the markdown:
- We are currently using pandoc 2.6 from https://github.com/jgm/pandoc/releases/tag/2.6 (there are versions for Windows, macOS, and Linux)
- documentation is at https://pandoc.org/MANUAL.html - See "Pandoc's Markdown" (https://pandoc.org/MANUAL.html#pandocs-markdown) and "Markdown Variants" (https://pandoc.org/MANUAL.html#markdown-variants)

The command line we are currently using is fairly simple, including a link to a .css file, flags to generate a Table of Contents (TOC), and setting up a basic standalone HTML file with <head> and <body> tags:

pandoc -f gfm -t html <filename>.md -c styles/markdown-styles-v1.8-cn.css --toc --toc-depth=5 -s -o <filename>.html --metadata title="Title of Committee Note Version 1.0"

A customized version of this command line for this Work Product should be included in the "Introduction" section of the accompanying markdown and HTML files.

Notes:
- The TOC is generated at the top of the resulting HTML body. For final publication (by OASIS staff), it will be reformatted and moved down to the expected location below the OASIS Front Matter.
- The "front matter" lists without bullets (file URIs, Editors, etc.) use space-backslash for each list item except the last, to force a new line without a full paragraph break.
- The generated HTML file will include a tag which links to the .css file

Submit for publication:
After the TC verifies that the HTML file derived from the markdown is correct, the TC Editors should prepare a ZIP file for publication, including:
- the markdown file
- any images, in an "images" directory
- the .css style sheet, in a "styles" directory
- any other files which are a part of the Work Product
- there is usually no need to include an HTML version in the ZIP file

