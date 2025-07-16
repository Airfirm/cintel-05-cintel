# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

# from collections import deque
from shiny import reactive, render
from shiny.express import ui, input, render
import random
from datetime import datetime
from faicons import icon_svg
# import shiny
# print(shiny.__version__)  # Need >=0.7.0 for ui.icon()

# --------------------------------------------
# Optional: Import font awesome icons as you like
# --------------------------------------------

# from faicons import icon_svg

# --------------------------------------------
# FOR OPTIONAL LOCAL DEVELOPMENT
# --------------------------------------------

# Add all packages not in the Std Library
# to requirements.txt ONLY when working locally:
#
# faicons
# shiny
# shinylive
# 
# And install them into an active project virtual environment (usually in .venv)
# --------------------------------------------

# --------------------------------------------
# SET UP THE REACTIVE CONTENT
# --------------------------------------------

# --------------------------------------------
# PLANNING: We want to get a fake temperature and 
# Time stamp every N seconds. 
# For now, we'll avoid storage and just 
# Try to get the fake live data working and sketch our app. 
# We can do all that with one reactive calc.
# Use constants for update interval so it's easy to modify.
# ---------------------------------------------------------

# --------------------------------------------
# First, set a constant UPDATE INTERVAL for all live data
# Constants are usually defined in uppercase letters
# Use a type hint to make it clear that it's an integer (: int)
# --------------------------------------------
UPDATE_INTERVAL_SECS: int = 1
# --------------------------------------------

# Initialize a REACTIVE CALC that our display components can call
# to get the latest data and display it.
# The calculation is invalidated every UPDATE_INTERVAL_SECS
# to trigger updates.

# It returns everything needed to display the data.
# Very easy to expand or modify.
# (I originally looked at REACTIVE POLL, but this seems to work better.)
# --------------------------------------------

@reactive.calc()
def reactive_calc_combined():

    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now" and use string format strftime() method to format it
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return everything we need
    return latest_dictionary_entry

# ------------------------------------------------
# Define the Shiny UI Page layout - Page Options
# ------------------------------------------------

# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI

ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# ------------------------------------------------
# Define the Shiny UI Page layout - Sidebar
# ------------------------------------------------

# Sidebar is typically used for user interaction/information
# Note the with statement to create the sidebar followed by a colon
# Everything in the sidebar is indented consistently

with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

#---------------------------------------------------------------------
# In Shiny Express, everything not in the sidebar is in the main panel
#---------------------------------------------------------------------


ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")
# ui.p("☀️ Sun is out!")  # adds a sun emoji

# Option 1: Regular Sun
#ui.icon("sun")  # <i class="fa-regular fa-sun"></i>

# Option 2: Solid Sun (filled)
#ui.icon("sun", style="solid")  # <i class="fa-solid fa-sun"></i>

# Option 3: Animated Spinning Sun
#ui.icon("sun", class_="fa-spin")  # Spins infinitely

# ui.icon("sun", style="color: gold; font-size: 2rem;")

# icon_svg("sun")
# ui.HTML(icon_svg("sun"))

# ui.markdown('<i class="bi bi-sun" style="font-size: 2rem;"></i>')

# Use emoji (no dependencies)
ui.span("☀️", style="font-size: 2rem; color: gold;")

# Use SVG (self-contained)
ui.HTML("""
<svg width="32" height="32" viewBox="0 0 24 24" style="fill: gold;">
  <path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.415-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"/>
</svg>
""")

def icon_svg(icon_name: str) -> str:
    return f"""
    <svg width="32" height="32" fill="currentColor" class="bi bi-{icon_name}" viewBox="0 0 16 16">
        <use xlink:href="https://cdn.jsdelivr.net/npm/bootstrap-icons/bootstrap-icons.svg#{icon_name}"/>
    </svg>
    """

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"
