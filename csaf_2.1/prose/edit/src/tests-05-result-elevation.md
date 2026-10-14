## Test Result Elevation

Test result elevation allows to modify the test result of one or more test or preset.
The following options are defined:

- `warning-as-error`: updates warnings to errors for all test results it is applied to
- `info-as-warning`: updates information to warnings for all test results it is applied to
- `info-as-error`: updates information to errors for all test results it is applied to
- `as-level-up`: updates warnings to errors and information to warnings (in this order) for all test results it is applied to
- `all-as-error`: updates warnings to errors and information to errors for all test results it is applied to

CSAF validators SHOULD implement the options in a way that if no additional parameters are given they apply to all executed tests.
If parameters are provided, the test result elevation applies only to the tests specified in the parameters.
CSAF validators SHALL determine the overall validation status after the test result elevation.

> For example, a CSAF document failing test [sec](unused-definition-of-product-id) would be valid without test result elevation.
> If the CSAF validator is instructed to use the test result elevation `warning-as-error`,
> the CSAF validator determines that the same CSAF document is invalid as the warning resulting from the failing test
> [sec](unused-definition-of-product-id) is reported as error and therefore changes the overall result.
> These options help issuing parties to ensure data quality within their CSAF documents as they can be used in automated checks,
> e.g. CI/CD pipelines.
