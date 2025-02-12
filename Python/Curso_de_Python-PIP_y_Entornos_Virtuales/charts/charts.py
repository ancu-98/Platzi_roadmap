import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels = ['A','B','C']
    values = [100, 34, 99]

    fiq, ax = pyplot.subplots()
    ax.pie(values, labels=labels)
    pyplot.savefig('pie.png')
    pyplot.close()