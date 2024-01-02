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
## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. For deep learning, a laptop with a powerful GPU, a high-performance CPU, at least 16GB of RAM, a fast SSD, and an efficient cooling system is recommended.
4. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
 

