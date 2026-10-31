.POSIX:
.SILENT:
.DEFAULT_GOAL = check

# Vision variant: records/ are authored, the views are derived from them (see VISION.md).
#   make derive   write the views (test sections of the prose, testcases.json, views/roles/*.md)
#   make check    fail when a view differs from what the records give (run before committing)
#   make prose    derive, then build the prose as before (prose/edit, needs nide)

python ?= python3

.PHONY: derive check prose
derive:
	$(python) -I bin/vision.py derive

check:
	$(python) -I bin/vision.py check

prose: derive
	$(MAKE) -C prose/edit
