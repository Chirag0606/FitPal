import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html

st.set_page_config(page_title="FitPal", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_exercise = load_lottieurl(
    "https://lottie.host/be61eaa2-187d-4807-bba6-029887e23150/DpeM3zUiuz.json")

lottie_body = load_lottieurl(
    "https://lottie.host/6613eeae-b699-4564-8096-9bdab4a7f70d/65GqP0wRe3.json")

lottie_bmi = load_lottieurl(
    "https://lottie.host/a9489483-028e-47a5-a1cb-75ffeefa22b1/LvuAoBfDva.json")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image("logo.png")
    with col3:
        st.write(' ')
    st.title("FitPal")
    st.sidebar.success("You are at our Home Page!!")
    st.write("##")
    st.sidebar.subheader(
        "The road to fitness isn't a sprint, it's a marathon. Lace up, take a breath, and set your pace.")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader("Introducing FitPal: Your Personal Fitness Companion")
        st.write("Are you striving to achieve your peak performance as a sports enthusiast or a busy working professional aiming to stay fit amidst your hectic schedule? Look no further than FitPal  the all-inclusive app designed to help you effortlessly monitor your BMI and Body Fat Percentage, all from the comfort of your smartphone.")
    with right_column:
        st_lottie(lottie_exercise, height=200, key="exercise")

with st.container():
    st.write("---")
    left_body, right_body = st.columns((1, 2))
    st.write("##")
    with left_body:
        st_lottie(lottie_body, height=300, key="body")
    with right_body:
        st.subheader("Body Fat Calculator")
        st.write(" Understanding your body composition is crucial for optimizing your training regimen. FitPal incorporates a cutting-edge Body Fat Percentage measurement tool, enabling you to track changes in your body composition over time. This information empowers you to tailor your workouts and nutrition for more effective results.")

        def open_page(url):
            open_script = """
            <script type="text/javascript">
                window.open('%s', '_blank').focus();
            </script>
            """ % (url)
            html(open_script)
        st.button('Click to Calculate your Body Fat', on_click=open_page,
                  args=('http://localhost:8501/Body-Fat_Calculator',))
        st.write(
            "[Check out more about Body Fat Percentage](https://en.wikipedia.org/wiki/Body_fat_percentage)")


with st.container():
    st.write("---")
    left_bmi, right_bmi = st.columns((2, 1))
    st.write("##")
    with left_bmi:
        st.subheader("BMI Calculator")
        st.write(" FitPal provides you with a convenient and accurate BMI calculator, allowing you to quickly determine your Body Mass Index. Simply input your height and weight, and let FitPal generate your BMI, aiding you in understanding your overall health status and setting realistic fitness goals.")

        def open_page(url):
            open_script = """
            <script type="text/javascript">
                window.open('%s', '_blank').focus();
            </script>
            """ % (url)
            html(open_script)
        st.button('Click to Calculate your BMI', on_click=open_page,
                  args=('http://localhost:8501/BMI_Calculator',))
        st.write(
            "[Check out more about BMI](https://en.wikipedia.org/wiki/Body_mass_index)")
    with right_bmi:
        st_lottie(lottie_bmi, height=300, key="bmi")
