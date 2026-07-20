from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "Islam_Mansour_CV.pdf"

NAVY = colors.HexColor("#072033")
TEAL = colors.HexColor("#007a74")
INK = colors.HexColor("#191e22")
GRAY = colors.HexColor("#536069")
PALE = colors.HexColor("#9eb5b4")


def section(title, styles):
    return [
        Spacer(1, 2.6 * mm),
        Paragraph(title.upper(), styles["Section"]),
        Spacer(1, 0.8 * mm),
        HRFlowable(width="100%", thickness=0.55, color=PALE, spaceBefore=0, spaceAfter=1.35 * mm),
    ]


def entry(title, stack, description, styles, date=None):
    right = f'<font color="#536069"><i>{date}</i></font>' if date else ""
    heading = (
        f'<b><font color="#072033">{title}</font></b>'
        f'  <font color="#536069"><i>|  {stack}</i></font>'
        f'{("<br/>" + right) if right else ""}'
    )
    return KeepTogether([
        Paragraph(heading, styles["EntryTitle"]),
        Paragraph(description, styles["Body"]),
    ])


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=14.5 * mm,
        rightMargin=14.5 * mm,
        topMargin=11.5 * mm,
        bottomMargin=10.5 * mm,
        title="Islam Mansour - Applied Data Science CV",
        author="Islam Mansour",
        subject="CV for data science, machine learning and data engineering roles",
    )

    base = getSampleStyleSheet()
    styles = {
        "Name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=23,
            leading=23, textColor=NAVY, spaceAfter=1.2 * mm,
        ),
        "Role": ParagraphStyle(
            "Role", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.5,
            leading=9.2, textColor=TEAL, spaceAfter=1.5 * mm,
        ),
        "Contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica", fontSize=8.2,
            leading=9, textColor=GRAY, spaceAfter=1.2 * mm,
        ),
        "Summary": ParagraphStyle(
            "Summary", parent=base["Normal"], fontName="Helvetica", fontSize=9.05,
            leading=11.15, textColor=INK, spaceBefore=1.7 * mm, spaceAfter=0,
        ),
        "Section": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.45,
            leading=10.2, textColor=TEAL, tracking=0.7, spaceAfter=0,
        ),
        "EntryTitle": ParagraphStyle(
            "EntryTitle", parent=base["Normal"], fontName="Helvetica", fontSize=8.9,
            leading=10.2, textColor=INK, spaceBefore=0.6 * mm, spaceAfter=0.5 * mm,
        ),
        "Body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica", fontSize=8.55,
            leading=10.25, textColor=INK, spaceAfter=1.45 * mm,
        ),
        "Compact": ParagraphStyle(
            "Compact", parent=base["Normal"], fontName="Helvetica", fontSize=8.55,
            leading=10.1, textColor=INK, spaceAfter=0.95 * mm,
        ),
    }

    story = [
        Paragraph("ISLAM MANSOUR", styles["Name"]),
        Paragraph("APPLIED DATA SCIENCE STUDENT  |  MACHINE LEARNING &amp; DATA ENGINEERING", styles["Role"]),
        Paragraph("Hamburg, Germany  |  +49 176 34249274  |  islamwm05@outlook.de", styles["Contact"]),
        HRFlowable(width="100%", thickness=1.1, color=NAVY, spaceBefore=0.4 * mm, spaceAfter=0),
        Paragraph(
            "Applied Data Science student ranked 6th in the degree program at TU Hamburg. "
            "Builds end-to-end products across machine learning, ETL, backend APIs, media processing and interactive analytics, "
            "with a focus on reliable implementation, validation and clear business-facing outputs.",
            styles["Summary"],
        ),
    ]

    story += section("Education", styles)
    story.append(entry(
        "B.Sc. Applied Data Science - Hamburg University of Technology (TU Hamburg)",
        "Ranked 6th in the degree program",
        "Focus: machine learning, statistics, databases and data engineering. Relevant coursework includes Big Data, algorithms and data structures, and statistics.",
        styles,
        "2022 - 2026",
    ))

    story += section("Selected Projects", styles)
    story.extend([
        entry(
            "Production-Style Churn Prediction API",
            "Python | Scikit-learn | FastAPI | Pydantic",
            "Deployed a trained gradient-boosting model as a documented REST API. Added schema validation, health-check endpoints, batch prediction and model serialization.",
            styles,
        ),
        entry(
            "ETL Pipeline &amp; Data Warehouse",
            "Python | SQL | Pandas | SQLite",
            "Integrated CSV, JSON and SQLite sources into staging and mart layers. Implemented CTEs, window functions, automated SQL views and six passing data-quality tests covering nulls, uniqueness and referential integrity.",
            styles,
        ),
        entry(
            "Interactive Sales Dashboard",
            "Streamlit | Plotly | SQLite | Flask",
            "Built a dashboard with cached SQL access, KPI cards and live filters for region, month and category.",
            styles,
        ),
        entry(
            "Chess API with AI",
            "FastAPI | Pydantic | SQLite | Minimax | Stockfish",
            "Implemented legal-move validation, persistent PvP games, move history and selectable minimax, random or Stockfish opponents.",
            styles,
        ),
        entry(
            "Git-Style Repository API",
            "REST API | Push/Pull Workflows",
            "Created API-driven push and pull workflows for transferring and synchronizing project content.",
            styles,
        ),
        entry(
            "Media Optimization API",
            "REST API | Image & Video Processing",
            "Built automated upload and transformation endpoints that optimize images and selected video formats.",
            styles,
        ),
        entry(
            "Virtual GPU Renderer",
            "Python | NumPy | Rasterization | Shaders",
            "Implemented a software GPU pipeline with programmable shaders, depth testing, textures and Phong lighting.",
            styles,
        ),
        entry(
            "Data Cleaning & EDA",
            "Python | Pandas | Seaborn | Matplotlib",
            "Resolved missing values, duplicates, category inconsistencies and outliers in real-estate data, then produced statistical and visual analysis.",
            styles,
        ),
        Paragraph(
            '<b><font color="#072033">Additional projects:</font></b> '
            "NLP sentiment analysis, four-model churn benchmark, automated PDF reporting, C++ ray tracing, animated 3D chess and C terminal games.",
            styles["Body"],
        ),
    ])

    story += section("Technical Skills", styles)
    story.extend([
        Paragraph('<b><font color="#072033">Programming:</font></b> Python, SQL, C++, C', styles["Compact"]),
        Paragraph('<b><font color="#072033">Data &amp; ML:</font></b> Pandas, NumPy, Scikit-learn, Gradient Boosting, Random Forest, NLP, TF-IDF, Matplotlib, Seaborn, Plotly', styles["Compact"]),
        Paragraph('<b><font color="#072033">Engineering &amp; Tools:</font></b> REST APIs, ETL pipelines, Pydantic, SQLite, FastAPI, Flask, Streamlit, Git, media processing, software rendering, Linux', styles["Compact"]),
    ])

    story += section("Languages", styles)
    story.append(Paragraph(
        '<b><font color="#072033">Arabic:</font></b> Native &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; '
        '<b><font color="#072033">German:</font></b> Fluent &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; '
        '<b><font color="#072033">English:</font></b> Fluent',
        styles["Compact"],
    ))

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
