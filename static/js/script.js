var navLinks = document.getElementById("navLinks");

      function showMenu() {
        navLinks.style.right = "0px";
      }

      function hideMenu() {
        navLinks.style.right = "-200px";
      }

      document.addEventListener("DOMContentLoaded", () => {
        const faqs = document.querySelectorAll(".faq");

        faqs.forEach((faq) => {
          const question = faq.querySelector(".question");

          question.addEventListener("click", () => {
            // Close other open FAQs
            faqs.forEach((item) => {
              if (item !== faq && item.classList.contains("active")) {
                item.classList.remove("active");
              }
            });

            // Toggle current FAQ
            faq.classList.toggle("active");
          });
        });
      });

      document.getElementById("openChatbotBtn").onclick = function() {
    document.getElementById("chatbotContainer").style.display = "block";
};

document.getElementById("closeChatbotBtn").onclick = function() {
    document.getElementById("chatbotContainer").style.display = "none";
};

document.getElementById("sendBtn").onclick = function() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() !== "") {
        let chatHistory = document.getElementById("chatHistory");
        let userMessage = document.createElement("p");
        userMessage.textContent = "You: " + userInput;
        chatHistory.appendChild(userMessage);
        chatHistory.scrollTop = chatHistory.scrollHeight;
        
        // Simulate a chatbot response (you'll replace this with your ML model integration)
        let botMessage = document.createElement("p");
        botMessage.textContent = "Bot: This is a sample response.";
        chatHistory.appendChild(botMessage);
        chatHistory.scrollTop = chatHistory.scrollHeight;

        document.getElementById("userInput").value = "";
    }
};

// Close the popup if the user clicks outside of it
window.onclick = function(event) {
    if (event.target == document.getElementById("chatbotContainer")) {
        document.getElementById("chatbotContainer").style.display = "none";
    }
};

const apiKey = "8805259a09763c59b9addbf0a5b031ba";
      const apiUrl =
        "https://api.openweathermap.org/data/2.5/weather?&units=metric&q=";

        const searchBox = document.querySelector(".search input");
        const searchBtn = document.querySelector(".search button");
        const weatherIcon = document.querySelector(".weather-icon");
        
      async function checkWeather(city) {
        const response = await fetch(apiUrl + city + `&appid=${apiKey}`);

        if(response.status == 404){
            document.querySelector(".error").style.display = "block";
            document.querySelector(".weather").style.display = "none";
        }else{
            var data = await response.json();

        console.log(data);

        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°c";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + " km/h";

        if(data.weather[0].main == "Clouds"){
            weatherIcon.src = "images/clouds.png";
        }else if(data.weather[0].main == "Clear"){
            weatherIcon.src = "images/clear.png";
        }else if(data.weather[0].main == "Rain"){
            weatherIcon.src = "images/rain.png";
        }else if(data.weather[0].main == "Drizzle"){
            weatherIcon.src = "images/drizzle.png";
        }else if(data.weather[0].main == "Mist"){
            weatherIcon.src = "images/mist.png";
        }     
        document.querySelector(".error").style.display = "none";
        }
      }
      searchBtn.addEventListener("click", () => {
             checkWeather(searchBox.value); // Pass the city name to the checkWeather function
      });


   