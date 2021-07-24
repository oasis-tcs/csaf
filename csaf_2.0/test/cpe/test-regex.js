const { exit } = require('process')
var fs = require('fs')

var args = process.argv.slice(2);
var obj = JSON.parse(fs.readFileSync(args[0], 'utf8'))

var pattern = obj.$defs.full_product_name_t.properties.product_identification_helper.properties.cpe.pattern
var r = new RegExp(pattern)

console.log('Current regex to test:', '\n', pattern)

var cpeStr = fs.readFileSync(args[1], 'utf8').split('\n')

var failed = false

cpeStr.forEach(element => {
    if (element.length > 0) {
        var result = (r.exec(element) != null)
        failed = failed | !result
        if (!result) {
            console.log(result, '\t', element)
        } 
    }
});

exit(failed)