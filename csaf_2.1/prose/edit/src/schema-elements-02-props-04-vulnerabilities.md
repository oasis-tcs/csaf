### Vulnerabilities Property

Vulnerabilities (`vulnerabilities`) of value type `array` with `1` or more objects representing vulnerabilities by providing one or more
properties represents a list of all relevant vulnerability information items.

```
    "vulnerabilities": {
      // ...
      "items": {
        // ...
      }
    }
```

The Vulnerability item of value type `object` with `1` or more properties is a container for the aggregation of all fields that are related to
a single vulnerability in the document.
Any vulnerability MAY provide the optional properties Acknowledgments (`acknowledgments`), Common Vulnerabilities and Exposures (CVE) (`cve`),
Common Weakness Enumeration (CWE) (`cwes`), Disclosure Date (`disclosure_date`), Discovery Date (`discovery_date`),
List of first known exploitation dates (`first_known_exploitation_dates`), Flags (`flags`), IDs (`ids`), Involvements (`involvements`),
Metrics (`metrics`), Notes (`notes`), Product Status (`product_status`), References (`references`), Remediations (`remediations`),
Threats (`threats`), and Title (`title`).

```
    "properties": {
      "acknowledgments": {
        // ...
      },
      "cve": {
        // ...
      },
      "cwes": {
        // ...
      },
      "disclosure_date": {
        // ...
      },
      "discovery_date": {
        // ...
      },
      "first_known_exploitation_dates": {
        // ...
      },
      "flags": {
        // ...
      },
      "ids": {
        // ...
      },
      "involvements": {
        // ...
      },
      "metrics": {
        // ...
      },
      "notes": {
        // ...
      },
      "product_status": {
        // ...
      },
      "references": {
        // ...
      },
      "remediations": {
        // ...
      },
      "threats": {
        // ...
      },
      "title": {
        // ...
      }
    }
```

#### Vulnerabilities Property - Acknowledgments

Vulnerability acknowledgments (`acknowledgments`) of value type Acknowledgments Type (`acknowledgments_t`) contains a list of
acknowledgment elements associated with this vulnerability item.

```
    "acknowledgments": {
      // ...
    },
```

#### Vulnerabilities Property - CVE

CVE (`cve`) has value type `string` with `pattern` (regular expression):

```
    ^CVE-[0-9]{4}-[0-9]{4,}$
```

CVE holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability.

#### Vulnerabilities Property - CWEs

List of CWEs (`cwes`) of value type `array` with `1` or more unique items (a set) of value type `object` contains a list of CWEs.

```
    "cwes": {
      // ...
      "items": {
        // ...
      }
    },
```

> It is expected that the list of CWEs is ordered from the most specific weakness ID to the least specific one.

