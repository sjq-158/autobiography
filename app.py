import base64
from datetime import date
from pathlib import Path
from urllib.parse import quote

import numpy as np
import pandas as pd
import streamlit as st

NAME = "Ericka Fatima Reign R. Ligaray"
SECTION = "CS365 - Applied AI"
PROGRAM = "BS Computer Science, 3rd year"
INITIALS = "EL"
IMG_DIR = Path(__file__).parent / "assets" / "images"

# ID card details (edit these)
ID_NAME = "Ericka Ligaray"
ID_DOB = "[Month DD]"
ID_MBTI = "[MBTI]"
ID_HOBBIES = "Reading comics and books, gardening"
ID_COLOR = "[Fav color]"
ID_NO = "#001-A1"

st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon=":material/person:", layout="wide")

# ---------- dark / light ----------
_, top_right = st.columns([5, 1.3])
dark = top_right.toggle(":material/dark_mode: Dark mode", key="dark")

LIGHT = {
    "bg": "#FFF7D6", "side": "#FFF2B2", "card": "#FFF2B2", "card2": "#A8C6E7",
    "text": "#1F3A5F", "muted": "#4F6B8F", "accent": "#7FA8D6", "accent2": "#FFE08A",
    "line": "rgba(31,58,95,.2)", "input": "#FFFFFF",
    "tagbg": "#FFF7D6", "tagtext": "#1F3A5F", "blockbg": "#1F3A5F", "blocktext": "#FFFFFF",
    "hero1": "#A8C6E7", "hero2": "#FFF2B2", "hero3": "#FFE08A",
    "bandbg": "#1F3A5F", "bandtext": "#FFF7D6",
    # menu: dark yellow chosen item with blue text
    "navbg": "#1F3A5F", "navtext": "#FFF7D6", "navhl": "#FFE08A", "navhltext": "#1F3A5F",
    "scheme": "light",
}
DARK = {
    "bg": "#0E1A2B", "side": "#132238", "card": "#1A2C47", "card2": "#2A4468",
    "text": "#EAF1FA", "muted": "#A9BBD3", "accent": "#7FA8D6", "accent2": "#FFE08A",
    "line": "rgba(234,241,250,.2)", "input": "#1A2C47",
    "tagbg": "#2A4468", "tagtext": "#EAF1FA", "blockbg": "#FFE08A", "blocktext": "#1F3A5F",
    "hero1": "#1F3A5F", "hero2": "#2B4A75", "hero3": "#6B5E2E",
    "bandbg": "#7FA8D6", "bandtext": "#10243D",
    # menu: opposite, blue chosen item with dark yellow text
    "navbg": "#1A2C47", "navtext": "#EAF1FA", "navhl": "#3D6FB3", "navhltext": "#FFE08A",
    "scheme": "dark",
}
P = DARK if dark else LIGHT

# ---------- svg icons (feather / lucide style) ----------
ICONS = {
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    "trophy": '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "cap": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
    "heart": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "mail": '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    "search": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "gamepad": '<line x1="6" x2="10" y1="12" y2="12"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="15" x2="15.01" y1="13" y2="13"/><line x1="18" x2="18.01" y1="11" y2="11"/><rect width="20" height="12" x="2" y="6" rx="2"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "activity": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "bars": '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "folder": '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>',
}

# ---------- menu setup ----------
PAGES = ["About", "Autobiography", "Skills", "Works", "Contact"]
NAV_ICONS = {"About": "user", "Autobiography": "book", "Skills": "bars", "Works": "trophy", "Contact": "mail"}

if "page" not in st.session_state:
    st.session_state.page = "About"
current = st.session_state.page


def nav_css():
    """Per-page svg icons (drawn with a mask so they follow the text color) and the typing speed."""
    rules = []
    for p, name in NAV_ICONS.items():
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + ICONS[name] + "</svg>"
        )
        uri = "data:image/svg+xml," + quote(svg)
        rules.append(
            f'.stApp .st-key-nav [class*="st-key-nav_o"][class*="_{p}"] button::before'
            f'{{-webkit-mask:url("{uri}") center/contain no-repeat;mask:url("{uri}") center/contain no-repeat;}}'
        )
    n = len(current)
    rules.append(
        '.stApp .st-key-nav [class*="st-key-nav_on_"] button p::after'
        f"{{animation:typeReveal {n * 0.09:.2f}s steps({n},end) forwards,caretBlink .9s step-end infinite;}}"
    )
    return "".join(rules)


FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800"
    "&family=Inter:wght@400;500;600&display=swap');"
)
VARS = ":root{" + "".join(f"--{k}:{v};" for k, v in P.items()) + \
       "--paper:#FFF7D6;--ink:#1F3A5F;color-scheme:" + P["scheme"] + ";}"

BASE_CSS = """
.stApp{background:var(--bg);}
[data-testid="stHeader"]{background:transparent;}
[data-testid="stSidebar"]{background:var(--side);}
.stApp, .stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp input, .stApp textarea, .stApp button, .stApp th, .stApp td, .stApp summary,
[data-testid="stMetricValue"], [data-testid="stMetricLabel"]{
    font-family:'Poppins',sans-serif;
}
.stApp p, .stApp li, .stApp label, .stApp th, .stApp td, .stApp summary,
.stApp h1, .stApp h2, .stApp h3, .stApp h4,
[data-testid="stMetricValue"], [data-testid="stMetricLabel"]{color:var(--text);}
[data-testid="stCaptionContainer"] p{color:var(--muted);}
h1,h2,h3{font-weight:600;}
.stApp h1,.stApp h2,.stApp h3{text-transform:uppercase;font-weight:700;letter-spacing:.03em;}
hr{border-color:var(--line)!important;}

/* second font: Inter */
.tag,.id-card,.p-top,.p-sub,.tl-text,.badge{font-family:'Inter',sans-serif;}

/* ---------- keyframes (animista basic style) ---------- */
@keyframes fadeBottom{from{opacity:0;translate:0 40px}to{opacity:1;translate:0 0}}
@keyframes slideLeft{from{opacity:0;translate:-70px 0}to{opacity:1;translate:0 0}}
@keyframes scaleCenter{from{opacity:0;scale:.4}to{opacity:1;scale:1}}
@keyframes textFocus{from{filter:blur(14px);opacity:0}to{filter:blur(0);opacity:1}}
@keyframes bounceTop{
    0%{translate:0 -260px;opacity:0;animation-timing-function:ease-in}
    38%{translate:0 0;opacity:1;animation-timing-function:ease-out}
    55%{translate:0 -60px;animation-timing-function:ease-in}
    72%{translate:0 0;animation-timing-function:ease-out}
    81%{translate:0 -26px;animation-timing-function:ease-in}
    90%{translate:0 0;animation-timing-function:ease-out}
    95%{translate:0 -8px;animation-timing-function:ease-in}
    100%{translate:0 0}
}
@keyframes floaty{0%,100%{translate:0 0}50%{translate:0 -14px}}
@keyframes cardFloat{
    0%,100%{transform:translateY(0) rotate(2deg)}
    50%{transform:translateY(-12px) rotate(-1deg)}
}
@keyframes sway{
    0%,100%{transform:rotate(calc(var(--r) - 1.5deg))}
    50%{transform:rotate(calc(var(--r) + 1.5deg))}
}
@keyframes heartbeat{0%,100%{scale:1}14%{scale:1.25}28%{scale:1}42%{scale:1.25}70%{scale:1}}
@keyframes pulsate{0%,100%{scale:1;opacity:1}50%{scale:.6;opacity:.5}}
@keyframes wobble{
    0%,100%{translate:0 0;rotate:0deg}
    15%{translate:-10px 0;rotate:-5deg}
    30%{translate:8px 0;rotate:3deg}
    45%{translate:-6px 0;rotate:-3deg}
    60%{translate:4px 0;rotate:2deg}
    75%{translate:-2px 0;rotate:-1deg}
}
@keyframes spin{to{rotate:360deg}}
@keyframes grow{from{width:0}}
@keyframes gradientShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
@keyframes tabPop{0%{scale:.85}60%{scale:1.05}100%{scale:1}}
@keyframes typeReveal{from{width:100%}to{width:0}}
@keyframes caretBlink{0%,100%{border-left-color:var(--navhltext)}50%{border-left-color:transparent}}

/* scroll reveal: plays on load, and follows the scroll in browsers that support it */
.reveal{animation:fadeBottom .8s ease-out backwards var(--d,0s);}
@supports (animation-timeline: view()){
    .reveal, [data-testid="stMetric"], [class*="st-key-proj"], [data-testid="stForm"]{
        animation:fadeBottom linear both;
        animation-timeline:view();
        animation-range:entry 0% entry 70%;
    }
}
/* each page's columns slide up when you switch pages */
[data-testid="stColumn"]{animation:fadeBottom .6s ease-out backwards;}

/* ---------- hero ---------- */
.hero{
    position:relative;overflow:hidden;display:flex;flex-wrap:wrap;align-items:center;
    justify-content:space-between;gap:2.5rem;min-height:430px;padding:3rem;
    border-radius:26px;margin-bottom:1.2rem;
    background:linear-gradient(120deg,var(--hero1),var(--hero2),var(--hero3),var(--hero1));
    background-size:300% 300%;animation:gradientShift 14s ease infinite;
}
.hero-left{flex:1 1 340px;position:relative;z-index:2;}
.tags{display:flex;flex-wrap:wrap;gap:.6rem .8rem;}
.tag{
    display:inline-flex;align-items:center;gap:.5rem;background:var(--tagbg);color:var(--tagtext);
    padding:.45rem 1.1rem;font-weight:500;box-shadow:3px 4px 0 rgba(31,58,95,.28);
    transform:rotate(var(--r));
    animation:slideLeft .8s cubic-bezier(.2,.8,.2,1) backwards var(--d,0s),
              sway 5s ease-in-out infinite var(--d,0s);
}
.dot{width:10px;height:10px;border-radius:50%;background:#2E9E6B;animation:pulsate 1.6s ease-in-out infinite;}
.block{
    display:inline-block;background:var(--blockbg);color:var(--blocktext);
    font-size:clamp(1.8rem,4.2vw,3.2rem);font-weight:600;line-height:1.25;
    padding:.2rem 1.3rem;margin:1.1rem 0;animation:textFocus .9s ease-out backwards .25s;
}
.deco{position:absolute;z-index:1;opacity:.5;color:var(--text);}
.d1{top:8%;left:46%;animation:floaty 5s ease-in-out infinite,spin 20s linear infinite;}
.d2{bottom:9%;left:5%;animation:floaty 6s ease-in-out infinite .8s,spin 26s linear infinite reverse;}
.d3{top:10%;right:3%;animation:floaty 7s ease-in-out infinite 1.4s,spin 18s linear infinite;}
.d4{bottom:7%;right:44%;animation:floaty 4.5s ease-in-out infinite .4s;}

/* ---------- id card ---------- */
.id-card{
    position:relative;z-index:2;flex:0 1 500px;min-width:300px;background:var(--paper);
    color:var(--ink);border-radius:22px;overflow:hidden;box-shadow:0 18px 40px rgba(16,36,61,.3);
    transform:rotate(2deg);
    animation:bounceTop 1.2s both .3s,cardFloat 7s ease-in-out 1.6s infinite;
}
.id-card:hover{animation-play-state:paused,paused;scale:1.03;}
.id-head{
    background:var(--bandbg);color:var(--bandtext);display:flex;align-items:center;gap:1rem;
    padding:.9rem 1.4rem;font-weight:600;letter-spacing:.3em;font-size:.9rem;
}
.id-head .rule{flex:1;height:2px;background:currentColor;opacity:.6;}
.id-body{
    display:flex;flex-wrap:wrap;gap:1.4rem;align-items:center;padding:1.5rem;
    background-image:radial-gradient(rgba(127,168,214,.4) 1.5px,transparent 1.5px);background-size:22px 22px;
}
.id-photo{
    width:140px;height:140px;flex:none;border-radius:22px;border:6px solid #FFE08A;
    background:#A8C6E7;color:#1F3A5F;overflow:hidden;display:grid;place-items:center;
    box-shadow:0 0 0 4px #7FA8D6;
}
.id-photo img{width:100%;height:100%;object-fit:cover;display:block;}
.id-fields{flex:1 1 220px;min-width:200px;}
.id-row{display:flex;gap:.7rem;align-items:baseline;margin:.6rem 0;font-size:.82rem;}
.id-row .k{flex:none;width:6.2rem;font-weight:500;color:#4F6B8F;}
.id-row .v{
    flex:1;border-bottom:2px dotted rgba(31,58,95,.55);font-weight:600;
    font-size:.95rem;line-height:1.5;color:var(--ink);
}
.id-foot{
    background:#FFE08A;padding:.55rem 1.4rem;font-weight:600;font-size:.85rem;
    text-decoration:underline;color:#1F3A5F;
}

/* ---------- headings, chips, timeline ---------- */
.ico{flex:none;vertical-align:-.2em;}
.sec-head{display:flex;align-items:center;gap:.9rem;font-weight:800;font-size:2.8rem;line-height:1.1;text-transform:uppercase;letter-spacing:.02em;color:var(--text);margin:.2rem 0 .8rem;}
.sub-head{display:flex;align-items:center;gap:.7rem;font-weight:700;font-size:1.4rem;text-transform:uppercase;letter-spacing:.04em;color:var(--text);margin:1.2rem 0 .5rem;}
.sec-head .ico,.sub-head .ico{color:var(--accent);animation:floaty 3.5s ease-in-out infinite;}
.chips{display:flex;flex-wrap:wrap;gap:.7rem;margin:.4rem 0 1rem;}
.chip{
    display:inline-flex;align-items:center;gap:.5rem;background:var(--card);color:var(--text);
    border:1px solid var(--line);border-radius:999px;padding:.5rem 1rem;font-weight:500;
    animation:floaty 4s ease-in-out infinite var(--d,0s);
}
.chip .ico{color:var(--accent);}
.chip:hover{animation:wobble .8s;background:var(--accent2);color:#1F3A5F;}
.chip:hover .ico{color:#1F3A5F;}
.timeline{border-left:3px solid var(--accent);margin:.4rem 0 1rem .5rem;padding-left:1.2rem;}
.tl-item{position:relative;margin:.9rem 0;}
.tl-item::before{
    content:"";position:absolute;left:-1.7rem;top:.35rem;width:12px;height:12px;border-radius:50%;
    background:var(--accent2);border:2px solid var(--accent);animation:pulsate 2.4s ease-in-out infinite var(--d,0s);
}
.tl-level{font-weight:600;color:var(--text);}
.tl-text{color:var(--muted);font-size:.92rem;}
.yrs{color:var(--accent);font-weight:600;white-space:nowrap;}

/* ---------- skills bars ---------- */
.bar{margin:.8rem 0;}
.bar-top{display:flex;justify-content:space-between;font-weight:500;color:var(--text);margin-bottom:.3rem;}
.bar-track{height:14px;border-radius:999px;background:rgba(127,168,214,.25);border:1px solid var(--line);overflow:hidden;}
.bar-fill{
    height:100%;width:var(--w);border-radius:999px;background:linear-gradient(90deg,#7FA8D6,#FFE08A);
    animation:grow 1.2s cubic-bezier(.2,.8,.2,1) backwards var(--d,0s);
}

/* ---------- projects ---------- */
[class*="st-key-proj"]{background:var(--card);border-radius:18px;transition:transform .3s,box-shadow .3s;}
[class*="st-key-proj"]:hover{transform:translateY(-8px);box-shadow:0 16px 30px rgba(16,36,61,.22);}
.p-top{display:flex;align-items:center;gap:.5rem;color:var(--muted);font-size:.78rem;font-weight:500;text-transform:uppercase;letter-spacing:.06em;margin-top:.6rem;}
.p-title{margin:.3rem 0;font-size:1.3rem;font-weight:600;color:var(--text);}
.p-sub{color:var(--muted);font-size:.85rem;margin-bottom:.6rem;}
.badge{
    display:inline-flex;align-items:center;gap:.4rem;background:#FFE08A;color:#1F3A5F;font-weight:600;
    font-size:.8rem;padding:.3rem .8rem;border-radius:999px;margin-bottom:.6rem;
}
.badge .ico{animation:heartbeat 1.8s ease-in-out infinite;}
[data-testid="stImage"]{overflow:hidden;border-radius:14px;}
[data-testid="stImage"] img{transition:scale .4s;}
[data-testid="stImage"]:hover img{scale:1.05;}
.placeholder{
    background:var(--card2);color:var(--text);border:2px dashed var(--text);border-radius:14px;
    padding:2.6rem 1rem;text-align:center;font-weight:500;
}
.placeholder .ico{animation:floaty 3s ease-in-out infinite;}

/* ---------- native widgets ---------- */
[data-testid="stMetric"]{
    background:var(--card);border-left:6px solid var(--accent);padding:.9rem 1.1rem;border-radius:12px;
    transition:transform .25s,box-shadow .25s;
}
[data-testid="stMetric"]:hover{transform:translateY(-6px) rotate(-1deg);box-shadow:0 10px 22px rgba(16,36,61,.2);}
.stButton button,.stDownloadButton button,[data-testid="stFormSubmitButton"] button,.stLinkButton a{
    background:var(--accent)!important;border:none!important;border-radius:10px!important;
    transition:background .2s;
}
.stButton button *,.stDownloadButton button *,[data-testid="stFormSubmitButton"] button *,.stLinkButton a *{color:#10243D!important;}
.stLinkButton a{color:#10243D!important;}
.stButton button:hover,.stDownloadButton button:hover,[data-testid="stFormSubmitButton"] button:hover,.stLinkButton a:hover{
    background:var(--accent2)!important;animation:wobble .8s;
}
.stTextInput input,.stTextArea textarea,[data-baseweb="select"] > div,[data-baseweb="input"],
[data-baseweb="base-input"],[data-baseweb="textarea"]{background:var(--input)!important;color:var(--text)!important;}
[data-baseweb="tag"]{background:var(--accent)!important;}
[data-baseweb="tag"] *{color:#10243D!important;}
[data-baseweb="popover"],[data-baseweb="menu"],ul[role="listbox"]{background:var(--card)!important;color:var(--text)!important;}
li[role="option"]{color:var(--text)!important;}
[data-testid="stAlert"]{background:var(--card2)!important;border-radius:12px;}
[data-testid="stAlert"] *{color:var(--text)!important;}
[data-testid="stExpander"] details{background:var(--card);border:1px solid var(--line);border-radius:12px;}
[data-testid="stForm"]{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.2rem;}
[data-testid="stTable"] table{color:var(--text);border-color:var(--line);}
[data-testid="stTable"] th{background:var(--card2);}
[data-testid="stTable"] th,[data-testid="stTable"] td{border-color:var(--line)!important;}
.footer{display:flex;justify-content:center;align-items:center;gap:.6rem;color:var(--muted);padding:2rem 0 .8rem;}
.footer .ico{color:var(--accent);animation:heartbeat 1.6s ease-in-out infinite;}

/* ---------- menu bar (comes last so it wins over the generic button styles) ---------- */
.stApp .st-key-nav{
    background:var(--navbg);border:1px solid var(--line);border-radius:999px;padding:.55rem .7rem;
    box-shadow:0 10px 24px rgba(16,36,61,.25);margin-bottom:1.4rem;
}
.stApp .st-key-nav [data-testid="stHorizontalBlock"]{align-items:center;gap:.5rem;}
.stApp .st-key-nav [data-testid="stColumn"]{animation:none;min-width:0;}
.stApp .st-key-nav .stButton{width:100%;}
.stApp .st-key-nav button{
    width:100%;display:flex;align-items:center;justify-content:center;gap:.6rem;height:auto;
    padding:1.05rem .8rem;border:none!important;border-radius:999px;box-shadow:none!important;
    background:transparent!important;color:var(--navtext)!important;animation:none;
    transition:background .25s,translate .25s;
}
.stApp .st-key-nav button::before{content:"";flex:none;width:22px;height:22px;background:currentColor;}
.stApp .st-key-nav button *{color:inherit!important;}
.stApp .st-key-nav button p{
    position:relative;display:inline-block;margin:0;white-space:nowrap;
    font-size:1.2rem;font-weight:600;letter-spacing:.01em;
}
.stApp .st-key-nav button:hover{background:rgba(255,255,255,.14)!important;translate:0 -3px;animation:none;}
.stApp .st-key-nav button:focus,.stApp .st-key-nav button:active{
    color:var(--navtext)!important;box-shadow:none!important;outline:none;
}
/* chosen item */
.stApp .st-key-nav [class*="st-key-nav_on_"] button,
.stApp .st-key-nav [class*="st-key-nav_on_"] button:hover,
.stApp .st-key-nav [class*="st-key-nav_on_"] button:focus,
.stApp .st-key-nav [class*="st-key-nav_on_"] button:active{
    background:var(--navhl)!important;color:var(--navhltext)!important;translate:0 0;
}
.stApp .st-key-nav [class*="st-key-nav_on_"] button{animation:tabPop .45s cubic-bezier(.34,1.56,.64,1);}
.stApp .st-key-nav [class*="st-key-nav_on_"] button p{font-weight:700;}
/* typing effect: a cover in the chosen color shrinks away, its left edge is the blinking caret */
.stApp .st-key-nav [class*="st-key-nav_on_"] button p::after{
    content:"";position:absolute;top:0;bottom:0;right:-4px;width:100%;box-sizing:border-box;
    background:var(--navhl);border-left:2px solid var(--navhltext);
}
.nav-badge{
    width:64px;height:64px;border-radius:50%;display:grid;place-items:center;
    background:var(--navtext);color:var(--navbg);font-weight:800;font-size:1.3rem;letter-spacing:.02em;
}
.nav-pill{
    background:var(--navtext);color:var(--navbg);border-radius:999px;padding:1.05rem 1.6rem;
    font-weight:600;font-size:1.05rem;text-align:center;white-space:nowrap;
}
@media (max-width:900px){
    .stApp .st-key-nav button p{font-size:.95rem;}
    .stApp .st-key-nav button::before{width:16px;height:16px;}
    .nav-badge,.nav-pill{display:none;}
}

@media (prefers-reduced-motion: reduce){
    *{animation:none!important;transition:none!important;}
    .stApp .st-key-nav [class*="st-key-nav_on_"] button p::after{display:none!important;}
}
"""

