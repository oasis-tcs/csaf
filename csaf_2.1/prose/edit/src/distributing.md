# Distributing CSAF documents

This section lists requirements and roles defined for distributing CSAF documents.
The first subsection provides all requirements - the second one the roles.
It is mandatory to fulfill the basic role "CSAF publisher". The last section provides specific rules for the process of retrieving CSAF documents.

## Requirements

The requirements in this subsection are consecutively numbered to be able to refer to them directly.
The order does not give any hint about the importance.
Not all requirements have to be fulfilled to conform to this specification - the sets of
requirements per conformance clause are defined in section [sec](#roles).

### Requirement 1: Valid CSAF document

The document is a valid CSAF document (cf. Conformance clause 1).

### Requirement 2: Filename

The CSAF document has a filename according to the rules in section [sec](#filename).

### Requirement 3: TLS

The CSAF document is per default retrievable from a website which uses TLS for encryption and server authenticity.
The CSAF document MUST NOT be downloadable from a location which does not encrypt the transport when crossing organizational
boundaries to maintain the chain of custody.

### Requirement 4: TLP:WHITE

If the CSAF document is labeled TLP:WHITE, it MUST be freely accessible.

This does not exclude that such a document is also available in an access protected customer portal.
However, there MUST be one copy of the document available for people without access to the portal.

> Reasoning: If an advisory is already in the media, an end user should not be forced to collect the pieces of information from a
> press release but be able to retrieve the CSAF document.

### Requirement 5: TLP:AMBER and TLP:RED

CSAF documents labeled TLP:AMBER or TLP:RED MUST be access protected.
If they are provided via a web server this SHALL be done under a different path than for TLP:WHITE,
TLP:GREEN and unlabeled CSAF documents. TLS client authentication, access tokens or any other automatable authentication method SHALL be used.

An issuing party MAY agree with the recipients to use any kind of secured drop at the recipients' side to avoid putting them on their own website.
However, it MUST be ensured that the documents are still access protected.

### Requirement 6: No Redirects

Redirects SHOULD NOT be used. If they are inevitable only HTTP Header redirects are allowed.

> Reasoning: Clients should not parse the payload for navigation and some, as e.g. `curl`, do not follow any other kind of redirects.

### Requirement 7: provider-metadata.json

The party MUST provide a valid `provider-metadata.json` according to the schema
[CSAF provider metadata](https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json) for its own metadata.
The `publisher` object SHOULD match the one used in the CSAF documents of the issuing party but can be set to whatever value a
CSAF aggregator SHOULD display over any individual `publisher` values in the CSAF documents themselves.

> This information is used to collect the data for CSAF aggregators, listers and end users.
> The CSAF provider metadata schema ensures the consistency of the metadata for a CSAF provider across the ecosystem.
> Other approaches, like extracting the `publisher` object from CSAF documents, are likely to fail if the object differs between CSAF documents.
>
> It is suggested to put the file `provider-metadata.json` adjacent to the ROLIE feed documents (requirement 15)
> or in the main directory adjacent to the year folders (requirement 14), `changes.csv` (requirement 13) and the `index.txt` (requirement 12).
> Suggested locations to store the `provider-metadata.json` are:
>
> * https://www.example.com/.well-known/csaf/provider-metadata.json
> * https://domain.tld/security/data/csaf/provider-metadata.json
> * https://psirt.domain.tld/advisories/csaf/provider-metadata.json
> * https://domain.tld/security/csaf/provider-metadata.json

*Example 1 (minimal with ROLIE document):*

```
  {
    "canonical_url": "https://www.example.com/.well-known/csaf/provider-metadata.json",
    "distributions": [
      {
        "rolie": {
          "feeds": [
            {
              "summary": "All TLP:WHITE advisories of Example Company.",
              "tlp_label": "WHITE",
              "url": "https://www.example.com/.well-known/csaf/feed-tlp-white.json"
            }
          ]
        }
      }
    ],
    "last_updated": "2024-01-24T20:20:56.169Z",
    "list_on_CSAF_aggregators": true,
    "metadata_version": "2.1",
    "mirror_on_CSAF_aggregators": true,
    "public_openpgp_keys": [
      {
        "fingerprint": "8F5F267907B2C4559DB360DB2294BA7D2B2298B1",
        "url": "https://keys.example.net/vks/v1/by-fingerprint/8F5F267907B2C4559DB360DB2294BA7D2B2298B1"
      }
    ],
    "publisher": {
      "category": "vendor",
      "name": "Example Company ProductCERT",
      "namespace": "https://psirt.example.com"
    },
    "role": "csaf_trusted_provider"
  }
```

If a CSAF publisher (cf. section [sec](#role-csaf-publisher)) does not provide the `provider-metadata.json`,
an aggregator SHOULD contact the CSAF publisher in question to determine the values for `list_on_CSAF_aggregators` and `mirror_on_CSAF_aggregators`.
If that is impossible or if the CSAF publisher is unresponsive the following values MUST be used:

```
    "list_on_CSAF_aggregators": true,
    "mirror_on_CSAF_aggregators": false
```

> This prevents that CSAF documents of a CSAF publisher which have been collected by one CSAF aggregator A are mirrored again on a
> second CSAF aggregator B. Such cascades are prone to outdated information.
> If the first aggregator A collects the CSAF documents on best effort and B copies the files from A and announces that this is done weekly,
> one might assume that B's CSAF documents are more recent.
> However, that is not the case as B's information depends on A.

### Requirement 8: security.txt

In the security.txt there MUST be at least one field `CSAF` which points to the `provider-metadata.json` (requirement 7).
If this field indicates a web URI, then it MUST begin with "https://" (as per section 2.7.2 of [cite](#RFC7230)).
See [cite](#SECURITY-TXT) for more details.

> The security.txt was published as [cite](#RFC9116) in April 2022. At the time of this writing,
> the `CSAF` field is in the process of being officially added.

*Examples 1:*

```
CSAF: https://domain.tld/security/data/csaf/provider-metadata.json
CSAF: https://psirt.domain.tld/advisories/csaf/provider-metadata.json
CSAF: https://domain.tld/security/csaf/provider-metadata.json
CSAF: https://www.example.com/.well-known/csaf/provider-metadata.json
```

It is possible to advertise more than one `provider-metadata.json` by adding multiple `CSAF` fields,
e.g. in case of changes to the organizational structure through merges or acquisitions.
However, this SHOULD NOT be done and removed as soon as possible.
If one of the URLs fulfills requirement 9, this MUST be used as the first CSAF entry in the security.txt.

### Requirement 9: Well-known URL for provider-metadata.json

The URL path `/.well-known/csaf/provider-metadata.json` under the main domain of the issuing authority serves directly
the `provider-metadata.json` according to requirement 7.
The use of the scheme "HTTPS" is required. See [cite](#RFC8615) for more details.

*Example 1:*

```
  https://www.example.com/.well-known/csaf/provider-metadata.json
```

### Requirement 10: DNS path

The DNS record `csaf.data.security.domain.tld` SHALL resolve as a web server which serves directly
the `provider-metadata.json` according to requirement 7.
The use of the scheme "HTTPS" is required.

### Requirement 11: One folder per year

The CSAF documents MUST be located within folders named `<YYYY>` where `<YYYY>` is the year given in the
value of `/document/tracking/initial_release_date`.

*Examples 1:*

```
2021
2020
```

### Requirement 12: index.txt

The index.txt file within MUST provide a list of all filenames of CSAF documents which are located in the sub-directories with their filenames.

*Example 1:*

```
2020/example_company_-_2020-yh4711.json
2019/example_company_-_2019-yh3234.json
2018/example_company_-_2018-yh2312.json
```

> This can be used to download all CSAF documents.

### Requirement 13: changes.csv

The file changes.csv MUST contain the filename as well as the value of `/document/tracking/current_release_date` for each
CSAF document in the sub-directories without a heading; lines MUST be sorted by the `current_release_date` timestamp with the latest one first.

*Example 1:*

```
"2020/example_company_-_2020-yh4711.json","2020-07-01T10:09:07Z"
"2018/example_company_-_2018-yh2312.json","2020-07-01T10:09:01Z"
"2019/example_company_-_2019-yh3234.json","2019-04-17T15:08:41Z"
"2018/example_company_-_2018-yh2312.json","2019-03-01T06:01:00Z"
```

### Requirement 14: Directory listings

Directory listing SHALL be enabled to support manual navigation.

### Requirement 15: ROLIE feed

Resource-Oriented Lightweight Information Exchange (ROLIE) is a standard to ease discovery of security content.
ROLIE is built on top of the Atom Publishing Format and Protocol, with specific requirements that support publishing security content.
All CSAF documents with the same TLP level MUST be listed in a single ROLIE feed.
At least one of the feeds

* TLP:WHITE
* TLP:GREEN
* unlabeled

MUST exist.
Each ROLIE feed document MUST be a JSON file that conforms with [cite](#RFC8322).

*Example 1:*

```
  {
    "feed": {
      "id": "example-csaf-feed-tlp-white",
      "title": "Example CSAF feed (TLP:WHITE)",
      "link": [
        {
          "rel": "self",
          "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-white.json"
        }
      ],
      "category": [
        {
          "scheme": "urn:ietf:params:rolie:category:information-type",
          "term": "csaf"
        }
      ],
      "updated": "2024-01-01T12:00:00.000Z",
      "entry": [
        {
          "id": "ESA-2024-001",
          "title": "Multiple vulnerabilities in ABC 0.0.2",
          "link": [
            {
              "rel": "self",
              "href": "https://psirt.domain.tld/advisories/csaf/2024/esa-2024-001.json"
            },
            {
              "rel": "hash",
              "href": "https://psirt.domain.tld/advisories/csaf/2024/esa-2024-001.json.sha512"
            },
            {
              "rel": "signature",
              "href": "https://psirt.domain.tld/advisories/csaf/2024/esa-2024-001.json.asc"
            }
          ],
          "published": "2024-01-01T11:00:00.000Z",
          "updated": "2024-01-01T12:00:00.000Z",
          "summary": {
            "content": "Multiple vulnerabilities were fixed in ABC 0.0.3"
          },
          "content": {
            "type": "application/json",
            "src": "https://psirt.domain.tld/advisories/csaf/2024/esa-2024-001.json"
          },
          "format": {
            "schema": "https://docs.oasis-open.org/csaf/csaf/v2.1/csaf_json_schema.json",
            "version": "2.1"
          }
        }
      ]
    }
  }
```

Any existing hash file (requirement 18) MUST be listed in the corresponding entry of the ROLIE feed as an item of
the array `link` having the `rel` value of `hash`.
Any existing signature file (requirement 19) MUST be listed in the corresponding entry of the ROLIE feed as an item of the array `link`
having the `rel` value of `signature`.

### Requirement 16: ROLIE service document

The use and therefore the existence of ROLIE service document is optional.
If it is used, each ROLIE service document MUST be a JSON file that conforms with [cite](#RFC8322) and lists the ROLIE feed documents.

*Example 1:*

```
  {
    "service": {
      "workspace": [
        {
          "title": "Public CSAF feed",
          "collection": [
            {
              "title": "Example CSAF feed (TLP:WHITE)",
              "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-white.json",
              "categories": {
                "category": [
                  {
                    "scheme": "urn:ietf:params:rolie:category:information-type",
                    "term": "csaf"
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  }
```

### Requirement 17: ROLIE category document

The use and therefore the existence of ROLIE category document is optional.
If it is used, each ROLIE category document MUST be a JSON file that conforms with [cite](#RFC8322).
ROLIE categories SHOULD be used for to further dissect CSAF documents by one or more of the following criteria:

* document category
* document language
* values of the branch category within the Product Tree including but not limited to
  * `vendor`
  * `product_family`
  * `product_name`
  * `product_version`
* type of product

  *Examples 1:*

  ```
    CPU
    Firewall
    Monitor
    PLC
    Printer
    Router
    Sensor
    Server
  ```

* areas or sectors, the products are used in

  *Examples 2:*

  ```
    Chemical
    Commercial
    Communication
    Critical Manufacturing
    Dams
    Energy
    Healthcare
    Water
  ```

* any other categorization useful to the consumers

*Example 3:*

```
  {
    "categories": {
      "category": [
        {
            "term": "Example Company Product A"
        },
        {
            "term": "Example Company Product B"
        }
      ]
    }
  }
```

### Requirement 18: Integrity

All CSAF documents SHALL have at least one hash file computed with a secure cryptographic hash algorithm (e.g. SHA-512 or SHA-3)
to ensure their integrity. The filename is constructed by appending the file extension which is given by the algorithm.

MD5 and SHA1 SHOULD NOT be used.

*Example 1:*

```
File name of CSAF document: example_company_-_2019-yh3234.json
File name of SHA-256 hash file: example_company_-_2019-yh3234.json.sha256
File name of SHA-512 hash file: example_company_-_2019-yh3234.json.sha512
```

The file content SHALL start with the first byte of the hexadecimal hash value.
Any subsequent data (like a filename) which is optional SHALL be separated by at least one space.

*Example 2:*

```
ea6a209dba30a958a78d82309d6cdcc6929fcb81673b3dc4d6b16fac18b6ff38  example_company_-_2019-yh3234.json
```

If a ROLIE feed exists, each hash file MUST be listed in it as described in requirement 15.

### Requirement 19: Signatures

All CSAF documents SHALL have at least one OpenPGP signature file which is provided under the same filename which is
extended by the appropriate extension. See [cite](#RFC4880) for more details.

*Example 1:*

```
File name of CSAF document: example_company_-_2019-yh3234.json
File name of signature file: example_company_-_2019-yh3234.json.asc
```

If a ROLIE feed exists, each signature file MUST be listed in it as described in requirement 15.

### Requirement 20: Public OpenPGP Key

The public part of the OpenPGP key used to sign the CSAF documents MUST be available.
It SHOULD also be available at a public key server.

> For example, the public part of the OpenPGP key could be placed in a directory `openpgp` adjacent to the `provider-metadata.json`.

The OpenPGP key SHOULD have a strength that is considered secure.

> Guidance on OpenPGP key strength can be retrieved from technical guidelines of competent authorities.

### Requirement 21: List of CSAF providers

The file `aggregator.json` MUST be present and valid according to the
JSON schema [CSAF aggregator](https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json).
It MUST NOT be stored adjacent to a `provider-metadata.json`.

> Suggested locations to store the `aggregator.json` are:
>
> * https://www.example.com/.well-known/csaf-aggregator/aggregator.json
> * https://domain.tld/security/data/aggregator/csaf/aggregator.json
> * https://psirt.domain.tld/advisories/aggregator/csaf/aggregator.json
> * https://domain.tld/security/aggregator/csaf/aggregator.json

The file `aggregator.json` SHOULD only list the latest version of the metadata of a CSAF provider.

*Example 1:*

```
  {
    "aggregator": {
      "category": "lister",
      "contact_details": "Example CSAF Lister can be reached at contact_us@lister.example, or via our website at https://lister.example/security/csaf/aggregator/contact.",
      "issuing_authority": "This service is provided as it is. It is free for everybody.",
      "name": "Example CSAF Lister",
      "namespace": "https://lister.example"
    },
    "aggregator_version": "2.1",
    "canonical_url": "https://aggregator.example/.well-known/csaf-aggregator/aggregator.json",
    "csaf_providers": [
      {
        "metadata": {
          "last_updated": "2024-01-12T20:20:56.169Z",
          "publisher": {
            "category": "vendor",
            "name": "Example Company ProductCERT",
            "namespace": "https://psirt.example.com"
          },
          "url": "https://www.example.com/.well-known/csaf/provider-metadata.json"
        }
      },
      {
        "metadata": {
          "last_updated": "2024-01-12T21:35:38.000Z",
          "publisher": {
            "category": "coordinator",
            "name": "Example Coordinator CERT",
            "namespace": "https://cert.example"
          },
          "url": "https://cert.example/advisories/csaf/provider-metadata.json"
        }
      }
    ],
    "last_updated": "2024-01-24T22:35:38.978Z"
  }
```

### Requirement 22: Two disjoint issuing parties

The file `aggregator.json` (requirement 21) lists at least two disjoint CSAF providers (including CSAF trusted providers)
or one CSAF publisher and one CSAF provider (including CSAF trusted provider).

### Requirement 23: Mirror

The CSAF documents for each issuing party that is mirrored MUST be in a different folder.
The folder name SHOULD be retrieved from the name of the issuing authority.
This folders MUST be adjacent to the `aggregator.json` (requirement 21).
Each such folder MUST at least:

* provide a `provider-metadata.json` for the current issuing party.
* provide the ROLIE feed document according to requirement 15 which links to the local copy of the CSAF document.

*Example 1:*

```
  {
    "aggregator": {
      "category": "aggregator",
      "contact_details": "Example Aggregator can be reached at contact_us@aggregator.example, or via our website at https://aggregator.example/security/csaf/aggregator/contact.",
      "issuing_authority": "This service is provided as it is. It is free for everybody.",
      "name": "Example Aggregator",
      "namespace": "https://aggregator.example"
    },
    "aggregator_version": "2.1",
    "canonical_url": "https://aggregator.example/.well-known/csaf-aggregator/aggregator.json",
    "csaf_providers": [
      {
        "metadata": {
          "last_updated": "2024-01-12T20:20:56.169Z",
          "publisher": {
            "category": "vendor",
            "name": "Example Company ProductCERT",
            "namespace": "https://psirt.example.com"
          },
          "url": "https://www.example.com/.well-known/csaf/provider-metadata.json"
        },
        "mirrors": [
          "https://aggregator.example/.well-known/csaf-aggregator/Example_Company_ProductCERT/provider-metadata.json"
        ]
      },
      {
        "metadata": {
          "last_updated": "2024-01-12T21:35:38.000Z",
          "publisher": {
            "category": "coordinator",
            "name": "Example Coordinator CERT",
            "namespace": "https://cert.example"
          },
          "url": "https://cert.example/advisories/csaf/provider-metadata.json"
        },
        "mirrors": [
          "https://aggregator.example/.well-known/csaf-aggregator/Example_Coordinator_CERT/provider-metadata.json"
        ]
      }
    ],
    "last_updated": "2024-01-24T22:35:38.978Z"
  }
```

## Roles

This subsection groups the requirements from the previous subsection into named sets which target the roles with the same name.
This allows end users to request their suppliers to fulfill a certain set of requirements.
A supplier can use roles for advertising and marketing.

The roles "CSAF publisher", "CSAF provider", and "CSAF trusted provider" are intended directly for issuing parties and form the first group.
The second group consists of the roles "CSAF lister" and "CSAF aggregator".
They collect data from the aforementioned issuing parties of the first group and provide them in a single place to aid in automation.
Parties of the second group can also issue their own advisories.
However, they MUST follow the rules for the first group for that.

Both, a CSAF lister and a CSAF aggregator, decide based on their own rules which issuing parties to list respectively to mirror.
However, an issuing party MAY apply to be listed or mirrored.

Issuing parties MUST indicate through the value `false` in `list_on_CSAF_aggregators` if they do not want to be listed.
Issuing parties MUST indicate through the value `false` in `mirror_on_CSAF_aggregators` if they do not want to be mirrored.

The values are independent.
The combination of the value `false` in `list_on_CSAF_aggregators` and `true` in `mirror_on_CSAF_aggregators` implies that
the issuing party does not want to be listed without having the CSAF documents mirrored.
Therefore, a CSAF aggregator can list that issuing party if it mirrors the files.

### Role: CSAF publisher

A distributing party satisfies the "CSAF publisher" role if the party:

* satisfies the requirements 1 to 4 in section [sec](#requirements).
* distributes only CSAF documents on behalf of its own.

### Role: CSAF provider

A CSAF publisher satisfies the "CSAF provider" role if the party fulfills the following three groups of requirements:

Firstly, the party:

* satisfies the "CSAF publisher" role profile.
* additionally satisfies the requirements 5 to 7 in section [sec](#requirements).

Secondly, the party:

* satisfies at least one of the requirements 8 to 10 in section [sec](#requirements).

Thirdly, the party:

* satisfies the requirements 11 to 14 in section [sec](#requirements) or requirements 15 to 17 in section [sec](#requirements).

> If the party uses the ROLIE-based distribution, it MUST also satisfy requirements 15 to 17.
> If it uses the directory-based distribution, it MUST also satisfy requirements 11 to 14.

### Role: CSAF trusted provider

A CSAF provider satisfies the "CSAF trusted provider" role if the party:

* satisfies the "CSAF provider" role profile.
* additionally satisfies the requirements 18 to 20 in section [sec](#requirements).

### Role: CSAF lister

A distributing party satisfies the "CSAF lister" role if the party:

* satisfies the requirements 6, 21 and 22 in section [sec](#requirements).
* uses the value `lister` for `/aggregator/category`.
* does not list any mirror pointing to a domain under its own control.

> The purpose of this role is to provide a list of URLs where to find CSAF documents.
> It is not assumed that the list will be complete.

### Role: CSAF aggregator

A distributing party satisfies the "CSAF aggregator" role if the party:

* satisfies the requirements 1 to 6 and 21 to 23 in section [sec](#requirements).
* uses the value `aggregator` for `/aggregator/category`.
* lists a mirror for at least two disjoint issuing parties pointing to a domain under its own control.
* links the public part of the OpenPGP key used to sign CSAF documents for each mirrored issuing party in
  the corresponding `provider-metadata.json`.
* provides for each CSAF document that is mirrored a signature (requirement 19) and a hash (requirement 18).
  Both SHALL be listed in the ROLIE feed. If the issuing party provides those files for a CSAF document, they SHOULD be copied as well.
  If the issuing party does not provide those files, they SHALL be created by the CSAF aggregator.
  Such a signature does not imply any liability of CSAF aggregator for the content of the corresponding CSAF document.
  It just confirms that the CSAF document provided has not been modified after being downloaded from the issuing party.
  A CSAF aggregator MAY add additional signatures and hashes for a CSAF document.

Additionally, a CSAF aggregator MAY list one or more issuing parties that it does not mirror.

> The purpose of this role is to provide a single point where CSAF documents can be retrieved.
> Multiple CSAF aggregators are expected to exist around the world. None of them is required to mirror all CSAF documents of all issuing parties.
> CSAF aggregators can be provided for free or as a paid service.
>
> To aid in automation, CSAF aggregators MAY mirror CSAF documents from CSAF publishers.
> Regarding the terms of use they SHOULD consult with the issuing party.
> The purpose of this option is that a consumer can retrieve CSAF documents from a CSAF publisher as if this issuing party would be a
> CSAF trusted provider. To reach that goal, a CSAF aggregator collects the CSAF documents from the CSAF publisher and mirrors it.
> The collection process MAY be automated or manual. CSAF aggregators announce the collection interval through the field `update_interval` in
> the corresponding item of the CSAF publishers list (`csaf_publishers`) in their `aggregator.json`.
> To minimize the implementation efforts and process overhead, a CSAF aggregator MAY upload the CSAF documents of a CSAF publisher into
> an internal instance of a CSAF provider software.
> Such construct is called "CSAF proxy provider" as it can be mirrored by the CSAF aggregator software.
> However, such a CSAF proxy provider MUST NOT be accessible from anyone else than the CSAF aggregator itself.
> Otherwise, that would violate the second rule of section [sec](#role-csaf-publisher).
> Therefore, it is recommended to expose the CSAF proxy provider only on localhost and allow the access only from the CSAF aggregator software.

## Retrieving rules

The retrieving process executes in two phases: Finding the `provider-metadata.json` (requirement 7 in section [sec](#requirements)) and
retrieving CSAF documents.

> A retrieving party SHOULD do the first phase every time.
> Based on the setup and use case of the retrieving party it MAY choose to do it less often,
> e.g. only when adding new or updating distributing parties.
> In that case, it SHOULD to check regularly whether new information is available.

### Finding provider-metadata.json

**Direct locating**: The following process SHOULD be used to determine the location of a `provider-metadata.json`
(requirement 7 in section [sec](#requirements)) based on the main domain of the issuing party:

1. Checking the Well-known URL (requirement 9 in section [sec](#requirements))
2. Checking the security.txt (requirement 8 in section [sec](#requirements))
3. Checking the DNS path (requirement 10 in section [sec](#requirements))
4. Select one or more `provider-metadata.json` to use.

> The term "checking" used in the listing above SHOULD be understood as follows:
> Try to access the resource and test whether the response provides an expected result as defined in the requirement in section 7.1.
> If that is the case, the step was successful - otherwise not.

The first two steps SHOULD be performed in all cases as the security.txt MAY advertise additional `provider-metadata.json`.
The third step SHOULD only be performed if the first two did not result in the location of at least one `provider-metadata.json`.

**Indirect locating**: A retrieving party MAY choose to determine the location of a `provider-metadata.json` by retrieving
its location from an `aggregator.json` (requirement 21 in section [sec](#requirements)) of a CSAF lister or CSAF aggregator.

### Retrieving CSAF documents

Given a `provider-metadata.json`, the following process SHOULD be used to retrieve CSAF documents:

1. Parse the `provider-metadata.json` to determine whether the directory-based (requirements 11 to 14 in section [sec](#requirements))
   or ROLIE-based distribution (requirements 15 to 17 in section [sec](#requirements)) is used.
   If both are present, the ROLIE information SHOULD be preferred.
2. For any CSAF trusted provider, the hash and signature files (requirements 18 to 19 in section [sec](#requirements)) SHOULD be retrieved together
   with the CSAF document.
   They MUST be checked before further processing the CSAF document.
3. Test the CSAF document against the schema.
4. Execute mandatory tests on the CSAF document.

-------
