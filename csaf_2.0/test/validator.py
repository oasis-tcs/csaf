import jsonschema
from jsonschema.validators import Draft202012Validator, RefResolver
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

schema_store = {schema['$id']: schema}

with open(json_input, 'r') as f:
    input_data = f.read()
    input_obj = json.loads(input_data)

if len(json_referenced_schemas) > 0:
    for i in json_referenced_schemas:
        with open(i, 'r') as f:
            current_ref_schema_data = f.read()
            current_ref_schema = json.loads(current_ref_schema_data)
            schema_store[current_ref_schema['$id']] = current_ref_schema

resolver = RefResolver.from_schema(schema_store[list(schema_store)[0]], store=schema_store)
validator = Draft202012Validator(schema, resolver, jsonschema.draft202012_format_checker)
validator.validate(input_obj)