Every CWE item of value type `object` with the three mandatory properties Weakness ID (`id`), Weakness Name (`name`), CWE version (`version`)
holds the MITRE standard Common Weakness Enumeration (CWE) for the weakness associated.
For more information cf. [cite](#CWE).

```
      "properties": {
        "id": {
          // ...
        },
        "name": {
          // ...
        },
        "version": {
          // ...
        }
      }
```

The Weakness ID (`id`) has value type `string` with `pattern` (regular expression):

```
    ^CWE-[1-9]\\d{0,5}$
```

It holds the ID for the weakness associated.

*Examples 1:*

```
    CWE-22
    CWE-352
    CWE-79
```

The Weakness name (`name`) has value type `string` of `1` or more characters with `pattern` (regular expression):

```
    ^[^\\s\\-_\\.](.*[^\\s\\-_\\.])?$
```

The Weakness name holds the full name of the weakness as given in the CWE specification.

*Examples 2:*

```
    Cross-Site Request Forgery (CSRF)
    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
```

The CWE version (`version`) has value type `string` with `pattern` (regular expression):

```
    ^[1-9]\\d*\\.([0-9]|([1-9]\\d+))(\\.\\d+)?$
```

It holds the version string of the CWE specification this weakness was extracted from.
When creating or modifying a CSAF document, the latest published version of the CWE specification SHOULD be used.

*Examples 3:*

```
    "1.0",
    "3.4.1",
    "4.0",
    "4.11",
    "4.12"
```

#### Vulnerabilities Property - Disclosure Date

Disclosure date (`disclosure_date`) of value type `string` with format `date-time` holds the date and time
the vulnerability was originally disclosed to the public.

For vulnerabilities not yet disclosed to the public, a disclosure date in the future SHOULD indicate the
intended date for disclosure of the vulnerability.
This is also sometimes called embargo date.
As disclosure dates may change during a vulnerability disclosure process, an issuing party SHOULD produce an updated CSAF document
to confirm that the vulnerability was in fact disclosed to the public at that time or update the `disclosure_date` with the new
intended date in the future.

#### Vulnerabilities Property - Discovery Date

Discovery date (`discovery_date`) of value type `string` with format `date-time` holds the date and time the vulnerability was originally discovered.

#### Vulnerabilities Property - First Known Exploitation Dates

List of first known exploitation dates (`first_known_exploitation_dates`) of value type `array` with `1` or more unique items (a set)
contains a list of dates of first known exploitations.

```
    "first_known_exploitation_dates": {
      // ...
      "items": {
        // ...
      }
    },
```

Every First known exploitation date item of value type `object` with the two mandatory properties Date of the information (`date`) and
Date of the exploitation (`exploitation_date`) holds at least `3` properties and contains information on when this vulnerability was
first known to be exploited in the wild in the products specified.
At least one of the optional elements Group IDs (`group_ids`) and Product IDs (`product_ids`) MUST be present to state for which products or
product groups this date is applicable.

> This information can be helpful to determine the risk of compromise.
> It can also be used to provide an indication for the time frame to be considered in a threat hunt for the exploitation this vulnerability.

```
    "properties": {
      "date": {
        // ...
      },
      "exploitation_date": {
        // ...
      },
      "group_ids": {
        // ...
      },
      "product_ids": {
        // ...
      }
    }
```

Date of the information (`date`) of value type `string` with format `date-time` contains the date when the information was last updated.

Date of the exploitation (`exploitation_date`) of value type `string` with format `date-time` contains the date when the exploitation happened.

> Different document issuers might have different knowledge about exploitations in the wild that happened.
> Therefore, the `exploitation_date` can differ.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current
first known exploitation date item applies to.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current first known exploitation date item
applies to.

#### Vulnerabilities Property - Flags

List of flags (`flags`) of value type `array` with `1` or more unique items (a set) of value type `object` contains a list of machine readable flags.

```
    "flags": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Flag item of value type `object` with the mandatory property Label (`label`) contains product specific information in regard to
this vulnerability as a single machine readable flag.
For example, this could be a machine readable justification code why a product is not affected.
At least one of the optional elements Group IDs (`group_ids`) and Product IDs (`product_ids`) MUST be present to state for which products or
product groups this flag is applicable.

> These flags enable the receiving party to automate the selection of actions to take.

In addition, any Flag item MAY provide the three optional properties Date (`date`), Group IDs (`group_ids`) and Product IDs (`product_ids`).

```
    "properties": {
      "date": {
        // ...
      },
      "group_ids": {
        // ...
      },
      "label": {
        // ...
      },
      "product_ids": {
        // ...
      }
    }
```

Date of the flag (`date`) of value type `string` with format `date-time` contains the date when assessment was done or the flag was assigned.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current flag item applies to.

Label of the flag (`label`) of value type `string` and `enum` specifies the machine readable label. Valid `enum` values are:

```
    component_not_present
    inline_mitigations_already_exist
    vulnerable_code_cannot_be_controlled_by_adversary
    vulnerable_code_not_in_execute_path
    vulnerable_code_not_present
```

The given values reflect the VEX not affected justifications.
See [VEX-Justification] for more details.
The values MUST be used as follows:

* `component_not_present`: The software is not affected because the vulnerable component is not in the product.
* `vulnerable_code_not_present`: The product is not affected because the code underlying the vulnerability is not present in the product.

  > Unlike `component_not_present`, the component in question is present, but for whatever reason (e.g. compiler options)
  > the specific code causing the vulnerability is not present in the component.

* `vulnerable_code_cannot_be_controlled_by_adversary`: The vulnerable component is present, and the component contains the vulnerable code.
  However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.
* `vulnerable_code_not_in_execute_path`: The affected code is not reachable through the execution of the code,
  including non-anticipated states of the product.

  > Components that are neither used nor executed by the product.

* `inline_mitigations_already_exist`: Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current flag item applies to.

#### Vulnerabilities Property - IDs

List of IDs (`ids`) of value type `array` with `1` or more unique ID items of value type `object` represents a list of unique labels or
tracking IDs for the vulnerability (if such information exists).

```
    "ids": {
      // ...
      "items": {
        // ...
      }
    },
```

Every ID item of value type `object` with the two mandatory properties System Name (`system_name`) and Text (`text`) contains a single unique label or
tracking ID for the vulnerability.

```
      "properties": {
        "system_name": {
          // ...
        },
        "text": {
          // ...
        }
      }
```

System name (`system_name`) of value type `string` with `1` or more characters indicates the name of the vulnerability tracking or numbering system.

*Examples 1:*

```
    Cisco Bug ID
    GitHub Issue
```

Text (`text`) of value type `string` with `1` or more characters is unique label or tracking ID for the vulnerability (if such information exists).

*Examples 2:*

```
    CSCso66472
    oasis-tcs/csaf#210
```

> General examples may include an identifier from a vulnerability tracking system that is available to customers, such as:
>
> * a Cisco bug ID,
> * a GitHub Issue number,
> * an ID from a Bugzilla system, or
> * an ID from a public vulnerability database such as the X-Force Database.
>
> The ID MAY be a vendor-specific value but is not to be used to publish the CVE tracking numbers
> (MITRE standard Common Vulnerabilities and Exposures), as these are specified inside the dedicated CVE element.

#### Vulnerabilities Property - Involvements

List of involvements (`involvements`) of value type `array` with `1` or more unique items (a set) of value type `object` contains a list of involvements.

```
    "involvements": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Involvement item of value type `object` with the two mandatory properties Party (`party`), Status (`status`) and
the five optional properties Party contact information (`contact`), Date of involvement (`date`), Group IDs (`group_ids`),
Product IDs (`product_ids`), and Summary (`summary`) is a container that allows the document producers to comment on the level of
involvement (or engagement) of themselves (or third parties) in the vulnerability identification, scoping, and remediation process.
It can also be used to convey the disclosure timeline.
The ordered tuple of the values of `party` and `date` (if present) SHALL be unique within `involvements`.

```
        "properties": {
          "contact": {
            // ...
          },
          "date": {
            // ...
          },
          "group_ids" {
            // ...
          },
          "party": {
            // ...
          },
          "product_ids": {
            // ...
          },
          "status": {
            // ...
          },
          "summary": {
            // ...
          }
        }
```

Party contact information (`contact`) contains the contact information of the party that was used in this state.

> In many cases, that could be an email address.

Date of involvement (`date`) of value type `string` with format `date-time` holds the date and time of the involvement entry.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current
involvement item applies to.

Party category (`party`) of value type `string` and `enum` defines the category of the involved party.
Valid values are:

```
    coordinator
    discoverer
    other
    user
    vendor
```

These values follow the same definitions as given for the publisher category (cf. section [sec](#document-property-publisher-category)).

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current
involvement item applies to.

Party status (`status`) of value type `string` and `enum` defines contact status of the involved party.
Valid values are:

```
    completed
    contact_attempted
    disputed
    in_progress
    not_contacted
    open
```

Each status is mutually exclusive - only one status is valid for a particular vulnerability at a particular time. As the vulnerability ages,
a party's involvement could move from state to state.
However, in many cases, a document producer may choose not to issue CSAF documents at each state, or simply omit this element altogether.
It is recommended, however, that vendors that issue CSAF documents indicating an open or in-progress involvement SHOULD eventually expect to issue
a document containing one of the statuses `disputed` or `completed` as the latest one.

> The two vulnerability involvement status states, `contact_attempted` and `not_contacted` are intended for use by document producers other than
> vendors (such as research or coordinating entities).

The value `completed` indicates that the party asserts that investigation of the vulnerability is complete.
No additional information, fixes, or documentation from the party about the vulnerability should be expected to be released.

The value `contact_attempted` indicates that the document producer attempted to contact the party.

The value `disputed` indicates that the party disputes the vulnerability report in its entirety.
This status SHOULD be used when the party believes that a vulnerability report regarding a product is completely inaccurate
(that there is no real underlying security vulnerability) or that the technical issue being reported has no security implications.

The value `in_progress` indicates that some hotfixes, permanent fixes, mitigations, workarounds,
or patches may have been made available by the party, but more information or fixes may be released in the future.
The use of this status by a vendor indicates that future information from the vendor about the vulnerability is to be expected.

The value `not_contacted` indicates that the document producer has not attempted to make contact with the party.

The value `open` is the default status.
It doesn’t indicate anything about the vulnerability remediation effort other than the fact that the party has acknowledged awareness of
the vulnerability report.
The use of this status by a vendor indicates that future updates from the vendor about the vulnerability are to be expected.

Summary of involvement (`summary`) of value type `string` with `1` or more characters contains additional context regarding what is going on.

#### Vulnerabilities Property - Metrics

List of metrics (`metrics`) of value type `array` with `1` or more unique items (a set)
contains metric objects for the current vulnerability.

```
    "metrics": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Metric item of value type `object` with the mandatory properties `content` and `products` and
the optional property `source` contains all metadata about the metric including products it applies to and the source and the content itself.

```
        "properties": {
          "content": {
            // ...
          },
          "products": {
            // ...
          },
          "source": {
            // ...
          }
        }
```

##### Vulnerabilities Property - Metrics - Content

Content (`content`) of value type `object` with the optional properties CVSS v2 (`cvss_v2`), CVSS v3 (`cvss_v3`), CVSS v4 (`cvss_v4`),
EPSS (`epss`), and SSVC v2 (`ssvc_v2`) specifies information about (at least one) metric or score for the given products regarding
the current vulnerability.
A Content object has at least `1` property.

```
        "properties": {
          "cvss_v2": {
            // ...
          },
          "cvss_v3": {
            "oneOf": [
              // ...
            ]
          },
          "cvss_v4": {
            // ...
          },
          "epss": {
            // ...
          },
          "ssvc_v2": {
            // ....
          }
        }
```

The property CVSS v2 (`cvss_v2`) holding a CVSS v2.0 value abiding by the schema at
[https://www.first.org/cvss/cvss-v2.0.json](https://www.first.org/cvss/cvss-v2.0.json).
See [cite](#CVSS2) for details.

The property CVSS v3 (`cvss_v3`) holding a CVSS v3.x value abiding by one of the schemas at
[https://www.first.org/cvss/cvss-v3.0.json](https://www.first.org/cvss/cvss-v3.0.json) or
[https://www.first.org/cvss/cvss-v3.1.json](https://www.first.org/cvss/cvss-v3.1.json).
See [cite](#CVSS30) respectively [cite](#CVSS31) for details.

The property CVSS v4 (`cvss_v4`) holding a CVSS v4.0 value abiding by the schema at
[https://www.first.org/cvss/cvss-v4.0.1.json](https://www.first.org/cvss/cvss-v4.0.1.json).
See [cite](#CVSS40) for details.

The property SSVC v2 (`ssvc_v2`) holding an SSVC Decision Point Value Selection v2.0.0 value abiding by the schema at
[https://certcc.github.io/SSVC/data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json](https://certcc.github.io/SSVC/data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json).
See [cite](#SSVC) for details.

The property EPSS (`epss`) of value type `object` with the three mandatory properties Percentile (`percentile`), Probability (`probability`)
and EPSS timestamp (`timestamp`) contains the EPSS data.
See [cite](#EPSS) for details.

```
            "properties": {
              "percentile": {
                // ...
              },
              "probability": {
                // ...
              },
              "timestamp": {
                // ...
              }
            }
```

Percentile (`percentile`) has value type `string` with `pattern` (regular expression):

```
    ^(([0]\\.([0-9])+)|([1]\\.[0]+))$
```

The value contains the rank ordering of probabilities from highest to lowest.

Probability (`probability`) has value type `string` with `pattern` (regular expression):

```
    ^(([0]\\.([0-9])+)|([1]\\.[0]+))$
```

The value contains the likelihood that any exploitation activity for this Vulnerability is being observed in the 30 days following the given timestamp.

EPSS timestamp (`timestamp`) of value type `string` with format `date-time` holds the date and time the EPSS value was recorded.

##### Vulnerabilities Property - Metrics - Products

Product IDs (`products`) of value type `products_t` with `1` or more items indicates for which products the given content applies.
A metric object SHOULD reflect the associated product's status (for example,
a fixed product no longer contains a vulnerability and should have a CVSS score of `0`, or simply no score listed;
the known affected versions of that product can list the vulnerability score as it applies to them).

##### Vulnerabilities Property - Metrics - Source

Source (`source`) of value type `string` with format `uri` contains the URL of the source that originally determined the metric.
If no source is given, then the metric was assigned by the document author.

> For example, this could point to the vendor advisory, discoverer blog post, a multiplier's assessment or other sources that provide metric information.

#### Vulnerabilities Property - Notes

Vulnerability notes (`notes`) of value type Notes Type (`notes_t`) holds notes associated with this vulnerability item.

```
    "notes": {
      // ...
    },
```

The following combinations of `category` and `title` have a special meaning and MUST be used as stated below:

| `category` | `title` | content of `text` |
|---------------|---------------|-------------------|
| `description` | CVE Description | Contains the official and unchanged CVE description for this specific vulnerability. |
| `description` | Preconditions | Contains a description of the preconditions that have to be fulfilled to be able to exploit the vulnerability, e.g. user account or physical access. |
| `summary` | Vulnerability Summary | Contains a summary of the vulnerability which is not the official CVE description. |

If a note is specific to a product or product group it MUST be bound via the `group_ids` respectively `product_ids`.

#### Vulnerabilities Property - Product Status

Product status (`product_status`) of value type `object` with `1` or more properties contains different lists of `product_ids` which
provide details on the status of the referenced product related to the current vulnerability.
The nine defined properties are First affected (`first_affected`), First fixed (`first_fixed`), Fixed (`fixed`), Known affected (`known_affected`),
Known not affected (`known_not_affected`), Last affected (`last_affected`), Recommended (`recommended`),
Under investigation (`under_investigation`) and Unknown (`unknown`) are all of value type Products (`products_t`).

```
    "product_status": {
      // ...
      "properties": {
        "first_affected": {
          // ...
        },
        "first_fixed": {
          // ...
        },
        "fixed": {
          // ...
        },
        "known_affected": {
          // ...
        },
        "known_not_affected": {
          // ...
        },
        "last_affected": {
          // ...
        },
        "recommended": {
          // ...
        },
        "under_investigation": {
          // ...
        },
        "unknown": {
          // ...
        }
      }
    },
```

First affected (`first_affected`) of value type Products (`products_t`) represents that these are the first versions of the releases known to be
affected by the vulnerability.

First fixed (`first_fixed`) of value type Products (`products_t`) represents that these versions contain the first fix for the vulnerability but
may not be the recommended fixed versions.

Fixed (`fixed`) of value type Products (`products_t`) represents that these versions contain a fix for the vulnerability but
may not be the recommended fixed versions.

Known affected (`known_affected`) of value type Products (`products_t`) represents that these versions are known to be affected by the vulnerability.
Actions are recommended to remediate or address this vulnerability.

> This could include for instance learning more about the vulnerability and context,
> and/or making a risk-based decision to patch or apply defense-in-depth measures.
> See `/vulnerabilities[]/remediations`, `/vulnerabilities[]/notes` and `/vulnerabilities[]/threats` for more details.

Known not affected (`known_not_affected`) of value type Products (`products_t`) represents that these versions are known not to be affected by
the vulnerability.
No remediation is required regarding this vulnerability.

> This could for instance be because the code referenced in the vulnerability is not present, not exposed, compensating controls exist,
> or other factors.
> See `/vulnerabilities[]/flags` and `/vulnerabilities[]/threats` in category `impact` for more details.

Last affected (`last_affected`) of value type Products (`products_t`) represents that these are the last versions in a release train known to be
affected by the vulnerability. Subsequently released versions would contain a fix for the vulnerability.

Recommended (`recommended`) of value type Products (`products_t`) represents that these versions have a fix for the vulnerability and are
the vendor-recommended versions for fixing the vulnerability.

Under investigation (`under_investigation`) of value type Products (`products_t`) represents that it is not known yet whether these versions are or
are not affected by the vulnerability.
However, it is still under investigation - the result will be provided in a later release of the document.

Unknown (`unknown`) of value type Products (`products_t`) represents that it is not known whether these versions are or are not affected by the
vulnerability.
There is also no investigation and therefore the status might never be determined.

The individual properties form the following product status groups:

* Affected:

   ```
   /vulnerabilities[]/product_status/first_affected[]
   /vulnerabilities[]/product_status/known_affected[]
   /vulnerabilities[]/product_status/last_affected[]
   ```

* Not affected:

  ```
  /vulnerabilities[]/product_status/known_not_affected[]
  ```

* Fixed:

  ```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  ```

* Under investigation:

  ```
  /vulnerabilities[]/product_status/under_investigation[]
  ```

* Unknown:

  ```
  /vulnerabilities[]/product_status/unknown[]
  ```

As the aforementioned product status groups contradict each other,
the sets formed by the contradicting groups within one vulnerability item MUST be pairwise disjoint.

> Note: An issuer might recommend (`/vulnerabilities[]/product_status/recommended`) a product version from any group - also from the affected group,
> i.e. if it was discovered that fixed versions introduce a more severe vulnerability.

#### Vulnerabilities Property - References

Vulnerability references (`references`) of value type References Type (`references_t`) holds a
list of references associated with this vulnerability item.

```
    "references": {
      // ...
    },
```

#### Vulnerabilities Property - Remediations

List of remediations (`remediations`) of value type `array` with `1` or more Remediation items contains a list of remediations.

```
    "remediations": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Remediation item of value type `object` with the two mandatory properties Category (`category`) and
Details (`details`) specifies details on how to handle (and presumably, fix) a vulnerability.
At least one of the optional elements Group IDs (`group_ids`) and Product IDs (`product_ids`) MUST be present to state for which
products or product groups this remediation is applicable.

In addition, any Remediation MAY expose the six optional properties Date (`date`), Entitlements (`entitlements`), Group IDs (`group_ids`),
Product IDs (`product_ids`), Restart required (`restart_required`), and URL (`url`).

```
      "properties": {
        "category": {
          // ...
        },
        "date": {
          // ...
        },
        "details": {
          // ...
        },
        "entitlements": {
          // ...
        },
        "group_ids": {
          // ...
        },
        "product_ids": {
          // ...
        },
        "restart_required": {
          // ...
        },
        "url": {
          // ...
        }
      }
```

##### Vulnerabilities Property - Remediations - Category

Category of the remediation (`category`) of value type `string` and `enum` specifies the category which this remediation belongs to.
Valid values are:

```
    fix_planned
    mitigation
    no_fix_planned
    none_available
    optional_patch
    vendor_fix
    workaround
```

The value `workaround` indicates that the remediation contains information about a configuration or specific deployment scenario that
can be used to avoid exposure to the vulnerability. There MAY be none, one, or more workarounds available.
This is typically the “first line of defense” against a new vulnerability before a mitigation or vendor fix has been issued or even discovered.

The value `mitigation` indicates that the remediation contains information about a configuration or deployment scenario that
helps to reduce the risk of the vulnerability but that does not resolve the vulnerability on the affected product.
Mitigations MAY include using devices or access controls external to the affected product.
Mitigations MAY or MAY NOT be issued by the original author of the affected product,
and they MAY or MAY NOT be officially sanctioned by the document producer.

The value `vendor_fix` indicates that the remediation contains information about an official fix that
is issued by the original author of the affected product.
Unless otherwise noted, it is assumed that this fix fully resolves the vulnerability.

The value `optional_patch` indicates that the remediation contains information about an patch that
is issued by the original author of the affected product.
Its application is not necessary, but might be desired by the user, e.g. to calm a security scanner by
updating a dependency to a fixed version even though the dependency in the affected version was used
in the product in a way that the product itself was not affected.
Unless otherwise noted, it is assumed that this does not change the state regarding the vulnerability.

> This is sometimes also referred to as a "regulatory compliance patch".

The value `none_available` indicates that there is currently no fix or other remediation available.
The text in field `details` SHOULD contain details about why there is no fix or other remediation.

The value `fix_planned` indicates that there is a fix for the vulnerability planned but not yet ready.
An issuing party might choose to use this category to announce that a fix is currently developed.
The text in field `details` SHOULD contain details including a date when a customer can expect the fix to be ready and distributed.

The value `no_fix_planned` indicates that there is no fix for the vulnerability and it is not planned to provide one at any time.
This is often the case when a product has been orphaned, declared end-of-life, or otherwise deprecated.
The text in field `details` SHOULD contain details about why there will be no fix issued.

Some category values contradict each other and thus are mutually exclusive per product.
Therefore, such a combination MUST NOT be used in the list of remediations for the same product.
This is independent from whether the product is referenced directly or indirectly through a product group.
The following tables shows the allowed and prohibited combinations:

| category value   | `workaround` | `mitigation` | `vendor_fix` | `optional_patch` | `none_available` | `fix_planned` | `no_fix_planned` |
|:----------------:|:------------:|:------------:|:------------:|:----------------:|:----------------:|:-------------:|:----------------:|
| `workaround`     | allowed      | allowed      | allowed      | prohibited       | prohibited       | allowed       | allowed          |
| `mitigation`     | allowed      | allowed      | allowed      | prohibited       | prohibited       | allowed       | allowed          |
| `vendor_fix`     | allowed      | allowed      | allowed      | prohibited       | prohibited       | prohibited    | prohibited       |
| `optional_patch` | prohibited   | prohibited   | prohibited   | allowed          | prohibited       | prohibited    | prohibited       |
| `none_available` | prohibited   | prohibited   | prohibited   | prohibited       | allowed          | prohibited    | prohibited       |
| `fix_planned`    | allowed      | allowed      | prohibited   | prohibited       | prohibited       | allowed       | prohibited       |
| `no_fix_planned` | allowed      | allowed      | prohibited   | prohibited       | prohibited       | prohibited    | allowed          |

Table 1: Remediation Combinations

Some category values contradict certain product status groups.
Therefore, such a combination MUST NOT exist in a vulnerability item for the same product.
This is independent from whether the product is referenced directly or indirectly through a product group.
The following tables shows the allowed, discouraged and prohibited combinations:

| category value   | Affected   | Not Affected | Fixed       | Under Investigation | Unknown     | Recommended |
|:----------------:|:----------:|:------------:|:-----------:|:-------------------:|:-----------:|:-----------:|
| `workaround`     | allowed    | prohibited   | prohibited  | discouraged         | discouraged | allowed     |
| `mitigation`     | allowed    | prohibited   | prohibited  | discouraged         | discouraged | allowed     |
| `vendor_fix`     | allowed    | prohibited   | prohibited  | discouraged         | discouraged | allowed     |
| `optional_patch` | prohibited | allowed      | discouraged | allowed             | allowed     | allowed     |
| `none_available` | allowed    | prohibited   | prohibited  | allowed             | allowed     | allowed     |
| `fix_planned`    | allowed    | discouraged  | prohibited  | discouraged         | discouraged | allowed     |
| `no_fix_planned` | allowed    | discouraged  | prohibited  | allowed             | allowed     | allowed     |

Table 2: Product Status Remediation Category Combinations

The following preference for combinations of remediation categories and product status groups is RECOMMENDED:

1. `vendor_fix` and Recommended
2. `mitigation` & Recommended
3. `workaround` & Recommended
4. `optional_patch` & Recommended
5. `vendor_fix` & Affected
6. `mitigation` & Affected
7. `workaround` & Affected
8. `optional_patch` & Under Investigation
9. `optional_patch` & Unknown
10. `fix_planned` & Recommended
11. `fix_planned` & Affected
12. `optional_patch` & Not Affected
13. `none_available` & Recommended
14. `no_fix_planned` & Recommended
15. `none_available` & Affected
16. `none_available` & Under Investigation
17. `none_available` & Unknown
18. `no_fix_planned` & Affected
19. `no_fix_planned` & Under Investigation
20. `no_fix_planned` & Unknown

The remaining discouraged combinations are appended at the end of the list:

1. `optional_patch` & Fixed
2. `vendor_fix` & Under Investigation
3. `vendor_fix` & Unknown
4. `mitigation` & Under Investigation
5. `mitigation` & Unknown
6. `workaround` & Under Investigation
7. `workaround` & Unknown
8. `fix_planned` & Under Investigation
9. `fix_planned` & Unknown
10. `fix_planned` & Not Affected
11. `no_fix_planned` & Not Affected

CSAF Viewers MAY sort the remediation items accordingly.

##### Vulnerabilities Property - Remediations - Date

Date of the remediation (`date`) of value type `string` with format `date-time` contains the date from which the remediation is available.

##### Vulnerabilities Property - Remediations - Details

Details of the remediation (`details`) of value type `string` with `1` or more characters contains a thorough human-readable
discussion of the remediation.

##### Vulnerabilities Property - Remediations - Entitlements

List of entitlements (`entitlements`) of value type `array` with `1` or more items of type Entitlement of the remediation as `string`
with `1` or more characters contains a list of entitlements.

```
                "entitlements": {
                  // ....
                  "items": {
                    // ...
                  }
                },
```

Every Entitlement of the remediation contains any possible vendor-defined constraints for obtaining fixed software or hardware that
fully resolves the vulnerability.

##### Vulnerabilities Property - Remediations - Group IDs

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of
Product Groups the current remediation item applies to.

##### Vulnerabilities Property - Remediations - Product IDs

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current remediation item applies to.

##### Vulnerabilities Property - Remediations - Restart Required

Restart required by remediation (`restart_required`) of value type `object` with the one mandatory property Category (`category`) and
the optional property Details (`details`) provides information on the category of restart required by this remediation to become effective.

```
      "restart_required": {
        // ...
        "properties": {
          "category": {
            // ...
          }
          "details": {
            // ...
          }
        }
      },
```

Category of restart (`category`) of value type `string` and `enum` specifies what category of restart is required by
this remediation to become effective.
Valid values are:

```
    connected
    dependencies
    machine
    none
    parent
    service
    system
    vulnerable_component
    zone
```

The values MUST be used as follows:

* `none`: No restart required.
* `vulnerable_component`: Only the vulnerable component (as given by the elements of `product_ids` or `group_ids` in the current remediation item)
   needs to be restarted.
* `service`: The vulnerable component and the background service used by the vulnerable component need to be restarted.
* `parent`: The vulnerable component and its parent process need to be restarted. This could be the case if the parent process has no build-in way
  to restart the vulnerable component or process values / context is only given at the start of the parent process.
* `dependencies`: The vulnerable component and all components which require the vulnerable component to work need to be restarted.
  This could be the case e.g. for a core service of a software.
* `connected`: The vulnerable component and all components connected (via network or any type of inter-process communication)
  to the vulnerable component need to be restarted.
* `machine`: The machine on which the vulnerable component is installed on needs to be restarted.
  This is the value which SHOULD be used if an OS needs to be restarted.
  It is typically the case for OS upgrades.
* `zone`: The security zone in which the machine resides on which the vulnerable component is installed needs to be restarted.
  This value might be useful for a remediation if no patch is available.
  If the malware can be wiped out by restarting the infected machines but the infection spreads fast the controlled shutdown of all machines at
  the same time and restart afterwards can leave one with a clean system.
* `system`: The whole system which the machine resides on which the vulnerable component is installed needs to be restarted.
  This MAY include multiple security zones. This could be the case for a major system upgrade in an ICS system or a protocol change.

Additional restart information (`details`) of value type `string` with `1` or more characters provides additional information for the restart.
This can include details on procedures, scope or impact.

##### Vulnerabilities Property - Remediations - URL

URL (`url`) of value type `string` with format `uri` contains the URL where to obtain the remediation.

#### Vulnerabilities Property - Threats

List of threats (`threats`) of value type `array` with `1` or more items of value type `object` contains
information about a vulnerability that can change with time.

```
    "threats": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Threat item of value type `object` with the two mandatory properties Category (`category`) and Details (`details`) contains
the vulnerability kinetic information.
This information can change as the vulnerability ages and new information becomes available.
In addition, any Threat item MAY expose the three optional properties Date (`date`), Group IDs (`group_ids`), and Product IDs (`product_ids`).

```
    "properties": {
      "category": {
        // ...
      }
      "date": {
        // ...
      },
      "details": {
        // ...
      },
      "group_ids": {
        // ...
      },
      "product_ids": {
        // ...
      }
    }
```

Category of the threat (`category`) of value type `string` and `enum` categorizes the threat according to the rules of the specification.
Valid values are:

```
    exploit_status
    impact
    target_set
```

The value `exploit_status` indicates that the `details` field contains a description of the degree to which an exploit for the vulnerability is known.
This knowledge can range from information privately held among a very small group to an issue that has been described to the public at
a major conference or is being widely exploited globally.
For consistency and simplicity, this section can be a mirror image of the CVSS `exploitMaturity` (v4.0),
respectively `exploitCodeMaturity` (v3.1 and v3.0) or `exploitability` (v2.0) metric.
However, it can also contain a more contextual status, such as "Weaponized" or "Functioning Code".

The value `impact` indicates that the `details` field contains an assessment of the impact on the user or the target set if
the vulnerability is successfully exploited or a description why it cannot be exploited.
If applicable, for consistency and simplicity, this section can be a textual summary of the three CVSS impact metrics.
These metrics measure how a vulnerability detracts from the three core security properties of an information system:
Confidentiality, Integrity, and Availability.

The value `target_set` indicates that the `details` field contains a description of
the currently known victim population in whatever terms are appropriate.
Such terms MAY include: operating system platform, types of products, user segments, and geographic distribution.

Date of the threat (`date`) of value type `string` with format `date-time` contains the date when the assessment was done or the threat appeared.

Details of the threat (`details`) of value type `string` with `1` or more characters represents a thorough human-readable discussion of the threat.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current threat item applies to.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current threat item applies to.

#### Vulnerabilities Property - Title

Title (`title`) has value type `string` with `1` or more characters and gives the document producer the ability to apply a canonical name or
title to the vulnerability.

-------
