from matplotlib.pyplot import *
from numpy import linspace
from scipy.stats import beta

x = linspace(0, 1, 75)

fig = figure()
ax = fig.add_subplot(111)
ax.plot(x, beta.pdf(x, 0.5, 0.5), label=r"$\alpha=\beta=0.5$")
ax.plot(x, beta.pdf(x, 5, 1), label=r"$\alpha=5, \beta=1$")
ax.plot(x, beta.pdf(x, 1, 3), label=r"$\alpha=1, \beta=3$")
ax.plot(x, beta.pdf(x, 2, 2), label=r"$\alpha=2, \beta=2$")
ax.plot(x, beta.pdf(x, 2, 5), label=r"$\alpha=2, \beta=5$")
ax.grid(True)
ax.minorticks_on()
ax.legend(loc=9)
setp(ax.get_legend().get_texts(), fontsize='small')
ax.set_ylim(0, 2.6)
ax.set_xlabel("x")
ax.set_ylabel("PDF")

fig.savefig("Beta_distribution_pdf.pdf", bbox_inches="tight",
            pad_inches=.15)
