import streamlit as st
from database import create_database
from auth import register, login
from dashboard import show_dashboard

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="FOMM Image to Video",
    page_icon="",
    layout="centered"
)

# -----------------------------
# Database
# -----------------------------

create_database()

# -----------------------------
# Session state
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "user_id" not in st.session_state:
    st.session_state.user_id = None

# -----------------------------
# Dashboard
# -----------------------------

if st.session_state.logged_in:

    show_dashboard(
        st.session_state.username,
        st.session_state.user_id
    )

# -----------------------------
# Login / Register
# -----------------------------

else:

    st.markdown(
        "<h1 style='text-align:center;'>🎬 FOMM Image to Video</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "AI-powered image animation using First Order Motion Model"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    option = st.radio(
        "Choose an option",
        ["Login", "Register"],
        horizontal=True
    )

    st.write("")

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    st.write("")

    # -------------------------
    # Register
    # -------------------------

    if option == "Register":

        if st.button(
            "Create Account",
            use_container_width=True,
            type="primary"
        ):

            if username and password:

                user_id = register(
                    username,
                    password
                )

                if user_id:

                    st.success(
                        "Registration successful! You can now login."
                    )

                else:

                    st.error(
                        "Username already exists!"
                    )

            else:

                st.error(
                    "Please enter username and password."
                )

    # -------------------------
    # Login
    # -------------------------

    else:

        if st.button(
            "Login",
            use_container_width=True,
            type="primary"
        ):

            user = login(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.username = user[1]
                st.session_state.user_id = user[0]

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    st.write("")

    st.caption(
        "Powered by Python • PyTorch • FOMM • Streamlit"
    )

