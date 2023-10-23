# CSAF and Content Delivery Networks (CDNs)

If you want to use a CDN to provide your CSAF files, please find some remarks below:

- **Activate caching**: Most files are more or less static - activate caching to minimize risk for (D)DoS.
- **Include path exemption**: The path `.well-known/csaf/` and potentially `.well-known/security.txt` need to be accessible for all HTTP-clients (also those that are usually detected as bots).

  *Specifically, at least the files in this path ending on `.json`, `.asc`, `.sha256` and `sha512` should be excluded.*
- **Flush cache when updating files**: When new files are written or old files updated, the cache must be updated. Usually, this can be done through the API the CDN provides. Instead of flushing the whole cache (easy way), a more precise way can be used as files that need to be updated in the cache depend on the distribution method:

  **Directory-based distribution:**

  ```
  <path-to-updated-CSAF-document>.json
  <path-to-updated-CSAF-document>.json.asc
  <path-to-updated-CSAF-document>.json.sha256
  <path-to-updated-CSAF-document>.json.sha512
  <path-of-index>.txt
  <path-of-changes>.csv
  ```

  *Example:*

  The CSAF advisory `ESA-2023-31816` was changed. Consequently, the following files in the cache need to be updated.

  ```
  .well-known/csaf/white/2023/esa-2023-31816.json
  .well-known/csaf/white/2023/esa-2023-31816.json.asc
  .well-known/csaf/white/2023/esa-2023-31816.json.sha256
  .well-known/csaf/white/2023/esa-2023-31816.json.sha512
  .well-known/csaf/white/index.txt
  .well-known/csaf/white/changes.csv
  ```

  **ROLIE-based distribution:**

  ```
  <path-to-updated-CSAF-document>.json
  <path-to-updated-CSAF-document>.json.asc
  <path-to-updated-CSAF-document>.json.sha256
  <path-to-updated-CSAF-document>.json.sha512
  <path-of-ROLIE-feed>.json
  <path-of-ROLIE-categories>.json
  <path-of-ROLIE-services>.json
  ```

  *Example:*

  The CSAF advisory `ESA-2023-31816` was changed. Consequently, the following files in the cache need to be updated.

  ```
  .well-known/csaf/white/2023/esa-2023-31816.json
  .well-known/csaf/white/2023/esa-2023-31816.json.asc
  .well-known/csaf/white/2023/esa-2023-31816.json.sha256
  .well-known/csaf/white/2023/esa-2023-31816.json.sha512
  .well-known/csaf/white/csaf-feed-tlp-white.json
  .well-known/csaf/white/csaf-categories-tlp-white.json
  .well-known/csaf/service.json
  ```
