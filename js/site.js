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
  if (location == "" || location == null || location == undefined){
    alert("Please enter a location");
    return;
  }
  else{
    fetch(`https://austinmarquis30.pythonanywhere.com/app1/weather_scraper?location=${encodeURIComponent(location)}`)
    .then(response => {
      if (!response.ok) {
        alert("Please enter a valid location");
        return
      }
      return response.text();
    })
    .then(data => {
      $('#weatherResults').html(data);
    })
  }

}

function validatePassword() {
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('confirmPassword').value;
  var confirmPasswordMessage = document.getElementById('confirmPasswordMessage');

  if (password === confirmPassword) {
      confirmPasswordMessage.style.color = 'green';
      confirmPasswordMessage.textContent = 'Passwords match.';
  } else {
    confirmPasswordMessage.style.color = 'red';
    confirmPasswordMessage.textContent = 'Passwords do not match.';
  }
}

function GetRecognizer(location) {
  if (location == "" || location == null || location == undefined){
    alert("Please enter a location");
    return;
  }
  else{
    fetch(`https://austinmarquis30.pythonanywhere.com/app1/weather_scraper?location=${encodeURIComponent(location)}`)
    .then(response => {
      if (!response.ok) {
        alert("Please enter a valid location");
        return
      }
      return response.text();
    })
    .then(data => {
      $('#weatherResults').html(data);
    })
  }
}

function GetRecognizer() {
  var fileInput = document.getElementById('customPicture');
  var file = fileInput.files[0];
  var formData = new FormData();

  formData.append('image', file);

  fetch(`https://austinmarquis30.pythonanywhere.com/app4/image_recognition`, {
      method: 'POST',
      body: formData
  })
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    console.log(data); // Print the response data to the console
    var predictedLabel = data.predicted_label;
    predictedLabel = predictedLabel.slice(0, -1);
      $('#recognitionResults').html(predictedLabel);
})
.catch(error => {
    console.error('There was a problem with the fetch operation:', error);
});
}