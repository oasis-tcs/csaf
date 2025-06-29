### Document Property

Document level meta-data (`document`) of value type `object` with the 6 mandatory properties Category (`category`),
CSAF Version (`csaf_version`), Distribution (`distribution`), Publisher (`publisher`), Title (`title`),
and  Tracking (`tracking`) captures the meta-data about this document describing a particular set of security advisories.
In addition, the `document` object MAY provide the 7 optional properties Acknowledgments (`acknowledgments`),
Aggregate Severity (`aggregate_severity`), Language (`lang`), License expression (`license_expression`), Notes (`notes`),
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
        "license_expression": {
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

Rules for document sharing (`distribution`) of value type `object` with the mandatory property Traffic Light Protocol (TLP) (`tlp`) and the
optional properties Sharing Group (`sharing_group`) and Text (`text`) describes any constraints on how this document might be shared.

```
    "distribution": {
      // ...
      "properties": {
        "sharing_group": {
          // ...
        },
        "text": {
          // ...
        },
        "tlp": {
          // ...
        }
      }
    },
```

If multiple values are present, the TLP information SHOULD be preferred as this aids in automation.
The Sharing Group SHALL be interpreted as specification to the TLP information.
Therefore, the Sharing Group MAY also be used to convey special TLP restrictions:

*Examples 1:*

```
    E-ISAC members-only
    Only releasable to European Energy sector
    Releasable to NATO countries
```

> Note that for such restrictions the Sharing Group Name MUST exist and all participants MUST know the associated Sharing Group IDs to allow for automation.

##### Document Property - Distribution - Sharing Group

Sharing Group (`sharing_group`) of value type `object` with the mandatory property Sharing Group ID (`id`) and
the optional property Sharing Group Name (`name`) contains information about the group this document is intended to be shared with.

```
        "sharing_group": {
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

Sharing Group ID (`id`) of value type `string` with format `uuid` and `pattern` (regular expression):

```
    ^(([0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12})|([0]{8}-([0]{4}-){3}[0]{12})|([f]{8}-([f]{4}-){3}[f]{12}))$
```

Sharing Group ID provides the unique ID for the sharing group.
This ID is intended to be globally unique and MAY also be used by different issuing parties to share CSAF data within a closed group,
e.g. during a Multi-Party Coordinated Vulnerability Disclosure case.

> Note, that participants in such cases usually differ. Therefore, it is advised to use one ID per case.
> Otherwise, the consequences of adding or removing parties from a case and the implications to other cases have to be considered.

The ID SHOULD NOT change throughout different CSAF documents, if the same sharing group is addressed.
It MUST differ if a different sharing group is addressed.

> It is assumed that the ID is globally unique, if constructed according to the specification for UUID Version 4.

The ID SHALL be valid according to [cite](#RFC9562) and recorded in the 8-4-4-4-12 notation in lower case.
The ID SHALL be a UUID Version 4 for any closed sharing group, i.e. `TLP:GREEN` and above.

The following ID values SHOULD NOT be used unless there are technical reasons for them.
Therefore, they are reserved for implementation-specific situations:

- A system MAY use the Max UUID for `TLP:CLEAR` CSAF documents.
  > For example, the system uses the UUID as an indication whether a user allowed to see the document.
  > The security considerations from [cite](#RFC9562) should be reflected on.
- A system MAY use the Nil UUID for CSAF documents that MUST NOT be shared.
  > For example, the CSAF document is just being drafted and the accidental leakage should be prevented.

> Note, that both values do not indicate a closed sharing group.

A CSAF document with `TLP:CLEAR` SHOULD NOT contain a sharing group value and SHALL NOT contain any other value for the Sharing Group ID than Max UUID (`ffffffff-ffff-ffff-ffff-ffffffffffff`).

If an issuing party distributes multiple versions of a single CSAF document to different sharing groups, the rules for CSAF modifier (cf. section [sec](#conformance-clause-8-csaf-modifier)) regarding the generation of the value of `/document/tracking/id` SHALL be applied.
This implies that usually the sharing group ID is used as a prefix to the original `/document/tracking/id`.

Sharing Group Name (`name`) of value type `string` with one or more characters contains a human-readable name for the sharing group.

The Sharing Group Name is optional and can be chosen freely by the entity establishing the sharing group.
However, the following values are reserved for the conditions below:

- For the Max UUID, the value of `name` SHALL exist and be `Public`.
- For the Nil UUID, the value of `name` SHALL exist and be `No sharing allowed`.

##### Document Property - Distribution - Text

The Textual description (`text`) of value type `string` with 1 or more characters provides a textual description of additional constraints.

*Examples 1:*

```
    Copyright 2024, Example Company, All Rights Reserved.
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
    AMBER+STRICT
    CLEAR
    GREEN
    RED
```

> Note: In the TLP specification there are only 4 labels. The part `+STRICT` is an extension to `TLP:AMBER`.
> To simplify the JSON structure, avoid additional business level tests and aid in parsing, consumption and
> processing, it is provided as a label to be selected instead of having a separate field.

The default value for `label` is `CLEAR`.

> Note: This provides the suggested default value for anyone writing CSAF documents as the majority of those
> are intended to be publicly available.

The URL of TLP version (`url`) with value type `string` with format `uri` provides a URL where to find
the textual description of the TLP version which is used in this document.
The default value is the URL to the definition by FIRST:

```
    https://www.first.org/tlp/
```

*Examples 1:*

```
    https://www.us-cert.gov/tlp
    https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/TLP/merkblatt-tlp.pdf
```

#### Document Property - Language

Document language (`lang`) of value type Language Type (`lang_t`) identifies the language used by this document,
corresponding to IETF BCP 47 / RFC 5646.

#### Document Property - License Expression

License expression (`license_expression`) of value type `string` with 1 or more characters contains the SPDX license expression for the CSAF document.
It MUST NOT contain a license text.
See annex B of [cite](#SPDX301) for details.
The `DocumentRef` part given in that ABNF MUST NOT be used in CSAF.
Any SPDX license identifier not from the official SPDX license identifier list MUST contain a prefix of the form
`LicenseRef-<license-inventoring-entity>-` where `<license-inventoring-entity>` is replaced with a unique name for the entity that provided the
database this license identifier was found in.
The unique name MAY be a domain name.
The same applies for `AdditionRef-` user defined identifiers.

In addition, the following rules apply:

- License identification:
  1. The SPDX License List Version 3.26.0 or later MUST be consulted to identify the appropriate SPDX license identifier or
     construct an expression based on a SPDX license identifier.
     Deprecated license identifiers SHOULD NOT be used.
     SPDX license identifiers that were deprecated before the version listed above MUST NOT be used.
     > The list is available at <https://spdx.org/licenses/>.
     > It includes also the exceptions.
  2. If the appropriate license identifier is not found in the SPDX License List or expression been possible to constructed,
     the license database AboutCode's "ScanCode LicenseDB" MUST be consulted as a next step.
     License identifiers from this database MUST use the prefix `LicenseRef-scancode-`.
     > The database is currently available at <https://scancode-licensedb.aboutcode.org/>.

     The construction of a license expression with such an identifier is also allowed.
  3. If the first two steps did not result in an appropriate license identifier or expression and no extant identifier was found,
     the issuing party SHALL create their own license identifier following the rules above.
     The license identifier SHOULD contain the version number of the license.
     The license text MUST be made available through exactly one document note using the `category` `legal_disclaimer`.
     The `title` MUST be `License` for English or an unspecified document language.
     For any other language, it SHOULD be the language specific translation of that term.

- License similarity:
  - Annex C of [cite](#SPDX301) applies.

*Examples 1:*

```
  CC-BY-4.0
  LicenseRef-www.example.org-Example-CSAF-License-3.0+
  LicenseRef-scancode-public-domain
  MIT OR any-OSI
```

#### Document Property - Notes

Document notes (`notes`) of value type Notes Type (`notes_t`) holds notes associated with the whole document.

```
    "notes": {
      // ...
    },
```

The following combinations of `category` and `title` have a special meaning and MUST be used as stated below:

| `category` | `title` | content of `text` |
|---------------|---------------|-------------------|
| `description` | Product Description | Contains a description of a product given in the `product_tree` in regards to field of application and core functionality. This SHOULD be bound to the corresponding product or product group. |
| `general` | General Security Recommendations | Contains general advise and security recommendations that are related, generic and might be independently applicable of the content of the CSAF document. |
| `legal_disclaimer` | License | Contains the only license text of the document license. |
| `summary` | Summary | Contains a short summary of the content of the advisory. |

If a note is specific to a product or product group it MUST be bound via the `group_ids` respectively `product_ids`.

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
    multiplier
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

The value `multiplier` indicates individuals or organizations that use existing CSAF documents or information that could
be represented in CSAF, and create their own CSAF documents for distribution to a specific target audience.
A single multiplier might have target audiences.
> For example, a National CSIRT might create different CSAF documents for the same vulnerability for critical
  infrastructure companies in different sectors, government agencies, non-critical industry, and the public based on
  information sharing agreements and threats to the target group.
  
The creation step can make use of a CSAF modifier that replaces metadata, e.g. the document publisher.
Currently, this value includes multipliers, republishers, and forwarders.

The value `translator` indicates individuals or organizations that translate CSAF documents.
This includes all manner of language translators, also those who work for the party issuing the original advisory.

The value `other` indicates a catchall for everyone else. Currently this includes editors, reviewers,
and miscellaneous contributors.

The value `user` indicates anyone using a vendor’s product.

The value `vendor` indicates developers or maintainers of information system products or services.
This includes all authoritative product vendors, product security incident response teams (PSIRTs),
open source projects as well as product resellers and distributors, including authoritative vendor partners.

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
It SHALL NOT start or end with a white space and SHALL NOT contain a newline sequence.

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

Initial release date (`initial_release_date`) with value type `string` with format `date-time` holds the date when this document was first released to the specified target group.

> For `TLP:CLEAR` documents, this is usually the timestamp when the document was published.
> For `TLP:GREEN` and higher, this is the timestamp when it was first made available to the specific group.
> Note that the initial release date does not change after the initial release even if the document is later on released to a broader audience.

If the timestamp of the initial release date was set incorrectly, it MUST be corrected.
This change MUST be tracked with a new entry in the revision history.

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
