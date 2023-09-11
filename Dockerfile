FROM python:3.8

RUN apt-get update && \
    apt-get install -y libgl1-mesa-dev


RUN pip install opencv-python scikit-image matplotlib streamlit imageio plotly cython scipy av ninja && \
    pip install torch torchvision && \
    pip install git+https://github.com/facebookresearch/fvcore && \
    pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI


RUN git clone https://github.com/facebookresearch/detectron2.git detectron_repo && \
    cd detectron_repo && \
    pip install -e .

EXPOSE 8501


CMD ["/bin/bash"]