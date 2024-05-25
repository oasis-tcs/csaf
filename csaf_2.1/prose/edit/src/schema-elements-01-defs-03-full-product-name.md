### Full Product Name Type

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

#### Full Product Name Type - Name

Textual description of the product (`name`) has value type `string` with 1 or more characters.
The value SHOULD be the product's full canonical name, including version number and other attributes,
as it would be used in a human-friendly document.

*Examples 1:*

```
    Cisco AnyConnect Secure Mobility Client 2.3.185
    Microsoft Host Integration Server 2006 Service Pack 1
```

#### Full Product Name Type - Product ID

Product ID (`product_id`) holds a value of type Product ID (`product_id_t`).

#### Full Product Name Type - Product Identification Helper

Helper to identify the product (`product_identification_helper`) of value type `object` provides in its properties at least
one method which aids in identifying the product in an asset database.
Of the given eight properties `cpe`, `hashes`, `model_numbers`, `purl`, `sbom_urls`, `serial_numbers`, `skus`,
and `x_generic_uris`, one is mandatory.

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

##### Full Product Name Type - Product Identification Helper - CPE

Common Platform Enumeration representation (`cpe`) of value type `string` of 5 or more characters with `pattern` (regular expression):

```
    ^((cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,\\/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,\\/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|([c][pP][eE]:\\/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6}))$
```

The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external to this specification.
See [CPE23-N] for details.

##### Full Product Name Type - Product Identification Helper - Hashes

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

Each File hash of value type `object` contains one hash value and algorithm of the file to be identified.
Any File hash object has the 2 mandatory properties `algorithm` and `value`.

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

The algorithm of the cryptographic hash representation (`algorithm`) of value type `string` with one or more characters contains
the name of the cryptographic hash algorithm used to calculate the value.
The default value for `algorithm` is `sha256`.

*Examples 1:*

```
      blake2b512
      sha256
      sha3-512
      sha384
      sha512
```

