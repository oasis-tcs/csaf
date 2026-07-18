// OASIS brand stylesheet for typst documents.
// Import in your per-spec pandoc template and apply with:
//   #import "../etc/oasis.typ": oasis-setup
//   #show: oasis-setup

#let oasis-setup(doc) = {

  // ── Typography ──────────────────────────────────────────────────────────────

  set text(font: "New Computer Modern", size: 10pt)
  set par(justify: true, leading: 0.65em)

  // ── Code blocks ─────────────────────────────────────────────────────────────
  // Font only; size is controlled by channels.typst.code-size in nide.yaml
  // (small → 0.85em, footnote → 0.75em, normal → 1em — default: small)

  show raw: set text(font: "New Computer Modern Math")
  show raw.where(block: true): it => block(
    fill: rgb("#e8e8e8"),
    inset: (x: 8pt, y: 6pt),
    radius: 3pt,
    width: 100%,
    it,
  )

  // ── Section headings (OASIS blue #446CAA, bold at all levels) ───────────────

  let oasis-blue = rgb("#446CAA")
  show heading: set text(fill: oasis-blue, weight: "bold")

  // ── Blockquotes (informal notes / editorial comments) ───────────────────────

  show quote.where(block: true): it => block(
    fill: rgb("#e8e8e8"),
    inset: (left: 12pt, rest: 8pt),
    radius: 3pt,
    width: 100%,
    it.body,
  )

  // ── Links ───────────────────────────────────────────────────────────────────

  show link: set text(fill: rgb("#0000EE"))

  // ── Tables ──────────────────────────────────────────────────────────────────
  // Header row: OASIS blue (#1a8cff) background, white bold text.
  // Non-header rows: no fill (page background shows through).

  set table(
    inset: 6pt,
    stroke: 0.5pt,
    fill: (x, y) => if y == 0 { rgb("#1a8cff") } else { none },
  )
  show table.cell.where(y: 0): set text(fill: white, weight: "bold")
  show figure.where(kind: table): set figure.caption(position: top)
  // Authors can reduce cell text size for wide tables by placing
  // \tablefontsize=small or \tablefontsize=footnote before the table in the source.
  // The directive is a no-op in the HTML and GFM-plus channels.
  // Caption is figure.caption, not table.cell, so it is always unaffected.
  let _nide-table-sizes = ("small": 0.85em, "footnote": 0.75em, "normal": 1em)
  let _nide-small-table = state("_nide-small-table", "normal")
  show figure.where(kind: table): it => context {
    set block(breakable: true)
    let sz-name = _nide-small-table.get()
    _nide-small-table.update("normal")
    if sz-name != "normal" {
      show table.cell: set text(size: _nide-table-sizes.at(sz-name))
      it
    } else {
      it
    }
  }

  // ── Definition lists ────────────────────────────────────────────────────────

  show terms.item: it => block(breakable: false)[
    #text(weight: "bold")[#it.term]
    #block(inset: (left: 1.5em, top: -0.4em))[#it.description]
  ]

  doc
}
