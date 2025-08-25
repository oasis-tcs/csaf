### Non-Existing License Identifier

It MUST be tested that all license identifier and exceptions used exist.
This SHALL be tested for the SPDX license list and AboutCode's "ScanCode LicenseDB".
The test MAY be skipped for other license inventoring entities.

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
  "license_expression": "A-License-Identifier-That-Does-Not-Exist",
```

> The license identifier does not exist in the SPDX license list.
