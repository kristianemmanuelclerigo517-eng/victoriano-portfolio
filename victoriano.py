
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Angel Anania Victoriano | Personal Journal",
    page_icon="✦",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

def show_image(filename, caption=None):
    image_path = IMAGE_DIR / filename

    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: images/{filename}")

# ---------------- DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600;700&family=Space+Mono&display=swap');

.stApp {
    background: #F3F0E8;
    color: #202B35;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #202B35 !important;
}

h1 {
    font-size: 3.5rem !important;
}

h2 {
    font-size: 2.5rem !important;
}

p {
    color: #5D625F;
    line-height: 1.85;
}

.mono {
    font-family: 'Space Mono', monospace;
    color: #C46B43;
    font-size: 12px;
    letter-spacing: 2px;
}

.hero {
    background: #202B35;
    padding: 55px 45px;
    border-radius: 5px;
    color: #F3F0E8;
}

.hero h1 {
    color: #F3F0E8 !important;
    font-size: 4rem !important;
    line-height: 1.05;
}

.hero p {
    color: #D4D0C6;
    max-width: 570px;
}

.hero-label {
    color: #E59A6C;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 3px;
}

.section-number {
    font-family: 'Space Mono', monospace;
    color: #C46B43;
    font-size: 13px;
    letter-spacing: 2px;
}

.journal-card {
    background: #E8E3D8;
    border-left: 4px solid #C46B43;
    padding: 24px;
    margin-bottom: 12px;
}

.dark-card {
    background: #202B35;
    padding: 32px;
    border-radius: 5px;
}

.dark-card h2, .dark-card h3 {
    color: #F3F0E8 !important;
}

.dark-card p {
    color: #D4D0C6;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: #E8E3D8;
    border-radius: 3px;
    padding: 12px 20px;
}

div[data-testid="stRadio"] > div {
    gap: 8px;
}

div[data-testid="stRadio"] label {
    background: #E8E3D8;
    padding: 8px 16px;
    border-radius: 3px;
}

div[data-testid="stRadio"] label:hover {
    background: #DCD4C6;
}