# the chart is drawn by Streamlit with its own theme, so flip it in dark mode
DARK_EXTRA = '[data-testid="stVegaLiteChart"]{filter:invert(1) hue-rotate(180deg);border-radius:12px;}' if dark else ""

st.markdown(f"<style>{FONT_IMPORT}{VARS}{BASE_CSS}{nav_css()}{DARK_EXTRA}</style>", unsafe_allow_html=True)


# ---------- helpers ----------
def icon(name, size=20):
    return (
        f'<svg class="ico" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        f'{ICONS[name]}</svg>'
    )


def deco(cls, size):
    return (
        f'<svg class="deco {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'fill="currentColor">{ICONS["star"]}</svg>'
    )


def clean(s):
    # markdown treats indented lines and blank lines as code, so flatten the html first
    return "".join(line.strip() for line in s.splitlines())


def html(s):
    st.markdown(clean(s), unsafe_allow_html=True)


def heading(name, text, sub=False):
    cls = "sub-head" if sub else "sec-head"
    html(f'<div class="{cls} reveal">{icon(name, 28 if sub else 42)}<span>{text}</span></div>')


@st.cache_data
def _b64(path_str, mtime):
    path = Path(path_str)
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def img_uri(filename):
    path = IMG_DIR / filename
    return _b64(str(path), path.stat().st_mtime) if path.exists() else None


