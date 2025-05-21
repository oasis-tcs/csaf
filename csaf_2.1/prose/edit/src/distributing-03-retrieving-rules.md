## Retrieving rules

The retrieving process executes in two phases: Finding the `provider-metadata.json` (requirement 7 in section [sec](#requirements)) and
retrieving CSAF documents.

> A retrieving party SHOULD do the first phase every time.
> Based on the setup and use case of the retrieving party it MAY choose to do it less often,
> e.g. only when adding new or updating distributing parties.
> In that case, it SHOULD to check regularly whether new information is available.

### Finding provider-metadata.json

**Direct locating**: The following process SHOULD be used to determine the location of a `provider-metadata.json`
(requirement 7 in section [sec](#requirements)) based on the main domain of the issuing party:

1. Checking the Well-known URL (requirement 9 in section [sec](#requirements))
2. Checking the security.txt (requirement 8 in section [sec](#requirements))
3. Checking the DNS path (requirement 10 in section [sec](#requirements))
4. Select one or more `provider-metadata.json` to use.

> The term "checking" used in the listing above SHOULD be understood as follows:
> Try to access the resource and test whether the response provides an expected result as defined in the requirement in section 7.1.
> If that is the case, the step was successful - otherwise not.

The first two steps SHOULD be performed in all cases as the security.txt MAY advertise additional `provider-metadata.json`.
The third step SHOULD only be performed if the first two did not result in the location of at least one `provider-metadata.json`.

**Indirect locating**: A retrieving party MAY choose to determine the location of a `provider-metadata.json` by retrieving
its location from an `aggregator.json` (requirement 21 in section [sec](#requirements)) of a CSAF lister or CSAF aggregator.

### Retrieving CSAF documents

Given a `provider-metadata.json`, the following process SHOULD be used to retrieve CSAF documents:

1. Parse the `provider-metadata.json` to determine whether the directory-based (requirements 11 to 14 in section [sec](#requirements))
   or ROLIE-based distribution (requirements 15 to 17 in section [sec](#requirements)) is used.
   If both are present, the ROLIE information SHOULD be preferred.
2. For any CSAF trusted provider, the hash and signature files (requirements 18 to 19 in section [sec](#requirements)) SHOULD be retrieved together
   with the CSAF document.
   They MUST be checked before further processing the CSAF document.
3. Test the CSAF document against the schema.
4. Execute mandatory tests on the CSAF document.

-------
