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

*Examples 1:*

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

*Examples 1:*

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
