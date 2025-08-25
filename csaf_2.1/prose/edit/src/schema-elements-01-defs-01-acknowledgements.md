### Acknowledgments Type

List of Acknowledgments (`acknowledgments_t`) type instances of value type `array` with `1` or more elements contain
a list of `Acknowledgment` elements.

```
    "acknowledgments_t": {
      // ...
      "items": {
        // ...
      }
    },
```

The value type of Acknowledgment is `object` with at least one and at most four properties. Every such element acknowledges contributions by
describing those that contributed.
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

#### Acknowledgments Type - Names

List of acknowledged names (`names`) of value type `array` with `1` or more items holds the names of contributors being recognized.
Every such item of value type `string` with `1` or more characters represents the name of the contributor and contains the name of
a single contributor being recognized.

*Examples 1:*

```
    Albert Einstein
    Johann Sebastian Bach
```

#### Acknowledgments Type - Organization

The contributing organization (`organization`) of value type `string` with `1` or more characters and holds the name of
the contributing organization being recognized.

*Examples 1:*

```
    CISA
    Google Project Zero
    Talos
```

#### Acknowledgments Type - Summary

Summary of the acknowledgment (`summary`) of value type `string` with `1` or more characters SHOULD represent any contextual details
the document producers wish to make known about the acknowledgment or acknowledged parties.

*Example 1:*

```
    First analysis of Coordinated Multi-Stream Attack (CMSA)
```

#### Acknowledgments Type - URLs

List of URLs (`urls`) of acknowledgment is a container (value type `array`) for `1` or more `string` of type URL that specifies
a list of URLs or location of the reference to be acknowledged.
Any URL of acknowledgment contains the URL or location of the reference to be acknowledged.
Value type is `string` with format URI (`uri`).

#### Acknowledgments Type - Example

*Example 1:*

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

The above SHOULD lead to the following outcome in a human-readable advisory:

> We thank the following parties for their efforts:
>
> * Johann Sebastian Bach, Georg Philipp Telemann, Georg Friedrich Händel from Baroque composers for wonderful music
> * CISA for coordination efforts (see: <https://cisa.gov>)
> * BSI for assistance in coordination
> * Antonio Vivaldi for influencing other composers
