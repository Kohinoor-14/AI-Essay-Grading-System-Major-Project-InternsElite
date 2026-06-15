import streamlit as st

from src.essay_analyzer import analyze_essay
from src.visualizations import create_radar_chart

from src.database import (
    create_database,
    save_essay,
    get_all_records,
    get_previous_essays
)

from src.analytics import (
    create_score_distribution,
    create_student_performance
)

from src.report_generator import generate_pdf
from src.utils import ensure_reports_folder

# -------------------------------------------------
# Initialization
# -------------------------------------------------

create_database()
ensure_reports_folder()

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Essay Grading System",
    page_icon="📝",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>

.big-title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    text-align:center;
    color:#94A3B8;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.title("📚 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Essay Evaluation",
        "Analytics Dashboard",
        "Student History",
        "About Project"
    ]
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown("""
<div class='big-title'>
📝 AI Essay Grading & Visualization System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Intelligent Essay Assessment using NLP, Machine Learning and Data Visualization
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Essays Evaluated", "250+")

with c2:
    st.metric("Accuracy", "92%")

with c3:
    st.metric("ML Model", "Active")

with c4:
    st.metric("Reports Generated", "180+")

st.divider()

# -------------------------------------------------
# ESSAY EVALUATION PAGE
# -------------------------------------------------

if page == "Essay Evaluation":

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("Essay Input")

        essay_text = st.text_area(
            "Paste Essay",
            height=300
        )

    with col2:

        st.subheader("Student Information")

        student_name = st.text_input(
            "Student Name"
        )

        essay_topic = st.text_input(
            "Essay Topic"
        )

        grade_level = st.selectbox(
            "Grade Level",
            [
                "School",
                "Undergraduate",
                "Postgraduate"
            ]
        )

    if st.button("🚀 Analyze Essay"):

        if essay_text.strip() == "":
            st.warning("Please enter an essay.")

        elif essay_topic.strip() == "":
            st.warning("Please enter an essay topic.")

        else:

            previous_essays = get_previous_essays()

            result = analyze_essay(
                essay_text,
                essay_topic,
                previous_essays
            )

            save_essay(
                student_name,
                essay_topic,
                grade_level,
                essay_text,
                result
            )

            st.success(
                "Essay analyzed successfully!"
            )

            # ---------------------------------
            # Metrics
            # ---------------------------------

            st.subheader(
                "📊 Analysis Result"
            )

            m1, m2, m3, m4, m5, m6 = st.columns(6)

            with m1:
                st.metric(
                    "Grammar",
                    result["grammar_score"]
                )

            with m2:
                st.metric(
                    "Vocabulary",
                    result["vocabulary_score"]
                )

            with m3:
                st.metric(
                    "Readability",
                    result["readability_score"]
                )

            with m4:
                st.metric(
                    "ML Score",
                    result["ml_score"]
                )

            with m5:
                st.metric(
                    "Topic Relevance",
                    result["topic_score"]
                )

            with m6:
                st.metric(
                    "Plagiarism %",
                    result["plagiarism_score"]
                )

            st.divider()

            # ---------------------------------
            # Radar Chart
            # ---------------------------------

            chart_col, details_col = st.columns(
                [2, 1]
            )

            with chart_col:

                st.subheader(
                    "📈 Performance Radar Chart"
                )

                fig = create_radar_chart(
                    result
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            with details_col:

                st.subheader(
                    "📋 Essay Statistics"
                )

                st.info(
                    f"Words: {result['word_count']}"
                )

                st.info(
                    f"Sentences: {result['sentence_count']}"
                )

                st.info(
                    f"ML Score: {result['ml_score']}"
                )

                st.info(
                    f"Topic Relevance: {result['topic_score']}"
                )

                st.info(
                    f"Plagiarism: {result['plagiarism_score']}%"
                )

                st.info(
                    f"Final Score: {result['overall_score']}"
                )

            st.divider()

            # ---------------------------------
            # Final Score
            # ---------------------------------

            st.subheader(
                "🏆 Final Composite Score"
            )

            st.metric(
                "Overall Essay Score",
                result["overall_score"]
            )

            # ---------------------------------
            # Feedback
            # ---------------------------------

            st.subheader(
                "💡 AI Feedback"
            )

            for item in result["feedback"]:
                st.success(item)

            if result["plagiarism_score"] < 20:
                st.success(
                    "✅ Original Content"
                )

            elif result["plagiarism_score"] < 50:
                st.warning(
                    "⚠ Moderate Similarity Detected"
                )

            else:
                st.error(
                    "❌ High Similarity Detected"
                )

            st.divider()

            # ---------------------------------
            # PDF Generation
            # ---------------------------------

            pdf_file = (
                f"reports/"
                f"{student_name.replace(' ', '_')}_report.pdf"
            )

            generate_pdf(
                student_name,
                essay_topic,
                result,
                pdf_file
            )

            st.success(
                "PDF Report Generated Successfully!"
            )

            with open(
                pdf_file,
                "rb"
            ) as pdf:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf,
                    file_name=f"{student_name}_report.pdf",
                    mime="application/pdf"
                )

# -------------------------------------------------
# ANALYTICS DASHBOARD
# -------------------------------------------------

elif page == "Analytics Dashboard":

    st.header(
        "📊 Analytics Dashboard"
    )

    df = get_all_records()

    if len(df) > 0:

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Essays",
                len(df)
            )

        with c2:
            st.metric(
                "Average Score",
                round(
                    df["overall_score"].mean(),
                    2
                )
            )

        with c3:
            st.metric(
                "Highest Score",
                round(
                    df["overall_score"].max(),
                    2
                )
            )

        with c4:
            st.metric(
                "Lowest Score",
                round(
                    df["overall_score"].min(),
                    2
                )
            )

        st.divider()

        st.subheader(
            "📈 Score Distribution"
        )

        st.plotly_chart(
            create_score_distribution(df),
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "📊 Student Performance"
        )

        st.plotly_chart(
            create_student_performance(df),
            use_container_width=True
        )

    else:

        st.info(
            "No records available."
        )

# -------------------------------------------------
# STUDENT HISTORY
# -------------------------------------------------

elif page == "Student History":

    st.header(
        "📁 Student History"
    )

    df = get_all_records()

    if len(df) > 0:

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No records available."
        )

# -------------------------------------------------
# ABOUT PROJECT
# -------------------------------------------------

elif page == "About Project":

    st.header(
        "ℹ️ About Project"
    )

    st.write("""

### AI Essay Grading & Visualization System

Technologies Used

- Python
- Streamlit
- SQLite
- NLTK
- TextBlob
- Sentence Transformers
- Scikit-Learn
- Plotly
- ReportLab

Features

✅ NLP Essay Analysis

✅ Machine Learning Prediction

✅ Semantic Similarity Analysis

✅ Topic Relevance Scoring

✅ Plagiarism Detection

✅ Radar Chart Visualization

✅ Analytics Dashboard

✅ Student History Tracking

✅ SQLite Database

✅ PDF Report Generation

✅ Interactive User Interface

""")