## 3.1 Definitions

The definitions (`$defs`) introduce the following domain specific types into the CSAF language:
Acknowledgments (`acknowledgments_t`), Branches (`branches_t`), Full Product Name (`full_product_name_t`), Language (`lang_t`), Notes (`notes_t`),
Product Group ID (`product_group_id_t`), Product Groups (`product_groups_t`), Product ID (`product_id_t`), Products (`products_t`), References (`references_t`),
and Version (`version_t`).

```
    "$defs": {
        "acknowledgments_t": {
            // ...
        },
        "branches_t": {
            // ...
        },
        "full_product_name_t": {
            // ...
        },
        "lang_t": {
            // ...
        },
        "notes_t": {
            // ...
        },
        "product_group_id_t": {
            // ...
        },
        "product_groups_t": {
             // ...
        },
        "product_id_t": {
            // ...
        },
        "products_t": {
            // ...
        },
        "references_t": {
            // ...
        },
        "version_t": {
            // ...
        }
    },
```

### 3.1.1 Acknowledgments Type

List of Acknowledgments (`acknowledgments_t`) type instances of value type `array` with 1 or more elements contain a list of `Acknowledgment` elements.

```
    "acknowledgments_t": {
      // ...
      "items": {
        // ...
      }
    },
```

The value type of Acknowledgment is `object` with at least 1 and at most 4 properties. Every such element acknowledges contributions by describing those that contributed.
The properties are: `names`, `organization`, `summary`, and `urls`.

```
        "properties": {
          "names": {
            // ...
          },
          "organization": {
            // ...
          },
          "summary": {
            // ...
          },
          "urls": {
            // ...
          }
        }
```

#### 3.1.1.1 Acknowledgments Type - Names

List of acknowledged names (`names`) has value type `array` with 1 or more items holds the names of contributors being recognized.
Every such item of value type `string` with 1 or more characters represents the name of the contributor and contains the name of a single contributor being recognized.

*Examples 1:*

```
    Albert Einstein
    Johann Sebastian Bach
```

#### 3.1.1.2 Acknowledgments Type - Organization

The contributing organization (`organization`) has value type `string` with 1 or more characters and holds the name of the contributing organization being recognized.

*Examples 2:*

```
    CISA
    Google Project Zero
    Talos
```

#### 3.1.1.3 Acknowledgments Type - Summary

Summary of the acknowledgment (`summary`) of value type `string` with 1 or more characters SHOULD represent any contextual details the document producers wish to make known about the acknowledgment or acknowledged parties.

*Example 3:*

```
    First analysis of Coordinated Multi-Stream Attack (CMSA)
```

#### 3.1.1.4 Acknowledgments Type - URLs

List of URLs (`urls`) of acknowledgment is a container (value type `array`) for 1 or more `string` of type URL that specifies a list of URLs or location of the reference to be acknowledged.
Any URL of acknowledgment contains the URL or location of the reference to be acknowledged.
Value type is string with format URI (`uri`).

#### 3.1.1.5 Acknowledgments Type - Example

*Example 4:*

```
  "acknowledgments": [
    {
      "names": [
        "Johann Sebastian Bach",
        "Georg Philipp Telemann",
        "Georg Friedrich Händel"
      ],
      "organization": "Baroque composers",
      "summary": "wonderful music"
    },
    {
      "organization": "CISA",
      "summary": "coordination efforts",
      "urls": [
        "https://cisa.gov"
      ]
    },
    {
      "organization": "BSI",
      "summary": "assistance in coordination"
    },
    {
      "names": [
        "Antonio Vivaldi"
      ],
      "summary": "influencing other composers"
    }
  ],
```

The example 4 above SHOULD lead to the following outcome in a human-readable advisory:

