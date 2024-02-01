document.addEventListener('mousemove', e => {
  document.body.style.setProperty('--x', `${e.pageX}px`);
  document.body.style.setProperty('--y', `${e.pageY}px`);
});

const sections = document.querySelectorAll("section[id]");

window.addEventListener("scroll", navHighlighter);

function navHighlighter() {
  let scrollY = window.pageYOffset;
  
  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 50;
    sectionId = current.getAttribute("id");
    
    if (
      scrollY > sectionTop &&
      scrollY <= sectionTop + sectionHeight
    ){
      document.querySelector(".navigation a[href*=" + sectionId + "]").classList.add("active");
    } else {
      document.querySelector(".navigation a[href*=" + sectionId + "]").classList.remove("active");
    }
  });
}

function GetWeather(location) {
  fetch(`http://austinmarquis30.pythonanywhere.com/weather_scraper?location=${encodeURIComponent(location)}`)
      .then(response => response.text())
      .then(data => {
        $('#weatherResults').append(data);
      });
}