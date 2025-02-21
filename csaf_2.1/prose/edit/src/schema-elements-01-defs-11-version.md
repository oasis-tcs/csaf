### Version Type

The Version (`version_t`) type has value type `string` with `pattern` (regular expression):

```
    ^(0|[1-9][0-9]*)$|^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The version specifies a version string to denote clearly the evolution of the content of the document.
There are two options how it can be used:

* semantic versioning (preferred; according to the rules below)
* integer versioning

A CSAF document MUST use only one versioning system.

*Examples 1:*

```
    1
    4
    0.9.0
    1.4.3
    2.40.0+21AF26D3
```

#### Version Type - Integer versioning

Integer versioning increments for each version where the `/document/tracking/status` is `final` the version number by one.
The regular expression for this type is:

```
^(0|[1-9][0-9]*)$
```

The following rules apply:

1. Once a versioned document has been released, the contents of that version MUST NOT be modified.
   Any modifications MUST be released as a new version.
2. Version zero (0) is for initial development before the `initial_release_date`.
   The document status MUST be `draft`. Anything MAY change at any time. The document SHOULD NOT be considered stable.
3. Version 1 defines the initial release to the intended target group.
   Each new version where `/document/tracking/status` is `final` has a version number incremented by one.
4. Pre-release versions (document status `draft`) MUST carry the new version number.
   Sole exception is before the initial release (see rule 2).
   The combination of document status `draft` and version 1 MAY be used to indicate that the content is unlikely to change.
5. Build metadata is never included in the version.
6. Precedence MUST be determined by integer comparison.

#### Version Type - Semantic versioning

Semantic versioning derived the rules from [SemVer]. The regular expression for this type is:

```
^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The goal of this structure is to provide additional information to the end user whether a new comparison with the asset database is needed.
The "public API" in regards to CSAF is the CSAF document with its structure and content.
This results in the following rules:

1. A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes.
   X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically.
   For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
2. Once a versioned document has been released, the contents of that version MUST NOT be modified.
   Any modifications MUST be released as a new version.
3. Major version zero (0.y.z) is for initial development before the `initial_release_date`.
   The document status MUST be `draft`. Anything MAY change at any time.
   The document SHOULD NOT be considered stable. Changes which would increment the major version according to rule 7 are
   tracked in this stage with (0.y.z) by incrementing the minor version y instead.
   Changes that would increment the minor or patch version according to rule 6 or 5 are both tracked in this stage with
   (0.y.z) by incrementing the patch version z instead.
4. Version 1.0.0 defines the initial release to the intended target group.
   The way in which the version number is incremented after this release is dependent on the content and structure of
   the document and how it changes.
5. Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced.
   A bug fix is defined as an internal change that fixes incorrect behavior.

   > In the context of the document this is the case e.g. for spelling mistakes.

6. Minor version Y (x.Y.z | x > 0) MUST be incremented if the content of an existing element changes except for
   those which are covert through rule 7. It MUST be incremented if substantial new information are introduced or new elements are provided.
   It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.
7. Major version X (X.y.z | X > 0) MUST be incremented if a new comparison with the end user's asset database is required.
   This includes:

   * changes (adding, removing elements or modifying content) in `/product_tree` or elements which contain `/product_tree` in their path
   * adding or removing items of `/vulnerabilities`
   * adding or removing elements in:
     * `/vulnerabilities[]/product_status/first_affected`
     * `/vulnerabilities[]/product_status/known_affected`
     * `/vulnerabilities[]/product_status/last_affected`
   * removing elements from:
     * `/vulnerabilities[]/product_status/first_fixed`
     * `/vulnerabilities[]/product_status/fixed`
     * `/vulnerabilities[]/product_status/known_not_affected`

   It MAY also include minor and patch level changes.
   Patch and minor version MUST be reset to 0 when major version is incremented.
8. A pre-release version (document status `draft`) MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately
   following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-].
   Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes.
   Pre-release versions have a lower precedence than the associated normal version.
   A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as
   denoted by its associated normal version.

   *Examples 1:*

   ```
   1.0.0-0.3.7
   1.0.0-alpha
   1.0.0-alpha.1
   1.0.0-x-y-z.--
   1.0.0-x.7.z.92
   ```

9. Pre-release MUST NOT be included if `/document/tracking/status` is `final`.
10. Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following
    the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-].
    Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence.
    Thus two versions that differ only in the build metadata, have the same precedence.

    *Examples 2:*

    ```
    1.0.0+20130313144700
    1.0.0+21AF26D3----117B344092BD
    1.0.0-alpha+001
    1.0.0-beta+exp.sha.5114f85
    ```

11. Precedence refers to how versions are compared to each other when ordered.

    1. Precedence MUST be calculated by separating the version into major, minor,
       patch and pre-release identifiers in that order (Build metadata does not figure into precedence).
    2. Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows:
       Major, minor, and patch versions are always compared numerically.

       *Example 3:*

       ```
       1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
       ```

    3. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:

       *Example 4:*

       ```
       1.0.0-alpha < 1.0.0
       ```

    4. Precedence for two pre-release versions with the same major, minor,
       and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:

       1. Identifiers consisting of only digits are compared numerically.
       2. Identifiers with letters or hyphens are compared lexically in ASCII sort order.
       3. Numeric identifiers always have lower precedence than non-numeric identifiers.
       4. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.

       *Example 5:*

       ```
       1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0
       ```

Note, that the following values do no conform the semantic versioning described above.

*Examples 6 (which are invalid):*

```
  1.16.13.14-Cor
  1.0.0-x-y-z.–
  1.0.0+21AF26D3—-117B344092BD
  2.5.20+3f93da6b+7cc
  3.20.0-00
```
