from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime
import random


def generate_pdf(
        student_name,
        essay_topic,
        result,
        filename):

    doc = SimpleDocTemplate(filename)

    # PDF Metadata
    doc.title = "AI Essay Evaluation Report"
    doc.author = "Kohinoor Soni"
    doc.subject = "AI Essay Grading & Visualization System"

    styles = getSampleStyleSheet()

    content = []

    # =====================================
    # Logo
    # =====================================

    try:

        logo = Image(
            "assets/logo.png",
            width=120,
            height=120
        )

        content.append(logo)

    except Exception:
        pass

    # =====================================
    # Header
    # =====================================

    content.append(
        Paragraph(
            "KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "AI Essay Grading & Visualization System",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # Report Information
    # =====================================

    report_id = (
        "REP-" +
        str(random.randint(1000, 9999))
    )

    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    content.append(
        Paragraph(
            f"<b>Report ID:</b> {report_id}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Date:</b> {current_time}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # Student Information
    # =====================================

    content.append(
        Paragraph(
            "Student Information",
            styles["Heading2"]
        )
    )

    student_table = Table(
        [
            ["Student Name", student_name],
            ["Essay Topic", essay_topic]
        ],
        colWidths=[120, 250]
    )

    student_table.setStyle(
        TableStyle([

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black),

            ("BACKGROUND",
             (0, 0),
             (0, -1),
             colors.lightgrey),

            ("FONTNAME",
             (0, 0),
             (0, -1),
             "Helvetica-Bold")

        ])
    )

    content.append(student_table)

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # Evaluation Results
    # =====================================

    content.append(
        Paragraph(
            "Evaluation Results",
            styles["Heading2"]
        )
    )

    score_table = Table(
        [

            ["Metric", "Score"],

            ["Grammar Score",
             str(result["grammar_score"])],

            ["Vocabulary Score",
             str(result["vocabulary_score"])],

            ["Readability Score",
             str(result["readability_score"])],

            ["ML Score",
             str(result["ml_score"])],

            ["Topic Relevance",
             str(result["topic_score"])],

            ["Plagiarism %",
             str(result["plagiarism_score"])],

            ["Final Score",
             str(result["overall_score"])]

        ],
        colWidths=[220, 120]
    )

    score_table.setStyle(
        TableStyle([

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black),

            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.lightblue),

            ("FONTNAME",
             (0, 0),
             (-1, 0),
             "Helvetica-Bold"),

            ("ALIGN",
             (1, 1),
             (1, -1),
             "CENTER")

        ])
    )

    content.append(score_table)

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # Grade Calculation
    # =====================================

    final_score = result["overall_score"]

    if final_score >= 90:
        grade = "A+"

    elif final_score >= 80:
        grade = "A"

    elif final_score >= 70:
        grade = "B"

    elif final_score >= 60:
        grade = "C"

    else:
        grade = "D"

    content.append(
        Paragraph(
            f"<b>Final Grade:</b> {grade}",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # Performance Summary
    # =====================================

    content.append(
        Paragraph(
            "Performance Summary",
            styles["Heading2"]
        )
    )

    if final_score >= 90:

        summary = """
        Excellent performance. The essay demonstrates
        strong grammar, readability, vocabulary usage,
        topic relevance, and originality.
        """

    elif final_score >= 75:

        summary = """
        Good performance. The essay is well structured
        with minor areas for improvement.
        """

    else:

        summary = """
        Average performance. Further improvement in
        grammar, vocabulary, readability and content
        quality is recommended.
        """

    content.append(
        Paragraph(
            summary,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # AI Feedback
    # =====================================

    content.append(
        Paragraph(
            "AI Feedback",
            styles["Heading2"]
        )
    )

    for item in result["feedback"]:

        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # Footer
    # =====================================

    content.append(
        Paragraph(
            "------------------------------------------------------------",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Generated by AI Essay Grading & Visualization System",
            styles["Italic"]
        )
    )

    content.append(
        Paragraph(
            "Department of Computer Science & Engineering",
            styles["Italic"]
        )
    )

    content.append(
        Paragraph(
            "KIIT University",
            styles["Italic"]
        )
    )

    # =====================================
    # Build PDF
    # =====================================

    doc.build(content)