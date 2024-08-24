import streamlit as st
import tensorflow as tf
import numpy as np

# Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64)) #loading image in tf format to 64x64 size    
    input_arr = tf.keras.preprocessing.image.img_to_array(image) #converting image to array
    input_arr = np.array([input_arr]) #this will turn array to a batch as we inputted model with batches
    prediction = model.predict(input_arr) #It will return prob of each class
    result_index = np.argmax(prediction)
    return result_index

# Sidebar
st.sidebar.header("Step into the future of agriculture—where every leaf tells a story.🍃✨")
st.sidebar.title("Dashboard")
st.sidebar.write("Explore our other tabs here..") 
app_mode = st.sidebar.selectbox("Switch To Another Tab",["Home","About","Disease Prediction"])
st.sidebar.image("img123.jpg", caption="Solving Farmers Issues")
st.sidebar.image("img125.jpg", caption="Predicting various Diseases")

# 3rd page
if(app_mode=="Disease Prediction"):
    st.header("Plant Disease Prediction System")
    image_path = "img123.jpg"
    st.image(image_path,use_column_width=True)
    st.header(" Welcome to the Plant Disease Prediction System! 🌿🔍")
    st.markdown("""
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Prediction** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Prediction** page in the sidebar to upload an image and experience the power of our Plant Disease Prediction System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page. 

  """)
    
#About Project
elif(app_mode=="About"):
    st.header("About")
    st.video("vid1.mp4", start_time=12, loop=True, autoplay=True, muted=True)
    st.header("🌱 Our Commitment to Agricultural Innovation 🌾")
    st.markdown("""
                🌱 About Us: Our Commitment to Agricultural Innovation 🌾
👥 Who We Are
We are a team of passionate engineers, data scientists, and agricultural experts dedicated to transforming the way plant diseases are detected and managed. With a strong background in artificial intelligence, machine learning, and agronomy, we’ve come together to create a solution that addresses one of the most pressing challenges in agriculture: early and accurate disease detection in crops.

🌍 Our Vision
Our vision is to revolutionize the agricultural sector by providing innovative tools that empower farmers to protect their crops and increase yields. We believe that technology can play a crucial role in ensuring food security, reducing crop losses, and promoting sustainable farming practices. By making advanced technology accessible to everyone, we aim to contribute to a world where healthy crops and abundant harvests are the norm.

🎯 Our Mission
Our mission is to deliver a powerful yet easy-to-use plant disease prediction system that leverages the latest advancements in artificial intelligence. We strive to help farmers and agriculturists identify plant diseases early, take timely action, and ultimately improve the quality and quantity of their harvests. We are committed to continuous improvement, constantly refining our algorithms and expanding our dataset to cover a wider range of crops and diseases.

🔍 The Problem We Address
Plant diseases are a significant threat to global agriculture, leading to substantial economic losses and food scarcity. Early detection and treatment are critical, but traditional methods of identifying plant diseases can be time-consuming, expensive, and often inaccurate. Farmers need a reliable, efficient, and cost-effective solution that can help them safeguard their crops against disease outbreaks.

💡 Our Solution
To address this challenge, we have developed a cutting-edge plant disease prediction system that utilizes machine learning algorithms trained on extensive datasets. Our system can analyze images of plants and accurately identify diseases, providing users with detailed information and actionable recommendations. This technology empowers farmers to make informed decisions quickly, preventing the spread of disease and minimizing crop losses.

🚀 Why We Stand Out
🔬 Advanced Technology: Our platform uses state-of-the-art AI models, ensuring high accuracy and reliability in disease detection.
📚 Comprehensive Dataset: We continuously expand our dataset to include a wide variety of crops and diseases, making our system versatile and effective in different agricultural contexts.
🖥️ User-Centric Design: We prioritize user experience, designing our system to be intuitive and accessible, so that farmers with varying levels of technical expertise can benefit from it.
🌾 Commitment to Agriculture: We are deeply invested in the success of the agricultural community and work tirelessly to provide tools that make a real difference in the lives of farmers.
💼 Our Team
Our team is composed of individuals who share a common passion for agriculture and technology. We bring together diverse expertise in fields such as:

💻 Computer Engineering: Developing the software infrastructure that powers our system.
🧠 Artificial Intelligence and Machine Learning: Creating and refining the algorithms that drive accurate disease predictions.
🌱 Agronomy and Plant Science: Ensuring our solutions are grounded in agricultural best practices and are applicable in real-world farming scenarios.
🌟 Our Future Goals
Looking ahead, we aim to expand our system to cover more plant species and diseases, making it a global tool for farmers everywhere. We also plan to integrate additional features, such as pest detection and climate impact analysis, to offer a more comprehensive suite of tools for crop management. As we grow, we remain committed to our core values of innovation, accuracy, and user-centricity.

🤝 Join Us on Our Journey
We invite you to join us on this exciting journey towards healthier crops and more prosperous harvests. Whether you’re a farmer looking to protect your crops, a researcher interested in agricultural technology, or a partner seeking to collaborate on innovative solutions, we welcome you to connect with us.

Explore our platform, learn about our work, and see how we can make a difference together.
                """)

#First page
elif(app_mode=="Home"):
    st.header("Empowering farmers with cutting-edge tools for a prosperous tomorrow.🌾💡")
    st.header("Disease Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
          
    #Predict button
    if(st.button("Predict")):
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))  
st.video("vid2.mp4", start_time=0, loop=True, autoplay=True, muted=True)
st.header("Discover the power of AI in safeguarding our crops and securing our future.🤖🌿")
st.video("vid3.mp4", start_time=0, loop=True, autoplay=True, muted=True)
st.header("Join us on a journey to revolutionize crop protection and boost yields!🌍✨")







    