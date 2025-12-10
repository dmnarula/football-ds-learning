import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager improt FontProperties


def register_font(font_path: str):
    # Register custom font
    fm.fontManager.addfont(font_path)
    font_name = fm.FontProperties(fname=font_path).get_name()
    return font_name

def set_plot_style():
  # Register font files - Montserrat
  font_paths = [
      "/content/football-ds-learning/fonts/Montserrat-Regular.ttf",
      "/content/football-ds-learning/fonts/Montserrat-Medium.ttf",
      "/content/football-ds-learning/fonts/Montserrat-SemiBold.ttf",
      "/content/football-ds-learning/fonts/Montserrat-Bold.ttf",
      "/content/football-ds-learning/fonts/Montserrat-Light.ttf",
  ]

  for path in font_paths:
    register_font(path)

  # Set defaults
  plt.rcParams["font.family"] = 'Montserrat'
  plt.rcParams["font.weight"] = 'regular'
  plt.rcParams["figure.facecolor"] = "#f2f2f2"
  plt.rcParams["axes.facecolor"] = "#f2f2f2"
  plt.rcParams["axes.edgecolor"] = "#999999"
  plt.rcParams["axes.linewidth"] = 0.8


  # Specific styles
  title_font = FontProperties(family="Montserrat", weight="semibold", size=44)
  subtitle_font = FontProperties(family="Montserrat", weight="medium", size=22)
  dot_label_font = FontProperties(family="Montserrat", weight="medium", size=16)
  axis_font = FontProperties(family="Montserrat", weight="medium", size=28)
  label_font = FontProperties(family="Montserrat", weight="medium", size=20)
  tick_font = FontProperties(family="Montserrat", weight="regular", size=16)
  footer_font = FontProperties(family="Montserrat", weight="regular", size=14)

  return title_font, subtitle_font, dot_label_font, axis_font, label_font, tick_font, footer_font
