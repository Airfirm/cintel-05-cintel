from shiny import reactive, render
from shiny.express import ui, input  # ← added input
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
    use_f = input.use_fahrenheit()  # ← now works because input is imported
    temp_c = round(random.uniform(-18, -16), 1)
    temp = round(temp_c * 9/5 + 32, 1) if use_f else temp_c
    unit = "F" if use_f else "C"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = {"temp": temp, "timestamp": timestamp, "unit": unit}
    reactive_value_wrapper.get().append(new_entry)
    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)
    return deque_snapshot, df, new_entry

ui.page_opts(title="🌐 Antarctic Live Dashboard", fillable=True)

with ui.sidebar(open="open"):
    ui.h2("🧊 Antarctic Explorer", class_="text-center")
    ui.p("Real-time temperature readings in Antarctica.", class_="text-center")
    
    # ✅ checkbox should be inside sidebar
    ui.input_checkbox("use_fahrenheit", "Display temperature in Fahrenheit", False)

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
            _, _, entry = reactive_calc_combined()
            return f"{entry['temp']} °{entry['unit']}"
        ui.p("🔥 Warmer than usual", class_="text-warning")

    with ui.card(full_screen=True):
        ui.card_header("🕒 Current Date and Time", class_="bg-gradient-purple text-blue p-2")
        @render.text
        def display_time():
            _, _, entry = reactive_calc_combined()
            return f"{entry['timestamp']}"

with ui.card(full_screen=True):
    ui.card_header("📋 Most Recent Readings", class_="bg-primary text-white p-2")
    @render.data_frame
    def display_df():
        _, df, _ = reactive_calc_combined()
        return render.DataGrid(df, width="100%")

with ui.card():
    ui.card_header("📈 Temperature Trend", class_="bg-gradient-blue text-white p-2")
    @render_plotly
    def display_plot():
        _, df, entry = reactive_calc_combined()
        if not df.empty:
            unit = entry["unit"]  # ✅ fix: retrieve current unit
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            fig = px.scatter(
                df,
                x="timestamp",
                y="temp",
                title=f"Temperature Readings ({unit}) + Trend",
                labels={"temp": f"Temperature (°{unit})", "timestamp": "Time"},
                color_discrete_sequence=["blue"]
            )
            x_vals = list(range(len(df)))
            y_vals = df["temp"]
            slope, intercept, *_ = stats.linregress(x_vals, y_vals)
            df['best_fit_line'] = [slope * x + intercept for x in x_vals]
            fig.add_scatter(
                x=df["timestamp"],
                y=df["best_fit_line"],
                mode="lines",
                name="Trend Line",
                line=dict(color="red")
            )
            fig.update_layout(xaxis_title="Time", yaxis_title=f"Temperature (°{unit})")
        return fig