> We thank the following parties for their efforts:
>
> * Johann Sebastian Bach, Georg Philipp Telemann, Georg Friedrich Händel from Baroque composers for wonderful music
> * CISA for coordination efforts (see: https://cisa.gov)
> * BSI for assistance in coordination
> * Antonio Vivaldi for influencing other composers

### 3.1.2 Branches Type

List of branches (`branches_t`) with value type `array` contains 1 or more branch elements as children of the current element.

```
    "branches_t": {
      //...
      "items": {
        // ...
      }
    },
```

Every Branch holds exactly 3 properties and is a part of the hierarchical structure of the product tree.
The properties `name` and `category` are mandatory. In addition, the object contains either a `branches` or a `product` property.

```
        "properties": {
          "branches": {
            // ...
          },
          "category": {
            // ...
          },
          "name": {
            // ...
          },
          "product": {
            // ...
          }
        }
```

> `branches_t` supports building a hierarchical structure of products that allows to indicate the relationship of products to each other and enables grouping for simpler referencing. As an example, the structure MAY use the following levels: `vendor` -> `product_family` -> `product_name` -> `product_version`.
> It is recommended to use the hierarchical structure of `vendor` -> `product_name` -> `product_version` whenever possible to support the identification and matching of products on the consumer side.

#### 3.1.2.1 Branches Type - Branches

List of branches (`branches`) has the value type `branches_t`.

#### 3.1.2.2 Branches Type - Category

Category of the branch (`category`) of value type `string` and `enum` describes the characteristics of the labeled branch.
Valid `enum` values are:

```
    architecture
    host_name
    language
    legacy
    patch_level
    product_family
    product_name
    product_version
    product_version_range
    service_pack
    specification
    vendor
```

The value `architecture` indicates the architecture for which the product is intended.

The value `host_name` indicates the host name of a system/service.

The value `language` indicates the language of the product.

The value `legacy` indicates an entry that has reached its end of life.

The value `patch_level` indicates the patch level of the product.

The value `product_family` indicates the product family that the product falls into.

The value `product_name` indicates the name of the product.

The value `product_version` indicates exactly a single version of the product. The value of the adjacent `name` property can be numeric or some other descriptor. However, it MUST NOT contain version ranges of any kind.

> It is recommended to enumerate versions wherever possible. Nevertheless, the TC understands that this is sometimes impossible. To reflect that in the specification and aid in automatic processing of CSAF documents the value `product_version_range` was introduced. See next section for details.

The value `product_version_range` indicates a range of versions for the product. The value of the adjacent `name` property SHOULD NOT be used to convey a single version.

The value `service_pack` indicates the service pack of the product.

The value `specification` indicates the specification such as a standard, best common practice, etc.

The value `vendor` indicates the name of the vendor or manufacturer that makes the product.

#### 3.1.2.3 Branches Type - Name

Name of the branch (`name`) of value type `string` with 1 or more characters contains the canonical descriptor or 'friendly name' of the branch.

*Examples 5:*

```
    10
    365
    Microsoft
    Office
    PCS 7
    SIMATIC
    Siemens
    Windows
```

A leading `v` or `V` in the value of `name` SHOULD only exist for the categories `product_version` or `product_version_range` if it is part of the product version as given by the vendor.

##### 3.1.2.3.1 Branches Type - Name under Product Version

If adjacent property `category` has the value `product_version`, the value of `name` MUST NOT contain version ranges of any kind.

*Examples 6 for `name` when using `product_version`:*

```
    10
    17.4
    v3
```

> The `product_version` is the easiest way for users to determine whether their version is meant (provided that the given ancestors in the product tree matched): If both version strings are the same, it is a match - otherwise not. Therefore, it is always recommended to enumerate product versions instead of providing version ranges.

*Examples 7 for `name` when using `product_version` which are invalid:*

```
    8.0.0 - 8.0.1
    8.1.5 and later
    <= 2
    prior to 4.2
    All versions < V3.0.29
    V3.0, V4.0, V4.1, V4.2
```

> All the examples above contain some kind of a version range and are therefore invalid under the category `product_version`.

##### 3.1.2.3.2 Branches Type - Name under Product Version Range

If adjacent property `category` has the value `product_version_range`, the value of `name` MUST contain version ranges. The value of MUST obey to exactly one of the following options:

1. Version Range Specifier (vers)

    > vers is an ongoing community effort to address the problem of version ranges. Its draft specification is available at [VERS].

    vers MUST be used in its canonical form. To convey the term "all versions" the special string `vers:all/*` MUST be used.

    *Examples 8 for `name` when using `product_version_range` with vers:*

    ```
        vers:gem/>=2.2.0|!= 2.2.1|<2.3.0
        vers:npm/1.2.3|>=2.0.0|<5.0.0
        vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1
        vers:tomee/>=8.0.0-M1|<=8.0.1
    ```

    > Through the definitions of the vers specification a user can compute whether a given version is in a given range.

2. Vers-like Specifier (vls)

    This option uses only the `<version-constraint>` part from the vers specification. It MUST NOT have an URI nor the `<versioning-scheme>` part. It is a fallback option and SHOULD NOT be used unless really necessary.
    > The reason for that is, that it is nearly impossible for tools to reliable determine whether a given version is in the range or not.

    Tools MAY support this on best effort basis.

    *Examples 9 for `name` when using `product_version_range` with vls:*

    ```
        <=2
        <4.2
        <V3.0.29
        >=8.1.5
    ```

#### 3.1.2.4 Branches Type - Product

Product (`product`) has the value type Full Product Name (`full_product_name_t`).

### 3.1.3 Full Product Name Type

Full Product Name (`full_product_name_t`) with value type `object` specifies information about the product and assigns the product ID.
The properties `name` and `product_id` are required. The property `product_identification_helper` is optional.

```
    "full_product_name_t": {
      // ...
      "properties": {
        "name": {
          // ...
        },
        "product_id": {
          // ...
        },
        "product_identification_helper": {
          // ...
        }
      }
    },
```

#### 3.1.3.1 Full Product Name Type - Name

Textual description of the product (`name`) has value type `string` with 1 or more characters.
The value SHOULD be the product's full canonical name, including version number and other attributes, as it would be used in a human-friendly document.

*Examples 10:*

```
    Cisco AnyConnect Secure Mobility Client 2.3.185
    Microsoft Host Integration Server 2006 Service Pack 1
```

#### 3.1.3.2 Full Product Name Type - Product ID

Product ID (`product_id`) holds a value of type Product ID (`product_id_t`).

#### 3.1.3.3 Full Product Name Type - Product Identification Helper

Helper to identify the product (`product_identification_helper`) of value type `object` provides in its properties at least one method which aids in identifying the product in an asset database.
Of the given eight properties `cpe`, `hashes`, `model_numbers`, `purl`, `sbom_urls`, `serial_numbers`, `skus`, and `x_generic_uris`, one is mandatory.

```
    "product_identification_helper": {
      // ...
      "properties": { 
        "cpe": {
          // ...
        },
        "hashes": {
          // ...
        },
        "model_numbers": {
          // ...
        },
        "purl": {
          // ...
        },
        "sbom_urls": {
          // ...
        },
        "serial_numbers": {
          // ...
        },
        "skus": {
          // ...
        },
        "x_generic_uris": {
          // ...
        }
      }
```

##### 3.1.3.3.1 Full Product Name Type - Product Identification Helper - CPE

Common Platform Enumeration representation (`cpe`) of value type `string` of 5 or more characters with `pattern` (regular expression):

```
    ^(cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6})$
```

The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external to this specification. See [CPE23-N] for details.

##### 3.1.3.3.2 Full Product Name Type - Product Identification Helper - Hashes

List of hashes (`hashes`) of value type `array` holding at least one item contains a list of cryptographic hashes usable to identify files.

```
    "hashes": {
      // ...
      "items": {
        // ...
      }
    },
```

Cryptographic hashes of value type `object` contains all information to identify a file based on its cryptographic hash values.
Any cryptographic hashes object has the 2 mandatory properties `file_hashes` and `filename`.

```
        "properties": {
          "file_hashes": {
            // ...
          },
          "filename": {
            // ...
          }
        }
```

List of file hashes (`file_hashes`) of value type `array` holding at least one item contains a list of cryptographic hashes for this file.

```
    "file_hashes": {
      // ...
      "items": {
        // ...
      }
    },
```

Each File hash of value type `object` contains one hash value and algorithm of the file to be identified. Any File hash object has the 2 mandatory properties `algorithm` and `value`.

```
        "properties": {
          "algorithm": {
            // ...
          },
          "value": {
            // ...
          }
        }
```

The algorithm of the cryptographic hash representation (`algorithm`) of value type `string` with one or more characters contains the name of the cryptographic hash algorithm used to calculate the value.
The default value for `algorithm` is `sha256`.

*Examples 11:*

```
      blake2b512
      sha256
      sha3-512
      sha384
      sha512
```

These values are derived from the currently supported digests OpenSSL [OPENSSL]. Leading dashes were removed.

> The command `openssl dgst -list` (Version 1.1.1f from 2020-03-31) outputs the following:
>
>```
>  Supported digests:
>  -blake2b512                -blake2s256                -md4                      
>  -md5                       -md5-sha1                  -ripemd                   
>  -ripemd160                 -rmd160                    -sha1                     
>  -sha224                    -sha256                    -sha3-224                 
>  -sha3-256                  -sha3-384                  -sha3-512                 
>  -sha384                    -sha512                    -sha512-224               
>  -sha512-256                -shake128                  -shake256                 
>  -sm3                       -ssl3-md5                  -ssl3-sha1                
>  -whirlpool
>```

The Value of the cryptographic hash representation (`value`) of value type `string` of 32 or more characters with `pattern` (regular expression):

```
    ^[0-9a-fA-F]{32,}$
```

The Value of the cryptographic hash attribute contains the cryptographic hash value in hexadecimal representation.

*Examples 12:*

```
    37df33cb7464da5c7f077f4d56a32bc84987ec1d85b234537c1c1a4d4fc8d09dc29e2e762cb5203677bf849a2855a0283710f1f5fe1d6ce8d5ac85c645d0fcb3
    4775203615d9534a8bfca96a93dc8b461a489f69124a130d786b42204f3341cc
    9ea4c8200113d49d26505da0e02e2f49055dc078d1ad7a419b32e291c7afebbb84badfbd46dec42883bea0b2a1fa697c
```

The filename representation (`filename`) of value type `string` with one or more characters contains the name of the file which is identified by the hash values.

*Examples 13:*

```
    WINWORD.EXE
    msotadddin.dll
    sudoers.so
```

If the value of the hash matches and the filename does not, a user SHOULD prefer the hash value. In such cases, the filename SHOULD be used as informational property.

##### 3.1.3.3.3 Full Product Name Type - Product Identification Helper - Model Numbers

The list of models (`model_numbers`) of value type `array` with 1 or more unique items contains a list of full or abbreviated (partial) model numbers.

A list of models SHOULD only be used if a certain range of model numbers with its corresponding software version is affected, or the model numbers change during update.

This can also be used to identify hardware. If necessary, the software, or any other related part, SHALL be bind to that via a product relationship.

```
    "model_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given model number of value type `string` with at least 1 character represents a full or abbreviated (partial) model number of the component to identify.

> The terms "model", "model number" and "model variant" are mostly used synonymously. Often it is abbreviated as "MN", M/N" or "model no.".

If a part of a model number of the component to identify is given, it SHOULD begin with the first character of the model number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

*Examples 14:*

```
    6RA8096-4MV62-0AA0
    6RA801?-??V62-0AA0
    IC25T060ATCS05-0
```

##### 3.1.3.3.4 Full Product Name Type - Product Identification Helper - PURL

The package URL (PURL) representation (`purl`) is a `string` of 7 or more characters with `pattern` (regular expression):

```
    ^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+
```

> The given pattern does not completely evaluate whether a PURL is valid according to the [PURL] specification. It provides a more generic approach and general guidance to enable forward compatibility.
> CSAF uses only the canonical form of PURL to conform with section 3.3 of [RFC3986]. Therefore, URLs starting with `pkg://` are considered invalid.

This package URL (PURL) attribute refers to a method for reliably identifying and locating software packages external to this specification. See [PURL] for details.

##### 3.1.3.3.5 Full Product Name Type - Product Identification Helper - SBOM URLs

The list of SBOM URLs (`sbom_urls`) of value type `array` with 1 or more items contains a list of URLs where SBOMs for this product can be retrieved.

> The SBOMs might differ in format or depth of detail. Currently supported formats are SPDX, CycloneDX, and SWID.

```
    "sbom_urls": {
        //...
      "items": {
        //...
      }
    },
```

Any given SBOM URL of value type `string` with format `uri` contains a URL of one SBOM for this product.

*Examples 15:*

```
    https://raw.githubusercontent.com/CycloneDX/bom-examples/master/SBOM/keycloak-10.0.2/bom.json
    https://swinslow.net/spdx-examples/example4/main-bin-v2
```

##### 3.1.3.3.6 Full Product Name Type - Product Identification Helper - Serial Numbers

The list of serial numbers (`serial_numbers`) of value type `array` with 1 or more unique items contains a list of full or abbreviated (partial) serial numbers.

A list of serial numbers SHOULD only be used if a certain range of serial numbers with its corresponding software version is affected, or the serial numbers change during update.

```
    "serial_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given serial number of value type `string` with at least 1 character represents a full or abbreviated (partial) serial number of the component to identify.

If a part of a serial number of the component to identify is given, it SHOULD begin with the first character of the serial number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### 3.1.3.3.7 Full Product Name Type - Product Identification Helper - SKUs

The list of stock keeping units (`skus`) of value type `array` with 1 or more items contains a list of full or abbreviated (partial) stock keeping units.

A list of stock keeping units SHOULD only be used if the list of relationships is used to decouple e.g. hardware from the software, or the stock keeping units change during update. In the latter case the remediations SHALL include the new stock keeping units is or a description how it can be obtained.

> The use of the list of relationships in the first case is important. Otherwise, the end user is unable to identify which version (the affected or the not affected / fixed one) is used.

```
    "skus": {
        //...  
      "items": {
        //...  
      }
    },
```

Any given stock keeping unit of value type `string` with at least 1 character represents a full or abbreviated (partial) stock keeping unit (SKU) of the component to identify.

> Sometimes this is also called "item number", "article number" or "product number".

If a part of a stock keeping unit of the component to identify is given, it SHOULD begin with the first character of the stock keeping unit and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### 3.1.3.3.8 Full Product Name Type - Product Identification Helper - Generic URIs

List of generic URIs (`x_generic_uris`) of value type `array` with at least 1 item contains a list of identifiers which are either vendor-specific or derived from a standard not yet supported.

```
    "x_generic_uris": {
      // ...
      "items": {
        // ...
      }
    }  
```

Any such Generic URI item of value type `object` provides the two mandatory properties Namespace (`namespace`) and URI (`uri`).

```
        "properties": {
          "namespace": {
            // ...
          },
          "uri": {
            // ...
          }
        }
```

The namespace of the generic URI (`namespace`) of value type `string` with format `uri` refers to a URL which provides the name and knowledge about the specification used or is the namespace in which these values are valid.

The URI (`uri`) of value type `string` with format `uri` contains the identifier itself.

> These elements can be used to reference a specific component from an SBOM:

*Example 16 linking a component from a CycloneDX SBOM using the bomlink mechanism:*

```
          "x_generic_uris": [
            {
              "namespace": "https://cyclonedx.org/capabilities/bomlink/",
              "uri": "urn:cdx:411dafd2-c29f-491a-97d7-e97de5bc2289/1#pkg:maven/org.jboss.logging/jboss-logging@3.4.1.Final?type=jar"
            }
          ]
```

*Example 17 linking a component from an SPDX SBOM:*

```
          "x_generic_uris": [
            {
              "namespace": "https://spdx.github.io/spdx-spec/document-creation-information/#65-spdx-document-namespace-field",
              "uri": "https://swinslow.net/spdx-examples/example4/main-bin-v2#SPDXRef-libc"
            }
          ]
```

### 3.1.4 Language Type

Language type (`lang_t`) has value type `string` with `pattern` (regular expression):

```
    ^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])$
