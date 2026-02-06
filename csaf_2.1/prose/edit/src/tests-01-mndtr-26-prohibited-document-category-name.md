### Prohibited Document Category Name

It MUST be tested that the document category is not equal to the (case insensitive) name (without the prefix `csaf_`) or
value of any other profile than "CSAF Base".
Any occurrences of dash, hyphen, minus, white space, and underscore characters are removed from the values on both sides before the
case insensitive match.

> The characters listed above are independent of their graphical variants.
> In general, all corresponding unicode characters are part of the group.
> For example, dash, hyphen and underscore characters include, but are not limited to:
>
> * Em dash
> * En dash
> * Figure dash
> * Horizontal bar
> * Hyphen
> * Hyphen-minus
> * Non-breaking hyphen
> * Low line
> * Combining low line
> * Fullwidth low line

This applies for both, the comparison against the name and value.
Also the value MUST NOT start with the reserved prefix `csaf_` except if the value is exactly `csaf_base`.

This test does only apply for CSAF documents with the profile "CSAF Base".
Therefore, it MUST be skipped if the document category matches one of the values defined for the profile other than "CSAF Base".

> For CSAF 2.1, the test must be skipped for the following values in `/document/category`:
>
> ```
>  csaf_base
>  csaf_deprecated_security_advisory
>  csaf_informational_advisory
>  csaf_security_advisory
>  csaf_security_incident_response
>  csaf_superseded
>  csaf_vex
>  csaf_withdrawn
> ```

This is the only mandatory test related to the profile "CSAF Base" as the required fields SHALL be checked by validating the JSON schema.

The relevant path for this test is:

```
  /document/category
```

*Examples 1 (for currently prohibited values):*

```
  Csaf_a
  CsaF_VeX
  CSafDeprecatedSecurity—Advisory
  csafvex
  Deprecated Security Advisory
  Informational Advisory
  Security      Advisory
  security-incident-response
  Superseded
  V_eX
  veX
  withdrawn
```

*Example 2 (which fails the test):*

```
  "category": "Security_Incident_Response"
```

> The value `Security_Incident_Response` is the name of a profile where the space was replaced with underscores.
