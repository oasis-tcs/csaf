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

### Requirement 4: TLP:CLEAR

If the CSAF document is labeled TLP:CLEAR, it MUST be freely accessible.

This does not exclude that such a document is also available in an access protected customer portal.
However, there MUST be one copy of the document available for people without access to the portal.

> Reasoning: If an advisory is already in the media, an end user should not be forced to collect the pieces of information from a
> press release but be able to retrieve the CSAF document.

### Requirement 5: TLP:AMBER, TLP:AMBER+STRICT and TLP:RED

CSAF documents labeled TLP:AMBER, TLP:AMBER+STRICT or TLP:RED MUST be access protected.
If they are provided via a web server this SHALL be done under a different path than for TLP:CLEAR,
TLP:GREEN and unlabeled CSAF documents. TLS client authentication, access tokens or any other automatable authentication method SHALL be used.

An issuing party MAY agree with the recipients to use any kind of secured drop at the recipients' side to avoid putting them on their own website.
However, it MUST be ensured that the documents are still access protected.

### Requirement 6: No Redirects

Redirects SHOULD NOT be used. If they are inevitable only HTTP Header redirects are allowed.

> Reasoning: Clients should not parse the payload for navigation and some, as e.g. `curl`, do not follow any other kind of redirects.

If any redirects are used, there SHOULD not be more than 5 and MUST NOT be more than 10 consecutive redirects.

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
              "last_updated": "2024-01-24T20:20:56.169Z",
              "summary": "All TLP:CLEAR advisories of Example Company.",
              "tlp_label": "CLEAR",
              "url": "https://www.example.com/.well-known/csaf/feed-tlp-clear.json"
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

