### Deprecated License Identifier

It MUST be tested that all license identifier and exceptions used are not deprecated.
This SHALL be tested for the SPDX license list and AboutCode's "ScanCode LicenseDB".
The test MAY be skipped for other license inventoring entities.

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
  "license_expression": "GFDL-1.1",
```

> The license identifier `GFDL-1.1` was deprecated as of version 3.0.
