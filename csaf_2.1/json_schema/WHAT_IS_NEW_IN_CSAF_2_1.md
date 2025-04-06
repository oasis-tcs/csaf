# What's New in CSAF 2.1
The following is a quick reference of the changes between the CSAF 2.0 and CSAF 2.1 JSON schemas. 

##  Document-Level Enhancements

- **Distribution Object:**
  - **Required Property:**  
    • In CSAF 2.1, the `"distribution"` property is now mandatory (it appears in the list of required properties in the `"document"` object).  
    • In CSAF 2.0, `"distribution"` was optional.
    
  - **New Sharing Group:**  
    • CSAF 2.1 introduces an optional `"sharing_group"` within `"distribution"`. This sub-object requires an `"id"` and may include a human‐readable `"name"`.  
    • This sharing group was not defined in CSAF 2.0.
    
  - **Traffic Light Protocol (TLP) Labels:**  
    • In CSAF 2.1, the TLP `"label"` enumeration has been revised to include: `"AMBER"`, `"AMBER+STRICT"`, `"CLEAR"`, `"GREEN"`, and `"RED"`.  
    • In CSAF 2.0, the allowed values were `"AMBER"`, `"GREEN"`, `"RED"`, and `"WHITE"`.  
    • This change reflects an update in how document sharing sensitivity is expressed.

- **Publisher Object:**
  - **Additional Category Value:**  
    • In CSAF 2.1 the `"publisher"` object’s `"category"` enumeration has been expanded to include `"multiplier"`, alongside the previous values such as `"coordinator"`, `"discoverer"`, `"other"`, `"translator"`, `"user"`, and `"vendor"`.  
    • This new category is not available in CSAF 2.0.
    

---

## Product Identification Enhancements

- **Full Product Name – Product Identification Helper:**
  - **Package URL Field:**
    - **CSAF 2.1:**  
      • The field has been renamed from `"purl"` to `"purls"` and its type changed from a single string to an array of strings. This enables listing multiple package URLs for a product.  
      • The array requires at least one entry and enforces uniqueness.
      
    - **CSAF 2.0:**  
      • A singular `"purl"` field (a string) was used for representing the package URL.
      
---

## Vulnerability Representation Changes

- **Weakness Enumeration:**
  - **CSAF 2.1:**  
    • The vulnerability object now uses the property `"cwes"` (plural) instead of a singular `"cwe"`.  
    • It is defined as an array where each CWE object must include the fields `"id"`, `"name"`, and an additional `"version"` field.  
    • This allows multiple weaknesses to be listed and adds specificity with versioning.
    
  - **CSAF 2.0:**  
    • Vulnerabilities were represented with a single `"cwe"` object (not an array) and required only `"id"` and `"name"`.
    
- **Date Field for Vulnerability Disclosure:**
  - **CSAF 2.1:**  
    • Uses `"disclosure_date"` to indicate when the vulnerability was disclosed to the public.  
    • Also includes `"discovery_date"` to indicate when the vulnerability was initially discovered.
    
  - **CSAF 2.0:**  
    • Uses `"release_date"` (for when the vulnerability was released into the wild) instead of `"disclosure_date"`.
    
- **Metrics vs. Scores:**
  - **CSAF 2.1:**  
    • Replaces the `"scores"` property with `"metrics"`.  
    • Each metric item now contains a `"content"` object that can reference multiple scoring systems including:
      - CVSS v2 and v3 (with support for both CVSS v3.0 and v3.1)
      - **Newly added:** CVSS v4 and SSVC v1  
    • The metric item also includes `"products"` and an optional `"source"`.
    
  - **CSAF 2.0:**  
    • Used a `"scores"` array where each score item primarily referenced `"cvss_v2"` and `"cvss_v3"` alongside the list of `"products"`.
    
- **Remediation Enhancements:**
  - **CSAF 2.1:**  
    • In the `"remediations"` property, the `"category"` enumeration has been expanded to include new values:
      - `"fix_planned"`
      - `"optional_patch"`
    - The other values such as `"mitigation"`, `"no_fix_planned"`, `"none_available"`, and `"vendor_fix"` remain.
    
  - **CSAF 2.0:**  
    • The enumeration for remediation categories was limited to `"mitigation"`, `"no_fix_planned"`, `"none_available"`, `"vendor_fix"`, and `"workaround"`.

    
