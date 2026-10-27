import streamlit as st
import requests


COLAB_URL = "https://5000-gpu-t4-s-kkb-ass1b2-3s9y0np9p1y7z-b.asia-southeast1-2.prod.colab.dev"


def show_dashboard(username, user_id):

    st.title("FOMM Image to Video")
    st.write("Welcome,", username)

    st.subheader("Select Source Image")

    source_image = st.file_uploader(
        "Upload Source Image",
        type=["jpg", "jpeg", "png"]
    )

    st.subheader("Select Driving Video")

    driving_video = st.file_uploader(
        "Upload Driving Video",
        type=["mp4"]
    )

    if source_image:
        st.image(source_image, width=300)

    if driving_video:
        st.video(driving_video)

    if st.button("Generate Video"):

        if not source_image or not driving_video:
            st.error("Please upload both files.")
            return

        with st.spinner("Generating video using FOMM..."):

            try:

                files = {
                    "source_image": (
                        source_image.name,
                        source_image.getvalue(),
                        source_image.type
                    ),
                    "driving_video": (
                        driving_video.name,
                        driving_video.getvalue(),
                        driving_video.type
                    )
                }

                response = requests.post(
                    f"{COLAB_URL}/generate",
                    files=files,
                    timeout=600
                )

                if response.status_code == 200:

                    output_path = "output/generated_video.mp4"

                    with open(output_path, "wb") as file:
                        file.write(response.content)

                    st.success("Video generated successfully!")

                    st.subheader("Generated Video")

                    st.video(output_path)

                    with open(output_path, "rb") as file:
                        st.download_button(
                            "Download Video",
                            file,
                            file_name="generated_video.mp4",
                            mime="video/mp4"
                        )

                else:

                    st.error(
                        f"Colab backend error: {response.status_code}"
                    )

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not connect to Colab: {error}"
                )