hr {
    border-color: #D9D2C5;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<p class="mono">FIELD NOTES / PERSONAL COLLECTION / 2026</p>
""", unsafe_allow_html=True)

page = st.radio(
    "Explore",
    [
        "Home",
        "About",
        "Education",
        "Reading",
        "Gardening",
        "Motorcycling",
        "Mechanical Engineering"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# ---------------- HOME ----------------

if page == "Home":

    left, right = st.columns([1.3, 0.9], gap="large")

    with left:
        st.markdown("""
        <div class="hero">
            <p class="hero-label">WELCOME TO MY JOURNAL</p>
            <h1>Angel Anania<br>Victoriano.</h1>
            <br>
            <p>
                A collection of my interests, experiences, passions,
                and the little things that make my journey meaningful.
                Every page tells a different part of my story.
            </p>
            <br>
            <p class="hero-label">READ · GROW · EXPLORE</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        show_image("profile.jpg")

    st.write("")
    st.markdown('<p class="mono">01 / THE PERSON BEHIND THE JOURNAL</p>',
                unsafe_allow_html=True)
    st.header("A life filled with curiosity.")

    st.write("""
    I enjoy activities that allow me to learn, discover, and
    experience something new. Whether I am reading a good book,
    taking care of plants, or going on a motorcycle ride,
    I find joy in making the most of every experience.
    """)

    st.divider()

    st.markdown('<p class="mono">02 / MY INTERESTS</p>',
                unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.markdown("### 01")
        st.subheader("Reading")
        st.write("Discovering stories and ideas through books.")

    with b:
        st.markdown("### 02")
        st.subheader("Gardening")
        st.write("Finding satisfaction in nurturing and growing plants.")

    with c:
        st.markdown("### 03")
        st.subheader("Motorcycling")
        st.write("Enjoying the freedom and excitement of the open road.")

    st.write("")
    st.markdown("""
    <div class="dark-card">
        <p class="mono">A PERSONAL REMINDER</p>
        <h2>There is always something new to discover.</h2>
        <p>Every experience is a chapter worth remembering.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- ABOUT ----------------

elif page == "About":

    st.markdown('<p class="mono">CHAPTER 01 / ABOUT ME</p>',
                unsafe_allow_html=True)
    st.title("The person behind the pages.")

    left, right = st.columns([0.9, 1.1], gap="large")

    with left:
        show_image("profile.jpg")

    with right:
        st.subheader("Angel Anania Victoriano")

        st.write("""
        I am a student who enjoys exploring different interests
        and learning from everyday experiences.

        I find happiness in simple activities such as reading,
        gardening, and motorcycling. These hobbies give me
        opportunities to relax, express myself, and appreciate
        the world around me.

        I believe that personal growth comes from being curious,
        staying open to new experiences, and continuously learning.
        """)

        st.markdown("""
        <div class="journal-card">
            <p class="mono">PERSONAL MOTTO</p>
            <h3>Keep exploring. Keep growing.</h3>
        </div>
        """, unsafe_allow_html=True)


# ---------------- EDUCATION ----------------

elif page == "Education":

    st.markdown('<p class="mono">CHAPTER 02 / EDUCATION</p>',
                unsafe_allow_html=True)
    st.title("My academic journey.")

    st.write("""
    Education is an important part of my story. Each institution
    represents another step toward learning, growth, and new opportunities.
    """)

    st.write("")

    st.markdown("""
    <div class="journal-card">
        <p class="mono">01 / ELEMENTARY</p>
        <h3>Lingig Elementary School</h3>
        <p>Where my educational journey began.</p>
    </div>

    <div class="journal-card">
        <p class="mono">02 / SENIOR HIGH SCHOOL</p>
        <h3>Lingig National High School</h3>
        <p>STEM Strand</p>
    </div>

    <div class="journal-card">
        <p class="mono">03 / COLLEGE</p>
        <h3>North Eastern Mindanao State University</h3>
        <p>NEMSU</p>
        <p>Bachelor of Science in Mechanical Engineering</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- READING ----------------

elif page == "Reading":

    st.markdown('<p class="mono">CHAPTER 03 / READING</p>',
                unsafe_allow_html=True)
    st.title("Between the pages.")

    left, right = st.columns([1, 1], gap="large")

    with left:
        show_image("reading.jpg")

    with right:
        st.subheader("A quiet world of stories.")

        st.write("""
        Reading is one of the ways I explore different perspectives
        and discover new ideas. Every book offers something different,
        whether it is an interesting story, a meaningful lesson,
        or information that expands my understanding.

        It allows me to slow down, imagine, and learn beyond
        what I experience in everyday life.
        """)

        st.markdown("""
        <div class="journal-card">
            <p class="mono">MY TAKEAWAY</p>
            <h3>Every book opens a new door.</h3>
        </div>
        """, unsafe_allow_html=True)


# ---------------- GARDENING ----------------

elif page == "Gardening":

    st.markdown('<p class="mono">CHAPTER 04 / GARDENING</p>',
                unsafe_allow_html=True)
    st.title("A little space to grow.")

    show_image("gardening.jpg")

    st.subheader("Growing something meaningful.")

    st.write("""
    Gardening is a hobby that teaches patience, care, and appreciation
    for nature. Taking care of plants and watching them grow can be
    a rewarding experience.

    It reminds me that meaningful progress takes time and that
    even small efforts can lead to beautiful results.
    """)

    st.markdown("""
    <div class="dark-card">
        <p class="mono">A THOUGHT TO REMEMBER</p>
        <h2>Growth takes patience, care, and time.</h2>
    </div>
    """, unsafe_allow_html=True)


# ---------------- MOTORCYCLING ----------------

elif page == "Motorcycling":

    st.markdown('<p class="mono">CHAPTER 05 / MOTORCYCLING</p>',
                unsafe_allow_html=True)
    st.title("Beyond familiar roads.")

    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        show_image("motorcycling.jpg")

    with right:
        st.subheader("The joy of the journey.")

        st.write("""
        Motorcycling gives me the opportunity to explore places,
        enjoy the scenery, and experience the excitement of the road.

        More than reaching a destination, I appreciate the journey
        itself and the memories created along the way.
        """)

        st.markdown("""
        <div class="journal-card">
            <p class="mono">THE ROAD AHEAD</p>
            <h3>Every ride has a story.</h3>
        </div>
        """, unsafe_allow_html=True)


# ---------------- MECHANICAL ENGINEERING ----------------

elif page == "Mechanical Engineering":

    st.markdown('<p class="mono">CHAPTER 06 / MY FIELD OF STUDY</p>',
                unsafe_allow_html=True)
    st.title("Mechanical Engineering.")

    left, right = st.columns([1, 1], gap="large")

    with left:
        show_image("engineering.jpg")

    with right:
        st.subheader("Learning how things work.")

        st.write("""
        Mechanical Engineering is a field that combines mathematics,
        science, creativity, and problem-solving to understand,
        design, and improve machines and mechanical systems.

        As a student of this field, I look forward to developing
        technical knowledge, practical skills, and the ability
        to approach engineering challenges with curiosity.
        """)

    st.divider()

    st.markdown('<p class="mono">AREAS OF INTEREST</p>',
                unsafe_allow_html=True)

    x, y, z = st.columns(3)

    with x:
        st.markdown("### Design")
        st.write("Understanding how products and mechanical systems are designed.")

    with y:
        st.markdown("### Innovation")
        st.write("Exploring ideas that can improve existing technology.")

    with z:
        st.markdown("### Problem-solving")
        st.write("Applying logic and engineering principles to challenges.")


# ---------------- FOOTER ----------------

st.divider()

st.markdown("""
<p style="text-align:center; color:#8B887F; font-size:12px;">
    ANGEL ANANIA VICTORIANO · PERSONAL JOURNAL · 2026
</p>
""", unsafe_allow_html=True)

