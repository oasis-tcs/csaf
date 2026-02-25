### Subpath Type

Subpath (`subpath_t`) of value type `object` contains the next node along the current path its relationship to the previous node.
The properties `category` and `next_product_reference` are required.

```
      "properties": {
        "category": {
          // ...
        },
        "next_product_reference": {
          // ...
        }
      },
```

Relationship category (`category`) of value type `string` and `enum` defines the category of relationship between the previous item
and the referenced next product.
Valid `enum` values are:

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

Next product reference (`next_product_reference`) of value type Product ID (`product_id_t`) holds a Product ID that refers
to the Full Product Name element, which is referenced as the second element of the relationship.
