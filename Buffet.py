from sjvisualizer import DataHandler, Canvas, BarRace, StaticImage
import json

EXCEL_FILE = "C:\Data\Data Visualization\Buffet_2022Q2.xlsx"
FPS = 60
DURATION = 0.5

df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=FPS*DURATION*60).df

canvas = Canvas.canvas()

bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas)
canvas.add_sub_plot(bar_chart)

canvas.add_title("Buffet Invests", color=(0,0,0))
canvas.add_sub_title("From 1994 - 2022", color=(150,150,150))

canvas.add_time(df=df, time_indicator="year")

canvas.play(fps=FPS)
