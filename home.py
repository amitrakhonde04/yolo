import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')
def main():
    st.title("Welcome to Object Detection Web App 👋")
    st.write("Welcome to our Object Detection Web App!")
    st.write("This app allows you to perform object detection on images using pre-trained models.")
    st.write("Choose an option from the sidebar to get started.")

    st.sidebar.title("Options")
    option = st.sidebar.radio("Select an option", ["Home", "About", "Object Detection"])

    if option == "Home":
        show_home_page()
    elif option == "About":
        show_about_page()
    elif option == "Object Detection":
        show_object_detection_page()

def show_home_page():
    st.header("Home Page")
    st.write("This is the home page of our Object Detection Web App.")
    st.write("Please use the sidebar to navigate to different sections.")
    st.write("[Click here for the detection on image](/Yolo/)")
    st.write("[Click here for the detection on camera](/Live_cam/)")

def show_about_page():
    st.header("About")
    st.write("About our Object Detection Web App:")
    st.write("- This app allows you to perform object detection on images using pre-trained models.")
    st.write("- This app allows you to perform object detection on live camera as well.")
    st.write("- It is pre-trained models and provides information about detected objects.")
    st.write("- explore the app and provide feedback.")

def show_object_detection_page():
    st.header("Object Detection")
    st.write("Upload an image or use webcam input to perform object detection.")
    st.write("click the 'Detect Objects' button to see the results.")
    
    

if __name__ == "__main__":
    main()