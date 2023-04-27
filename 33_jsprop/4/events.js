// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //e.stopPropagation();
  //A: It'll stop the next pop-ups in the query (only one pop-up will pop up)
};


//Q: Does the order in which the event listeners are attached matter?
//A: Order does not matter; in the order of children hierarchy

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
//A: Since the order of pop-ups follow the heredity order (children first), then if all args are true, the youngest will be the only one popping up
// Setting bool arg true only works if you are the 

for (var x=0; x < tds.length; x++) {
  // tds[x].addEventListener('click', clicky, true);
  tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  // trs[x].addEventListener('click', clicky, false);
}

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

//table: 
// A: Always prioritizes true, and if the arg is true, then it follows the events that are true in the order of highest parent first,
// and if it's false then it follows the regular order of the lowest/youngest child first