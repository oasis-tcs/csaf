# Registry for Vulnerability ID Systems for CSAF (RVISC)

This document explains the Registry for Vulnerability ID Systems for CSAF (RVISC).

## Overview

The RVISC is the registry used to identify registered vulnerability id systems.
It also states their naming constraints.
See also section [3.2.4.8 of the CSAF 2.1 specification](https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html#vulnerabilities-property---ids).
The RVISC consists of two parts:

1. [Registry](https://registry.csaf.dev/id/registry/)
   The registry contains all currently registered Vulnerability ID Systems.
   The data recorded includes amongst other things:

   - `common_name`: Contains a human-readable short name for the system.
   - `system_name`: Indicates the registered URL of the vulnerability tracking or numbering system.
     This value is used in CSAF as `system_name`.
     See also test [6.3.20](https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html#use-of-unregistered-id-system).
   - `text_pattern`: Contains an anchored JSON pattern that can be used to validate the identifiers.
     This value is used in CSAF to check whether the ID provided matches the constraints given by the entry in the registry.
     See also test [6.2.53](https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html#matching-text-for-registered-id-system).

2. [Mapping](https://registry.csaf.dev/id/mapping/)
   The mapping tries to support the conversion of values observed in the wild to existing registered RVISC entries.
   There are two kind of mappings - differentiate by the value of `ambiguous`. Mapping with `ambiguous` set to

   - `true` identify mappings where the old system name is being using for multiple different vulnerability ID systems.
     Such entries cannot be mapped automatically and need human interaction.
   - `false` identify values that can be mapped automatically.

Both parts are JSON files - there respective JSON schemas are linked in the `$schema` value.

## Mapping

During a mapping, the tool iterates over the items in `$.vulnerabilities[*].ids[*]` of an existing CSAF.
For each entry, the mapping follows these steps:

1. The tool takes the current `system_name` and searches for an exact match in `$.entries[*].old_system_name`
   of the mapping file.
   If no such entry exists, the mapping fails.
2. If such entry exists, the tool checks which `pattern_precondition` matches on the current value of `text`.
   If no such entry exists, the mapping fails.
3. If such entry exists, the tool executes the steps described in `rule`.
   If the tool does not implement that rule, the mapping fails.

If the tool ends up with multiple candidates of possible mappings to execute in step 3, the tool MAY provide an option for the user
to select the correct one.
The tool SHALL NOT select a mapping without further information.
If the mapping failed, the user SHALL be informed about the reason why the mapping failed.

## Registration

To register an ID system in RVISC, open an issue with necessary information at the OASIS Open CSAF TC repo.
The reporter MUST be the owner or a representative of the system and provide sufficient proof for that.
In special circumstances, a OASIS CSAF TC member MAY act as reporter or/and change controller.
The editors or TC members appointed to coordinate RVISC check the basic information and provide first feedback.
Then, the TC discusses the suggested entry and any mappings provided during a regular TC meeting.
Upon request of a TC member, the TC does a vote whether the ID system is going to be accepted into RVISC.
OASIS voting rules apply.
If the TC decides to accept the ID system into RVISC, the editors or TC members appointed to coordinate RVISC
will work with the change controller to facilitate that.
Pull Requests against the OASIS Open TC repo can only be provided by TC members - other PRs have to be closed for compliance reasons.

## Changes

Changes against the mapping file do not need a vote in the TC, if all following conditions apply:

- the changes are suggested by the change controller,
- approved by the editors,
- sufficient real world examples exist and are provided, that this mapping is useful and reasonable, and
- there is no evidence that the mapping rule would have a negative impact on other RVISC entries.

If these conditions are not met, the process for the registration of ID systems applies.
