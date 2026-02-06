import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H1("Student Dashboard", style={'textAlign': 'left', 'margin': '10px', "fontSize": '30px'}),

        html.Div([
            html.Button("Home", style={'borderRadius': '10px', 'backgroundColor': '#2c3e50', 'color': 'white', 'border': 'none', 'padding': '8px 18px', "fontSize": '20px'}),
            html.Button("Exam History", style={'borderRadius': '10px', 'backgroundColor': '#2c3e50', 'color': 'white', 'border': 'none', 'padding': '8px 18px', "fontSize": '20px'}),
            html.Button("Logout", style={'borderRadius': '10px', 'backgroundColor': '#e74c3c', 'color': 'white', 'border': 'none', 'padding': '8px 18px', "fontSize": '20px'})
        ], style={
            "display": "flex",
            "gap": "20px",
            'justifyContent': 'flex-end',
            'alignItems': 'center'
        })

    ], style={
        "backgroundColor": "#2c3e50",
        "color": "white",
        "padding": "10px 20px",
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center"
    }),

    html.Div([

        html.Div([
            html.H2("Student Information", style={"fontSize": '30px'}),
            html.Img(src="/assets/ben.jpg", alt="Student Photo",
                     style={"borderRadius": "50%", "marginBottom": "0px", 'width': '300px', 'height': '280px'}),

            html.P("Ben10", style={"fontSize": '20px', 'fontWeight': 'bold', 'textAlign': 'center', 'margin': '0px'}),
            html.P("4MC24CS164", style={"fontSize": '20px', 'fontWeight': 'bold', 'textAlign': 'center', 'margin': '0px'}),
            html.P("ben10@gmail.com", style={"fontSize": '20px', 'fontWeight': 'bold', 'textAlign': 'center', 'margin': '0px'}),

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

        ], style={"backgroundColor": "#f8f9fa", "padding": "10px", "flex": "1"}),

        html.Div([
            html.H1("Main Content")
        ], style={"padding": "20px", "flex": "4"})

    ], style={"display": "flex", "minHeight": "90vh"})

])

if __name__ == '__main__':
    app.run(debug=True)
