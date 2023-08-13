# 8 Safety, Security, and Data Protection Considerations

CSAF documents are based on JSON, thus the security considerations of [RFC8259] apply and are repeated here as service for the reader:
>Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
>Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).  This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.  The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to that language's syntax.

In addition, CSAF documents may be rendered by consumers in various human-readable formats like HTML or PDF.
Thus, for security reasons, CSAF producers and consumers SHALL adhere to the following:

* CSAF producers SHOULD NOT emit messages that contain HTML, even though all variants of Markdown permit it. To include HTML, source code, or any other content that may be interpreted or executed by a CSAF consumer, e.g. to provide a proof-of-concept, the issuing party SHALL use Markdown's fenced code blocks or inline code option.
* Deeply nested markup can cause a stack overflow in the Markdown processor [GFMENG]. To reduce this risk, CSAF consumers SHALL use a Markdown processor that is hardened against such attacks.
  **Note**: One example is the GitHub fork of the `cmark` Markdown processor [GFMCMARK].
* To reduce the risk posed by possibly malicious CSAF files that do contain arbitrary HTML (including, for example, javascript: links), CSAF consumers SHALL either disable HTML processing (for example, by using an option such as the --safe option in the cmark Markdown processor) or run the resulting HTML through an HTML sanitizer.
CSAF consumers that are not prepared to deal with the security implications of formatted messages SHALL NOT attempt to render them and SHALL instead fall back to the corresponding plain text messages. As also any other programming code can be contained within a CSAF document, CSAF consumers SHALL ensure that none of the values of a CSAF document is run as code. Moreover, it SHALL be treated as unsafe (user) input.
  > Additional, supporting mitigation measures like retrieving only CSAF documents from trusted sources and check their integrity and signature before parsing the document SHOULD be in place to reduce the risk further.

-------
