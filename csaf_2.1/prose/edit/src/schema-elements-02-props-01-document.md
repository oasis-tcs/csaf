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

*Examples 1:*

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

*Examples 1:*

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
    2.1
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

*Examples 1:*

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
the textual description of the TLP version which is used in this document.
The default value is the URL to the definition by FIRST:

```
    https://www.first.org/tlp/
```

*Examples 1:*

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

*Example 1:*

```
    Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

##### Document Property - Publisher - Issuing Authority

Issuing authority (`issuing_authority`) of value type `string` with 1 or more characters Provides information about
the authority of the issuing party to release the document, in particular, the party's constituency and responsibilities or other obligations.

##### Document Property - Publisher - Name

The Name of publisher (`name`) of value type `string` with 1 or more characters contains the name of the issuing party.

*Example 1:*

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

*Examples 1:*

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

*Examples 1:*

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

*Example 1:*

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

*Examples 1:*

```
    Red Hat rhsa-to-cvrf
    Secvisogram
    TVCE
```

Engine version (`version`) of value type `string` with 1 or more characters contains the version of the engine that generated the CSAF document.

> Although it is not formally required, the TC suggests to use a versioning which is compatible with Semantic Versioning as described in
> the external specification [SemVer]. This could help the end user to identify when CSAF consumers have to be updated.

*Examples 2:*

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

*Examples 1:*

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
