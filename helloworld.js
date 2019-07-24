console.log("Judith");

// var h1tag = document.getElementsByTagName('h1')[0];
//
// var cn = document.getElementsByClassName('headings')

var adj = ['brave', 'resilient', 'amazing', 'lovely', 'awesome', 'obsessed with me'];
var p = 0;
var l = document.getElementById('adjective');

function adjChange(){
  l.innerHTML = adj[p];
  p ++;
  if (p >= adj.length){
    p = 0;
  }
}

var fonts = ["'Hanalei', cursive", "'Oswald', sans-serif", "'Butcherman', cursive"]
var f = document.getElementById('rand font')
var pos = 0
function fontChange(){
  // f.setAttribute("style", `font-family: ${fonts[pos]}`);
  f.style.fontFamily = fonts[pos]
  pos ++;
  if (pos >= fonts.length){
    pos = 0;
  }
}
