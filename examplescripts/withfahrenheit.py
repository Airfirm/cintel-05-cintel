# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

from shiny import reactive, render
from shiny.express import ui, input
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats
from faicons import icon_svg

# --------------------------------------------
UPDATE_INTERVAL_SECS: int = 3
DEQUE_SIZE: int = 5
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp_c = round(random.uniform(-18, -16), 1)
    temp_f = round((temp_c * 9 / 5) + 32, 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = {"temp_c": temp_c, "temp_f": temp_f, "timestamp": timestamp}
    reactive_value_wrapper.get().append(new_entry)
    df = pd.DataFrame(reactive_value_wrapper.get())
    return reactive_value_wrapper.get(), df, new_entry

ui.page_opts(title="PyShiny Express: Live Data Example", fillable=True)

with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p("A demonstration of real-time temperature readings in Antarctica.", class_="text-center")
    ui.input_switch("temp_unit", "Display Temperature in Fahrenheit", False)
    ui.hr()
    ui.h6("Links:")
    ui.a("GitHub Source", href="https://github.com/Afm/cintel-0-intel/", target="_blank")
    ui.a("GitHub App", href="https://github.com/Afm/cintel-0-intel/", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("PyShiny Express", href="https://shiny.posit.co/blog/posts/shiny-express/", target="_blank")
    ui.a("Python Standard Library", href="https://docs.python.org/3/library/index.html", target="_blank")

with ui.layout_columns():
    with ui.value_box(showcase=icon_svg("sun"), theme="bg-gradient-orange-red"):
        "Current Temperature"
        @render.text
        def display_temp():
            _, _, latest = reactive_calc_combined()
            temp = latest['temp_f'] if input.temp_unit() else latest['temp_c']
            unit = "F" if input.temp_unit() else "C"
            return f"{temp} °{unit}"
        ui.p("warmer than usual")

    with ui.card(full_screen=True):
        ui.card_header("Current Date and Time", class_="text-primary")
        @render.text
        def display_time():
            _, _, latest = reactive_calc_combined()
            return f"{latest['timestamp']}"

with ui.card(full_screen=True):
    ui.card_header("Most Recent Readings", class_="text-success")
    @render.data_frame
    def display_df():
        _, df, _ = reactive_calc_combined()
        df = df.rename(columns={"temp_c": "Temp (C)", "temp_f": "Temp (F)"})
        return render.DataGrid(df, width="100%")

with ui.card():
    ui.card_header("Chart with Current Trend", class_="text-info")
    @render_plotly
    def display_plot():
        _, df, _ = reactive_calc_combined()
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            y_col = "temp_f" if input.temp_unit() else "temp_c"
            y_label = "Temperature (°F)" if input.temp_unit() else "Temperature (°C)"
            fig = px.scatter(df, x="timestamp", y=y_col, title="Temperature Readings with Trend", labels={y_col: y_label, "timestamp": "Time"}, color_discrete_sequence=["blue"])
            x_vals = list(range(len(df)))
            y_vals = df[y_col]
            slope, intercept, *_ = stats.linregress(x_vals, y_vals)
            df['trend'] = [slope * x + intercept for x in x_vals]
            fig.add_scatter(x=df["timestamp"], y=df['trend'], mode='lines', name='Trend Line', line=dict(color="red"))
            fig.update_layout(xaxis_title="Time", yaxis_title=y_label)
            return fig
