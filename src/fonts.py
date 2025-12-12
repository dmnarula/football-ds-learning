import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties


def register_font(font_path: str):
    # Register custom font
    fm.fontManager.addfont(font_path)
    font_name = fm.FontProperties(fname=font_path).get_name()
    return font_name

# Setting plot style
def set_plot_style():

  # Register font files - Montserrat
  base = "/content/football-ds-learning/fonts/"
  font_paths = [
      f"{base}/Montserrat-Regular.ttf",
      f"{base}/Montserrat-Medium.ttf",
      f"{base}/Montserrat-SemiBold.ttf",
      f"{base}/Montserrat-Bold.ttf",
      f"{base}/Montserrat-Light.ttf",
  ]

  for path in font_paths:
    register_font(path)

  # Set defaults
  plt.rcParams.update({
      "font.family": "Montserrat",
      
      "figure.facecolor": "#f2f2f2",
      "axes.facecolor": "#f2f2f2",
      "axes.edgecolor": "#999999",
      "axes.linewidth": 0.8,

      "axes.grid": True,
      "grid.color": "#DDDDDD",
      "grid.linewidth": 0.6,
      "grid.alpha": 0.8,
      "axes.axisbelow": True,

      "xtick.color": "#888888",
      "ytick.color": "#888888",
      "xtick.direction": "out",
      "ytick.direction": "out",
      "xtick.major.size": 4,
      "ytick.major.size": 4,
      "xtick.major.width": 0.6,
      "ytick.major.width": 0.6,

      "legend.frameon": True,
      "legend.facecolor": "#f2f2f2",
      "legend.edgecolor": "none"
  })



  # Specific styles
  title_font = FontProperties(family="Montserrat", weight="semibold", size=44)
  subtitle_font = FontProperties(family="Montserrat", weight="medium", size=22)
  dot_label_font = FontProperties(family="Montserrat", weight="medium", size=16)
  axis_font = FontProperties(family="Montserrat", weight="medium", size=28)
  label_font = FontProperties(family="Montserrat", weight="medium", size=20)
  tick_font = FontProperties(family="Montserrat", weight="regular", size=16)
  footer_font = FontProperties(family="Montserrat", weight="regular", size=14)

  return {
      "title": FontProperties(family="Montserrat", weight="semibold", size=44),
      "subtitle": FontProperties(family="Montserrat", weight="medium", size=22),
      "dot": FontProperties(family="Montserrat", weight="medium", size=16),
      "axis": FontProperties(family="Montserrat", weight="medium", size=28),
      "label": FontProperties(family="Montserrat", weight="medium", size=20),
      "tick": FontProperties(family="Montserrat", weight="regular", size=16),
      "footer": FontProperties(family="Montserrat", weight="regular", size=14),
  }


# Pretty Label
def pretty_label(var):
    # Special cases first
    if "xg" in var or "xa" in var or "xgi" in var:
        label = (
            var.replace("predicted_", "Predicted ")
                .replace("xg", "xG")
                .replace("xa", "xA")
                .replace("xgi", "xGI")
        )
        return (
            label.replace("_per90", " per 90")
                    .replace("_", " ")
        )

    # Default formatting
    return (
        var.replace("_per90", " per 90")
           .replace("_", " ")
           .title()
    )

