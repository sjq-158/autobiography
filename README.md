# Autobiography and Portfolio

A personal site built with Streamlit for Applied AI.
It has my autobiography, my skills, three projects, and a contact form.

**Name:** Ericka Fatima Reign R. Ligaray
**Section:** [Your Section]
**Live app:** [paste your .streamlit.app link here]

## What's inside

- About, Autobiography, Skills, Projects, and Contact tabs
- A sidebar with filters, a like button, and a downloadable summary
- Skills shown as a table and a bar chart
- A contact form that responds after you submit it

### Streamlit components used

`title`, `header`, `subheader`, `write`, `markdown`, `dataframe`, `bar_chart`,
`button`, `slider`, `selectbox`, `checkbox`, `text_input`, `text_area`, `radio`,
`multiselect`, `sidebar`, `columns`, `image`, `tabs`, `metric`, `form`,
`session_state`, `download_button`, `progress`, `expander`, `container`,
`toast`, `balloons`, `link_button`, and a custom theme.

## Run it locally

Windows (PowerShell):

```powershell
git clone https://github.com/sjq-158/autobiography.git
cd autobiography
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Mac/Linux:

```bash
git clone https://github.com/sjq-158/autobiography.git
cd autobiography
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Folder structure

```
autobiography/
├── .streamlit/config.toml   # theme colors
├── assets/images/           # profile and project pictures
├── app.py                   # the app
├── requirements.txt
└── README.md
```

## Editing the content

Personal details are near the top of `app.py` (name, section, skills, projects,
milestones). Add pictures to `assets/images/` and match the filenames.

## Deploy on Streamlit Community Cloud

1. Push the repo to GitHub (it must be public and include `requirements.txt`).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app**, pick this repo, branch `main`, and main file `app.py`.
4. Deploy, then paste the link at the top of this README.

## Design

- Colors: `#7FA8D6`, `#FFF2B2`, `#A8C6E7`, `#FFE08A`, `#FFF7D6`
- Font: Poppins