```

The value identifies a language, corresponding to IETF BCP 47 / RFC 5646.
See IETF language registry: [https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)

> CSAF skips those grandfathered language tags that are deprecated at the time of writing the specification. Even though the private use language tags are supported they should not be used to ensure readability across the ecosystem.
> It is recommended to follow the conventions for the capitalization of the subtags even though it is not mandatory as most users are used to that.

*Examples 18:*

```
    de
    en
    fr
    frc
    jp
```

### 3.1.5 Notes Type

List of notes (`notes_t`) of value type `array` with 1 or more items of type `Note` contains notes which are specific to the current context.

```
    "notes_t": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Note item is `object` with the mandatory properties `category` and `text` providing a place to put all manner of text blobs related to the current context.
A Note `object` MAY provide the optional properties `audience` and `title`.

```
    "properties": {
      "audience": {
        // ...
      },
      "category": {
        // ...
      },
      "text": {
        // ...
      },
      "title": {
        // ...
      }
    }
```

Audience of note (`audience`) of value type `string` with 1 or more characters indicates who is intended to read it.

*Examples 19:*

```
    all
    executives
    operational management and system administrators
    safety engineers
```

Note category (`category`) of value type `string` and `enum` contains the information of what kind of note this is.
Valid `enum` values are:

```
    description
    details
    faq
    general
    legal_disclaimer
    other
    summary
```

