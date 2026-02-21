<!--
---
toc:
  auto: false
  label: Guidance on the Size of CSAF Documents
  enumerate: Appendix C.
  children:
  - label: File Size
    enumerate: C.1
  - label: Array Length
    enumerate: C.2
  - label: String Length
    enumerate: C.3
  - label: Date
    enumerate: C.4
  - label: Enum
    enumerate: C.5
  - label: URI Length
    enumerate: C.6
  - label: UUID Length
    enumerate: C.7
---
-->
# Guidance on the Size of CSAF Documents

This appendix provides informative guidance on the size of CSAF documents.

The TC carefully considered all known aspects to provide size limits for CSAF documents for this version of the specification with
the result that hard limits SHOULD NOT be enforced.
However, since there is the need for guidance to ensure interoperability in the ecosystem, the TC provides a set of soft limits.
A CSAF document which exceeds those, can still be valid but it might not be processable for some parties.

All _CSAF consumers_ SHOULD be able to process CSAF documents which comply with the limits below.
All _CSAF producers_ SHOULD NOT produce CSAF documents which exceed those limits.

> If you come across a case where these limits are exceeded, please provide feedback to the TC.

## File Size

A CSAF document in the specified JSON format encoded in UTF-8 SHOULD conform to known size limits of current technologies parsing JSON content,
e.g.: 150 MiB.

> The CSAF documents observed in the wild expose strongly varying sizes as per the use cases they serve.
> At least one database technology in wide use for storing CSAF documents rejects insert attempts when
> the transformed BSON size exceeds 16 megabytes.
> The BSON format optimizes for accessibility and not size.
> So, small integers and small strings may incur more overhead in the BSON format than in JSON.
> In addition, the BSON format adds length information for the entries inside the document,
> which adds to the size when storing CSAF document content in a BSON format.

## Array Length

An array SHOULD NOT have more than:

* 10 000 items for
  * `/document/acknowledgments`
  * `/document/acknowledgments[]/names`
  * `/document/acknowledgments[]/urls`
  * `/document/tracking/aliases`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/purls`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris`
  * `/product_tree/branches[]/product/product_identification_helper/hashes`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/branches[]/product/product_identification_helper/purls`
  * `/product_tree/branches[]/product/product_identification_helper/sbom_urls`
  * `/product_tree/branches[]/product/product_identification_helper/x_generic_uris`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/full_product_names[]/product_identification_helper/purls`
  * `/product_tree/full_product_names[]/product_identification_helper/sbom_urls`
  * `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/purls`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris`
  * `/vulnerabilities[]/acknowledgments`
  * `/vulnerabilities[]/acknowledgments[]/names`
  * `/vulnerabilities[]/acknowledgments[]/urls`
  * `/vulnerabilities[]/cwes`
  * `/vulnerabilities[]/ids`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/decision_point_resources`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/values`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/target_ids`
  * `/vulnerabilities[]/remediations[]/entitlements`

