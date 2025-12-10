import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

def register_font(font_path: str):
    """Registers a custom TTF font for Matplotlib"""
    fm.fontManager.addfont(font_path)
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rcParams['font.family'] = font_name
    return font_name
