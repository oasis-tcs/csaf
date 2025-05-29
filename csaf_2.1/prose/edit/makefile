.POSIX:
.SILENT:
.DEFAULT_GOAL = build

pyversion = py312
linelength = 120
black = black -S -l $(linelength) --target-version $(pyversion) --quiet bin
lint = ruff check bin
types = mypy bin

.PHONY: all
all: lint types build

.PHONY: format
format:
	command -v ruff >/dev/null 2>&1 || { echo >&2 "make format requires ruff but it's not installed - you can install with: 'pip install ruff'.  Aborting."; exit 1; }
	$(lint) --fix
	command -v black >/dev/null 2>&1 || { echo >&2 "make format requires black but it's not installed - you can install with: 'pip install black'.  Aborting."; exit 1; }
	$(black)

.PHONY: lint
lint:
	$(lint) --diff
	$(black) --check --diff
	command -v unmake >/dev/null 2>&1 || { echo >&2 "make lint requires unmake but it's not installed - you can install with: 'cargo install unmake'.  Aborting."; exit 1; }
	unmake makefile

.PHONY: types
types:
	command -v mypy >/dev/null 2>&1 || { echo >&2 "make types requires mypy but it's not installed - you can install with: 'pip install mypy'.  Aborting."; exit 1; }
	$(types)

.PHONY: inversions
inversions: invert-sections invert-examples

.PHONY: invert-examples
invert-examples: ; bin/invert_eg_labels.py

.PHONY: invert-sections
invert-sections: ; bin/invert_sec_labels.py

.PHONY: render
render: render-html

.PHONY: render-markdown
render-markdown: inversions
	bin/volatile.py && \
	cp -a build/tmp.md ../share/csaf-v2.1-draft.md && \
	printf "Rendered user facing delivery item in markdown format:\n" && \
	ls -l ../share/csaf-v2.1-draft.md

.PHONY: render-html
render-html: render-markdown
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make render-html requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	command -v tidy >/dev/null 2>&1 || { echo >&2 "make render-html requires tidy but it's not installed - you can get help on installing by searching for it on the wild internets.  Aborting."; exit 1; }
	pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345  \
		--css style/base.css --css style/skin.css --standalone -o build/tmp.html && \
	bin/toccata.py && \
	timeout 2 tidy -config etc/tidy-config.txt build/injected.html -ashtml 2>/dev/null | \
		sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > ../share/csaf-v2.1-draft.html && \
	printf "Rendered user facing delivery item in html format:\n" && \
	ls -l ../share/csaf-v2.1-draft.html

.PHONY: build
build: render status

.PHONY: status
status:
	printf "Current version control status:\n"; \
	git status
