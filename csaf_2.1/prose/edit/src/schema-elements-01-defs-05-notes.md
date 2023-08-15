### Notes Type

List of notes (`notes_t`) of value type `array` with 1 or more items of type `Note` contains notes which are specific to the current context.

```
    "notes_t": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Note item is `object` with the mandatory properties `category` and `text` providing a place to put
all manner of text blobs related to the current context.
A Note `object` MAY provide the optional properties `audience` and `title`.

```
    "properties": {
      "audience": {
        // ...
      },
      "category": {
        // ...
      },
      "text": {
        // ...
      },
      "title": {
        // ...
      }
    }
```

Audience of note (`audience`) of value type `string` with 1 or more characters indicates who is intended to read it.

*Examples 19:*

```
    all
    executives
    operational management and system administrators
    safety engineers
```

Note category (`category`) of value type `string` and `enum` contains the information of what kind of note this is.
Valid `enum` values are:

```
    description
    details
    faq
    general
    legal_disclaimer
    other
    summary
```

The value `description` indicates the note is a description of something.
The optional sibling property `title` MAY have more information in this case.

The value `details` indicates the note is a low-level detailed discussion.
The optional sibling property `title` MAY have more information in this case.

The value `faq` indicates the note is a list of frequently asked questions.

The value `general` indicates the note is a general, high-level note.
The optional sibling property `title` MAY have more information in this case.

The value `legal_disclaimer` indicates the note represents any possible legal discussion, including constraints, surrounding the document.

The value `other` indicates the note is something that doesn’t fit the other categories.
The optional sibling attribute `title` SHOULD have more information to indicate clearly what kind of note to expect in this case.

The value `summary` indicates the note is a summary of something.
The optional sibling property `title` MAY have more information in this case.

Note content (`text`) of value type `string` with 1 or more characters holds the content of the note.
Content varies depending on type.

Title of note (`title`) of value type `string` with 1 or more characters provides a concise description of what
is contained in the text of the note.

*Examples 20:*

```
    Details
    Executive summary
    Technical summary
    Impact on safety systems
```
