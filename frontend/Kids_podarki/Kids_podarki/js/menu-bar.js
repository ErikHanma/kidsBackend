document.querySelector(".catalog").addEventListener("click", () => {
    document.querySelector(".catalog").classList.toggle("active")
})
document.querySelector("body"),addEventListener("click", (e) => {
    if (e.target !== document.querySelector(".catalog")) {
        document.querySelector(".catalog").classList.remove("active")
    }

})

// window.addEventListener('DOMContentLoaded', function() {
//     const urlParams = new URLSearchParams(window.location.search);
//     const filterValue = urlParams.get('filter');

//     if (filterValue) {
//         const filterElements = document.querySelectorAll(`[data-filter=".${filterValue}"]`);
//         filterElements.forEach(function(element) {
//             element.click();
//         });
//     }
// });