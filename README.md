## Instance-Segmentation With MaskRCNN Using Detectron2



<div align="center">
    <img src="https://github.com/ELSOUDY2030/Instance-Segmentation/blob/main/img/gifmaker_me.gif" width="500" height="500">
</div>

# Instance Segmentation Tooth Dentistry

This project employs the Mask R-CNN model to perform instance segmentation specifically for dental applications within the field of dentistry. With this model, it becomes possible to recognize and delineate individual teeth while also assessing their conditions, including but not limited to implants, root canals, and crowns, using dental X-ray images. This comprehensive README offers insights into the project, its configuration, and potential applications.


## Data

This dataset comprises dental X-ray images that include a variety of diseases. These images will be processed using Instance Segmentation with MaskRCNN.

    
    https://universe.roboflow.com/bassem-ahmed-mzidg/dentistry-vbril
    

## Installation

- **Start by cloning the project repository using the following link:**

    ```
   https://github.com/ELSOUDY2030/Instance-Segmentation.git
    ```

- **Next, you'll need to download the model. You can get it from the following location:**

    ```
    https://drive.google.com/file/d/1-6Z0pLzjVd05vCLe2_NR5KsVkDLBk5CU/view?usp=sharing
    ```
    
- **Now, it's time to build the Docker image. Execute the following command:**

    ```
   docker build -t MaskRCNN .
    ```

- **Finally, run the Docker container using the following command:**

    ```
   docker container run -it -v C:\clone\location:/docker -p 8501:8501 --name torch deep/torch:v1.0  /bin/bash
    ```



## How to Utilize It?

1. **With Docker**
   
- **Change directory:**

    ```
   cd docker
    ```

- **Run Streamlit as a Python module:**

    ```
    python -m streamlit run main.py
    ```

 2. **without Docker**

- **Install Detectron and Streamlit**


## Get in Touch

[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-512.png" />](https://wa.me/+201279548818)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />](https://www.linkedin.com/in/mohammad-nomer/)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-256.png" />](mailto:mohammadnomer2030@gmail.com)
&nbsp;&nbsp;



## Give Feedback

Please share your feedback on how I can improve and any ideas to enhance the model. I'm eager to receive any advice that can help me develop my skills.

&nbsp;&nbsp;

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Lobster&size=50&duration=4000&pause=300&color=FFC107&background=FFFFFF00&center=true&vCenter=true&width=1200&height=240&lines=Thank+you" alt="Typing SVG" /></a>
