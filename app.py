from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

NAME = "Ericka Fatima Reign R. Ligaray"
SECTION = "CS365 - Applied AI"
PROGRAM = "BS Computer Science, 3rd year"
IMG_DIR = Path(__file__).parent / "assets" / "images"

st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="👋", layout="wide")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
    --blue: #7FA8D6;
    --blue-soft: #A8C6E7;
    --yellow: #FFF2B2;
    --yellow-deep: #FFE08A;
    --cream: #FFF7D6;
    --navy: #1F3A5F;
}

.stApp, .stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3,
.stApp h4, .stApp input, .stApp textarea, .stApp button,
[data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3 { color: var(--navy); font-weight: 600; }

/* hero: cut-out label style */
.hero {
    background: linear-gradient(135deg, var(--blue-soft), var(--yellow));
    padding: 2.2rem 2rem 2rem 2rem;
    border-radius: 18px;
    margin-bottom: 1.2rem;
}
.tag {
    display: inline-block;
    background: var(--cream);
    color: var(--navy);
    padding: 0.3rem 0.9rem;
    margin: 0 0.4rem 0.4rem 0;
    font-weight: 500;
    box-shadow: 2px 3px 0 rgba(31, 58, 95, 0.25);
}
.tag1 { transform: rotate(-4deg); }
.tag2 { transform: rotate(2deg); }
.tag3 { transform: rotate(-1.5deg); margin-top: 0.8rem; }
.block {
    display: inline-block;
    background: var(--navy);
    color: #ffffff;
    font-size: 2.4rem;
    font-weight: 600;
    padding: 0.1rem 1.2rem;
    margin-top: 0.4rem;
    line-height: 1.3;
}

/* cards and buttons */
[data-testid="stMetric"] {
    background: var(--yellow);
    border-left: 6px solid var(--blue);
    padding: 0.8rem 1rem;
    border-radius: 10px;
}
.stTabs [data-baseweb="tab"] { font-weight: 500; }
.stButton button, .stDownloadButton button, [data-testid="stFormSubmitButton"] button {
    background: var(--blue);
    color: #ffffff;
    border: none;
    border-radius: 8px;
}
.stButton button:hover, .stDownloadButton button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    background: var(--navy);
    color: #ffffff;
}
.placeholder {
    background: var(--blue-soft);
    color: var(--navy);
    border: 2px dashed var(--navy);
    border-radius: 14px;
    padding: 3rem 1rem;
    text-align: center;
    font-weight: 500;
}
.footer { text-align: center; color: var(--navy); opacity: 0.7; padding: 1.5rem 0 0.5rem 0; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ---------- helpers ----------
def show_image(filename, label):
    """Show the image if it exists, otherwise a labeled stand-in."""
    path = IMG_DIR / filename
    if path.exists():
        st.image(str(path), caption=label)
    else:
        st.markdown(f'<div class="placeholder">{label}<br>(stand-in image)</div>',
                    unsafe_allow_html=True)


# ---------- data (edit these) ----------
skills = pd.DataFrame({
    "Skill": ["Python", "Streamlit", "SQL", "HTML/CSS", "Git", "Communication"],
    "Category": ["Programming", "Programming", "Data", "Web", "Tools", "Soft skill"],
    "Level": [80, 65, 60, 70, 55, 75],
})

projects = [
    {
        "title": "[Project One]",
        "role": "[Your role, e.g. Developer]",
        "tools": ["Python", "Streamlit"],
        "outcome": "[What it did or what you learned]",
        "link": "https://github.com/sjq-158",
        "image": "project1.jpg",
    },
    {
        "title": "[Project Two]",
        "role": "[Your role]",
        "tools": ["HTML/CSS", "Git"],
        "outcome": "[What it did or what you learned]",
        "link": "https://github.com/sjq-158",
        "image": "project2.jpg",
    },
    {
        "title": "[Project Three]",
        "role": "[Your role]",
        "tools": ["Python", "SQL"],
        "outcome": "[What it did or what you learned]",
        "link": "https://github.com/sjq-158",
        "image": "project3.jpg",
    },
]

milestones = pd.DataFrame({
    "Year": [2005, 2011, 2017, 2019, 2024],
    "Milestone": [
        "[Born in ...]",
        "[Started elementary at ...]",
        "[Finished elementary]",
        "[Started senior high]",
        "[Started college at CIT-U]",
    ],
})

# ---------- session state ----------
if "likes" not in st.session_state:
    st.session_state.likes = 0
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- sidebar ----------
with st.sidebar:
    st.header(NAME)
    st.caption(SECTION)
    st.write(PROGRAM)
    st.divider()

    st.subheader("Filters")
    all_tools = sorted({t for p in projects for t in p["tools"]})
    picked_tools = st.multiselect("Show projects that use", all_tools, default=all_tools)
    show_fun = st.checkbox("Show fun facts", value=True)

    st.divider()
    if st.button("👍 Like this page"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!")
    st.metric("Likes", st.session_state.likes)

    summary = (
        f"{NAME}\n{SECTION}\n{PROGRAM}\n\n"
        "Skills:\n" + "\n".join(f"- {r.Skill}: {r.Level}" for r in skills.itertuples())
    )
    st.download_button("Download my summary", summary, file_name="summary.txt")

# ---------- hero ----------
st.markdown(
    f"""
    <div class="hero">
        <span class="tag tag1">hello, i'm</span>
        <span class="tag tag2">{SECTION}</span><br>
        <div class="block">{NAME}</div><br>
        <span class="tag tag3">student · learner · builder</span>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Autobiography", "Skills", "Projects", "Contact"]
)

# ---------- about ----------
with tab_about:
    col_img, col_text = st.columns([1, 2], gap="large")
    with col_img:
        show_image("profile.jpg", "Photo of me")
    with col_text:
        st.header("About me")
        st.write(
            "[Write 3-4 sentences about yourself here. Keep it simple and sound like "
            "you. Who are you, what are you studying, what do you like doing?]"
        )
        m1, m2, m3 = st.columns(3)
        m1.metric("Year level", "3rd")
        m2.metric("Projects", len(projects))
        m3.metric("Avg. skill level", f"{np.round(skills['Level'].mean(), 1)}")

        if show_fun:
            st.info("Fun fact: [something small and true about you]")

# ---------- autobiography ----------
with tab_story:
    st.header("My story")
    left, right = st.columns(2, gap="large")
    with left:
        st.subheader("Background")
        st.write("[Where you grew up, your family, what your childhood was like.]")
        st.subheader("Education")
        st.markdown(
            "- **Elementary:** [school]\n"
            "- **Junior high:** [school]\n"
            "- **Senior high:** [school, strand]\n"
            "- **College:** Cebu Institute of Technology - University, [program]"
        )
    with right:
        st.subheader("Interests")
        st.write("[Hobbies, things you enjoy, what you do when you're free.]")
        interests = st.multiselect(
            "Pick what sounds most like me",
            ["Music", "Gaming", "Coding", "Reading", "Sports", "Cooking", "Art"],
            default=["Coding"],
        )
        if interests:
            st.write("You picked:", ", ".join(interests))

    st.subheader("Milestones")
    year_range = st.slider("Year range", 2005, 2026, (2005, 2026))
    shown = milestones[milestones["Year"].between(*year_range)]
    st.dataframe(shown, hide_index=True)

    with st.expander("Something I'm still working on"):
        st.write("[A goal, a habit, or something you want to get better at.]")

# ---------- skills ----------
with tab_skills:
    st.header("Skills")
    st.write("[One or two sentences about how you learned these.]")

    f1, f2 = st.columns(2)
    category = f1.selectbox("Category", ["All"] + sorted(skills["Category"].unique()))
    min_level = f2.slider("Minimum level", 0, 100, 0)

    view = skills.copy()
    if category != "All":
        view = view[view["Category"] == category]
    view = view[view["Level"] >= min_level]

    mode = st.radio("View as", ["Chart", "Table"], horizontal=True)
    if view.empty:
        st.warning("Nothing matches those filters.")
    elif mode == "Chart":
        st.bar_chart(view.set_index("Skill")["Level"], color="#7FA8D6")
    else:
        st.dataframe(view, hide_index=True)

    st.subheader("Currently improving")
    st.progress(65, text="Streamlit: 65%")
    st.progress(55, text="Git: 55%")

# ---------- projects ----------
with tab_projects:
    st.header("Projects")
    visible = [p for p in projects if set(p["tools"]) & set(picked_tools)]
    if not visible:
        st.warning("No projects match the tools picked in the sidebar.")
    else:
        cols = st.columns(len(visible), gap="medium")
        for col, p in zip(cols, visible):
            with col:
                with st.container(border=True):
                    show_image(p["image"], p["title"])
                    st.subheader(p["title"])
                    st.write(f"**Role:** {p['role']}")
                    st.write(f"**Tools:** {', '.join(p['tools'])}")
                    st.write(f"**Outcome:** {p['outcome']}")
                    st.link_button("View project", p["link"])

# ---------- contact ----------
with tab_contact:
    st.header("Contact / feedback")
    st.write("Leave a message or tell me what you think of the page.")

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        sender = c1.text_input("Your name")
        email = c2.text_input("Email")
        topic = st.selectbox("Topic", ["Feedback", "Question", "Collaboration", "Just saying hi"])
        feeling = st.radio("How's the page?", ["Love it", "It's okay", "Needs work"], horizontal=True)
        message = st.text_area("Message")
        ok_reply = st.checkbox("It's okay to reply to my email")
        sent = st.form_submit_button("Send")

    if sent:
        if not sender or not message:
            st.warning("Please add your name and a message.")
        else:
            st.session_state.messages.append(
                {"Date": date.today().isoformat(), "From": sender, "Topic": topic,
                 "Page": feeling, "Reply OK": ok_reply}
            )
            st.success(f"Thanks, {sender}! Your message went through.")
            st.balloons()

    if st.session_state.messages:
        st.subheader("Messages this session")
        st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)

st.markdown(f'<div class="footer">{NAME} · {SECTION}</div>', unsafe_allow_html=True)