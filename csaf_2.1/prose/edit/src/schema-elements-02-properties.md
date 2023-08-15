## Properties

These final three subsections document the three properties of a CSAF document.
The single mandatory property `document`, as well as the optional properties `product_tree` and `vulnerabilities` in that order.

### Document Property

Document level meta-data (`document`) of value type `object` with the 5 mandatory properties Category (`category`),
CSAF Version (`csaf_version`), Publisher (`publisher`), Title (`title`),
and  Tracking (`tracking`) captures the meta-data about this document describing a particular set of security advisories.
In addition, the `document` object MAY provide the 7 optional properties Acknowledgments (`acknowledgments`),
Aggregate Severity (`aggregate_severity`), Distribution (`distribution`), Language (`lang`), Notes (`notes`),
References (`references`), and Source Language (`source_lang`).

```
    "document": {
      // ...
      "properties": {
        "acknowledgments": {
          // ...
        },
        "aggregate_severity" : {
          // ...
        },
        "category": {
          // ...
        },
        "csaf_version": {
          // ...
        },
        "distribution": {
          // ...
        },
        "lang": {
          // ...
        },
        "notes": {
          // ...
        },
        "publisher": {
          // ...
        },
        "references": {
          // ...
        },
        "source_lang": {
          // ...
        },
        "title": {
          // ...
        },
        "tracking": {
          // ...
        }
      }
    },
```

#### Document Property - Acknowledgments

Document acknowledgments (`acknowledgments`) of value type Acknowledgments Type (`acknowledgments_t`) contains
a list of acknowledgment elements associated with the whole document.

```
    "acknowledgments": {
      // ...
    },
```

#### Document Property - Aggregate Severity

Aggregate severity (`aggregate_severity`) of value type `object` with the mandatory property `text` and
the optional property `namespace` is a vehicle that is provided by the document producer to convey the urgency and
criticality with which the one or more vulnerabilities reported should be addressed.
It is a document-level metric and applied to the document as a whole — not any specific vulnerability.
The range of values in this field is defined according to the document producer's policies and procedures.

```
    "aggregate_severity": {
      // ...
      "properties": {
        "namespace": {
          // ...
        },
        "text": {
          // ...
        }
      }
    },
```

The Namespace of aggregate severity (`namespace`) of value type `string` with format `uri` points to the namespace so referenced.

The Text of aggregate severity (`text`) of value type `string` with 1 or more characters provides a severity which is
independent of - and in addition to - any other standard metric for determining the impact or severity of a given vulnerability (such as CVSS).

*Examples 29:*

```
    Critical
    Important
    Moderate
```

#### Document Property - Category

Document category (`category`) with value type `string` of 1 or more characters with `pattern` (regular expression):

```
    ^[^\\s\\-_\\.](.*[^\\s\\-_\\.])?$
```

Document category defines a short canonical name, chosen by the document producer, which will inform the end user as to the category of document.

