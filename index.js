let Mustache = require('mustache');
let csv = require('fast-csv');
let _ = require('lodash');

const input_file = "tnpedia-2016.csv";
const output_file = "output.md";
const template_file = "MainTemplate.mustache";

const required_fields = [
                          'company',
                          'placement_day',
                          'source_info'
                        ];

const optional_fields = [
                          'parting_advice'
                        ];

let input_data = [ ];

csv.fromPath(input_file, { headers: true })
  .on("data", (data) => {

    if (_.every(required_fields, (value) => !_.isEmpty(data[value]))) {
      input_data.push(data);
    }
  })
  .on("end", () => {
    let fs = require('fs');
    fs.readFile(template_file, (err, data) => {
      let template = data.toString();
      fs.writeFile(output_file, Mustache.render(template, { items: input_data }), (err) => {
        if (err) {
          console.log("ERROR while templating using Mustache:");
          console.error(err);
          process.exit(1);
        } else {
          process.exit(0);
        }
      });
    });
  });
