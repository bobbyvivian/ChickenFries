// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // e.stopPropagation();
  //A: It'll stop the next pop-ups in the query (only one pop-up will pop up)
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)
//A: 3rd parameter (bool arg) makes this the only pop-up in the query. Omitting 3rd parameter defaults to false

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// A: Pop-ups appear in the order of children first-->goes up the branches of heredity
