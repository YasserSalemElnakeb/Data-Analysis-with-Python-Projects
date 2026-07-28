from sea_level_predictor import draw_plot


ax = draw_plot()

ax.figure.savefig(
    "sea_level_plot.png"
)