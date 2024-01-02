import streamlit as st
import os
import numpy as np
import pickle
from PIL import Image
import tensorflow as tf
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
import keras

st.title('Fashion Recommender System')

feature_list = np.array(pickle.load(open('embeddings.pkl','rb')))
filenames = pickle.load(open('filenames.pkl','rb'))

model=tf.keras.applications.resnet50.ResNet50(weights='imagenet' , include_top=False , input_shape = (224,224,3))
model.trainable =False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalMaxPooling2D()
])

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0
    
def feature_extraction(img_path, model):
    img= tf.keras.preprocessing.image.load_img(img_path,target_size=(224,224))
    img_array= tf.keras.preprocessing.image.img_to_array(img)
    expanded_img_array=np.expand_dims(img_array,axis=0)
    preprocessed_img=tf.keras.applications.resnet50.preprocess_input(expanded_img_array)
    #flatten
    result = model.predict(preprocessed_img).flatten()
    #normalize
    normalized_result = result/norm(result) 
    return normalized_result

 

def recommend(features,feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)

    distances, indices = neighbors.kneighbors([features])

    return indices

# steps
# file upload -> save
uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        # feature extract
        features = feature_extraction(os.path.join("uploads",uploaded_file.name),model)
        #st.text(features) #It shows features in the browser of the uploaded image
        #recommendention
        indices = recommend(features,feature_list)
        # show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(filenames[indices[0][0]])
        with col2:
            st.image(filenames[indices[0][1]])
        with col3:
            st.image(filenames[indices[0][2]])
        with col4:
            st.image(filenames[indices[0][3]])
        with col5:
            st.image(filenames[indices[0][4]])
    else:
        st.header("Some error occured in file upload")