def show_image(filename, label):
    """Show the image if it exists, otherwise a labeled stand-in."""
    path = IMG_DIR / filename
    if path.exists():
        st.image(str(path), caption=label)
    else:
        html(f'<div class="placeholder">{icon("user", 34)}<br>{label}<br>(stand-in image)</div>')


def go(p):
    st.session_state.page = p


# ---------- data (edit these) ----------
skills = pd.DataFrame({
    "Skill": ["Python", "Godot", "LibreSprite", "Streamlit", "Git", "Teamwork"],
    "Category": ["Programming", "Game dev", "Art", "Programming", "Tools", "Soft skill"],
    "Level": [80, 65, 60, 65, 55, 75],
})

works = [
    {
        "title": "Team PasanAI",
        "sub": "",
        "event": "AI Ready ASEAN Youth Challenge 2026",
        "result": "Philippines Top 10 Finalist",
        "role": "[your role]",
        "tools": ["[add tools]"],
        "details": "A tracking and warning system of peatland in Indonesia.",
        "link": "https://github.com/sjq-158",
        "image": "project1.jpg",
        "icon": "activity",
    },
    {
        "title": "Se Cognos Chess",
        "sub": "",
        "event": "DOST Next Level Game Development",
        "result": "Participant",
        "role": "Participant, Moyven Team",
        "tools": ["Godot", "LibreSprite"],
        "details": "A chess game with multiple variations.",
        "link": "https://github.com/sjq-158",
        "image": "project2.jpg",
        "icon": "gamepad",
    },
    {
        "title": "Banta",
        "sub": "Dark Vessel Detection for Maritime Domain Awareness in the West Philippine Sea",
        "event": "CEISSAFP Ideathon 2026",
        "result": "Top 10 Finalist",
        "role": "[your role]",
        "tools": ["ESA Sentinel-1", "NOAA VIIRS", "AIS"],
        "details": (
            "It introduces a standing detection layer built on free satellite data: ESA Sentinel-1 "
            "radar for high-resolution detection, NOAA VIIRS night-light data for wide nightly "
            "coverage, and AIS for identity verification."
        ),
        "link": "https://github.com/sjq-158",
        "image": "project3.jpg",
        "icon": "globe",
    },
]

