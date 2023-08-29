from plotool import RealtimeDrawing

dp = RealtimeDrawing(num_lines=2, style=["science", "ieee", "grid"])
for i in range(50):
    dp.add_data(i, i ** 2, "label1", 1)
    dp.add_data(i, i, "label2", 2)
    dp.plot_data()
dp.show()