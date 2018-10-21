'use strict';

let NUTRIENT_FACTS = ['Calories	Protein (g)',	'Fat (g)',	'Carbohydrates (g)',	'Sugar (g)',	'Sodium (mg)',	'Cholesterol (mg)',	'Saturated Fat (g)',	'Net Carbohydrates'];
let TABLE_HEADER = ['Fact', 'Value'];

// adds a table of the nutrition facts to the DOM
// TBD food String , facts JSON/array
function renderTable(food, facts) {
  // get the divs to render elements for
  let foodHeading = document.getElementById('foodHeading');
  let factsTableDiv = document.getElementById('factsTable');
  // create the new elements
  let foodH2 = document.createElement('h2');
  foodH2.text = 'Nutrition facts for ' + food;
  let factsTable = document.createElement('table'); 
  // add caption to the table and append it to the table
  let caption = document.createElement('caption');
  caption.text = 'Table of the nutrition facts for ' + food;
  factsTable.appendChild(caption);
  // add the rows to the table
  factsTable.appendChild(renderTableHeader(TABLE_HEADER));  // table header
  for(let fact of facts) {
    factsTable.appendChild(renderTableRow(fact));
  }
  // add the new elements to the DOM
  foodHeading.appendChild(foodH2);
  factsTableDiv.appendChild(factsTable);
}

// returns the row with all the column names
function renderTableHeader(data) {
  let thead = document.createElement('thead');
  let row = document.createElement('tr');   // creates the table row
  for(let item of data) {
    row.appendChild(renderRowColumn(item, 'th'));
  }
  thead.appendChild(row);
  return thead;
}

// returns a row element for a table
// TBD data = array/object, tag = "th" or "td"
function renderTableRow(data) {
  let row = document.createElement('tr');   // creates the table row
  row.appendChild(renderRowColumn(item, 'th'));
  row.appendChild(renderRowColumn(item, 'td'));
  return row;
}

// returns a data cell of the specified tag for a row
function renderRowColumn(data, tag) {
  let col = document.createElement(tag);
  col.text = data;
}
