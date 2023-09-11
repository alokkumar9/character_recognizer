import streamlit as st
import keras_ocr
import matplotlib.pyplot as plt
from PIL import Image
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-1wbqy5l {visibility: hidden;}
            .css-15zrgzn {visibility: hidden;}
            .css-klqnuk {visibility: hidden;}
            .en6cib64 {visibility: hidden;}
            .css-1u4fkce {visibility: hidden;}
            .en6cib62 {visibility: hidden;}

            .css-19rxjzo, .ef3psqc11 {
            background-color: purple;
            text-color: white;
            }

            div.stButton > button:first-child {
            background-color: darkgreen;
            text-weight: bold;
            }
            </style>
            """
st.markdown("<h1 style='text-align:center;'> Image Text Recognition</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'> By Alok</h4>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

placeholder=st.empty()
col1,col2=placeholder.columns(2)
col1.image("https://i.ibb.co/HdRnpzQ/example1.png", width=250)
col2.markdown("<p style='text-align:left;'> This is an example result</p>", unsafe_allow_html=True)

# Read images from folder path to image object
st.markdown("<h2>Upload an Image with Text</h2>",unsafe_allow_html=True)
uploaded_img= st.file_uploader("Browse File", type=['jpeg','jpg','png'],accept_multiple_files=False)
#container2=st.empty()

def on_click():
    if uploaded_img is not None:
        pipeline = keras_ocr.pipeline.Pipeline()
        print(uploaded_img.name)
        images = [
        keras_ocr.tools.read(img) for img in [uploaded_img
                                        ]]
        # generate text predictions from the images
        prediction_groups = pipeline.recognize(images)
        # plot the text predictions
        fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
        #for ax, image, predictions in zip(axs, images, prediction_groups):
        #keras_ocr.tools.drawAnnotations(image=images[0],predictions=prediction_groups[0], ax=axs)
        keras_ocr.tools.drawAnnotations(image=images[0], predictions=prediction_groups[0], ax=axs )

        columnbelow[0].pyplot(fig)
        print(images)

if uploaded_img is not None:
    btn=st.button("Recognize Text", on_click=on_click)

belowrecognize=st.empty()
columnbelow=belowrecognize.columns(1) #Returns list






