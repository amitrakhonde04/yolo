import streamlit as st 
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av

from yolo_predictions import YOLO_Pred

st.set_page_config(page_title="Camera_Detection",
                   layout='wide',
                   page_icon='./images/camera.png')

st.header("Detect on Live camera")
st.write("To perform object detection on live camera select the device.")


# load yolo model
yolo = YOLO_Pred('./models/best.onnx',
                 './models/data.yaml')


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    # any operation 
    #flipped = img[::-1,:,:]
    pred_img = yolo.predictions(img)

    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")


webrtc_streamer(key="example", 
                rtc_configuration= RTCConfiguration(
                    {"iceServers": [{url:['turn:turn.anyfirewall.com:443?transport=tcp'], credential: ['webrtc'],username: ['webrtc']}]}
                ),
                video_frame_callback=video_frame_callback,
                media_stream_constraints={"video":True,"audio":False})