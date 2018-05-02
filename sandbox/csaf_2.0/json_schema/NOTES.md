
# Done

- json field names are lowercase and separated by "_"
- "#text" replaced with just "text"
- "product_tree" really is an array of branches or full products.

# Design

Formatting: Start a new line after every brace or bracket. Indent with each brace or bracket.

Naming: Lowercase names with underscores separating words for properties ("snake_eyes").

Naming: Shared definitions end with "_t", as in "non_empty_string_t".

Naming: Shared definitions of arrays end use a plural noun form, such as "notes_t".

Ordering: Properties and definitions are listed alphabetically. Enumerations are listed alphabetically.

More than one: Whenever there's the opportunity for more than one value,
the schema specifically does not support having just one. That is, always [{}], not just {}.

Extensibility: the "propertyNames" feature of JSON schema prevents future extension, and is only used where
no extensibility is ever intended.

# Comments

## Email address?

Since CVEs require email addresses, shouldn't a contact email be a first-class citizen of the document, rather
than being buried in a contact_details string?

## Maximums?

While these documents could be, in the abstract, unbounded, in practice they cannot be. What kinds of upper limits
should we consider?

## Names?

Suggested name change: score_set_v3 doesn't identify that it is a CVSS v3 Score. Suggested name "cvss_v3_score".

Suggested name change: cvss_score_sets presumes CVSS as the only way to score. How aboute "scores"?

# Of note

Documents translated from the XML did not have dates of the form valid RFC 3339, Section 5.6. Added "Z" to all of them.

# Concerns

## Array vs. Instance

In a number of places, the sample documents used either an array of items, or a single item. Recommend
that it always be an array, if multiple items are possible. This will make it considerably easier
to parse in languages that are not dynamically typed.

Examples:
- /document_tracking/revision_tracking/revision vs. /document_tracking/revision_tracking/revision[]
- /product_tree/branch vs. /product_tree/branch[]
- /vulnerability vs. /vulnerability[]

## Language selection

In one of the files, we have "document_title" as a string, and the other as an object with "lang" and "text" properties.

## Revision History Simplification

Currently have
  /document_tracking/revision_history/revision[]
Why not just have
  /document_tracking/revision_history[]

## Conversion created "#text" nodes

I renamed the "#text" nodes to "text", but they should be named even better than that.

# Redesign

The overall schema includes a number of "document_" fields. "document_notes", "document_tracking", "document_references",
"document_distribution."

Proposal is that we create a "document" property, and put those other properties of the document under the "document"
property.

## Status

In CVRF, the "ProductStatuses" element contains an array of Status elements which contain a type and a list of products.

Suggestion for JSON format:

product_status : {
  "fixed": [],
  "first_affected": [],
  "known_affected": [],
  "known_not_affected": [],
  "first_fixed": [],
  "recommended": [],
  "last_affected": []
}

# Questions

## Examples in the schema?

JSON Schema allows for examples. Do we want to put examples in? Or leave that to the specification document?
