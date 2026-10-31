# Seeding the next version of CSAF

This folder serves as a showcase of an improved way
to edit, verify, and validate the next version of CSAF.

The main goals are (for now):

- extract examples to ensure validation
- refactor the source markdown into smaller chunks (per sections)
- set uo a binder text file that declares the order of concatenation of these source files
- automatically derive the section numbering from the order and an AST traversal
- generate the single elephant GFM+gh_cosmetics user facing delivery item from these source
- empower the editors by enfocing semantic references
- use vale for developer documentation spell checks
- use markdownlint to validate the sourc emarkdown files
- use pandoc and filters to generate html and pdf user facing delivery items
