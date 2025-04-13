# app.py
import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

# Load predicted data (exported from PySpark as CSV)
df = pd.read_csv("predicted_stock_prices.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = dash.Dash(__name__)

symbols = df["symbol"].unique()

app.layout = html.Div([
    html.H1("Stock Price Prediction Dashboard"),
    dcc.Dropdown(
        id="symbol-dropdown",
        options=[{"label": s, "value": s} for s in symbols],
        value=symbols[0]
    ),
    dcc.Graph(id="stock-graph")
])

@app.callback(
    dash.dependencies.Output("stock-graph", "figure"),
    [dash.dependencies.Input("symbol-dropdown", "value")]
)
def update_graph(symbol):
    filtered_df = df[df["symbol"] == symbol]
    return {
        "data": [
            go.Scatter(x=filtered_df["Date"], y=filtered_df["Next_Close"], name="Actual"),
            go.Scatter(x=filtered_df["Date"], y=filtered_df["prediction"], name="Predicted")
        ],
        "layout": go.Layout(title=f"Predictions for {symbol}")
    }

if __name__ == "__main__":
    app.run(debug=True)

