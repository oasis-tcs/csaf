.DEFAULT_GOAL := build
.PHONY: build
build:
	bin/volatile.py
	cp -a build/tmp.md ../share/csaf-v2.1-draft.md
	pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345  --css style/base.css --css style/skin.css --standalone -o build/tmp.html
	bin/toccata.py
	timeout 2 tidy -config etc/tidy-config.txt build/injected.html -ashtml | sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > ../share/csaf-v2.1-draft.html
	git status
