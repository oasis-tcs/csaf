import jsonschema
from jsonschema.validators import Draft202012Validator
from referencing import Registry, Resource
import simplejson as json
import sys

if len(sys.argv) < 3:
  print("<command> <schema.json> <validated.json> [<referenced-schema-01.json> [.. <referenced-schema-n.json>]]")
  sys.exit(1)


json_schema = sys.argv[1]
json_input = sys.argv[2]
json_referenced_schemas = sys.argv[3:]

with open(json_schema, 'r') as f:
    schema_data = f.read()
    schema = json.loads(schema_data)

registry = Registry().with_resource(schema['$id'], Resource.from_contents(schema))

with open(json_input, 'r') as f:
    input_data = f.read()
    input_obj = json.loads(input_data)

if len(json_referenced_schemas) > 0:
    for i in json_referenced_schemas:
        with open(i, 'r') as f:
            current_ref_schema_data = f.read()
            current_ref_schema = json.loads(current_ref_schema_data)
            registry = registry.combine(Registry().with_resource(current_ref_schema['$id'], Resource.from_contents(current_ref_schema)))

validator = Draft202012Validator(schema, registry=registry, format_checker=Draft202012Validator.FORMAT_CHECKER)
validator.validate(input_obj)
