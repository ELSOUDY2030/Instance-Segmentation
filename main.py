import streamlit as st
import cv2
import numpy as np
from PIL import Image
import detectron2
from detectron2.modeling import build_model
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.utils.visualizer import Visualizer

import matplotlib.pyplot as plt



st.markdown("""
    <style>
            .css-ffhzg2{
            background-image: url('https://i.pinimg.com/564x/5c/f2/66/5cf2660af5f4214def7166dc7a7c8062.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
    </style>
""", unsafe_allow_html=True)


cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
##cfg.MODEL.DEVICE = 'cpu' 
cfg.MODEL.WEIGHTS = "model_final.pth"
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 36
model = DefaultPredictor(cfg)




st.title("Bio About Me And Instance Segmentation Tooth Dentistry")



st.header("Mohammad Ahmed")
st.write('''I hold a degree in Electronics and Communications Engineering and have a strong background in deep learning and machine learning. Currently, I am focusing on projects in the fields of Natural Language Processing (NLP) and Computer Vision.

I have a diverse portfolio of projects that demonstrate my expertise in these domains. These projects not only showcase my technical skills but also my ability to tackle complex problems and deliver innovative solutions.

You can find my work and contributions on my GitHub profile: "https://github.com/ELSOUDY2030".

I am passionate about leveraging cutting-edge technology to solve real-world challenges and am always eager to collaborate on exciting projects in the fields of NLP and Computer Vision. Feel free to reach out if you'd like to connect or collaborate on any interesting projects.I hold a degree in Electronics and Communications Engineering and have a strong background in deep learning and machine learning. Currently, I am focusing on projects in the fields of Natural Language Processing (NLP) and Computer Vision.

I have a diverse portfolio of projects that demonstrate my expertise in these domains. These projects not only showcase my technical skills but also my ability to tackle complex problems and deliver innovative solutions.

You can find my work and contributions on my GitHub profile: GitHub Profile.

I am passionate about leveraging cutting-edge technology to solve real-world challenges and am always eager to collaborate on exciting projects in the fields of NLP and Computer Vision. Feel free to reach out if you'd like to connect or collaborate on any interesting projects.''')



st.header("Instance Segmentation Tooth Dentistry")
st.write('''
Precise Instance Segmentation: Our model accurately identifies and delineates individual objects within images, providing pixel-level segmentation masks for each instance.
Fast and Efficient: Powered by Detectron2, our solution leverages efficient backbone architectures for real-time or near-real-time instance segmentation without compromising accuracy.
Easy to-Use Interface: Our user-friendly web interface allows you to upload your images and instantly see the results of instance segmentation, making it accessible to both experts and newcomers in the field.
Interactive Visualization: Explore and interact with the segmented images using our intuitive visualization tools. Toggle between original and segmented views to understand the model's performance better.
Customizable: Tailor the instance segmentation model to your specific use case by fine-tuning it on your dataset. Our platform provides guides and resources to help you adapt the model effectively.
Scalable Deployment: Whether you're working on a personal project or an enterprise-level application, our model can be seamlessly integrated into your workflow with our deployment guides.
''')


uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the original image
    st.image(uploaded_image, caption="Original Image", use_column_width=True)

    # Read the uploaded image and convert it to a NumPy array
    image = Image.open(uploaded_image)
    image_np = np.array(image)
    #cv2.imwrite('img',uploaded_image)

    # When clicking the "Draw Box" button
    if st.button("Draw Box"):
        # You can draw a rectangle on the image, for example, here we draw a red rectangle
        out = model(image_np)
        instances = out['instances']
        instances = instances.to("cpu")
        metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
        v = Visualizer(image_np[:,:,::-1], metadata, scale = 10)
        output = v.draw_instance_predictions(instances)


        # Convert the image with the drawn rectangle to PIL format and display it
        st.image(output.get_image()[:, :, ::-1], caption="Image with Drawn Box", use_column_width=True)




















