### Public OpenPGP Key URL

It MUST be tested that the URL given as value of `public_openpgp_key_url` in the CSAF document
delivers a valid public OpenPGP key allowing encryption as ASCII armored file with the matching content type.
The test MUST be skipped if the URL results in a client or server error.

> As these might be temporary errors, they are reported through test [sec](#use-of-non-self-referencing-urls-failing-to-resolve).

The relevant path for this test is:

```list-of-jsonpaths
  $.document.publisher.contact.public_openpgp_key_url
```

*Example 1 (which fails the test):*

```
    "contact": {
      // ...
      "public_openpgp_key_url": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/test/validator/auxiliary/openpgp/expired.asc"
    },
```

> The `public_openpgp_key_url` points to an expired OpenPGP key.
