# Ericka Ligaray - Portfolio

My personal portfolio website for CS365 (Applied AI), built with Streamlit. It has my intro, my story, my interests, my skills, and the competitions I've joined.

## Pages

- **About** - a short intro and a photo of the student
- **Autobiography** - background, education timeline, interests, and a milestones table
- **Skills** - my skill levels, viewable as bars, a chart, or a table
- **Works** - Team PasanAI, Se Cognos Chess, and Banta
- **Contact** - a feedback form

## Running it

You need Python 3.9 or newer.

```bash
pip install streamlit pandas numpy pillow
streamlit run app.py
```

Then open the link Streamlit prints in the terminal (usually http://localhost:8501).

You can also access the program based on this link as well, https://autobiography-erickafatimaligaray.streamlit.app/. 

## Folder structure

```
.
├── app.py
├── README.md
└── assets
    └── images
        ├── profile.jpg     (About page photo)
        ├── profile2.jpg    (ID card photo)
        ├── project1.png
        ├── project2.png
        └── project3.jpg
```

If an image is missing, the page shows a placeholder instead of crashing.

## Content
Most of the content is near the top or in the data section of `app.py`:

- Name, section, and program are the constants at the top
- ID card details are the `ID_` variables
- Skills are in the `skills` table
- Projects are in the `works` list
- Education, milestones, and interests are in their own lists below that


## Made by
Ericka Fatima Reign R. Ligaray
BS Computer Science, 3rd year, Cebu Institute of Technology - University