* 40 000 items for
  * `/document/notes`
  * `/document/references`
  * `/vulnerabilities[]/involvements`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/references`
  * `/vulnerabilities[]/notes`
  * `/vulnerabilities[]/references`

* 100 000 for
  * `/document/tracking/revision_history`
  * `/product_tree/branches`
  * `/product_tree(/branches[])*/branches`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/model_numbers`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/serial_numbers`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/skus`
  * `/product_tree/branches[]/product/product_identification_helper/model_numbers`
  * `/product_tree/branches[]/product/product_identification_helper/serial_numbers`
  * `/product_tree/branches[]/product/product_identification_helper/skus`
  * `/product_tree/full_product_names`
  * `/product_tree/full_product_names[]/product_identification_helper/model_numbers`
  * `/product_tree/full_product_names[]/product_identification_helper/serial_numbers`
  * `/product_tree/full_product_names[]/product_identification_helper/skus`
  * `/product_tree/product_groups[]/product_ids`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/model_numbers`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/serial_numbers`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/skus`
  * `/vulnerabilities`

* 10 000 000 for
  * `/product_tree/product_groups`
  * `/product_tree/relationships`
  * `/vulnerabilities[]/remediations[]/group_ids`

* 100 000 000 for
  * `/document/notes[]/group_ids`
  * `/document/notes[]/product_ids`
  * `/vulnerabilities[]/first_known_exploitation_dates`
  * `/vulnerabilities[]/first_known_exploitation_dates[]/group_ids`
  * `/vulnerabilities[]/first_known_exploitation_dates[]/product_ids`
  * `/vulnerabilities[]/flags`
  * `/vulnerabilities[]/flags[]/group_ids`
  * `/vulnerabilities[]/flags[]/product_ids`
  * `/vulnerabilities[]/involvements[]/group_ids`
  * `/vulnerabilities[]/involvements[]/product_ids`
  * `/vulnerabilities[]/metrics`
  * `/vulnerabilities[]/metrics[]/products`
  * `/vulnerabilities[]/notes[]/group_ids`
  * `/vulnerabilities[]/notes[]/product_ids`
  * `/vulnerabilities[]/product_status/first_affected`
  * `/vulnerabilities[]/product_status/first_fixed`
  * `/vulnerabilities[]/product_status/fixed`
  * `/vulnerabilities[]/product_status/known_affected`
  * `/vulnerabilities[]/product_status/known_not_affected`
  * `/vulnerabilities[]/product_status/last_affected`
  * `/vulnerabilities[]/product_status/recommended`
  * `/vulnerabilities[]/product_status/under_investigation`
  * `/vulnerabilities[]/product_status/unknown`
  * `/vulnerabilities[]/remediations`
  * `/vulnerabilities[]/remediations[]/product_ids`
  * `/vulnerabilities[]/threats`
  * `/vulnerabilities[]/threats[]/group_ids`
  * `/vulnerabilities[]/threats[]/product_ids`

## String Length

A string SHOULD NOT have a length greater than:

* 1000 for
  * `/document/acknowledgments[]/names[]`
  * `/document/acknowledgments[]/organization`
  * `/document/aggregate_severity/text`
  * `/document/category`
  * `/document/distribution/sharing_group/name`
  * `/document/lang`
  * `/document/license_expression`
  * `/document/notes[]/audience`
  * `/document/notes[]/group_ids[]`
  * `/document/notes[]/product_ids[]`
  * `/document/notes[]/title`
  * `/document/publisher/name`
  * `/document/source_lang`
  * `/document/title`
  * `/document/tracking/aliases[]`
  * `/document/tracking/generator/engine/name`
  * `/document/tracking/generator/engine/version`
  * `/document/tracking/id`
  * `/document/tracking/revision_history[]/legacy_version`
  * `/document/tracking/revision_history[]/number`
  * `/document/tracking/version`
  * `/product_tree/branches[](/branches[])*/name`
  * `/product_tree/branches[](/branches[])*/product/name`
  * `/product_tree/branches[](/branches[])*/product/product_id`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/filename`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/model_numbers[]`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/serial_numbers[]`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/skus[]`
  * `/product_tree/branches[]/name`
  * `/product_tree/branches[]/product/name`
  * `/product_tree/branches[]/product/product_id`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/filename`
  * `/product_tree/branches[]/product/product_identification_helper/model_numbers[]`
  * `/product_tree/branches[]/product/product_identification_helper/serial_numbers[]`
  * `/product_tree/branches[]/product/product_identification_helper/skus[]`
  * `/product_tree/full_product_names[]/name`
  * `/product_tree/full_product_names[]/product_id`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/filename`
  * `/product_tree/full_product_names[]/product_identification_helper/model_numbers[]`
  * `/product_tree/full_product_names[]/product_identification_helper/serial_numbers[]`
  * `/product_tree/full_product_names[]/product_identification_helper/skus[]`
  * `/product_tree/product_groups[]/group_id`
  * `/product_tree/product_groups[]/product_ids[]`
  * `/product_tree/relationships[]/full_product_name/name`
  * `/product_tree/relationships[]/full_product_name/product_id`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/filename`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/model_numbers[]`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/serial_numbers[]`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/skus[]`
  * `/product_tree/relationships[]/product_reference`
  * `/product_tree/relationships[]/relates_to_product_reference`
  * `/vulnerabilities[]/acknowledgments[]/names[]`
  * `/vulnerabilities[]/acknowledgments[]/organization`
  * `/vulnerabilities[]/cve`
  * `/vulnerabilities[]/cwes[]/id`
  * `/vulnerabilities[]/cwes[]/name`
  * `/vulnerabilities[]/cwes[]/version`
  * `/vulnerabilities[]/flags[]/group_ids[]`
  * `/vulnerabilities[]/flags[]/product_ids[]`
  * `/vulnerabilities[]/first_known_exploitation_dates[]/group_ids[]`
  * `/vulnerabilities[]/ids[]/system_name`
  * `/vulnerabilities[]/ids[]/text`
  * `/vulnerabilities[]/involvements[]/contact`
  * `/vulnerabilities[]/involvements[]/group_ids[]`
  * `/vulnerabilities[]/metrics[]/content/cvss_v2/vectorString`
  * `/vulnerabilities[]/metrics[]/content/cvss_v3/vectorString`
  * `/vulnerabilities[]/metrics[]/content/cvss_v4/vectorString`
  * `/vulnerabilities[]/metrics[]/content/epss/percentile`
  * `/vulnerabilities[]/metrics[]/content/epss/probability`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/key`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/namespace`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/values[]/key`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/values[]/name`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/version`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/target_ids[]`
  * `/vulnerabilities[]/metrics[]/products[]`
  * `/vulnerabilities[]/notes[]/audience`
  * `/vulnerabilities[]/notes[]/group_ids[]`
  * `/vulnerabilities[]/notes[]/product_ids[]`
  * `/vulnerabilities[]/notes[]/title`
  * `/vulnerabilities[]/product_status/first_affected[]`
  * `/vulnerabilities[]/product_status/first_fixed[]`
  * `/vulnerabilities[]/product_status/fixed[]`
  * `/vulnerabilities[]/product_status/known_affected[]`
  * `/vulnerabilities[]/product_status/known_not_affected[]`
  * `/vulnerabilities[]/product_status/last_affected[]`
  * `/vulnerabilities[]/product_status/recommended[]`
  * `/vulnerabilities[]/product_status/under_investigation[]`
  * `/vulnerabilities[]/product_status/unknown[]`
  * `/vulnerabilities[]/remediations[]/group_ids[]`
  * `/vulnerabilities[]/remediations[]/product_ids[]`
  * `/vulnerabilities[]/threats[]/group_ids[]`
  * `/vulnerabilities[]/threats[]/product_ids[]`
  * `/vulnerabilities[]/title`

* 10 000 for
  * `/document/acknowledgments[]/summary`
  * `/document/distribution/text`
  * `/document/publisher/contact_details`
  * `/document/publisher/issuing_authority`
  * `/document/references[]/summary`
  * `/document/tracking/revision_history[]/summary`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/cpe`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/purls[]`
  * `/product_tree/branches[]/product/product_identification_helper/cpe`
  * `/product_tree/branches[]/product/product_identification_helper/purls[]`
  * `/product_tree/full_product_names[]/product_identification_helper/cpe`
  * `/product_tree/full_product_names[]/product_identification_helper/purls[]`
  * `/product_tree/product_groups[]/summary`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/cpe`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/purls[]`
  * `/vulnerabilities[]/acknowledgments[]/summary`
  * `/vulnerabilities[]/involvements[]/summary`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/decision_point_resources[]/summary`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/references[]/summary`
  * `/vulnerabilities[]/references[]/summary`
  * `/vulnerabilities[]/remediations[]/entitlements[]`

* 30 000 for
  * `/document/notes[]/text`
  * `/vulnerabilities[]/notes[]/text`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/description`
  * `/vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/values[]/description`

