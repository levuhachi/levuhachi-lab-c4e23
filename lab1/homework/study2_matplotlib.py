from matplotlib import pyplot

#1.Prepare data:
machine_count = [10,8,7]
#2.Prepare lables:
machine_name = ["Mac", "PC", "Linux"]
#3.Draw Pie:
# pyplot.pie(machine_count,labels = machine_name)
pyplot.pie(machine_count,labels=machine_name, autopct = "%.1f%%", explode = [0.15,0,0], shadow = True)
pyplot.axis("equal")  # để piechart có hình tròn
pyplot.title("Usage Behviours")
#4.Show:
pyplot.show()