> It is directly related to the profiles defined in section [sec](#profiles).

```
    "category": {
      // ...
    }
```

*Examples 30*:

```
    csaf_base
    csaf_security_advisory
    csaf_vex
    Example Company Security Notice
```

#### Document Property - CSAF Version

CSAF version (`csaf_version`) of value type `string` and `enum` gives the version of the CSAF specification which the document was generated for.
The single valid value for this `enum` is:

```
    2.0
```

#### Document Property - Distribution

Rules for sharing document (`distribution`) of value type `object` with at least 1 of the 2 properties Text (`text`) and
Traffic Light Protocol (TLP) (`tlp`) describes any constraints on how this document might be shared.

```
    "distribution": {
      // ...
      "properties": {
        "text": {
          // ...
        },
        "tlp": {
          // ...
        }
      }
    },
```

If both values are present, the TLP information SHOULD be preferred as this aids in automation.

##### Document Property - Distribution - Text

The Textual description (`text`) of value type `string` with 1 or more characters provides a textual description of additional constraints.

*Examples 31:*

```
    Copyright 2021, Example Company, All Rights Reserved.
    Distribute freely.
    Share only on a need-to-know-basis only.
```

##### Document Property - Distribution - TLP

Traffic Light Protocol (TLP) (`tlp`) of value type `object` with the mandatory property Label (`label`) and
the optional property URL (`url`) provides details about the TLP classification of the document.

```
    "tlp": {
      // ...
      "properties": {
        "label": {
          // ...
        },
        "url": {
          // ...
        }
      }
    }
```

The Label of TLP (`label`) with value type `string` and `enum` provides the TLP label of the document.
Valid values of the `enum` are:

```
    AMBER
    GREEN
    RED
    WHITE
```

The URL of TLP version (`url`) with value type `string` with format `uri` provides a URL where to find 
he textual description of the TLP version which is used in this document.
The default value is the URL to the definition by FIRST:

```
    https://www.first.org/tlp/
```

*Examples 32:*

```
    https://www.us-cert.gov/tlp
    https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Merkblatt_TLP.pdf
```

#### Document Property - Language

Document language (`lang`) of value type Language Type (`lang_t`) identifies the language used by this document,
corresponding to IETF BCP 47 / RFC 5646.

#### Document Property - Notes

Document notes (`notes`) of value type Notes Type (`notes_t`) holds notes associated with the whole document.

```
    "notes": {
      // ...
    },
```

#### Document Property - Publisher

Publisher (`publisher`) has value type `object` with the mandatory properties Category (`category`), Name (`name`) and
Namespace (`namespace`) and provides information on the publishing entity.
The 2 other optional properties are: `contact_details` and `issuing_authority`.

```
    "publisher": {
      // ...
      "properties": {
        "category": {
          // ...
        },
        "contact_details": {
          // ...
        },
        "issuing_authority": {
          // ...
        },
        "name": {
          // ...
        }
        "namespace": {
          // ...
        }
      }
    },
```

##### Document Property - Publisher - Category

The Category of publisher (`category`) of value type `string` and `enum` provides information about the category of
publisher releasing the document.
The valid values are:

```
    coordinator
    discoverer
    other
    translator
    user
    vendor
```

The value `coordinator` indicates individuals or organizations that
manage a single vendor’s response or multiple vendors’ responses to a vulnerability, a security flaw, or an incident.
This includes all Computer Emergency/Incident Response Teams (CERTs/CIRTs) or agents acting on the behalf of a researcher.

The value `discoverer` indicates individuals or organizations that find vulnerabilities or security weaknesses.
This includes all manner of researchers.

The value `translator` indicates individuals or organizations that translate CSAF documents.
This includes all manner of language translators, also those who work for the party issuing the original advisory.

The value `other` indicates a catchall for everyone else. Currently this includes editors, reviewers, forwarders, republishers,
and miscellaneous contributors.

The value `user` indicates anyone using a vendor’s product.

The value `vendor` indicates developers or maintainers of information system products or services.
This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and
product resellers and distributors, including authoritative vendor partners.

##### Document Property - Publisher - Contact Details

Contact details (`contact_details`) of value type `string` with 1 or more characters provides information on how to contact the publisher,
possibly including details such as web sites, email addresses, phone numbers, and postal mail addresses.

*Example 33:*

```
    Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

##### Document Property - Publisher - Issuing Authority

Issuing authority (`issuing_authority`) of value type `string` with 1 or more characters Provides information about
the authority of the issuing party to release the document, in particular, the party's constituency and responsibilities or other obligations.

##### Document Property - Publisher - Name

The Name of publisher (`name`) of value type `string` with 1 or more characters contains the name of the issuing party.

*Example 34:*

```
     BSI
     Cisco PSIRT
     Siemens ProductCERT
```

##### Document Property - Publisher - Namespace

The Namespace of publisher (`namespace`) of value type `string` with format `uri` contains a URL which
is under control of the issuing party and can be used as a globally unique identifier for that issuing party.
The URL SHALL be normalized.

An issuing party can choose any URL which fulfills the requirements state above.
The URL MAY be dereferenceable. If an issuing party has chosen a URL, it SHOULD NOT change.
Tools can make use of the combination of `/document/publisher/namespace` and `/document/tracking/id` as it
identifies a CSAF document globally unique.

If an issuing party decides to change its Namespace it SHOULD reissue all CSAF documents with
an incremented (patch) version which has no other changes than:

* the new publisher information
* the updated revision history
* the updated item in `/document/references[]` which points to the new version of the CSAF document
* an added item in `/document/references[]` which points to the previous version of the CSAF document (if the URL changed)

*Example 35:*

```
    https://csaf.io
    https://www.example.com
```

#### Document Property - References

Document references (`references`) of value type References Type (`references_t`) holds a list of references associated with the whole document.

```
    "references": {
      // ...
    },
```

#### Document Property - Source Language

Source language (`source_lang`) of value type Language Type (`lang_t`) identifies if this copy of the document is
a translation then the value of this property describes from which language this document was translated.

The property MUST be present and set for any CSAF document with the value `translator` in `/document/publisher/category`.
The property SHALL NOT be present if the document was not translated.

> If an issuing party publishes a CSAF document with the same content in more than one language,
> one of these documents SHOULD be deemed the "original", the other ones SHOULD be considered translations from the "original".
> The issuing party can retain its original publisher information including the `category`.
> However, other rules defined in the conformance clause "CSAF translator" SHOULD be applied.

#### Document Property - Title

Title of this document (`title`) of value type `string` with 1 or more characters SHOULD be a canonical name for the document,
and sufficiently unique to distinguish it from similar documents.

*Examples 36:*

```
    Cisco IPv6 Crafted Packet Denial of Service Vulnerability
    Example Company Cross-Site-Scripting Vulnerability in Example Generator
```

#### Document Property - Tracking

Tracking (`tracking`) of value type `object` with the six mandatory properties: Current Release Date (`current_release_date`),
Identifier (`id`), Initial Release Date (`initial_release_date`), Revision History (`revision_history`), Status (`status`),
and Version (`version`) is a container designated to hold all management attributes necessary to track a CSAF document as a whole.
The two optional additional properties are Aliases (`aliases`) and Generator (`generator`).

```
    "tracking": {
      // ...
      "properties": {
        "aliases": {
          // ...
        },
        "current_release_date": {
          // ...
        },
        "generator": {
          // ...
        },
        "id": {
          // ...
        },
        "initial_release_date": {
          // ...
        },
        "revision_history": {
          // ...
        },
        "status": {
          // ...
        },
        "version": {
          // ...
        }
      }
    },
```

##### Document Property - Tracking - Aliases

Aliases (`aliases`) of value type `array` with 1 or more unique items (a `set`) representing Alternate Names contains a
list of alternate names for the same document.

```
    "aliases": {
      // ...
      "items": {
        // ...
      }
    },
```

Every such Alternate Name of value type `string` with 1 or more characters specifies a non-empty string that represents a
distinct optional alternative ID used to refer to the document.

*Example 37:*

```
    CVE-2019-12345
```

##### Document Property - Tracking - Current Release Date

Current release date (`current_release_date`) with value type `string` with format `date-time` holds the date when
the current revision of this document was released.

##### Document Property - Tracking - Generator

Document Generator (`generator`) of value type `object` with mandatory property Engine (`engine`) and
optional property Date (`date`) is a container to hold all elements related to the generation of the document.
These items will reference when the document was actually created, including the date it was generated and the entity that generated it.

```
        "generator": {
          // ...
          "properties": {
            "date": {
              // ...
            },
            "engine": {
              // ...
            }
          }
        },
```

Date of document generation (`date`) of value type `string` with format `date-time` SHOULD be the current date that the document was generated.
Because documents are often generated internally by a document producer and exist for a nonzero amount of time before being released,
this field MAY be different from the Initial Release Date and Current Release Date.

Engine of document generation (`engine`) of value type `object` with mandatory property Engine name (`name`) and
optional property Engine version (`version`) contains information about the engine that generated the CSAF document.

```
        "engine": {
          // ...
          "properties": {
            "name": {
              // ...
            },
            "version": {
              // ...
            }
          }
        },
```

Engine name (`name`) of value type `string` with 1 or more characters represents the name of the engine that generated the CSAF document.

*Examples 38:*

```
    Red Hat rhsa-to-cvrf
    Secvisogram
    TVCE
```

Engine version (`version`) of value type `string` with 1 or more characters contains the version of the engine that generated the CSAF document.

> Although it is not formally required, the TC suggests to use a versioning which is compatible with Semantic Versioning as described in
> the external specification [SemVer]. This could help the end user to identify when CSAF consumers have to be updated.

*Examples 39:*

```
    0.6.0
    1.0.0-beta+exp.sha.a1c44f85
    2
```

##### Document Property - Tracking - ID

Unique identifier for the document (`id`) of value type `string` with 1 or more characters with `pattern` (regular expression):

```
    ^[\\S](.*[\\S])?$
```

Unique identifier for the document holds the Identifier.

> It SHALL NOT start or end with a white space and SHALL NOT contain a line break.

The ID is a simple label that provides for a wide range of numbering values, types, and schemes.
Its value SHOULD be assigned and maintained by the original document issuing authority. It MUST be unique for that organization.

*Examples 40:*

```
    Example Company - 2019-YH3234
    RHBA-2019:0024
    cisco-sa-20190513-secureboot
```

> The combination of `/document/publisher/namespace` and `/document/tracking/id` identifies a CSAF document globally unique.

This value is also used to determine the filename for the CSAF document (cf. section [sec](#filename)).

##### Document Property - Tracking - Initial Release Date

Initial release date (`initial_release_date`) with value type `string` with format `date-time` holds the date when this document was first published.

##### Document Property - Tracking - Revision History

The Revision History (`revision_history`) with value type `array` of 1 or more Revision History Entries holds one revision item for each version of
the CSAF document, including the initial one.

```
        "revision_history": {
          // ...
          "items": {
            // ...
          }
        },
```

Each Revision contains all the information elements required to track the evolution of a CSAF document.
Revision History Entry items are of value type `object` with the three mandatory properties: Date (`date`), Number (`number`),
and Summary (`summary`).
In addition, a Revision MAY expose the optional property `legacy_version`.

```
        "properties": {
          "date": {
            // ...
          },
          "legacy_version": {
            // ...
          },
          "number": {
            // ...
          },
          "summary": {
            // ...
          }
        }
```

The Date of the revision (`date`) of value type `string` with format `date-time` states the date of the revision entry.

Legacy version of the revision (`legacy_version`) of value type `string` with 1 or more characters contains the version string used
in an existing document with the same content.

> This SHOULD be used to aid in the mapping between existing (human-readable) documents which might use a different version scheme and
> CSAF documents with the same content.
> It is recommended, to use the CSAF revision number to describe the revision history for any new human-readable equivalent.

The Number (`number`) has value type Version (`version_t`).

The Summary of the revision (`summary`) of value type `string` with 1 or more characters holds a single non-empty string representing
a short description of the changes.

Each Revision item which has a `number` of `0` or `0.y.z` MUST be removed from the document if the document status is `final`.
Versions of the document which are pre-release SHALL NOT have its own revision item.
All changes MUST be tracked in the item for the next release version.
Build metadata SHOULD NOT be included in the `number` of any revision item.

##### Document Property - Tracking - Status

Document status (`status`) of value type `string` and `enum` defines the draft status of the document.
The value MUST be one of the following:

```
    draft
    final
    interim
```

The value `draft` indicates, that this is a pre-release, intended for issuing party's internal use only,
or possibly used externally when the party is seeking feedback or indicating its intentions regarding a specific issue.

The value `final` indicates, that the issuing party asserts the content is unlikely to change.
“Final” status is an indication only, and does not preclude updates.
This SHOULD be used if the issuing party expects no, slow or few changes.

The value `interim` indicates, that the issuing party expects rapid updates.
This SHOULD be used if the expected rate of release for this document is significant higher than for other documents.
Once the rate slows down it MUST be changed to `final`. This MAY be done in a patch version.

> This is extremely useful for downstream vendors to constantly inform the end users about ongoing investigation.
> It can be used as an indication to pull the CSAF document more frequently.

##### Document Property - Tracking - Version

Version has the value type Version (`version_t`).

### Product Tree Property

Product Tree (`product_tree`) has value type `object` with 1 or more properties is a container for all fully qualified product names that
can be referenced elsewhere in the document.
The properties are Branches (`branches`), Full Product Names (`full_product_names`), Product Groups (`product_groups`),
and Relationships (`relationships`).

```
    "product_tree": {
      // ...
      "properties": {
        "branches": {
          // ...
        },
        "full_product_names": {
          // ...
        },
        "product_groups": {
          // ...
        },
        "relationships": {
          // ...
        }
      }
    },
```

#### Product Tree Property - Branches

List of branches (`branches`) has the value type `branches_t`.

#### Product Tree Property - Full Product Names

List of full product names (`full_product_names`) of value type `array` with 1 or more items of type `full_product_name_t` contains a
list of full product names.

#### Product Tree Property - Product Groups

List of product groups (`product_groups`) of value type `array` with 1 or more items of value type `object` contains a list of product groups.

```
    "product_groups": {
      // ...
      "items": {
        // ...
      }
    },
```

The product group items are of value type `object` with the 2 mandatory properties Group ID (`group_id`) and Product IDs (`product_ids`) and
the optional Summary (`summary`) property.

```
    "properties": {
      "group_id": {
        // ...
      },
      "product_ids": {
        // ...
      },
      "summary": {
        // ...
      }
    }
```

The summary of the product group (`summary`) of value type `string` with 1 or more characters gives a short, optional description of the group.

*Examples 41:*

```
    Products supporting Modbus.
    The x64 versions of the operating system.
```

Group ID (`group_id`) has value type Product Group ID (`product_group_id_t`).

List of Product IDs (`product_ids`) of value type `array` with 2 or more unique items of value type Product ID (`product_id_t`) lists
the product_ids of those products which known as one group in the document.

#### Product Tree Property - Relationships

List of relationships (`relationships`) of value type `array` with 1 or more items contains a list of relationships.

```
    "relationships": {
      // ...
      "items": {
        // ...
      }
    }
```

The Relationship item is of value type `object` and has four mandatory properties: Relationship category (`category`),
Full Product Name (`full_product_name`), Product Reference (`product_reference`), and Relates to Product Reference (`relates_to_product_reference`).
The Relationship item establishes a link between two existing `full_product_name_t` elements,
allowing the document producer to define a combination of two products that form a new `full_product_name` entry.

```
    "properties": {
      "category": {
        // ...
      },
      "full_product_name": {
        // ...
      },
      "product_reference": {
        // ...
      },
      "relates_to_product_reference": {
        // ...
      }
    }
```

> The situation where a need for declaring a Relationship arises,
> is given when a product is e.g. vulnerable only when installed together with another, or to describe operating system components.

Relationship category (`category`) of value type `string` and `enum` defines the category of relationship for the referenced component.
The valid values are:

```
    default_component_of
    external_component_of
    installed_on
    installed_with
    optional_component_of
```

The value `default_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is a default component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `external_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is an external component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `installed_on` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is installed on a platform entity with
another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `installed_with` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is installed alongside
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `optional_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is an optional component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

Full Product Name (`full_product_name`) of value type Full Product Name Type (`full_product_name_t`).

Product Reference (`product_reference`) of value type Product ID (`product_id_t`) holds a Product ID that refers to the Full Product Name element,
which is referenced as the first element of the relationship.

Relates to Product Reference (`relates_to_product_reference`) of value type Product ID (`product_id_t`) holds a Product ID that refers to
the Full Product Name element, which is referenced as the second element of the relationship.

*Example 42:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-908070601",
        "name": "Cisco AnyConnect Secure Mobility Client 4.9.04053"
      },
      {
        "product_id": "CSAFPID-908070602",
        "name": "Microsoft Windows"
      }
    ],
    "relationships": [
      {
        "product_reference": "CSAFPID-908070601",
        "category": "installed_on",
        "relates_to_product_reference": "CSAFPID-908070602",
        "full_product_name": {
          "product_id": "CSAFPID-908070603",
          "name": "Cisco AnyConnect Secure Mobility Client 2.3.185 installed on Microsoft Windows"
        }
      }
    ]
  }
