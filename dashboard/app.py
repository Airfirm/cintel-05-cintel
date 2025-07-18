from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats
from faicons import icon_svg

UPDATE_INTERVAL_SECS: int = 3
DEQUE_SIZE: int = 5
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(-18, -16), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_dictionary_entry = {"temp": temp, "timestamp": timestamp}
    reactive_value_wrapper.get().append(new_dictionary_entry)
    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)
    latest_dictionary_entry = new_dictionary_entry
    return deque_snapshot, df, latest_dictionary_entry

ui.page_opts(title="🌐 Antarctic Live Dashboard", fillable=True)

with ui.sidebar(open="open"):
    ui.h2("🧊 Antarctic Explorer", class_="text-center")
    ui.p("Real-time temperature readings in Antarctica.", class_="text-center")
    ui.hr()
    ui.h6("Resources:")
    ui.a("GitHub Source", href="https://github.com/Airfirm/cintel-05-cintel", target="_blank")
    ui.a("GitHub App", href="https://github.com/Airfirm/cintel-05-cintel/blob/main/dashboard/app.py", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("PyShiny Express", href="https://shiny.posit.co/blog/posts/shiny-express/", target="_blank")
    ui.a("Python Standard Library", href="https://docs.python.org/3/library/index.html", target="_blank")

with ui.layout_columns():
    with ui.value_box(
        showcase=icon_svg("sun"),
        theme="bg-gradient-orange-red",
    ):
        ui.h4("🌡️ Current Temperature", class_="text-white")
        @render.text
        def display_temp():
            _, _, latest_dictionary_entry = reactive_calc_combined()
            return f"{latest_dictionary_entry['temp']} °C"
        ui.p("🔥 Warmer than usual", class_="text-warning")

    with ui.card(full_screen=True):
        ui.card_header("🕒 Current Date and Time", class_="bg-gradient-purple text-blue p-2")
        @render.text
        def display_time():
            _, _, latest_dictionary_entry = reactive_calc_combined()
            return f"{latest_dictionary_entry['timestamp']}"

with ui.card(full_screen=True):
    ui.card_header("📋 Most Recent Readings", class_="bg-primary text-white p-2")
    @render.data_frame
    def display_df():
        _, df, _ = reactive_calc_combined()
        pd.set_option('display.width', None)
        return render.DataGrid(df, width="100%")

with ui.card():
    ui.card_header("📈 Temperature Trend", class_="bg-gradient-blue text-white p-2")
    @render_plotly
    def display_plot():
        _, df, _ = reactive_calc_combined()
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            fig = px.scatter(df, x="timestamp", y="temp", title="Temperature Readings + Trend", labels={"temp": "Temp (°C)", "timestamp": "Time"}, color_discrete_sequence=["darkblue"])
            x_vals = list(range(len(df)))
            y_vals = df["temp"]
            slope, intercept, _, _, _ = stats.linregress(x_vals, y_vals)
            df['best_fit_line'] = [slope * x + intercept for x in x_vals]
            fig.add_scatter(x=df["timestamp"], y=df['best_fit_line'], mode='lines', name='Trend Line', line=dict(color='red'))
            fig.update_layout(xaxis_title="Time", yaxis_title="Temperature (°C)")
        return fig

