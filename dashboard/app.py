# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    modelResults,
    econimicalDiscussion,
    technology,
    discussion,
    conclusions,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/price-performance":
        return modelResults.create_layout(app)
    elif pathname == "/dash-financial-report/portfolio-management":
        return econimicalDiscussion.create_layout(app)
    elif pathname == "/dash-financial-report/fees":
        return technology.create_layout(app)
    elif pathname == "/dash-financial-report/discussion":
        return discussion.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return conclusions.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            modelResults.create_layout(app),
            econimicalDiscussion.create_layout(app),
            technology.create_layout(app),
            discussion.create_layout(app),
            conclusions.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
