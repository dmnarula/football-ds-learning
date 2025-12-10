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

def set_plot_style():
  # Register font files - Montserrat
  base = Path(__file__).resolve().parents[1]
  font_dir = base / "fonts"
  
  font_files = [
      "Montserrat-Regular.ttf",
      "Montserrat-Medium.ttf",
      "Montserrat-SemiBold.ttf",
      "Montserrat-Bold.ttf",
      "Montserrat-Light.ttf",
  ]
  
  # Register all Montserrat fonts
  for fname in font_files:
    path = font_dir / fname
    if path.exists():
      register_font(str(path))
    else:
      print(f"Warning: Font file not found — {path}")

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
  return {
      "title": FontProperties(family="Montserrat", weight="semibold", size=44),
      "subtitle": FontProperties(family="Montserrat", weight="medium", size=22),
      "dot": FontProperties(family="Montserrat", weight="medium", size=16),
      "axis": FontProperties(family="Montserrat", weight="medium", size=28),
      "label": FontProperties(family="Montserrat", weight="medium", size=20),
      "tick": FontProperties(family="Montserrat", weight="regular", size=16),
      "footer": FontProperties(family="Montserrat", weight="regular", size=14)
  }
