from time_series_visualizer import draw_line_plot
from time_series_visualizer import draw_bar_plot
from time_series_visualizer import draw_box_plot


line = draw_line_plot()
line.savefig("line_plot.png")


bar = draw_bar_plot()
bar.savefig("bar_plot.png")


box = draw_box_plot()
box.savefig("box_plot.png")