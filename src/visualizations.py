import plotly.graph_objects as go


def create_radar_chart(result):

    categories = [
        "Grammar",
        "Vocabulary",
        "Readability",
        "ML Score",
        "Topic Relevance"
    ]

    values = [
        result["grammar_score"],
        result["vocabulary_score"],
        result["readability_score"],
        result["ml_score"],
        result["topic_score"]
    ]

    # Close polygon
    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Essay Evaluation'
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=550
    )

    return fig