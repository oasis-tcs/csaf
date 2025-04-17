### Usage of Non-Latest CWE Version

For each item in the CWE array it MUST be tested that the latest CWE version available at the time of the last revision was used.
The test SHALL fail if a later CWE version was used.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "tracking": {
      "current_release_date": "2024-01-21T10:00:00.000Z",
      // ...
    }
  },
  "vulnerabilities": [
    {
      "cwes": [
        {
          "id": "CWE-256",
          "name": "Plaintext Storage of a Password",
          "version": "4.12"
        }
      ]
    }
  ]
```

> The CWE version listed is `4.12`. However, version `4.13` was most recent version when the document was released on `2024-01-21T10:00:00.000Z`.

> A tool MAY suggest to use the latest version available at the time of the `current_release_date`.
> This is most likely also the overall latest CWE version as modifications to a CSAF document lead to a new `current_release_date`.