The value `description` indicates the note is a description of something. The optional sibling property `title` MAY have more information in this case.

The value `details` indicates the note is a low-level detailed discussion. The optional sibling property `title` MAY have more information in this case.

The value `faq` indicates the note is a list of frequently asked questions.

The value `general` indicates the note is a general, high-level note. The optional sibling property `title` MAY have more information in this case.

The value `legal_disclaimer` indicates the note represents any possible legal discussion, including constraints, surrounding the document.

The value `other` indicates the note is something that doesn’t fit the other categories. The optional sibling attribute `title` SHOULD have more information to indicate clearly what kind of note to expect in this case.

The value `summary` indicates the note is a summary of something. The optional sibling property `title` MAY have more information in this case.

Note content (`text`) of value type `string` with 1 or more characters holds the content of the note. Content varies depending on type.

Title of note (`title`) of value type `string` with 1 or more characters provides a concise description of what is contained in the text of the note.

*Examples 20:*

```
    Details
    Executive summary
    Technical summary
    Impact on safety systems
```

### 3.1.6 Product Group ID Type

The Product Group ID Type (`product_group_id_t`) of value type `string` with 1 or more characters is a reference token for product group instances.
The value is a token required to identify a group of products so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product Group ID (`product_group_id`) as long as it uniquely identifies a product group in the context of the current document.

