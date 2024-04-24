### Vulnerabilities Property

Vulnerabilities (`vulnerabilities`) of value type `array` with 1 or more objects representing vulnerabilities and providing 1 or more
properties represents a list of all relevant vulnerability information items.

```
    "vulnerabilities": {
      // ...
      "items": {
        // ...
      }
    }
```

The Vulnerability item of value type `object` with 1 or more properties is a container for the aggregation of all fields that are related to
a single vulnerability in the document.
Any vulnerability MAY provide the optional properties Acknowledgments (`acknowledgments`), Common Vulnerabilities and Exposures (CVE) (`cve`),
Common Weakness Enumeration (CWE) (`cwe`), Discovery Date (`discovery_date`), Flags (`flags`), IDs (`ids`), Involvements (`involvements`),
Notes (`notes`), Product Status (`product_status`), References (`references`), Release Date (`release_date`), Remediations (`remediations`),
Scores (`scores`), Threats (`threats`), and Title (`title`).

```
    "properties": {
      "acknowledgments": {
        // ...
      },
      "cve": {
        // ...
      },
      "cwe": {
        // ...
      },
      "discovery_date": {
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
      "notes": {
        // ...
      },
      "product_status": {
        // ...
      },
      "references": {
        // ...
      },
      "release_date": {
        // ...
      },
      "remediations": {
        // ...
      },
      "scores": {
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

CVE (`cve`) of value type `string` with `pattern` (regular expression):

```
    ^CVE-[0-9]{4}-[0-9]{4,}$
```

holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability.

#### Vulnerabilities Property - CWE

CWE (`cwe`) of value type `object` with the 2 mandatory properties Weakness ID (`id`) and Weakness Name (`name`) holds the
MITRE standard Common Weakness Enumeration (CWE) for the weakness associated. For more information cf. [cite](#CWE).

```
    "cwe": {
      // ...
      "properties": {
        "id": {
          // ...
        },
        "name": {
          // ...
        }
      }
    },
```

The Weakness ID (`id`) has value type `string` with `pattern` (regular expression):

```
    ^CWE-[1-9]\\d{0,5}$
```

and holds the ID for the weakness associated.

*Examples 1:*

```
    CWE-22
    CWE-352
    CWE-79
```

The Weakness name (`name`) has value type `string` with 1 or more characters and holds the full name of the weakness as given
in the CWE specification.

*Examples 2:*

```
    Cross-Site Request Forgery (CSRF)
    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
```

#### Vulnerabilities Property - Discovery Date

Discovery date (`discovery_date`) of value type `string` with format `date-time` holds the date and time the vulnerability was originally discovered.

#### Vulnerabilities Property - Flags

List of flags (`flags`) of value type `array` with 1 or more unique items (a set) of value type `object` contains a list of machine readable flags.

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

The given values reflect the VEX not affected justifications. See [VEX-Justification] for more details. The values MUST be used as follows:

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

List of IDs (`ids`) of value type `array` with one or more unique ID items of value type `object` represents a list of unique labels or
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

System name (`system_name`) of value type `string` with 1 or more characters indicates the name of the vulnerability tracking or numbering system.

*Examples 1:*

```
    Cisco Bug ID
    GitHub Issue
```

Text (`text`) of value type `string` with 1 or more characters is unique label or tracking ID for the vulnerability (if such information exists).

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

List of involvements (`involvements`) of value type `array` with 1 or more items of value type `object` contains a list of involvements.

```
    "involvements": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Involvement item of value type `object` with the 2 mandatory properties Party (`party`), Status (`status`) and
the 2 optional properties Date of involvement (`date`) and Summary (`summary`) is a container that allows the document producers to
comment on the level of involvement (or engagement) of themselves (or third parties) in the vulnerability identification, scoping,
and remediation process.
It can also be used to convey the disclosure timeline.
The ordered tuple of the values of `party` and `date` (if present) SHALL be unique within `involvements`.

```
        "properties": {
          "date": {
            // ...
          },
          "party": {
            // ...
          },
          "status": {
            // ...
          },
          "summary": {
            // ...
          },
        }
```

Date of involvement (`date`) of value type `string` with format `date-time` holds the date and time of the involvement entry.

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

Summary of involvement (`summary`) of value type `string` with 1 or more characters contains additional context regarding what is going on.

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

#### Vulnerabilities Property - Product Status

Product status (`product_status`) of value type `object` with 1 or more properties contains different lists of `product_ids` which
provide details on the status of the referenced product related to the current vulnerability.
The eight defined properties are First affected (`first_affected`), First fixed (`first_fixed`), Fixed (`fixed`), Known affected (`known_affected`),
Known not affected (`known_not_affected`), Last affected (`last_affected`), Recommended (`recommended`),
and Under investigation (`under_investigation`) are all of value type Products (`products_t`).

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
          // ..
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
See `/vulnerabilities[]/threats` in category `impact` for more details.

