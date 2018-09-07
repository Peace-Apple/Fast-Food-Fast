function editFood(){
    alert("You have clicked a food item for editing!");

}
function deleteFood(){
    alert("You have deleted a food item!");

}
/*function to verify user or admin*/
function Verify(){
    var username = document.querySelector("#username").value;
    var password = document.querySelector("#password").value;
    if(username==='apple' && password ==="apple"){
       window.location.href ="home.html";
    }else if(username==='admin' && password ==="admin"){
      var username = document.querySelector("#username").value;
      var password = document.querySelector("#password").value;
      window.location.href ="addfood.html";
  
    }else{
    }
  }
  