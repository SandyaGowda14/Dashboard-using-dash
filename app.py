import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# App creation
app = dash.Dash(__name__)

# =======================
# Dataset
# =======================

df = pd.read_csv("dataset.csv")
skill_df = pd.read_csv("skill.csv")

# =======================
# Graph Creation
# =======================

# Bar chart for marks
fig = px.bar(
    df,
    x="Subject",
    y="Marks",
    range_y=[0, 100],
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(
    marker_color="#415a77",
    opacity=1.0
)

# Doughnut chart for skills
pie_graph = px.pie(
    skill_df,
    values="percentage",
    names="skill",
    hole=0.45,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

pie_graph.update_traces(
    marker=dict(
        colors=[
            "#415a77",
            "#4f6d8c",
            "#6f8fa6",
            "#9bb3c7"
        ]
    ),
    textinfo="percent"
)

# Line graph for marks trend
line_fig = px.line(
    df,
    x="Subject",
    y="Marks",
    markers=True
)

line_fig.update_traces(
    line=dict(color="#1b263b", width=3),
    marker=dict(size=8)
)

line_fig.update_layout(
    yaxis_range=[0, 100]
)

# =======================
# App Layout
# =======================

app.layout = html.Div([

    # Header Section
    html.Div([

        html.H1(
            "Student Dashboard",
            style={
                "margin": "10px",
                "fontSize": "30px"
            }
        ),

        html.Div([
            html.Button(
                "Home",
                style={
                    "borderRadius": "10px",
                    "backgroundColor": "#2c3e50",
                    "color": "white",
                    "border": "none",
                    "padding": "8px 18px",
                    "fontSize": "18px"
                }
            ),

            html.Button(
                "Exam History",
                style={
                    "borderRadius": "10px",
                    "backgroundColor": "#2c3e50",
                    "color": "white",
                    "border": "none",
                    "padding": "8px 18px",
                    "fontSize": "18px"
                }
            ),

            html.Button(
                "Logout",
                style={
                    "borderRadius": "10px",
                    "backgroundColor": "#e74c3c",
                    "color": "white",
                    "border": "none",
                    "padding": "8px 18px",
                    "fontSize": "18px"
                }
            )

        ], style={
            "display": "flex",
            "gap": "20px",
            "alignItems": "center"
        })

    ], style={
        "backgroundColor": "#2c3e50",
        "color": "white",
        "padding": "10px 20px",
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center"
    }),

    # Main Body
    html.Div([

        # Student Information Section
        html.Div([
            html.H2("Student Information", style={"fontSize": "28px"}),

            html.Img(
                src="/assets/ben.jpg",
                alt="Student Photo",
                style={
                    "borderRadius": "50%",
                    "width": "250px",
                    "height": "250px",
                    "display": "block",
                    "margin": "auto"
                }
            ),

            html.P("Ben10", style={
                "fontSize": "18px",
                "fontWeight": "bold",
                "textAlign": "center"
            }),

            html.P("4MC24CS164", style={
                "fontSize": "18px",
                "fontWeight": "bold",
                "textAlign": "center"
            }),

            html.P("ben10@gmail.com", style={
                "fontSize": "18px",
                "fontWeight": "bold",
                "textAlign": "center"
            }),

            html.Br(),
            html.Hr(),

            html.H3("Achievements", style={
                "textAlign": "center",
                "fontWeight": "bold"
            }),

            html.Ul([
                html.Li("Top Scorer in Data Structures 🧑‍💻"),
                html.Li("College cricket team captain 2025 🏏"),
                html.Li("Branch Representative for Computer Science")
            ], style={
                "fontSize": "16px",
                "fontWeight": "bold"
            }),

        ], style={
            "backgroundColor": "#f8f9fa",
            "padding": "20px",
            "flex": "0.8"
        }),

        # Graph Section
        html.Div([

            html.H2("CIE Marks (Bar Chart)"),
            dcc.Graph(
                figure=fig,
                style={"height": "350px"}
            ),

            html.H2("Marks Trend (Line Graph)"),
            dcc.Graph(
                figure=line_fig,
                style={"height": "350px"}
            ),

            html.H2("Skill Distribution (Doughnut Chart)"),
            dcc.Graph(
                figure=pie_graph,
                style={"height": "350px"}
            )

        ], style={
            "padding": "20px",
            "flex": "2"
        })

    ], style={
        "display": "flex",
        "minHeight": "90vh"
    })

])

# =======================
# Run App
# =======================

if __name__ == "__main__":
    app.run(debug=True)
 