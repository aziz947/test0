import streamlit as st
st.error("Error")

st.title("Hello Gomycode ")
st.header("This is a header")
st.subheader("This is a subheader" )
st.text("Hello Gomycode!!!")
st.success("Success")
st.info("Information")
st.warning("Warning")
from PIL import Image
img = Image.open("Capture d'écran 2024-12-09 130635.png")
st.image(img, width=400)
if st.checkbox("Show/Hide"):
	# affiche le texte si la case à cocher renvoie la valeur True

     st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):

	st.success("Male")

else:

	st.success("Female")
hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)
hobbies = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')
st.button("Click me for no reason")
if(st.button("About")):

	st.text("Welcome To Gomycode!!!")    
name = st.text_input("Enter Your name", "Type Here ...")
level = st.slider("Select the level", 1, 5)
st.text('Selected: {}'.format(level))
    

