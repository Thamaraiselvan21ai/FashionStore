var username = document.getElementById("username");
var password =  document.getElementById("password");
var button = document.querySelector(".login-button");

function checkvalidity(){
        if(username.value == "" || password.value ==""){
            alert("Please provide Username & Password ")
        }
    
}

btn.addEventListener("click", checkvalidity)