education = [
    ("Elementary", "Saint Theodore School, Cadulawan, Minglanilla", "2012 - 2016"),
    ("Elementary", "Minglanilla Central School", "2016 - 2018"),
    ("Junior High School", "Minglanilla Science High School", "2018 - 2022"),
    ("Senior High School", "Minglanilla Science High School", "2022 - 2024"),
    ("College", "Cebu Institute of Technology - University, BS Computer Science", "2024 - present"),
]

milestones = pd.DataFrame({
    "Year": [2012, 2016, 2018, 2022, 2024, 2026],
    "Milestone": [
        "Started elementary at Saint Theodore School",
        "Moved to Minglanilla Central School",
        "Started junior high at Minglanilla Science High School",
        "Started senior high at Minglanilla Science High School",
        "Started BS Computer Science at CIT-U",
        "Top 10 Finalist at the AI Ready ASEAN Youth Challenge and the CEISSAFP Ideathon",
    ],
})

interests = [("book", "Reading comics and books"), ("leaf", "Gardening")]

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
    all_tools = sorted({t for w in works for t in w["tools"]})
    picked_tools = st.multiselect("Show works that use", all_tools, default=all_tools)
    show_fun = st.checkbox("Show fun fact", value=True)

    st.divider()
    if st.button("Like this page", icon=":material/favorite:"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!", icon=":material/favorite:")
    st.metric("Likes", st.session_state.likes)

    summary = (
        f"{NAME}\n{SECTION}\n{PROGRAM}\n\nWorks:\n"
        + "\n".join(f"- {w['title']} ({w['event']}): {w['result']}" for w in works)
        + "\n\nSkills:\n"
        + "\n".join(f"- {r.Skill}: {r.Level}" for r in skills.itertuples())
    )
    st.download_button("Download my summary", summary, file_name="summary.txt",
                       icon=":material/download:")

# ---------- hero with id card ----------
photo_uri = img_uri("profile.jpg")
photo = f'<img src="{photo_uri}" alt="Profile photo"/>' if photo_uri else icon("user", 64)
id_rows = "".join(
    f'<div class="id-row"><span class="k">{k}</span><span class="v">{v}</span></div>'
    for k, v in [("Name", ID_NAME), ("Date of birth", ID_DOB), ("MBTI", ID_MBTI),
                 ("Hobbies", ID_HOBBIES), ("Fav color", ID_COLOR)]
)

html(f"""
<div class="hero">
{deco("d1", 34)}{deco("d2", 26)}{deco("d3", 40)}{deco("d4", 22)}
<div class="hero-left">
<div class="tags">
<span class="tag" style="--r:-4deg;--d:.1s">hello, i'm</span>
<span class="tag" style="--r:2deg;--d:.25s">{SECTION}</span>
</div>
<div class="block">{NAME}</div>
<div class="tags">
<span class="tag" style="--r:-1.5deg;--d:.4s">student · learner · builder</span>
<span class="tag" style="--r:1.5deg;--d:.55s"><span class="dot"></span>{PROGRAM}</span>
</div>
</div>
<div class="id-card">
<div class="id-head"><span class="rule"></span>ABOUT ME<span class="rule"></span></div>
<div class="id-body">
<div class="id-photo">{photo}</div>
<div class="id-fields">{id_rows}</div>
</div>
<div class="id-foot">{ID_NO}</div>
</div>
</div>
""")

# ---------- menu bar ----------
with st.container(key="nav"):
    cols = st.columns([1, 2, 2.7, 2, 2, 2, 3.4], gap="small", vertical_alignment="center")
    cols[0].markdown(f'<div class="nav-badge">{INITIALS}</div>', unsafe_allow_html=True)
    for col, p in zip(cols[1:6], PAGES):
        state = "on" if current == p else "off"
        col.button(p, key=f"nav_{state}_{p}", on_click=go, args=(p,))
    cols[6].markdown(f'<div class="nav-pill">{SECTION}</div>', unsafe_allow_html=True)

page = current

# ---------- about ----------
if page == "About":
    col_img, col_text = st.columns([1, 2], gap="large")
    with col_img:
        show_image("profile.jpg", "Photo of me")
    with col_text:
        heading("user", "About me")
        st.write(
            "I am a curious and funny kid who is still searching for answers in life. "
            "I am trying new things, looking for fresh and bold ideas, and dare to achieve "
            "bigger leaps. Yet, I also like peace, quiet and solace."
        )
        if show_fun:
            st.info("Fun fact: I need to Ctrl + F first. I am not really keen on details "
                    "about myself.", icon=":material/search:")

# ---------- autobiography ----------
elif page == "Autobiography":
    heading("book", "My story")
    left, right = st.columns(2, gap="large")
    with left:
        heading("pin", "Background", sub=True)
        st.write("I am currently living in Cebu City and Minglanilla, travelling back and forth.")

        heading("cap", "Education", sub=True)
        items = "".join(
            f'<div class="tl-item" style="--d:{i * .3}s"><div class="tl-level">{lvl}</div>'
            f'<div class="tl-text">{school} <span class="yrs">{yrs}</span></div></div>'
            for i, (lvl, school, yrs) in enumerate(education)
        )
        html(f'<div class="timeline reveal">{items}</div>')

    with right:
        heading("heart", "Interests", sub=True)
        chips = "".join(
            f'<span class="chip" style="--d:{i * .5}s">{icon(n, 20)}{t}</span>'
            for i, (n, t) in enumerate(interests)
        )
        html(f'<div class="chips">{chips}</div>')

        heading("chat", "What about you?", sub=True)
        picks = st.multiselect(
            "What about you? What do you think about me?",
            ["Curious", "Funny", "Bold", "Peaceful", "Thoughtful", "Creative",
             "Mysterious", "Hard to figure out"],
        )
        if picks:
            chips = "".join(
                f'<span class="chip" style="--d:{i * .3}s">{icon("star", 18)}{p}</span>'
                for i, p in enumerate(picks)
            )
            html(f'<div class="chips">{chips}</div>')
            st.caption("Thanks for the honest take.")

    heading("folder", "Milestones", sub=True)
    year_range = st.slider("Year range", 2012, 2026, (2012, 2026))
    shown = milestones[milestones["Year"].between(*year_range)].copy()
    shown["Year"] = shown["Year"].astype(str)
    st.table(shown.set_index("Year"))

    with st.expander("Something I'm still working on"):
        st.write("[A goal, a habit, or something you want to get better at.]")

# ---------- skills ----------
elif page == "Skills":
    heading("bars", "Skills")
    st.write("[One or two sentences about how you learned these.]")

    f1, f2 = st.columns(2)
    category = f1.selectbox("Category", ["All"] + sorted(skills["Category"].unique()))
    min_level = f2.slider("Minimum level", 0, 100, 0)

    view = skills.copy()
    if category != "All":
        view = view[view["Category"] == category]
    view = view[view["Level"] >= min_level]

    mode = st.radio("View as", ["Bars", "Chart", "Table"], horizontal=True)
    if view.empty:
        st.warning("Nothing matches those filters.")
    elif mode == "Bars":
        bars = "".join(
            f'<div class="bar"><div class="bar-top"><span>{r.Skill}</span><span>{r.Level}%</span></div>'
            f'<div class="bar-track"><div class="bar-fill" style="--w:{r.Level}%;--d:{i * .15}s"></div></div></div>'
            for i, r in enumerate(view.itertuples())
        )
        html(f'<div class="reveal">{bars}</div>')
    elif mode == "Chart":
        # in dark mode the chart gets inverted by css, so the color is picked to come out light blue
        st.bar_chart(view.set_index("Skill")["Level"], color="#3A6B9E" if dark else "#7FA8D6")
    else:
        st.table(view.set_index("Skill"))

    st.metric("Average level", f"{np.round(view['Level'].mean(), 1)}" if not view.empty else "-")

    heading("activity", "Currently improving", sub=True)
    st.progress(65, text="Streamlit: 65%")
    st.progress(55, text="Git: 55%")

# ---------- works ----------
elif page == "Works":
    heading("trophy", "Works")
    visible = [w for w in works if set(w["tools"]) & set(picked_tools)]
    if not visible:
        st.warning("No works match the tools picked in the sidebar.")
    else:
        cols = st.columns(len(visible), gap="medium")
        for i, (col, w) in enumerate(zip(cols, visible)):
            with col:
                with st.container(border=True, key=f"proj_{i}"):
                    show_image(w["image"], w["title"])
                    sub = f'<div class="p-sub">{w["sub"]}</div>' if w["sub"] else ""
                    html(f"""
                    <div class="p-top">{icon(w["icon"], 18)}<span>{w["event"]}</span></div>
                    <div class="p-title">{w["title"]}</div>
                    {sub}
                    <span class="badge">{icon("trophy", 15)}{w["result"]}</span>
                    """)
                    st.write(f"**Role:** {w['role']}")
                    st.write(f"**Tools:** {', '.join(w['tools'])}")
                    st.write(f"**Details:** {w['details']}")
                    st.link_button("View project", w["link"], icon=":material/arrow_outward:")

# ---------- contact ----------
elif page == "Contact":
    heading("mail", "Contact / feedback")
    st.write("Leave a message or tell me what you think of the page.")

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        sender = c1.text_input("Your name")
        email = c2.text_input("Email")
        topic = st.selectbox("Topic", ["Feedback", "Question", "Collaboration", "Just saying hi"])
        feeling = st.radio("How's the page?", ["Love it", "It's okay", "Needs work"], horizontal=True)
        message = st.text_area("Message")
        ok_reply = st.checkbox("It's okay to reply to my email")
        sent = st.form_submit_button("Send", icon=":material/send:")

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
        heading("chat", "Messages this session", sub=True)
        st.table(pd.DataFrame(st.session_state.messages))

html(f'<div class="footer">{icon("heart", 18)}<span>{NAME} · {SECTION}</span></div>')