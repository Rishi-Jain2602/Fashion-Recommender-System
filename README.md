# Fashion-Recommender-System
## Introduction
The Fashion Recommender System project is a web-based application designed to assist users in discovering and exploring fashionable clothing items based on their preferences, style, and historical choices.

***

## Requirements
- Python 3.x
- Jupyter Notebook
- Python Libraries - Numpy, sklearn, tensorflow , pickle , streamlit, PIL, os, cv2(openCV)

***

## Installation
1. Clone the Repository
``` bash
git clone https://github.com/Rishi-Jain2602/Fashion-Recommender-System.git
```
2. Install the Project dependencies
```bash
pip install -r requirements.txt
```
3. Download Dataset

From that [Link](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small/code) just download 593Mb zip file. After downloading just extract image folder which will be our database which contains 44k+ images. Then you can either download the 'sample' folder which is attached with this repository(which contains sample images which we will use that while running the browser) or you can also download some random images of jeans, tshirt , watchers etc from the internet. 

4. Downloading app.py and main.py file from repository

First run app.py which will take time( if you are using normal laptop otherwise it will run very quickly) because it will create two pickle files.Then create a empty folder also name it as 'uploads'.

Then in the terminal write 

```bash
streamlit run main.py
```

This will open the website and where we can upload the sample images from that we will get 5 similar images automatically.

***Note :-*** Keep image ,sample and upload folder in same folder only which also contains:main.py , app.py files also.
***
## Model Training

### Knowlege Required
- Convolutional neural network (CNN) - ResNet
- Transfer Learning
- Python Libraries -  Numpy, sklearn, tensorflow , pickle , streamlit, PIL, os, cv2(openCV)

### Tools
- Vs code

### Importing Model using ResNet
![model](https://github.com/Rishi-Jain2602/Fashion-Recommender-System/assets/118871883/7d263d3f-de58-4187-9287-a5a3560acd74)

- Import ResNet it is an CNN Model which is already trained on various database. We can use this as Features Extractor.
- Here top layer is removed and we have used **GlobalMaxPooling2D** in top layer which is specifically designed to reduce the spatial dimensions (height and width) of the input feature map while retaining the most important information.
- In CNN , the initial layers learn low-level features, such as edges and textures, while deeper layers learn more complex and abstract features.
  
**Model Summary**

  ![Screenshot (4456)](https://github.com/Rishi-Jain2602/Fashion-Recommender-System/assets/118871883/deee69cc-42ec-413b-84c0-864ef004447d)

where non-trainable parameter means already trained parameters

### Extractng Features

![Extracting features](https://github.com/Rishi-Jain2602/Fashion-Recommender-System/assets/118871883/6caa31bc-123a-4177-92bb-31d8a7cd38cf)

- We will provide the image data base to resnet which will provide 2048 features of the images.
- In the begining it will convert images to array.
- Then we will expand the array because here keras work on bundles of images so we just expand the dimension
- Then the Preprocess_input will convert the features into proper format.It's shape will 1,2048
- At last we will flatten that array to 2048 features and then normalize it.

### Exporting Features

![dumping](https://github.com/Rishi-Jain2602/Fashion-Recommender-System/assets/118871883/7caa01c9-7530-4ebb-a2e1-2c4f384ea447)

- Here variable are filenames( Which stores the path of the images) and features list(It stores the extracted features of images) are been used to create pickle files.
- In the pickle files all the features are exported and can be used in other files.


***
## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. For deep learning, a laptop with a powerful GPU, a high-performance CPU, at least 16GB of RAM, a fast SSD, and an efficient cooling system is recommended.
4. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
 

