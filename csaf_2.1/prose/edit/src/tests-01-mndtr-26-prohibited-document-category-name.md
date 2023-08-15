### Prohibited Document Category Name

It MUST be tested that the document category is not equal to the (case insensitive) name (without the prefix `csaf_`) or
value of any other profile than "CSAF Base". Any occurrences of dash, whitespace,
and underscore characters are removed from the values on both sides before the match.
Also the value MUST NOT start with the reserved prefix `csaf_` except if the value is `csaf_base`.

This test does only apply for CSAF documents with the profile "CSAF Base".
Therefore, it MUST be skipped if the document category matches one of the values defined for the profile other than "CSAF Base".

> For CSAF 2.0, the test must be skipped for the following values in `/document/category`:
>
> ```
>   csaf_base
>   csaf_security_incident_response
>   csaf_informational_advisory
>   csaf_security_advisory
>   csaf_vex
> ```

This is the only mandatory test related to the profile "CSAF Base" as the required fields SHALL be checked by validating the JSON schema.

The relevant path for this test is:

```
  /document/category
```

*Examples 74 for currently prohibited values:*

```
  Csaf_a
  Informational Advisory
  security-incident-response
  Security      Advisory
  veX
  V_eX
```

*Example 75 which fails the test:*

```
  "category": "Security_Incident_Response"
```

> The value `Security_Incident_Response` is the name of a profile where the space was replaced with underscores.
