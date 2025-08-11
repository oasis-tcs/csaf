# The CSAF 2.1 Prose Folder

This place offers access to the editable sources of the v2.1 CSAF specification (to be).

In the `share` folder there are the user facing delivery items that offer layout and navigation
optimized for online viewing per

- a typical web interface of a version control server (like Codeberg, GitHub, GitLab, or SourceHut) - the Markdown file
- any typical browser (like Brave, Chrome, Edge, Firefox, Orion, or Safari) - the HTML file

Inside the `edit` folder we build these delivery items from the source files (also in Markdown format, but
split by concerns, verifiable per syntax, and offering clean structural constructs for definition lists etc.
instead of the specific idioms mixed in for ease of use in specific reading tools).

To generate both the Markdown and the HTML user facing delivery items simply call `make` inside the edit folder.

Execution of any `make` target / dependency that uses non-standard tools, will verify the tools are available.
In case essential tools for the task are missing,
make will abort printing some information on what is missing and how such tool can be installed.


## Typical Editor Tasks

When changing section labels, positions of sections, or when adding, moving, or deleting examples,
the mappings have to be updated

Please only modify two of the four mapping files. The other two will be derived from the former.

Changes to section mapping:

1. Edit `etc/section-display-to-label.json` to align with the document
2. Eventually (when moving sections or renaming the labels) edit `etc/example-global-to-local.json` too.
3. Execute `make inversions` to derive the coresponding `etc/section-label-to-display.json` and
   `etc/example-local-to-global.json` files, or directly call `make`.
   The latter has the `inversions` target as dependency.

Changes only to examples:

1. Edit `etc/example-global-to-local.json` too.
2. Execute `make invert-examples` to derive the coresponding `etc/example-local-to-global.json` file, or directly call `make`.
   The latter has the `inversions` target as dependency.

In case the `make` command does detect `inverso` tool needed for the inversions as missing,
but does not print out the installation hint: `pip install inverso` should do the trick.
