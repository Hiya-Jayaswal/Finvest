const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle");
      sidebar = body.querySelector("nav");
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if(getMode && getMode ==="dark"){
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if(getStatus && getStatus ==="close"){
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () =>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        localStorage.setItem("mode", "dark");
    }else{
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if(sidebar.classList.contains("close")){
        localStorage.setItem("status", "close");
    }else{
        localStorage.setItem("status", "open");
    }
})



    const xhr = new XMLHttpRequest();
    console.log(12)
    xhr.open("POST", "http://localhost:8000/api/information?question=Hello");
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    xhr.onload = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            displayResponse(xhr.responseText);
        } else {
            console.log(`Error: ${xhr.status}`);
        }
    };
    
    xhr.send(body);


    // const req = new XMLHttpRequest();
    // req.addEventListener("load", reqListener);
    // req.open("GET", "https://finance.yahoo.com/quote/AAPL/history");
    // req.send();
    // console.log(req.responseText())


    function reqListener () {
        console.log(this.responseText);
    }
    var oReq = new XMLHttpRequest();
    oReq.onload = reqListener;
    oReq.open("post", "http://localhost:8000/api/information?question=Hello");
    oReq.send();
    console.log(oReq.responseText())
    document.addEventListener('DOMContentLoaded', function () {
        const toggleSwitch = document.querySelector('.mode-toggle');
    
        function switchTheme(e) {
            if (e.target.checked) {
                document.body.classList.add('dark');
            } else {
                document.body.classList.remove('dark');
            }
        }
    
        toggleSwitch.addEventListener('change', switchTheme, false);
    });
    document.addEventListener("DOMContentLoaded", function () {
        const items = document.querySelectorAll(".accordion-item");
      
        items.forEach((item) => {
          item.addEventListener("click", function () {
            if (!this.classList.contains("active")) {
              closeAllAccordions();
              this.classList.add("active");
            }
          });
        });
      
        // Open the first accordion item on load
        items[0].classList.add("active");
      });
      
      function closeAllAccordions() {
        const items = document.querySelectorAll(".accordion-item");
        items.forEach((item) => {
          item.classList.remove("active");
        });
      }
      