* 250 000 for
  * `/vulnerabilities[]/remediations[]/details`
  * `/vulnerabilities[]/remediations[]/restart_required/details`
  * `/vulnerabilities[]/threats[]/details`

## Date

The maximum length of strings representing a temporal value is given by the format specifier. This applies to:

* `/document/tracking/current_release_date`
* `/document/tracking/generator/date`
* `/document/tracking/initial_release_date`
* `/document/tracking/revision_history[]/date`
* `/vulnerabilities[]/disclosure_date`
* `/vulnerabilities[]/discovery_date`
* `/vulnerabilities[]/first_known_exploitation_dates[]/date`
* `/vulnerabilities[]/first_known_exploitation_dates[]/exploitation_date`
* `/vulnerabilities[]/flags[]/date`
* `/vulnerabilities[]/involvements[]/date`
* `/vulnerabilities[]/metrics[]/content/epss/timestamp`
* `/vulnerabilities[]/metrics[]/content/ssvc_v2/timestamp`
* `/vulnerabilities[]/remediations[]/date`
* `/vulnerabilities[]/threats[]/date`

## Enum

A string which is an enum has a fixed maximum length given by its longest value.

> Later versions of CSAF might add, modify or delete possible value which could change the longest value.
> Therefore, this sizes should not be implemented as fixed limits if forward compatibility is desired.

