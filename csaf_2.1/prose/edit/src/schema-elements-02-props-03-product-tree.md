### Product Tree Property

Product Tree (`product_tree`) has value type `object` with `1` or more properties is a container for all fully qualified product names that
can be referenced elsewhere in the document.
The properties are Branches (`branches`), Full Product Names (`full_product_names`), Product Groups (`product_groups`),
and Product Paths (`product_paths`).

```yaml <!--json-path($..product_tree.properties)-->
<csaf-instance>:
  # ...
  product_tree:
    branches: $defs.branches_t
    full_product_names: Mapping
    product_groups: Sequence
    relationships: Sequence
```

#### Product Tree Property - Branches

List of branches (`branches`) has the value type `branches_t`.

#### Product Tree Property - Full Product Names

List of full product names (`full_product_names`) of value type `array` with `1` or more items of type `full_product_name_t` contains a
list of full product names.

#### Product Tree Property - Product Groups

List of product groups (`product_groups`) of value type `array` with `1` or more items of value type `object` contains a list of product groups.

```yaml <!--json-path($..product_tree..product_groups)-->
<csaf-instance>:
  # ...
  product_tree:
    # ...
    product_groups: Sequence
  # ...
```

The product group items are of value type `object` with the two mandatory properties Group ID (`group_id`) and Product IDs (`product_ids`) and
the optional Summary (`summary`) property.

```yaml <!--json-path($..product_tree..product_groups..properties)-->
<csaf-instance>:
  # ...
  product_tree:
    # ...
    product_groups:
    - # <product_group-instance>:
      group_id: $defs.product_group_id_t
      product_ids: Sequence
      summary: String
    # ...
  # ...
```

The summary of the product group (`summary`) of value type `string` with `1` or more characters gives a short, optional description of the group.

*Examples 1:*

```
    Products supporting Modbus.
    The x64 versions of the operating system.
```

Group ID (`group_id`) has value type Product Group ID (`product_group_id_t`).

List of Product IDs (`product_ids`) of value type `array` with `2` or more unique items of value type Product ID (`product_id_t`) lists
the product_ids of those products which known as one group in the document.

#### Product Tree Property - Product Paths

List of product paths (`product_paths`) of value type `array` with `1` or more items contains a list of product paths.

```yaml <!--json-path($..product_tree..relationships)-->
<csaf-instance>:
  # ...
  product_tree:
    # ...
    relationships: Sequence
  # ...
```

The Product path item is of value type `object` and has three mandatory properties:
Beginning product reference (`beginning_product_reference`),
Full Product Name (`full_product_name`), and Subpaths (`subpaths`).
The Product path item establishes a path along existing full_product_name_t elements,
allowing the document producer to define a path of multiple products that form a new full_product_name entry.

```yaml <!--json-path($..product_tree..relationships..properties)-->
<csaf-instance>:
  # ...
  product_tree:
    # ...
    relationships:
    - # <relationship-instance>:
      category: String.Enum
      full_product_name: $defs.full_product_name_t
      product_reference: $defs.product_id_t
      relates_to_product_reference: $defs.product_id_t
    # ...
  # ...
```

> The situation where a need for declaring a Product path arises,
> is given when a product is e.g. vulnerable only when installed together with another, or to describe operating system components.

Beginning product reference (`beginning_product_reference`) of value type Product ID (`product_id_t`) holds a Product ID
that refers to the Full Product Name element, which is the beginning node of the product path.
It is also the product, the first node in `subpaths` links to.

> The product referenced in `beginning_product_reference` is usually the product that is more closely identified by the product path.

Full Product Name (`full_product_name`) of value type Full Product Name Type (`full_product_name_t`).

List of product subpaths (`subpaths`) of value type `array` with `1` or more items of type Subpath (`subpath_t`)
contains an ordered list of product subpaths,
each one relating to the path defined by all previous elements up to the beginning node of the product path.

```
      "subpaths": {
        // ...
        "items": {
          // ...
        }
      }
```

*Example 1:*

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
    "product_paths": [
      {
        "beginning_product_reference": "CSAFPID-908070601",
        "full_product_name": {
          "product_id": "CSAFPID-908070603",
          "name": "Cisco AnyConnect Secure Mobility Client 4.9.04053 installed on Microsoft Windows"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070602",
          }
        ]
      }
    ]
  }
```

> The product `Cisco AnyConnect Secure Mobility Client 4.9.04053"` (Product ID: `CSAFPID-908070601`) and
> the product `Microsoft Windows` (Product ID: `CSAFPID-908070602`) form together
> a new product with the separate Product ID `CSAFPID-908070603`.
> The latter one can be used to refer to that combination in other parts of the CSAF document.
> In the preceding example, it might be the case that `Cisco AnyConnect Secure Mobility Client 4.9.04053"`
> is only vulnerable when installed on `Microsoft Windows`.
