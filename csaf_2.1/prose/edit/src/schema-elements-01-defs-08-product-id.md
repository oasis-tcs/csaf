### Product ID Type

The Product ID Type (`product_id_t`) of value type `string` with `1` or more characters is a reference token for product instances.
The value is a token required to identify a `full_product_name` so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product ID (`product_id`) as long as it uniquely identifies a product in the context of
the current document.

```
    "product_id_t": {
      // ...
    },
```

*Examples 1:*

```
    CSAFPID-0004
    CSAFPID-0008
```

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and
> the Product Group ID to support reading and parsing the document.