```

> The product `Cisco AnyConnect Secure Mobility Client 4.9.04053"` (Product ID: `CSAFPID-908070601`) and the product `Microsoft Windows`
> (Product ID: `CSAFPID-908070602`) form together a new product with the separate Product ID `CSAFPID-908070603`.
> The latter one can be used to refer to that combination in other parts of the CSAF document.
> In example 34, it might be the case that `Cisco AnyConnect Secure Mobility Client 4.9.04053"` is only
> vulnerable when installed on `Microsoft Windows`.

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

*Examples 43:*

```
    CWE-22
    CWE-352
    CWE-79
```

The Weakness name (`name`) has value type `string` with 1 or more characters and holds the full name of the weakness as given
in the CWE specification.

*Examples 44:*

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

*Example 45:*

```
    Cisco Bug ID
    GitHub Issue
```

Text (`text`) of value type `string` with 1 or more characters is unique label or tracking ID for the vulnerability (if such information exists).

*Example 46:*

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

#### Vulnerabilities Property - Product Status

Product status (`product_status`) of value type `object` with 1 or more properties contains different lists of product_ids which
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
* `vulnerable_component`: Only the vulnerable component (as given by the elements of `product_ids` or `group_ids` in the current remediation item
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

Value type of every such Score item is `object` with the mandatory property `products` and the optional properties `cvss_v2` and
`cvss_v3` specifies information about (at least one) score of the vulnerability and for which products the given value applies.
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
          }
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
For consistency and simplicity, this section can be a mirror image of the CVSS "Exploitability" metric.
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
