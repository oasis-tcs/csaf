### Public OpenPGP Key URL User ID

It SHALL be tested that the URL given as value of `public_openpgp_key_url` in the CSAF document
delivers a public OpenPGP key with an email in the user ID matching the sibling property `email`.
The test SHALL be skipped if the URL results in a client or server error or
the OpenPGP key retrieved is not in ASCII-armored format.
The test SHALL report if the user ID is not set or empty.

> The cases excluded are handled through tests [sec](#use-of-non-self-referencing-urls-failing-to-resolve)
> and [sec](#public-openpgp-key-url).

The relevant path for this test is:

```list-of-jsonpaths
  $.document.publisher.contact.public_openpgp_key_url
```

*Example 1 (which fails the test):*

```
    "contact": {
      "email": "test-6.3.24@csaf.example",
      "public_openpgp_key_url": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/test/validator/auxiliary/openpgp/5-years-valid.asc"
    },
```

> The `public_openpgp_key_url` points to an OpenPGP key where the user ID does not match the email given in the sibling property `email`.
>
> Note: A difference between the email address in the user ID and the value of the property `email` does not necessarily mean
> that the receiver of the email is unable to decrypt the messages.

Recommendation:

It is recommended that issuing parties conduct an analysis to make an informed decision based on pros and cons regarding the
inclusion of a matching email address into the user ID of the public OpenPGP key.
Sections [sec](#document-property---publisher---contact) and [sec](#safety-security-and-data-protection-considerations) contain advise to take into consideration.
