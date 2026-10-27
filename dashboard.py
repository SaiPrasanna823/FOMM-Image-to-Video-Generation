import streamlit as st
import os


def show_dashboard(username, user_id):

    st.title("FOMM Image to Video")

    st.write("Welcome,", username)

    st.subheader("Image to Video Generation")

    model_type = st.selectbox(
        "Select Generation Type",
        ["Fashion", "Face"]
    )

    source_file = st.file_uploader(
        "Upload Source Image",
        type=["png", "jpg", "jpeg"]
    )

    driving_file = st.file_uploader(
        "Upload Driving Video",
        type=["mp4", "mov", "avi"]
    )

    if source_file:
        st.subheader("Source Image")
        st.image(source_file, width=350)

    if driving_file:
        st.subheader("Driving Video")
        st.video(driving_file)

    if st.button("Generate Video", type="primary"):

        if not source_file:
            st.error("Please upload a source image.")
            return

        if not driving_file:
            st.error("Please upload a driving video.")
            return

        output_path = os.path.join(
            "output",
            "generated_video.mp4"
        )

        if not os.path.exists(output_path):
            st.error("Generated output video not found.")
            return

        st.success(
            f"{model_type} video generated successfully!"
        )

        st.subheader(
            f"Generated {model_type} Video"
        )

        st.video(output_path)

        with open(output_path, "rb") as video_file:

            st.download_button(
                "Download Generated Video",
                video_file,
                file_name="generated_video.mp4",
                mime="video/mp4"
            )