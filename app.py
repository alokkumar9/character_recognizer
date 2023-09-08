import streamlit as st
import keras_ocr
import matplotlib.pyplot as plt
from PIL import Image

pipeline = keras_ocr.pipeline.Pipeline()

# Read images from folder path to image object
images = [
    keras_ocr.tools.read(img) for img in ['https://imgv3.fotor.com/images/blog-cover-image/How-to-Make-Text-Stand-Out-And-More-Readable.jpg'
                                        ]
]

# generate text predictions from the images
prediction_groups = pipeline.recognize(images)

# plot the text predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
#for ax, image, predictions in zip(axs, images, prediction_groups):
#keras_ocr.tools.drawAnnotations(image=images[0],predictions=prediction_groups[0], ax=axs)
keras_ocr.tools.drawAnnotations(image=images[0], predictions=prediction_groups[0], ax=axs )


st.pyplot(fig)
print(images)