```
    "product_group_id_t": {
      // ...
    },
```

*Examples 21:*

```
    CSAFGID-0001
    CSAFGID-0002
    CSAFGID-0020
```

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and the Product Group ID to support reading and parsing the document.

### 3.1.7 Product Groups Type

List of Product Group ID (`product_groups_t`) of value type `array` with 1 or more unique items (a `set`) of type Product Group ID (`product_group_id_t`) specifies a list of `product_group_ids` to give context to the parent item.

```
    "product_groups_t": {
      // ...
      "items": {
        // ...
      }
    },
```

### 3.1.8 Product ID Type

The Product ID Type (`product_id_t`) of value type `string` with 1 or more characters is a reference token for product instances.
The value is a token required to identify a `full_product_name` so that it can be referred to from other parts in the document. There is no predefined or required format for the Product ID (`product_id`) as long as it uniquely identifies a product in the context of the current document.

```
    "product_id_t": {
      // ...
    },
```

*Examples 22:*

```
    CSAFPID-0004
    CSAFPID-0008
```

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and the Product Group ID to support reading and parsing the document.

### 3.1.9 Products Type

List of Product IDs (`products_t`) of value type `array` with 1 or more unique items (a `set`) of type Product ID (`product_id_t`) specifies a list of `product_ids` to give context to the parent item.

