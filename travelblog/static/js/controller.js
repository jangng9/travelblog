uejn
    //Validate Before Register
    //When User Click
    var usernameInput = document.getElementById('rusername');
    usernameInput.onfocus = function(){
        document.getElementById('warningEmail').style.display = "block";
    }
    usernameInput.onblur = function(){
        document.getElementById('warningEmail').style.display = "none";
    }
    var warningEmail = document.getElementById('warningEmail');
    // When the user starts to type something inside the Email field
    var emailPattern = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    usernameInput.onkeyup = function() {
      // Validate length
      if(usernameInput.value.match(emailPattern)) {
        warningEmail.classList.remove("invalid");
        warningEmail.classList.add("valid");
      } else {
        warningEmail.classList.remove("valid");
        warningEmail.classList.add("invalid");
      }
    }

    var nameInput = document.getElementById('rname');
    nameInput.onfocus = function(){
        document.getElementById('warningName_char').style.display = "block";
        document.getElementById('warningName_num').style.display = "block";
    }
    nameInput.onblur = function(){
        document.getElementById('warningName_char').style.display = "none";
        document.getElementById('warningName_num').style.display = "none";
    }

    var warningName_char = document.getElementById('warningName_char');
    var warningName_num = document.getElementById('warningName_num');
    // When the user starts to type something inside the password field
    nameInput.onkeyup = function() {
      // Validate only number and character allowed
      var invalidNamePattern = /[^a-zA-Z0-9]/g;
      if(nameInput.value.match(invalidNamePattern)) {
        warningName_char.classList.remove("valid");
        warningName_char.classList.add("invalid");
      } else {
        warningName_char.classList.remove("invalid");
        warningName_char.classList.add("valid");
      }

      // Validate length
      if(nameInput.value.length >= 4) {
        warningName_num.classList.remove("invalid");
        warningName_num.classList.add("valid");
      } else {
        warningName_num.classList.remove("valid");
        warningName_num.classList.add("invalid");
      }
    }

    var passwordInput = document.getElementById('rpassword');
    passwordInput.onfocus = function(){
        document.getElementById('warningPass').style.display = "block";
    }
    passwordInput.onblur = function(){
        document.getElementById('warningPass').style.display = "none";
    }

    var warningPass = document.getElementById('warningPass');
    // When the user starts to type something inside the password field
    passwordInput.onkeyup = function() {
      // Validate length
      if(passwordInput.value.length >= 6) {
        warningPass.classList.remove("invalid");
        warningPass.classList.add("valid");
      } else {
        warningPass.classList.remove("valid");
        warningPass.classList.add("invalid");
      }
    }

    var conPassInput = document.getElementById('conpassword');
    conPassInput.onfocus = function(){
        document.getElementById('warningConPass').style.display = "block";
    }
    conPassInput.onblur = function(){
        document.getElementById('warningConPass').style.display = "none";
    }
    var warningConPass = document.getElementById('warningConPass');
    conPassInput.onkeyup = function(){
        if(passwordInput.value == conPassInput.value){
        warningConPass.classList.remove("invalid");
        warningConPass.classList.add("valid");
      } else {
        warningConPass.classList.remove("valid");
        warningConPass.classList.add("invalid");
        }
    }

    //Validate Login
    var userInputLogin = document.getElementById('username');
    userInputLogin.onfocus = function(){
        document.getElementById('warningEmail_login').style.display = "block";
    }
    userInputLogin.onblur = function(){
        document.getElementById('warningEmail_login').style.display = "none";
    }
    var warningEmail_login = document.getElementById('warningEmail_login');
    userInputLogin.onkeyup = function(){
        if(userInputLogin.value.match(emailPattern)){
        warningEmail_login.classList.remove("invalid");
        warningEmail_login.classList.add("valid");
      } else {
        warningEmail_login.classList.remove("valid");
        warningEmail_login.classList.add("invalid");
        }
    }

    //hover icon effect

    function hoverlike(element) {
        element.setAttribute('src', '../static/images/home/liked.png');
    }

    function unhoverlike(element) {
        element.setAttribute('src', '../static/images/home/like.png');
    }

    function hoveredit(element) {
        element.setAttribute('src', '../static/images/home/penciled.png');
    }

    function unhoveredit(element) {
        element.setAttribute('src', 'images/home/pencil.png');
    }




