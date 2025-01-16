### Branches Type

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

> `branches_t` supports building a hierarchical structure of products that allows to indicate the relationship of products to each other and
> enables grouping for simpler referencing.
> As an example, the structure MAY use the following levels: `vendor` -> `product_family` -> `product_name` -> `product_version`.
> It is recommended to use the hierarchical structure of `vendor` -> `product_name` -> `product_version` whenever possible to support
> the identification and matching of products on the consumer side.

#### Branches Type - Branches

List of branches (`branches`) has the value type `branches_t`.

#### Branches Type - Category

Category of the branch (`category`) of value type `string` and `enum` describes the characteristics of the labeled branch.
Valid `enum` values are:

```
    architecture
    host_name
    language
    legacy
    patch_level
    platform
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

The value `platform` indicates the (CPU) platform for which the product is intended.

The value `product_family` indicates the product family that the product falls into.

The value `product_name` indicates the name of the product.

The value `product_version` indicates exactly a single version of the product.
The value of the adjacent `name` property can be numeric or some other descriptor.
However, it MUST NOT contain version ranges of any kind.

> It is recommended to enumerate versions wherever possible. Nevertheless, the TC understands that this is sometimes impossible.
> To reflect that in the specification and aid in automatic processing of CSAF documents the value `product_version_range` was introduced.
> See next section for details.

The value `product_version_range` indicates a range of versions for the product.
The value of the adjacent `name` property SHOULD NOT be used to convey a single version.

The value `service_pack` indicates the service pack of the product.

The value `specification` indicates the specification such as a standard, best common practice, etc.

The value `vendor` indicates the name of the vendor or manufacturer that makes the product.

#### Branches Type - Name

Name of the branch (`name`) of value type `string` with 1 or more characters contains the canonical descriptor or 'friendly name' of the branch.

*Examples 1:*

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

A leading `v` or `V` in the value of `name` SHOULD only exist for the categories `product_version` or `product_version_range` if it is
part of the product version as given by the vendor.

##### Branches Type - Name under Product Version

If adjacent property `category` has the value `product_version`, the value of `name` MUST NOT contain version ranges of any kind.

*Examples 1 (for `name` when using `product_version`):*

```
    10
    17.4
    v3
```

> The `product_version` is the easiest way for users to determine whether their version is meant
> (provided that the given ancestors in the product tree matched):
> If both version strings are the same, it is a match - otherwise not.
> Therefore, it is always recommended to enumerate product versions instead of providing version ranges.

*Examples 2 (for `name` when using `product_version` which are invalid):*

```
    8.0.0 - 8.0.1
    8.1.5 and later
    <= 2
    prior to 4.2
    All versions < V3.0.29
    V3.0, V4.0, V4.1, V4.2
```

> All the examples above contain some kind of a version range and are therefore invalid under the category `product_version`.

##### Branches Type - Name under Product Version Range

If adjacent property `category` has the value `product_version_range`, the value of `name` MUST contain version ranges.
The value of MUST obey to exactly one of the following options:

1. Version Range Specifier (vers)

    > vers is an ongoing community effort to address the problem of version ranges. Its draft specification is available at [cite](#VERS).

    vers MUST be used in its canonical form. To convey the term "all versions" the special string `vers:all/*` MUST be used.

    *Examples 1 (for `name` when using `product_version_range` with vers):*

    ```
        vers:gem/>=2.2.0|!= 2.2.1|<2.3.0
        vers:npm/1.2.3|>=2.0.0|<5.0.0
        vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1
        vers:tomee/>=8.0.0-M1|<=8.0.1
    ```

    > Through the definitions of the vers specification a user can compute whether a given version is in a given range.

2. Vers-like Specifier (vls)

    This option uses only the `<version-constraint>` part from the vers specification. It MUST NOT have an URI nor the `<versioning-scheme>` part.
    It is a fallback option and SHOULD NOT be used unless really necessary.
    > The reason for that is, that it is nearly impossible for tools to reliable determine whether a given version is in the range or not.

    Tools MAY support this on best effort basis.

    *Examples 2 (for `name` when using `product_version_range` with vls):*

    ```
        <=2
        <4.2
        <V3.0.29
        >=8.1.5
    ```

#### Branches Type - Product

Product (`product`) has the value type Full Product Name (`full_product_name_t`).
