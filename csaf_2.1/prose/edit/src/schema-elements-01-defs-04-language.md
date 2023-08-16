### Language Type

Language type (`lang_t`) has value type `string` with `pattern` (regular expression):

```
    ^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])$
```

The value identifies a language, corresponding to IETF BCP 47 / RFC 5646.
See IETF language registry: <https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry>

> CSAF skips those grandfathered language tags that are deprecated at the time of writing the specification.
> Even though the private use language tags are supported they should not be used to ensure readability across the ecosystem.
> It is recommended to follow the conventions for the capitalization of the subtags even though it is not mandatory as most users are used to that.

*Examples 1:*

```
    de
    en
    fr
    frc
    jp
```
