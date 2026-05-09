### Usage of Deprecated Profile

It MUST be tested that the `$.document.category` does not start with `csaf_deprecated_`.

> To implement this test it is deemed sufficient to do a "starts with" check.
> In contrast to test [sec](#prohibited-document-category-name), this test detects the use of a profile defined by CSAF that is deprecated.

The relevant path for this test is:

```
   $.document.category
```

*Example 1 (which fails the test):*

```
    "category": "csaf_deprecated_security_advisory",

```

> The document category starts with `csaf_deprecated_`.
