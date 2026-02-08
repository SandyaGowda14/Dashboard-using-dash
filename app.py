import dash
from dash import html, dcc
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

    #app creation

app = dash.Dash(__name__)

    #data set

df = pd.read_csv("dataset.csv")

skill_df = pd.read_csv("skill.csv")

    #graph creation

#bar chart for marks

fig=px.bar(df,
             x="Subject",
             y="Marks",
             #color="Subject",
             range_y=[0, 100],
             color_discrete_sequence=px.colors.qualitative.Pastel )

fig.update_traces(marker_color="#415a77", opacity=1.0,) 

#doughnut chart for skill

pie_graph = px.pie(skill_df, 
                   values='percentage', 
                   names='skill',
                   hole=0.45,
                   color_discrete_sequence=px.colors.qualitative.Pastel)

pie_graph.update_traces(
    marker=dict(colors=[
        "#415a77",  # dark
        "#4f6d8c",
        "#6f8fa6",
        "#9bb3c7"
    ]),
    textinfo="percent",
)

#app layout

app.layout = html.Div([

    html.Div([
        html.H1("Student Dashboard",
                style={'textAlign': 'left',
                        'margin': '10px',
                          "fontSize": '30px'}),

        html.Div([
            html.Button("Home",
                        style={'borderRadius': '10px',
                                'backgroundColor': '#2c3e50',
                                  'color': 'white',
                                    'border': 'none',
                                      'padding': '8px 18px',
                                        "fontSize": '20px'}),


            html.Button("Exam History", 
                        style={'borderRadius': '10px',
                                'backgroundColor': '#2c3e50',
                                  'color': 'white',
                                    'border': 'none',
                                      'padding': '8px 18px',
                                        "fontSize": '20px'}),


            html.Button("Logout",
                         style={'borderRadius': '10px',
                                 'backgroundColor': '#e74c3c',
                                   'color': 'white',
                                     'border': 'none',
                                       'padding': '8px 18px',
                                         "fontSize": '20px'})

        ], 
        
        style={
            "display": "flex",
            "gap": "20px",
            'justifyContent': 'flex-end',
            'alignItems': 'center'
        })

    ], 
    
    style={
        "backgroundColor": "#2c3e50",
        "color": "white",
        "padding": "10px 20px",
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center"
    }),

    html.Div([

        html.Div([
            html.H2("Student Information",
                     style={"fontSize": '30px'}),

            html.Img(src="/assets/ben.jpg", alt="Student Photo",
                     style={"borderRadius": "50%",
                             "marginBottom": "0px",
                               'width': '300px', 
                               'height': '280px',
                               'display': 'block', 
                               'marginLeft': 'auto',
                                 'marginRight': 'auto'}),

            html.P("Ben10", 
                   style={"fontSize": '20px', 
                          'fontWeight': 'bold', 
                          'textAlign': 'center', 
                          'margin': '0px'}),

            html.P("4MC24CS164",
                    style={"fontSize": '20px', 
                           'fontWeight': 'bold',
                             'textAlign': 'center', 
                             'margin': '0px'}),
            html.P("ben10@gmail.com",
                    style={"fontSize": '20px',
                            'fontWeight': 'bold', 
                            'textAlign': 'center', 
                            'margin': '0px'}),

            html.Br(),
            html.Hr(style={"border": "1px solid #dee2e6"}),

            html.P("Achievements", style={
                "fontSize": "30px",
                "textAlign": "center",
                "margin": "0px",
                "fontWeight": "bold"
            }),

            html.Ul([
                html.Li("Top Scorer in Data Structures 🧑‍💻"),
                html.Li("College cricket team captain 2025 🏏"),
                html.Li("Branch Representative for Computer Science")
            ], style={
                "listStyleType": "square",
                "paddingLeft": "10px",
                "textAlign": "left", 
                "fontSize": "18px",
                "fontWeight": "bold",
            }),

        ], style={"backgroundColor": "#f8f9fa", "padding": "10px", "flex": "0.5"}),

        html.Div([
            html.H1("CIE Marks", style={"fontSize": '30px'}),
            dcc.Graph(figure = fig,responsive=True, style={"height": "400px",'width': "100%",'magintop': "2000px",'paddingtop': "200px"})
        ], style={"padding": "20px", "flex": "1"}),
        
    html.Div([
        html.H1("Skill Distribution", style={"fontSize": '30px'}),
            dcc.Graph(figure=pie_graph,responsive=True,style={"height": "400px",'width': "100%", "marginTop": "20px"})
                ], style={"padding": "20px", "flex": "1"})
   
    ], style={"display": "flex", "minHeight": "90vh"}),

])

if __name__ == '__main__':
    app.run(debug=True)
