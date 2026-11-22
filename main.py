import streamlit as st
import random as rnd

# 1. Basic Text & Headers
st.title("Streamlit Crash Course")
st.header("1. Capturing User Input")
st.write("Every time you interact with a widget, Streamlit reruns this file from line 1.")

def generate_random_number():
    return rnd.randint(1, 100)

# 2. Input Widgets (they return values straight into variables)
name = st.text_input("Enter your name:", placeholder="e.g. Brandon")
age = st.slider("Pick a number:", min_value=1, max_value=100, value=25)
choice = st.selectbox("Favorite animal?", ["Cat", "Dog", "Otter"])

if st.button("Are you lucky in picking thee number?"):
    random_number = generate_random_number()
    if age == random_number:
        st.success(f"You picked {choice} and your age is {age}.")
    else:
        st.warning("Your number is wrong it should've been {random_number}.")

# 3. The Button + If Pattern
if st.button("Say Hello"):
    if name:
        st.success(f"Hey {name}! You picked {choice} and your number squared is {age ** 2}.")
        st.balloons()
    else:
        st.warning("Type a name first!")

# 4. File Uploader (Direct prep for the Cat vs. Dog app)
st.header("2. Image Upload Preview")
uploaded_file = st.file_uploader("Upload an image to test:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=300)
    st.info("Image loaded! In the next step, we pass this directly to our model.")