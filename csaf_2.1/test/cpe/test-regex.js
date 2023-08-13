const { exit } = require('process')
const fs = require('fs')

const args = process.argv.slice(2);
const obj = JSON.parse(fs.readFileSync(args[0], 'utf8'))

const pattern = obj.$defs.full_product_name_t.properties.product_identification_helper.properties.cpe.pattern
const r = new RegExp(pattern)

console.log('Current regex to test:', '\n', pattern)

const cpeStr = fs.readFileSync(args[1], 'utf8').split('\n')

let failed = false

cpeStr.forEach(element => {
    if (element.length > 0) {
        const result = (r.exec(element) != null)
        failed = failed | !result
        if (!result) {
            console.log(result, '\t', element)
        }
    }
});

exit(failed)
