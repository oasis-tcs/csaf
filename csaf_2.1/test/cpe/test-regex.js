const { exit } = require('process')
const fs = require('fs')

const args = process.argv.slice(2);
const obj = JSON.parse(fs.readFileSync(args[0], 'utf8'))

const pattern = obj.$defs.full_product_name_t.properties.product_identification_helper.properties.cpe.pattern
const r = new RegExp(pattern)

console.log('Current regex to test:', '\n', pattern)

const cpeStr = fs.readFileSync(args[1], 'utf8').split('\n')
const assertion = !((args[2] ?? true) === "false")

let failed = false

cpeStr.forEach(element => {
    if (element.length > 0) {
        const result = (r.exec(element) != null)
        failed = failed | (result !== assertion)
        if (result !== assertion) {
            console.log(result,'but expected', assertion, '\t', element)
        }
    }
});

exit(failed)
