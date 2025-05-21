import decimal
import jsonschema
from jsonschema.validators import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
import simplejson as json
import sys

# As documented in https://referencing.readthedocs.io/en/stable/api/#referencing.Specification:
# A specification defines the referencing behavior.
# As we use the referencing from Draft 2020-12, it seem save enough to specify that explicitly
# as the library does not support custom dialects (yet).
# This was extracted as a function as we need that in several places.
def create_resource_with_specification(schema):
    resource = None
    try:
        # First try to use the initially specified schema
        resource = Resource.from_contents(schema)
    except:
        # If that fails, explicitly use Draft 2020-12
        resource = Resource(schema, DRAFT202012)
    return resource
   

if len(sys.argv) < 3:
    print("<command> <schema.json> <validated.json> [<referenced-schema-01.json> [.. <referenced-schema-n.json>]]")
    sys.exit(1)


json_schema = sys.argv[1]
json_input = sys.argv[2]
json_referenced_schemas = sys.argv[3:]

# Load the schema
with open(json_schema, 'r') as f:
    schema_data = f.read()
    schema = json.loads(schema_data, parse_float=decimal.Decimal)

resource = create_resource_with_specification(schema)
registry = Registry().with_resource(resource.id(), resource)

# Load any referenced schema
if len(json_referenced_schemas) > 0:
    for i in json_referenced_schemas:
        with open(i, 'r') as f:
            current_ref_schema_data = f.read()
            current_ref_schema = json.loads(current_ref_schema_data, parse_float=decimal.Decimal)
            current_resource = create_resource_with_specification(current_ref_schema)
            registry = registry.combine(Registry().with_resource(current_resource.id().split('?')[0], current_resource))

registry = registry.crawl()

# Load the JSON to validate
with open(json_input, 'r') as f:
    input_data = f.read()
    input_obj = json.loads(input_data, parse_float=decimal.Decimal)

# Even though the meta schema should enforce the validation, we need to set the validator here 
# due to the missing support for custom dialects
# Nevertheless, this implementation will check correctly whether the format is valid
validator = Draft202012Validator(schema, registry=registry, format_checker=Draft202012Validator.FORMAT_CHECKER)
validator.validate(input_obj)
