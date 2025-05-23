## Roles

This subsection groups the requirements from the previous subsection into named sets which target the roles with the same name.
This allows end users to request their suppliers to fulfill a certain set of requirements.
A supplier can use roles for advertising and marketing.

The roles "CSAF publisher", "CSAF provider", and "CSAF trusted provider" are intended directly for issuing parties and form the first group.
The second group consists of the roles "CSAF lister" and "CSAF aggregator".
They collect data from the aforementioned issuing parties of the first group and provide them in a single place to aid in automation.
Parties of the second group can also issue their own advisories.
However, they MUST follow the rules for the first group for that.

Both, a CSAF lister and a CSAF aggregator, decide based on their own rules which issuing parties to list respectively to mirror.
However, an issuing party MAY apply to be listed or mirrored.

Issuing parties MUST indicate through the value `false` in `list_on_CSAF_aggregators` if they do not want to be listed.
Issuing parties MUST indicate through the value `false` in `mirror_on_CSAF_aggregators` if they do not want to be mirrored.

The values are independent.
The combination of the value `false` in `list_on_CSAF_aggregators` and `true` in `mirror_on_CSAF_aggregators` implies that
the issuing party does not want to be listed without having the CSAF documents mirrored.
Therefore, a CSAF aggregator can list that issuing party if it mirrors the files.

### Role: CSAF publisher

A distributing party satisfies the "CSAF publisher" role if the party:

* satisfies the requirements 1 to 4 in section [sec](#requirements).
* distributes only CSAF documents on behalf of its own.

### Role: CSAF provider

A CSAF publisher satisfies the "CSAF provider" role if the party fulfills the following three groups of requirements:

Firstly, the party:

* satisfies the "CSAF publisher" role profile.
* additionally satisfies the requirements 5 to 7, 24 and 25 in section [sec](#requirements).

Secondly, the party:

* satisfies at least one of the requirements 8 to 10 in section [sec](#requirements).

Thirdly, the party:

* satisfies the requirements 11 to 14 in section [sec](#requirements) or requirements 15 to 17 in section [sec](#requirements).

> If the party uses the ROLIE-based distribution, it MUST also satisfy requirements 15 to 17.
> If it uses the directory-based distribution, it MUST also satisfy requirements 11 to 14.

### Role: CSAF trusted provider

A CSAF provider satisfies the "CSAF trusted provider" role if the party:

* satisfies the "CSAF provider" role profile.
* additionally satisfies the requirements 18 to 20 in section [sec](#requirements).

### Role: CSAF lister

A distributing party satisfies the "CSAF lister" role if the party:

* satisfies the requirements 6, 21, 22, 24 and 25 in section [sec](#requirements).
* uses the value `lister` for `/aggregator/category`.
* does not list any mirror pointing to a domain under its own control.

> The purpose of this role is to provide a list of URLs where to find CSAF documents.
> It is not assumed that the list will be complete.

### Role: CSAF aggregator

A distributing party satisfies the "CSAF aggregator" role if the party:

* satisfies the requirements 1 to 6 and 21 to 25 in section [sec](#requirements).
* uses the value `aggregator` for `/aggregator/category`.
* lists a mirror for at least two disjoint issuing parties pointing to a domain under its own control.
* links the public part of the OpenPGP key used to sign CSAF documents for each mirrored issuing party in
  the corresponding `provider-metadata.json`.
* provides for each CSAF document that is mirrored a signature (requirement 19) and a hash (requirement 18).
  Both SHALL be listed in the ROLIE feed. If the issuing party provides those files for a CSAF document, they SHOULD be copied as well.
  If the issuing party does not provide those files, they SHALL be created by the CSAF aggregator.
  Such a signature does not imply any liability of CSAF aggregator for the content of the corresponding CSAF document.
  It just confirms that the CSAF document provided has not been modified after being downloaded from the issuing party.
  A CSAF aggregator MAY add additional signatures and hashes for a CSAF document.

Additionally, a CSAF aggregator MAY list one or more issuing parties that it does not mirror.

> The purpose of this role is to provide a single point where CSAF documents can be retrieved.
> Multiple CSAF aggregators are expected to exist around the world. None of them is required to mirror all CSAF documents of all issuing parties.
> CSAF aggregators can be provided for free or as a paid service.
>
> To aid in automation, CSAF aggregators MAY mirror CSAF documents from CSAF publishers.
> Regarding the terms of use they SHOULD consult with the issuing party.
> The purpose of this option is that a consumer can retrieve CSAF documents from a CSAF publisher as if this issuing party would be a
> CSAF trusted provider. To reach that goal, a CSAF aggregator collects the CSAF documents from the CSAF publisher and mirrors it.
> The collection process MAY be automated or manual. CSAF aggregators announce the collection interval through the field `update_interval` in
> the corresponding item of the CSAF publishers list (`csaf_publishers`) in their `aggregator.json`.
> To minimize the implementation efforts and process overhead, a CSAF aggregator MAY upload the CSAF documents of a CSAF publisher into
> an internal instance of a CSAF provider software.
> Such construct is called "CSAF proxy provider" as it can be mirrored by the CSAF aggregator software.
> However, such a CSAF proxy provider MUST NOT be accessible from anyone else than the CSAF aggregator itself.
> Otherwise, that would violate the second rule of section [sec](#role-csaf-publisher).
> Therefore, it is recommended to expose the CSAF proxy provider only on localhost and allow the access only from the CSAF aggregator software.
