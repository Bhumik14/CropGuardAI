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