The value of `/$schema` is a fixed URL, currently pointing to the JSON schema location.
It seems to be safe to assume that the length of this value is not greater than 150. This applies to:

* `/$schema` (59)

For all other values, it seems to be safe to assume that the length of each value is not greater than 50.
This applies to:

* `/document/csaf_version` (3)
* `/document/distribution/tlp/label` (12)
* `/document/notes[]/category` (16)
* `/document/publisher/category` (11)
* `/document/references[]/category` (8)
* `/document/tracking/status` (7)
* `/product_tree/branches[](/branches[])*/category` (15)
* `/product_tree/branches[]/category` (15)
* `/product_tree/relationships[]/category` (21)
* `/vulnerabilities[]/flags[]/label` (49)
* `/vulnerabilities[]/involvements[]/party` (11)
* `/vulnerabilities[]/involvements[]/status` (17)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/accessComplexity` (6)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/accessVector` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/authentication` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/availabilityImpact` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/availabilityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/collateralDamagePotential` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/confidentialityImpact` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/confidentialityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/exploitability` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/integrityImpact` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/integrityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/remediationLevel` (13)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/reportConfidence` (14)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/targetDistribution` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v2/version` (3)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/attackComplexity` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/attackVector` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/availabilityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/availabilityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/baseSeverity` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/confidentialityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/confidentialityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/environmentalSeverity` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/exploitCodeMaturity` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/integrityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/integrityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedAttackComplexity` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedAttackVector` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedAvailabilityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedConfidentialityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedIntegrityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedPrivilegesRequired` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedScope` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/modifiedUserInteraction` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/privilegesRequired` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/remediationLevel` (13)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/reportConfidence` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/scope` (9)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/temporalSeverity` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/userInteraction` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v3/version` (3)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/attackComplexity` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/attackRequirements` (7)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/attackVector` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/Automatable` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/availabilityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/baseSeverity` (8)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/confidentialityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/exploitMaturity` (16)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/integrityRequirement` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedAttackComplexity` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedAttackRequirements` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedAttackVector` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedPrivilegesRequired` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedSubAvailabilityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedSubConfidentialityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedSubIntegrityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedUserInteraction` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedVulnAvailabilityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedVulnConfidentialityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/modifiedVulnIntegrityImpact` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/privilegesRequired` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/providerUrgency` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/Recovery` (13)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/Safety` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/subAvailabilityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/subConfidentialityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/subIntegrityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/userInteraction` (7)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/valueDensity` (12)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/version` (3)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/vulnAvailabilityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/vulnConfidentialityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/vulnerabilityResponseEffort` (11)
* `/vulnerabilities[]/metrics[]/content/cvss_v4/vulnIntegrityImpact` (4)
* `/vulnerabilities[]/metrics[]/content/qualitative_severity_rating` (8)
* `/vulnerabilities[]/metrics[]/content/ssvc_v2/schemaVersion` (5)
* `/vulnerabilities[]/notes[]/category` (16)
* `/vulnerabilities[]/references[]/category` (8)
* `/vulnerabilities[]/remediations[]/category` (14)
* `/vulnerabilities[]/remediations[]/restart_required/category` (20)
* `/vulnerabilities[]/threats[]/category` (14)

## URI Length

A string with format `uri` SHOULD NOT have a length greater than 20000. This applies to:

* `/document/acknowledgments[]/urls[]`
* `/document/aggregate_severity/namespace`
* `/document/distribution/tlp/url`
* `/document/publisher/namespace`
* `/document/references[]/url`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls[]`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/branches[]/product/product_identification_helper/sbom_urls[]`
* `/product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/full_product_names[]/product_identification_helper/sbom_urls[]`
* `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls[]`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/uri`
* `/vulnerabilities[]/acknowledgments[]/urls[]`
* `/vulnerabilities[]/metrics[]/content/ssvc_v2/decision_point_resources[]/uri`
* `/vulnerabilities[]/metrics[]/content/ssvc_v2/references[]/uri`
* `/vulnerabilities[]/metrics[]/source`
* `/vulnerabilities[]/references[]/url`
* `/vulnerabilities[]/remediations[]/url`

## UUID Length

A string with format `uuid` SHOULD NOT have a length greater than 50. This applies to:

* `/document/distribution/sharing_group/id` (36)
