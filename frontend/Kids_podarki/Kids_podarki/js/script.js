
var modal = document.getElementById("modal");

var loginButton = document.querySelector(".vhod");

var closeButton = document.getElementsByClassName("close-button")[0];

var tabButtons = document.querySelectorAll(".tab-button");

var loginForm = document.getElementById("login-form");

var registerForm = document.getElementById("register-form");


loginButton.onclick = function(event) {
  event.preventDefault(); 
  modal.style.display = "block";
};


closeButton.onclick = function() {
  modal.style.display = "none";
};


window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};


tabButtons.forEach(function(button) {
  button.addEventListener("click", function() {

    tabButtons.forEach(function(btn) {
      btn.classList.remove("active");
    });


    this.classList.add("active");


    var tab = this.dataset.tab;
    var forms = document.querySelectorAll(".modal-form");
    forms.forEach(function(form) {
      if (form.dataset.tab === tab) {
        form.classList.add("active");
      } else {
        form.classList.remove("active");
      }
    });
  });
});

document.getElementById("sideBarBtn").addEventListener("click", (event) => {
  event.preventDefault(); 
  modal.style.display = "block";
  const sidebar = document.querySelector('.sidebar');
  sidebar.style.display = 'none';
})