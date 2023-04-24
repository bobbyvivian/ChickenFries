// Team TT :: Brianna Tieu and Vivian Teo
// SoftDev pd8
// K30 -- JS Paint
// 2023-04-25
// --------------------------------------------------

//retrieve node in DOM via ID
var c = document.getElementById("slate");
var makeButton = document.getElementById("buttonToggle");
var wipeButton = document.getElementById("buttonClear");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
    }
}

var drawRect = function(e) {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillRect(mouseX, mouseY, 10, 10)
}

var drawCircle = function(e) {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fill(mouseX, mouseY, 10, 10)
}

var draw = function(e) {
    // toggleMode;
    // if (mode==="rect") {
    //     drawRect;
    // }
    // else {
    //     drawRect;
    // }
    drawRect
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    var canvas = getElementById("slate");
    clearRect(canvas);
}    

c.addEventListener("click", draw) //passes the mouse event as parameter for the function

makeButton.addEventListener("click", wipeCanvas())