Last affected (`last_affected`) of value type Products (`products_t`) represents that these are the last versions in a release train known to be
affected by the vulnerability. Subsequently released versions would contain a fix for the vulnerability.

Recommended (`recommended`) of value type Products (`products_t`) represents that these versions have a fix for the vulnerability and are
the vendor-recommended versions for fixing the vulnerability.

Under investigation (`under_investigation`) of value type Products (`products_t`) represents that it is not known yet whether these versions are or
are not affected by the vulnerability.
However, it is still under investigation - the result will be provided in a later release of the document.

#### Vulnerabilities Property - References

Vulnerability references (`references`) of value type References Type (`references_t`) holds a
list of references associated with this vulnerability item.

```
    "references": {
      // ...
    },
```

#### Vulnerabilities Property - Release Date

Release date (`release_date`) with value type `string` of format `date-time` holds the date and time
the vulnerability was originally released into the wild.

#### Vulnerabilities Property - Remediations

List of remediations (`remediations`) of value type `array` with 1 or more Remediation items of value type `object` contains a list of remediations.

```
    "remediations": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Remediation item of value type `object` with the 2 mandatory properties Category (`category`) and
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
    mitigation
    no_fix_planned
    none_available
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
This value contradicts with the categories `none_available` and `no_fix_planned` for the same product.
Therefore, such a combination can't be used in the list of remediations.

The value `none_available` indicates that there is currently no fix or other remediation available.
The text in field `details` SHOULD contain details about why there is no fix or other remediation.
The values `none_available` and `vendor_fix` are mutually exclusive per product.

> An issuing party might choose to use this category to announce that a fix is currently developed.
It is recommended that this also includes a date when a customer can expect the fix to be ready and distributed.  

The value `no_fix_planned` indicates that there is no fix for the vulnerability and it is not planned to provide one at any time.
This is often the case when a product has been orphaned, declared end-of-life, or otherwise deprecated.
The text in field `details` SHOULD contain details about why there will be no fix issued.
The values `no_fix_planned` and `vendor_fix` are mutually exclusive per product.

##### Vulnerabilities Property - Remediations - Date

Date of the remediation (`date`) of value type `string` with format `date-time` contains the date from which the remediation is available.

##### Vulnerabilities Property - Remediations - Details

Details of the remediation (`details`) of value type `string` with 1 or more characters contains a thorough human-readable discussion of the remediation.

##### Vulnerabilities Property - Remediations - Entitlements

List of entitlements (`entitlements`) of value type `array` with 1 or more items of type Entitlement of the remediation as `string` with
1 or more characters contains a list of entitlements.

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

Restart required by remediation (`restart_required`) of value type `object` with the 1 mandatory property Category (`category`) and
the optional property Details (`details`) provides information on category of restart is required by this remediation to become effective.

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

Additional restart information (`details`) of value type `string` with 1 or more characters provides additional information for the restart.
This can include details on procedures, scope or impact.

##### Vulnerabilities Property - Remediations - URL

URL (`url`) of value type `string` with format `uri` contains the URL where to obtain the remediation.

#### Vulnerabilities Property - Scores

List of scores (`scores`) of value type `array` with 1 or more items of type score holds a list of score objects for the current vulnerability.

```
    "scores": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Score item is `object` with the mandatory property `products` and the optional properties `cvss_v2`,
`cvss_v3` and `cvss_v4` specifies information about (at least one) score of the vulnerability and for which products the given value applies.
Each Score item has at least 2 properties.

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
          "products": {
            // ...
          }
        }
```

The property CVSS v2 (`cvss_v2`) holding a CVSS v2.0 value abiding by the schema at
[https://www.first.org/cvss/cvss-v2.0.json](https://www.first.org/cvss/cvss-v2.0.json).

The property CVSS v3 (`cvss_v3`) holding a CVSS v3.x value abiding by one of the schemas at
[https://www.first.org/cvss/cvss-v3.0.json](https://www.first.org/cvss/cvss-v3.0.json) or
[https://www.first.org/cvss/cvss-v3.1.json](https://www.first.org/cvss/cvss-v3.1.json).

The property CVSS v4 (`cvss_v4`) holding a CVSS v4.0 value abiding by the schema at [https://www.first.org/cvss/cvss-v4.0.json](https://www.first.org/cvss/cvss-v4.0.json).

Product IDs (`products`) of value type `products_t` with 1 or more items indicates for which products the given scores apply.
A score object SHOULD reflect the associated product's status (for example,
a fixed product no longer contains a vulnerability and should have a CVSS score of 0, or simply no score listed;
the known affected versions of that product can list the vulnerability score as it applies to them).

#### Vulnerabilities Property - Threats

List of threats (`threats`) of value type `array` with 1 or more items of value type `object` contains
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

Details of the threat (`details`) of value type `string` with 1 or more characters represents a thorough human-readable discussion of the threat.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current threat item applies to.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current threat item applies to.

#### Vulnerabilities Property - Title

Title (`title`) has value type `string` with 1 or more characters and gives the document producer the ability to apply a canonical name or
title to the vulnerability.

-------
