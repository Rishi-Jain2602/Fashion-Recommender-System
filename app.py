import tensorflow as tf
import numpy as np
import keras
from numpy.linalg import norm
import os
import cv2
from tqdm import tqdm #It will track forloop
import pickle


#We will provide images to ResNet which will give us features of images

model=tf.keras.applications.resnet50.ResNet50(weights='imagenet' , include_top=False , input_shape = (224,224,3))
#We will not train over model , it is already trained in imagenet dataset
model.trainable =False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalMaxPooling2D()
])

print(model.summary())

def extract_features(img_path, model):
    img = keras.preprocessing.image.load_img(img_path,target_size=(224,224))
    img_array=keras.preprocessing.image.img_to_array(img)
    expanded_img_array=np.expand_dims(img_array,axis=0)
    preprocessed_img=tf.keras.applications.resnet50.preprocess_input(expanded_img_array)
    #flatten
    result = model.predict(preprocessed_img).flatten()
    #normalize
    normalized_result = result/norm(result)
    return normalized_result

filenames=[]
for file in os.listdir('images'):
    filenames.append(os.path.join('images',file))


features_list=[]
for file in tqdm(filenames):
    features_list.append(extract_features(file,model))

pickle.dump(features_list,open('embeddings.pkl','wb'))
pickle.dump(filenames,open('filenames.pkl','wb'))