These values are derived from the currently supported digests OpenSSL [cite](#OPENSSL). Leading dashes were removed.

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

*Examples 2:*

```
    37df33cb7464da5c7f077f4d56a32bc84987ec1d85b234537c1c1a4d4fc8d09dc29e2e762cb5203677bf849a2855a0283710f1f5fe1d6ce8d5ac85c645d0fcb3
    4775203615d9534a8bfca96a93dc8b461a489f69124a130d786b42204f3341cc
    9ea4c8200113d49d26505da0e02e2f49055dc078d1ad7a419b32e291c7afebbb84badfbd46dec42883bea0b2a1fa697c
```

The filename representation (`filename`) of value type `string` with one or more characters contains the name of
the file which is identified by the hash values.

*Examples 3:*

```
    WINWORD.EXE
    msotadddin.dll
    sudoers.so
```

If the value of the hash matches and the filename does not, a user SHOULD prefer the hash value.
In such cases, the filename SHOULD be used as informational property.

##### Full Product Name Type - Product Identification Helper - Model Numbers

The list of models (`model_numbers`) of value type `array` with 1 or more unique items contains a list of full or
abbreviated (partial) model numbers.

A list of models SHOULD only be used if a certain range of model numbers with its corresponding software version is affected,
or the model numbers change during update.

This can also be used to identify hardware.
If necessary, the software, or any other related part, SHALL be bind to that via a product relationship.

```
    "model_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given model number of value type `string` with at least 1 character represents a full or abbreviated (partial) model number of
the component to identify.

> The terms "model", "model number" and "model variant" are mostly used synonymously.
> Often it is abbreviated as "MN", M/N" or "model no.".

If a part of a model number of the component to identify is given,
it SHOULD begin with the first character of the model number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

*Examples 1:*

```
    6RA8096-4MV62-0AA0
    6RA801?-??V62-0AA0
    IC25T060ATCS05-0
```

##### Full Product Name Type - Product Identification Helper - purl

The package URL (purl) representation (`purl`) is a `string` of 7 or more characters with `pattern` (regular expression):

```
    ^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*\\/.+
```

> The given pattern does not completely evaluate whether a purl is valid according to the [cite](#PURL) specification.
> It provides a more generic approach and general guidance to enable forward compatibility.
> CSAF uses only the canonical form of purl to conform with section 3.3 of [cite](#RFC3986).
> Therefore, URLs starting with `pkg://` are considered invalid.

This package URL (purl) attribute refers to a method for reliably identifying and locating software packages external to this specification.
See [cite](#PURL) for details.

##### Full Product Name Type - Product Identification Helper - SBOM URLs

The list of SBOM URLs (`sbom_urls`) of value type `array` with 1 or more items contains
a list of URLs where SBOMs for this product can be retrieved.

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

*Examples 1:*

```
    https://raw.githubusercontent.com/CycloneDX/bom-examples/master/SBOM/keycloak-10.0.2/bom.json
    https://swinslow.net/spdx-examples/example4/main-bin-v2
```

##### Full Product Name Type - Product Identification Helper - Serial Numbers

The list of serial numbers (`serial_numbers`) of value type `array` with 1 or more unique items contains
a list of full or abbreviated (partial) serial numbers.

A list of serial numbers SHOULD only be used if a certain range of serial numbers with its corresponding software version is affected,
or the serial numbers change during update.

```
    "serial_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given serial number of value type `string` with at least 1 character represents a full or
abbreviated (partial) serial number of the component to identify.

If a part of a serial number of the component to identify is given,
it SHOULD begin with the first character of the serial number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### Full Product Name Type - Product Identification Helper - SKUs

The list of stock keeping units (`skus`) of value type `array` with 1 or more items contains a list of full or
abbreviated (partial) stock keeping units.

A list of stock keeping units SHOULD only be used if the list of relationships is used to decouple e.g. hardware from the software,
or the stock keeping units change during update.
In the latter case the remediations SHALL include the new stock keeping units or a description how it can be obtained.

> The use of the list of relationships in the first case is important.
> Otherwise, the end user is unable to identify which version (the affected or the not affected / fixed one) is used.

```
    "skus": {
        //...  
      "items": {
        //...  
      }
    },
```

Any given stock keeping unit of value type `string` with at least 1 character represents a full or
abbreviated (partial) stock keeping unit (SKU) of the component to identify.

> Sometimes this is also called "item number", "article number" or "product number".

If a part of a stock keeping unit of the component to identify is given, it SHOULD begin with the first character of
the stock keeping unit and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### Full Product Name Type - Product Identification Helper - Generic URIs

List of generic URIs (`x_generic_uris`) of value type `array` with at least 1 item contains a list of identifiers which are
either vendor-specific or derived from a standard not yet supported.

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

The namespace of the generic URI (`namespace`) of value type `string` with format `uri` refers to a URL which provides
the name and knowledge about the specification used or is the namespace in which these values are valid.

The URI (`uri`) of value type `string` with format `uri` contains the identifier itself.

> These elements can be used to reference a specific component from an SBOM:

*Example 1 (linking a component from a CycloneDX SBOM using the bomlink mechanism):*

```
          "x_generic_uris": [
            {
              "namespace": "https://cyclonedx.org/capabilities/bomlink/",
              "uri": "urn:cdx:411dafd2-c29f-491a-97d7-e97de5bc2289/1#pkg:maven/org.jboss.logging/jboss-logging@3.4.1.Final?type=jar"
            }
          ]
```

*Example 2 (linking a component from an SPDX SBOM):*

```
          "x_generic_uris": [
            {
              "namespace": "https://spdx.github.io/spdx-spec/latest/document-creation-information/#65-spdx-document-namespace-field",
              "uri": "https://swinslow.net/spdx-examples/example4/main-bin-v2#SPDXRef-libc"
            }
          ]
```
