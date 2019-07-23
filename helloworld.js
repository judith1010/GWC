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
