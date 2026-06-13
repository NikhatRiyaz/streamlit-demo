# pip install streamlit- for installint streamlit
# streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np


st.title("Streamlit Demo App")
st.header("This is a header function", divider= 'rainbow')
st.subheader("This is a subheader",divider='red')
st.markdown("## Streamlit")
st.caption("This is a caption")
st.code(range(50))
st.write("this is a text function")
st.write(range(30,2))

#status 
st.success("congratulations!!")
st.error("this is a syntax error")
st.warning("this function will be deprecated soon")
st.info("To display any information")
st.text("These are text functions")

#Input widgets
#checkbox
if st.checkbox("select/unselect"):
    st.text(f"user selected the checkbox")
else:
    st.text(f"user has not selected the checkbox")

# radio
state = st.radio("What's your fav color?",['Red','Maroon','Yellow','Purple'])
if state == 'Red':
    st.success("That's my fav color")
elif state == 'Maroon':
    st.write("That's my fav too")
elif state == 'Yellow':
    st.text(f"that's not my fav color")
else:
    st.text(f"I don't like that color anymore")

# selectbox
option = st.selectbox('How would you like to be contacted?',['email','mobile','telephone'])
st.write(f"You have selected", option)

# toggle
on = st.toggle('Features Activated')
if on:
    st.write("Features avtivated for you")
else:
    st.write("Feature not activated")

#charts
data = pd.DataFrame(np.random.randn(30,3),columns=['x','y','z'])
st.dataframe(data)
st.bar_chart(data)
st.area_chart(data)
st.scatter_chart(data)
st.line_chart(data)

# multiselect
option = st.multiselect("what's your fav color?",['Green','Yellow','Purple','Orange'])
st.write(f"you have selected", option)

# sidebar
st.sidebar.header("Navigation",divider = 'rainbow')
st.sidebar.radio("Here's my pages for ref",['Page1','Page2','Page3'])

# Media
st.file_uploader("Upload your files/foldes:")
#st.image(r"C:\Users\LENOVO\Downloads\guvi.png")
#st.video(r"https://www.youtube.com/watch?v=Ry1JIptRq1Y&t=7s")
#st.audio(r"C:\Users\LENOVO\Downloads\titanic_piano.mp3")
#st.page_link(r"https://docs.streamlit.io/develop/api-reference", label='streamlit-Docs')
# Button
st.button('Reset',type='primary')
if st.button("Sayhello"):
    st.write("Hello there!!")
else:
    st.write("Goodbye")

# data_editor
st.data_editor(data,num_rows='dynamic')

st.table(data)
st.color_picker("pick your color")

st.help()
st.snow()
st.balloons()

