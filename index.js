console.log("Hello World!");
// var i = 0;
//
// while (i <= 20){
//   console.log(i);
//   i += 2
// }

// for (i = 0; i <= 20; i+=2){
//     console.log(i);
// }
//
// for (i = 0; i < 20; i++){
//   if (i%2 == 0){
//     console.log(i);
//   }
// }

// function printNum(){
//   return 22.5;
// }
//
// var num = printNum();
// console.log(num);

// function printNum2(type){
//   if (type == 0){
//     alert("test")
//     return(123)
//   }
//   if (type == 1){
//     alert('hmmm')
//     return(24)
//   }
// }
//
// console.log(printNum2(0))
// console.log(printNum2(1))

var adj = ['brave', 'resilient', 'amazing', 'lovely', 'awesome', 'obsessed with me'];
var p = 0;
var l = document.getElementById('adjective');

document.getElementById('adjective').addEventListener("click",
function adjChange(){
  l.innerHTML = adj[p];
  p ++;
  if (p >= adj.length){
    p = 0;
  }
})

// function zoomin(){
//        var myImg = document.getElementById('pic');
//        var currWidth = myImg.clientWidth;
//        var currHeight = myImg.clientHeight;
//        if (currWidth == 1000){
//          alert("You have reached maximum zoom in")
//        }
//        else{
//          myImg.style.width = (currWidth + 5) + "px";
//          myImg.style.height = (currHeight + 5) + "px";
//        }
//        }

// function zoomout(){
//   var myImg = document.getElementById('pic');
//   var currWidth = myImg.clientWidth;
//   var currHeight = myImg.clientHeight;
//   if (currWidth == 100){
//     alert("You have reached maximum zoom out")
//   }
//   else{
//     myImg.style.width = (currWidth - 5) + "px";
//     myImg.style.height = (currHeight - 5) + "px";
//   }
// }

// document.getElementById('oh').addEventListener("click",
// function () {
//   document.getElementById('oh').style.color = 'blue'
//   // alert("Press 'obsessed with me' to discover more")
// })

document.getElementById('zi').addEventListener("click",
function (){
  var myImg = document.getElementById('pic');
  var currWidth = myImg.clientWidth;
  var currHeight = myImg.clientHeight;
  if (currWidth == 1000){
    alert("You have reached maximum zoom in")
  }
  else{
    myImg.style.width = (currWidth + 5) + "px";
    myImg.style.height = (currHeight + 5) + "px";
  }
})

document.getElementById('zo').addEventListener("click",
function (){
  myImg = document.getElementById('pic');
  var currWidth = myImg.clientWidth;
  var currHeight = myImg.clientHeight;
  if (currWidth == 100){
    alert("You have reached maximum zoom out")
  }
  else{
    myImg.style.width = (currWidth - 5) + "px";
    myImg.style.height = (currHeight - 5) + "px";
  }
})
