### Product Description without Product Reference

For each product description it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

> If the document language is English or unspecified, the product description can be identified by checking for a note containing the corresponding
> `category` and `title` combination from [sec](#document-property-notes).
> For other languages, the language specific translation is used.

If no language specific translation has been recorded, the test MUST be skipped and output an information to the user that no translation for
product description is known.

The relevant path for this test is:

```
  /document/notes[]
```

*Example 1 (which fails the test):*

```
    "notes": [
      {
        "category": "description",
        "text": "Product A is a local time tracking tool. It is mainly used by software developers and can be connected with most modern time-tracking systems.",
        "title": "Product Description"
      }
    ],
```

> The given note item does not specify to which products it applies to.