> The security.txt was published as [cite](#RFC9116) in April 2022.
> The `CSAF` field was officially added through the IANA registry.

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
the `provider-metadata.json` according to requirement 7. That implies that redirects SHALL NOT be used.
The use of the scheme "HTTPS" is required. See [cite](#RFC8615) for more details.

*Example 1:*

```
  https://www.example.com/.well-known/csaf/provider-metadata.json
```

### Requirement 10: DNS path

Assuming that the organization's main domain is `domain.tld`, the DNS record `csaf.data.security.domain.tld` SHALL resolve
to the IP address of a web server which serves directly the `provider-metadata.json` according to requirement 7.

> The `domain.tld` is just a placeholder for the organization's main domain.
> For the organization with the main domain being `example.com`, the necessary DNS record is `csaf.data.security.example.com`.

That implies that redirects SHALL NOT be used.
The use of the scheme "HTTPS" is required.

### Requirement 11: One folder per year

The CSAF documents MUST be located within folders named `<YYYY>` where `<YYYY>` is the year given in the
value of `/document/tracking/initial_release_date`.

*Examples 1:*

```
2024
2023
```

### Requirement 12: index.txt

The file index.txt MUST contain the list of all filenames of CSAF documents which are located in the sub-directories with their filenames.
Each entry SHALL be terminated by a newline sequence.
The last entry MAY skip the newline sequence.

> If different TLP labels are used, multiple index.txt exist.
> However, they are located in the corresponding folders and contain only the filenames of files for that TLP label.

*Example 1:*

```
2023/esa-2023-09953.json
2022/esa-2022-02723.json
2021/esa-2021-31916.json
2021/esa-2021-03676.json
```

> This can be used to download all CSAF documents.

### Requirement 13: changes.csv

The file `changes.csv` contains a list of CSAF documents in the current TLP level that were changed recently.
Therefore, it MUST contain the filename as well as the value of `/document/tracking/current_release_date` for each
CSAF document in the sub-directories without a heading; lines MUST be sorted by the `current_release_date` timestamp with the latest one first.
The `changes.csv` SHALL be a valid comma separated values format as defined by [cite](#RFC4180) without double quotes.

> Note: As a consequence of section [sec](#requirement-2-filename) Requirement 2 for filenames and section [sec](#requirement-11-one-folder-per-year)
> Requirement for directory names, there must not be any characters within the `changes.csv` that would require quoting.

*Example 1:*

```
2023/esa-2023-09953.json,2023-07-01T10:09:07Z
2021/esa-2021-03676.json,2023-07-01T10:09:01Z
2022/esa-2022-02723.json,2022-04-17T15:08:41Z
2021/esa-2021-31916.json,2022-03-01T06:01:00Z
```

> Note: As CSAF 2.0 requires quotes, an [cite](#RFC4180) parser can read both format revisions.

### Requirement 14: Directory listings

Server-side generated directory listing SHALL be enabled to support manual navigation.

> As the content of the directory listing is more or less static, there is little to no benefit in using of client-side scripts.
> Moreover, client-side scripts, like JavaScript, are usually not evaluated in text-based browsers and are also hard to check programmatically.

### Requirement 15: ROLIE feed

Resource-Oriented Lightweight Information Exchange (ROLIE) is a standard to ease discovery of security content.
ROLIE is built on top of the Atom Publishing Format and Protocol, with specific requirements that support publishing security content.
All CSAF documents with the same TLP level MUST be listed in a single ROLIE feed.
At least one of the feeds

* TLP:CLEAR
* TLP:GREEN
* unlabeled

MUST exist.
Each ROLIE feed document MUST be a JSON file that conforms with [cite](#RFC8322).

*Example 1:*

```
  {
    "feed": {
      "id": "example-csaf-feed-tlp-clear",
      "title": "Example CSAF feed (TLP:CLEAR)",
      "link": [
        {
          "rel": "self",
          "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-clear.json"
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
Additionally, it can also list the corresponding ROLIE category documents.
The ROLIE service document SHOULD use the filename `service.json` and reside next to the `provider-metadata.json`.

*Example 1:*

```
  {
    "service": {
      "workspace": [
        {
          "title": "Public CSAF feed",
          "collection": [
            {
              "title": "Example CSAF feed (TLP:CLEAR)",
              "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-clear.json",
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
A ROLIE category document SHOULD reside next to the corresponding ROLIE feed.
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
File name of CSAF document: esa-2022-02723.json
File name of SHA-256 hash file: esa-2022-02723.json.sha256
File name of SHA-512 hash file: esa-2022-02723.json.sha512
```

The file content SHALL start with the first byte of the hexadecimal hash value.
Any subsequent data (like a filename) which is optional SHALL be separated by at least one space.

*Example 2:*

```
ea6a209dba30a958a78d82309d6cdcc6929fcb81673b3dc4d6b16fac18b6ff38  esa-2022-02723.json
```

If a ROLIE feed exists, each hash file MUST be listed in it as described in requirement 15.

### Requirement 19: Signatures

All CSAF documents SHALL have at least one OpenPGP signature file which is provided under the same filename which is
extended by the appropriate extension.
This signature SHALL be presented as an ASCII armored file.
See [cite](#RFC4880) for more details.

*Example 1:*

```
File name of CSAF document: esa-2022-02723.json
File name of signature file: esa-2022-02723.json.asc
```

If a ROLIE feed exists, each signature file MUST be listed in it as described in requirement 15.

At all times, signatures MUST remain valid for a minimum of 30 days and ideally for at least 90 days. When executing
CSAF document signatures, the signing party SHOULD adhere to or surpass the prevailing best practices and recommendations
regarding key length.
Tools SHOULD treat the violation of the rules given in the first sentence as:

* warning if the signature is only valid for 90 days or less at the time of the verification,
* error, which MAY be ignored by the user per option, if the signature is only valid for 30 days or less at the time of
  the verification and
* error if the signature is expired at the time of the verification.

### Requirement 20: Public OpenPGP Key

The public part of the OpenPGP key used to sign the CSAF documents MUST be available.
This key file SHALL be presented as an ASCII armored file.
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
          "role": "csaf_provider",
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
          "role": "csaf_trusted_provider",
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

### Requirement 24: HTTP User-Agent

Access to the CSAF related files and directories provided, for both metadata and documents, MUST be allowed independent of the
value of HTTP User-Agent.

> Limit the value of HTTP User-Agents to a certain set would hinder adoption of tools retrieving the files.

The only exception is that the temporary blocking of certain HTTP User-Agents is allowed to mitigate an ongoing security incident
(e.g. a DoS attack on the web server serving the CSAF files).
However, a less severe measure with a similar effect SHOULD be used.
CSAF related files and directories SHOULD be exempted from temporary blocking.
The temporary blocking SHOULD be removed as soon as possible, at latest two weeks after the security incident process was completed.

> Also confer to the TC's guidance on content delivery networks and caching.

### Requirement 25: Access-Control-Allow-Origin

For any CSAF documents and related metadata, the web server SHOULD set the HTTP header `Access-Control-Allow-Origin: *`.

> The HTTP header enables users to access the CSAF data with web browser based clients.

The value of the HTTP header MAY be altered to allow just specified domains.
In such case, the response SHOULD follow the recommendations of [cite](#FETCH) including but not limited to those about the `Vary` header.

> Such restriction may allow the allow-listed domains to send credentials.
