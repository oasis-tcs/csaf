### Product Group ID Type

The Product Group ID Type (`product_group_id_t`) of value type `string` with 1 or more characters is a reference token for product group instances.
The value is a token required to identify a group of products so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product Group ID (`product_group_id`) as long as it uniquely identifies
a product group in the context of the current document.

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

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and
> the Product Group ID to support reading and parsing the document.
