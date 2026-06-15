import plotly.express as px


def create_score_distribution(df):

    fig = px.histogram(
        df,
        x="overall_score",
        nbins=10,
        title="Score Distribution"
    )

    return fig


def create_student_performance(df):

    fig = px.bar(
        df,
        x="student_name",
        y="overall_score",
        color="overall_score",
        title="Student Performance"
    )

    return fig