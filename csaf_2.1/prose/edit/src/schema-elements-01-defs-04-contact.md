### Contact Type

Contact Type (`contact_t`) of value type `object` with `1` or more properties contains information on how to contact the party.
The properties are Contact Details (`details`), Email (`email`), Public OpenPGP Key URL (`public_openpgp_key_url`), and
Contact URL (`url`).
If the property `public_openpgp_key_url` is set, the `email` SHALL be set as well.

```yaml <!--json-path($['$defs'].contact_t.properties)-->
$defs:
  # ...
  contact_t:
    details: String
    email: String.EMAIL
    public_openpgp_key_url: String.URI
    url: String.URI
  # ...
```

Contact details (`details`) of value type `string` with `1` or more characters contains details regarding ways to reach the party,
 e.g. through web sites, phone numbers, and postal mail addresses.

*Example 1:*

```
    Example Company can be reached at tel:+493023125232,
    or via our website at https://www.example.com/contact.
```

Email (`email`) of value type `string` of `6` or more characters with format `email` contains the email address
that can be used to reach the party.

*Examples 2:*

```
    productcert@example.net
    psirt@example.com
    reporter@securityresearcher.example
    vulnerability@coordinator.example
```

Public OpenPGP Key URL (`public_openpgp_key_url`) has value type `string` of `11` or more characters with format `uri`
and `pattern` (regular expression):

```
    ^https:\\/\\/
```

Public OpenPGP Key URL contains a URL pointing to a public OpenPGP key valid for the email of party provided
in the sibling property `email`.

> It is desired that the OpenPGP Key contains the same email address in its user ID as given through the property `email`.
> However, due to data protection and operation concerns neither a user ID in the OpenPGP key nor
> an exact match to the value of `email` is enforced by this standard.
> The use of aliases is permitted.
> The issuing party is responsible for ensuring the usability of the key provided.

The URL MAY point to a location that redirects.
Redirects SHALL fulfill the same requirements as specified in [sec](#requirement-6-no-redirects).
The content delivered SHALL be a valid OpenPGP key allowing encryption as ASCII armored file with the matching content type.
See [cite](#RFC4880) and [cite](#RFC3156) for more details.

*Examples 3:*

```
    https://coordinator.example/.well-known/openpgpkey/hu/nxdcs8npc6mn3xyfpcbiqhcu9s357r5m?l=vulnerability
    https://example.net/.well-known/openpgpkey/hu/euwmpyfh4rzf8ymbqhjjhrirgib4dyfs?l=productcert
    https://openpgpkey.securityresearcher.example/.well-known/openpgpkey/securityresearcher.example/hu/enudbakzkbdym3ymwjy9pcxztka75f73?l=reporter
    https://psirt.example.com/security/openpgp/latest
```

Contact URL (`url`) has value type `string` of `11` or more characters with format `uri` and `pattern` (regular expression):

```
    ^https:\\/\\/
```

Contact URL contains a URL that can be used to reach the party.

*Examples 4*:

```
    https://www.example.com/psirt/contact
    https://www.example.net/psirt/report-a-vulnerability--expert-form
    https://www.example.org/.well-known/security.txt
```
