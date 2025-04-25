# What's New in CSAF 2.1

The following is a quick reference of the changes between the CSAF 2.0 and CSAF 2.1 JSON schemas (including the main CSAF 2.1 JSON schema and the `provider_metadata.json` schema). 

----

##  CSAF JSON Schema Enhancements

### Document-Level Enhancements

- **Distribution Object:**
  - **Required Property:**  
    - In CSAF 2.1, the `"distribution"` property is now mandatory (it appears in the list of required properties in the `"document"` object).  
    - In CSAF 2.0, `"distribution"` was optional.
    
  - **New Sharing Group:**  
    - CSAF 2.1 introduces an optional `"sharing_group"` within `"distribution"`. This sub-object requires an `"id"` and may include a human-readable `"name"`.  
    - This sharing group was not defined in CSAF 2.0.
    
  - **Traffic Light Protocol (TLP) Labels:**  
    - In CSAF 2.1, the TLP `"label"` enumeration has been revised to include: `"AMBER"`, `"AMBER+STRICT"`, `"CLEAR"`, `"GREEN"`, and `"RED"`.  
    - In CSAF 2.0, the allowed values were `"AMBER"`, `"GREEN"`, `"RED"`, and `"WHITE"`.  
    - This change reflects an update in how document sharing sensitivity is expressed.

- **Publisher Object:**
  - **Additional Category Value:**  
    - In CSAF 2.1 the `"publisher"` object’s `"category"` enumeration has been expanded to include `"multiplier"`, alongside the previous values such as `"coordinator"`, `"discoverer"`, `"other"`, `"translator"`, `"user"`, and `"vendor"`.  
    - This new category is not available in CSAF 2.0.

---

### Product Identification Enhancements

- **Full Product Name – Product Identification Helper:**
  - **Package URL Field:**
    - **CSAF 2.1:**  
      - The field has been renamed from `"purl"` to `"purls"` and its type changed from a single string to an array of strings. This enables listing multiple package URLs for a product.  
      - The array requires at least one entry and enforces uniqueness.
      
    - **CSAF 2.0:**  
      - A singular `"purl"` field (a string) was used for representing the package URL.
      
---

### Vulnerability Representation Changes

- **Weakness Enumeration:**
  - **CSAF 2.1:**  
    - The vulnerability object now uses the property `"cwes"` (plural) instead of a singular `"cwe"`.  
    - It is defined as an array where each CWE object must include the fields `"id"`, `"name"`, and an additional `"version"` field.  
    - This allows multiple weaknesses to be listed and adds specificity with versioning.
    
  - **CSAF 2.0:**  
    - Vulnerabilities were represented with a single `"cwe"` object (not an array) and required only `"id"` and `"name"`.
    
- **Date Field for Vulnerability Disclosure:**
  - **CSAF 2.1:**  
    - Uses `"disclosure_date"` to indicate when the vulnerability was disclosed to the public.  
    - Also includes `"discovery_date"` to indicate when the vulnerability was initially discovered.
    
  - **CSAF 2.0:**  
    - Uses `"release_date"` (for when the vulnerability was released into the wild) instead of `"disclosure_date"`.
    
- **Metrics vs. Scores:**
  - **CSAF 2.1:**  
    - Replaces the `"scores"` property with `"metrics"`.  
    - Each metric item now contains a `"content"` object that can reference multiple scoring systems including:
      - CVSS v2 and v3 (with support for both CVSS v3.0 and v3.1)
      - **Newly added:** CVSS v4 and SSVC v1  
    - The metric item also includes `"products"` and an optional `"source"`.
    
  - **CSAF 2.0:**  
    - Used a `"scores"` array where each score item primarily referenced `"cvss_v2"` and `"cvss_v3"` alongside the list of `"products"`.
    
- **Remediation Enhancements:**
  - **CSAF 2.1:**  
    - In the `"remediations"` property, the `"category"` enumeration has been expanded to include new values:
      - `"fix_planned"`
      - `"optional_patch"`
    - The other values such as `"mitigation"`, `"no_fix_planned"`, `"none_available"`, and `"vendor_fix"` remain.
    
  - **CSAF 2.0:**  
    - The enumeration for remediation categories was limited to `"mitigation"`, `"no_fix_planned"`, `"none_available"`, `"vendor_fix"`, and `"workaround"`.

----

## Provider Metadata JSON Schema

Below is a comparison between the CSAF provider metadata schemas for version CSAF 2.1 and CSAF 2.0.

### Schema Identity and Required Properties

Of course, updating the new 2.1 version references.

- **Schema Declaration:**
  - **CSAF Provider 2.1:**  
    - Declares a `$schema` property and uses an `$id` pointing to the v2.1 URL.  
    - The required list explicitly includes `"$schema"`.
  
  - **CSAF Provider 2.0:**  
    - Uses an `$id` pointing to the v2.0 URL, but the `$schema` property is not required.
    - The property `"metadata_version"` is fixed to `"2.0"`.

## Distributions Structure

- **Directory-Based Distribution:**
  - **CSAF Provider 2.1:**  
    - The distribution mechanism for directory-based distribution is encapsulated as an object under the property `"directory"`.  
    - This object requires:
      - `"tlp_label"` – its value is obtained via a reference to the CSAF 2.1 document’s TLP label definition (which, in CSAF 2.1, typically uses values such as `"AMBER"`, `"AMBER+STRICT"`, `"CLEAR"`, `"GREEN"`, and `"RED"`).  
      - `"url"` – the base URL for the directory.

  - **CSAF Provider 2.0:**  
    - Uses a simpler approach where the directory distribution is provided as a single property named `"directory_url"` that directly holds the URL.

- **ROLIE Distribution:**
  - **Structure of ROLIE Feeds:**
    - **In 2.1:**  
      - The `"rolie"` object requires a `"feeds"` array where each feed object must include `"last_updated"`, `"tlp_label"`, and `"url"`.  
      - The `"tlp_label"` is referenced from the CSAF 2.1 document schema – this means its allowed values follow the updated standard (e.g. it no longer uses the literal `"WHITE"` but uses `"CLEAR"` instead).

    - **In 2.0:**  
      - The corresponding `"rolie"` object in v2.0 requires `"feeds"` where each feed object requires `"tlp_label"` and `"url"` (note the absence of a `"last_updated"` requirement).  
      - The enumeration for `"tlp_label"` in v2.0 is hardcoded to values such as `"UNLABELED"`, `"WHITE"`, `"GREEN"`, `"AMBER"`, and `"RED"`.

- **Services:**  
  - Both versions include a `"services"` array under the `"rolie"` distribution for listing service document URLs, and the definitions are similar.

---

## Public OpenPGP Keys

- **Key Requirements:**
  - **CSAF Provider 2.1:**  
    - The `"public_openpgp_keys"` array requires each key object to include both `"fingerprint"` and `"url"`.  
    - The `"fingerprint"` must meet a minimum length and a pattern (hexadecimal, at least 40 characters).
    
  - **CSAF Provider 2.0:**  
    - The similar array requires only the `"url"` property (with `"fingerprint"` being optional if present).

---

## 5. Publisher and Role References

- **Publisher Property:**
  - Both schemas use a reference to the corresponding `"publisher"` property from the CSAF document schema.  
  - In v2.1, it points to the v2.1 document schema’s publisher definition, while in v2.0 it points to the v2.0 version.
  
- **Role Property:**
  - Both versions define the `"role"` property with the same default (`"csaf_provider"`) and enumeration values (`"csaf_publisher"`, `"csaf_provider"`, `"csaf_trusted_provider"`).