```
    "products_t": {
      // ...
      "items": {
        // ...
      }
    },
```

### 3.1.10 References Type

List of references (`references_t`) of value type `array` with 1 or more items of type Reference holds a list of Reference objects.

```
    "references_t": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Reference item is `object` with the mandatory properties `url` and `summary` holding any reference to conferences, papers, advisories, and other resources that are related and considered related to either a surrounding part of or the entire document and to be of value to the document consumer.
A reference `object` MAY provide the optional property `category`.

```
    "properties": {
      "category": {
        // ...
      },
      "summary": {
        // ...
      },
      "url": {
        // ...
      }
    }
```

Category of reference (`category`) of value type `string` and `enum` indicates whether the reference points to the same document or vulnerability in focus (depending on scope) or to an external resource.
Valid `enum` values are:

```
    external
    self
```

The default value for `category` is `external`.

The value `external` indicates, that this document is an external reference to a document or vulnerability in focus (depending on scope).

The value `self` indicates, that this document is a reference to this same document or vulnerability (also depending on scope).

> This includes links to documents with the same content but different file format (e.g. advisories as PDF or HTML).

Summary of the reference (`summary`) of value type `string` with 1 or more characters indicates what this reference refers to.

URL of reference (`url`) of value type `string` with format `uri` provides the URL for the reference.

### 3.1.11 Version Type

The Version (`version_t`) type has value type `string` with `pattern` (regular expression):

```
    ^(0|[1-9][0-9]*)$|^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The version specifies a version string to denote clearly the evolution of the content of the document. There are two options how it can be used:

