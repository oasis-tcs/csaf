#! /usr/bin/env bash
# Transform PNG logo from OASIS into a DATA-URL format we can embed into the HTML
# shellcheck disable=SC2002
outfile="logo-data-url.txt"
tool="$0"
: "${1?"usage: $tool path-to-png-file"}"
printf "%s" "data:image/png;base64,$(cat "$1" | base64 | tr -d '\r\n')" > "${outfile}"
printf "INFO: tool(%s) wrote data-url representation of (%s) into (%s) at (%s)\n" "$0" "$1" "${outfile}" "${PWD}"
