### Use of Unregistered License

It MUST be tested that the all license identifiers and exceptions are listed either in the official SPDX license identifier list
or AboutCode's "ScanCode LicenseDB".

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
    "license_expression": "LicenseRef-www.example.com-no-work-pd",
```

> The `license_expression` contains a license identifier that is neither listed in the official SPDX license identifier list
> nor AboutCode's "ScanCode LicenseDB".