* semantic versioning (preferred; according to the rules below)
* integer versioning

A CSAF document MUST use only one versioning system.

*Examples 23:*

```
    1
    4
    0.9.0
    1.4.3
    2.40.0+21AF26D3
```

#### 3.1.11.1 Version Type - Integer versioning

Integer versioning increments for each version where the `/document/tracking/status` is `final` the version number by one. The regular expression for this type is:

```
^(0|[1-9][0-9]*)$
```

The following rules apply:

1. Once a versioned document has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.
2. Version zero (0) is for initial development before the `initial_release_date`. The document status MUST be `draft`. Anything MAY change at any time. The document SHOULD NOT be considered stable.
3. Version 1 defines the initial public release. Each new version where `/document/tracking/status` is `final` has a version number incremented by one.
4. Pre-release versions (document status `draft`) MUST carry the new version number. Sole exception is before the initial release (see rule 2). The combination of document status `draft` and version 1 MAY be used to indicate that the content is unlikely to change.
5. Build metadata is never included in the version.
6. Precedence MUST be calculate by integer comparison.

#### 3.1.11.2 Version Type - Semantic versioning

Semantic versioning derived the rules from [SemVer]. The regular expression for this type is:

```
^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The goal of this structure is to provide additional information to the end user whether a new comparison with the asset database is needed. The "public API" in regards to CSAF is the CSAF document with its structure and content. This results in the following rules:

1. A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
2. Once a versioned document has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.
3. Major version zero (0.y.z) is for initial development before the `initial_release_date`. The document status MUST be `draft`. Anything MAY change at any time. The document SHOULD NOT be considered stable. Changes which would increment the major version according to rule 7 are tracked in this stage with (0.y.z) by incrementing the minor version y instead. Changes that would increment the minor or patch version according to rule 6 or 5 are both tracked in this stage with (0.y.z) by incrementing the patch version z instead.
4. Version 1.0.0 defines the initial public release. The way in which the version number is incremented after this release is dependent on the content and structure of the document and how it changes.
5. Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

   > In the context of the document this is the case e.g. for spelling mistakes.

6. Minor version Y (x.Y.z | x > 0) MUST be incremented if the content of an existing element changes except for those which are covert through rule 7. It MUST be incremented if substantial new information are introduced or new elements are provided. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.
7. Major version X (X.y.z | X > 0) MUST be incremented if a new comparison with the end user's asset database is required. This includes:

   * changes (adding, removing elements or modifying content) in `/product_tree` or elements which contain `/product_tree` in their path
   * adding or removing items of `/vulnerabilities`
   * adding or removing elements in:
     * `/vulnerabilities[]/product_status/first_affected`
     * `/vulnerabilities[]/product_status/known_affected`
     * `/vulnerabilities[]/product_status/last_affected`
   * removing elements from:
     * `/vulnerabilities[]/product_status/first_fixed`
     * `/vulnerabilities[]/product_status/fixed`
     * `/vulnerabilities[]/product_status/known_not_affected`

   It MAY also include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.
8. A pre-release version (document status `draft`) MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version.

   *Examples 24:*

   ```
   1.0.0-0.3.7
   1.0.0-alpha
   1.0.0-alpha.1
   1.0.0-x-y-z.–
   1.0.0-x.7.z.92
   ```

9. Pre-release MUST NOT be included if `/document/tracking/status` is `final`.
10. Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence.

    *Examples 25:*

    ```
    1.0.0+20130313144700
    1.0.0+21AF26D3—-117B344092BD
    1.0.0-alpha+001
    1.0.0-beta+exp.sha.5114f85
    ```

11. Precedence refers to how versions are compared to each other when ordered.

    1. Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence).
    2. Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically.

       *Example 26:*

       ```
       1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
       ```

    3. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:

       *Example 27:*

       ```
       1.0.0-alpha < 1.0.0
       ```

    4. Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:

       1. Identifiers consisting of only digits are compared numerically.
       2. Identifiers with letters or hyphens are compared lexically in ASCII sort order.
       3. Numeric identifiers always have lower precedence than non-numeric identifiers.
       4. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.

       *Example 28:*

       ```
       1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0
       ```
