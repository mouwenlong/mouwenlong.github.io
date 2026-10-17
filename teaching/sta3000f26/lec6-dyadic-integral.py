"""Reproduce the deterministic sum-to-integral illustration for Lecture 6."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 13})
out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(8.4, 4.2))
g = lambda x: np.sqrt(np.log(1 / x))
x = np.linspace(0.012, 1, 1000)
ax.plot(x, g(x), color="#163d65", lw=2, label=r"$g(\epsilon)$ nonincreasing")
for right in [1/2, 1/4, 1/8, 1/16, 1/32]:
    left = right / 2
    ax.add_patch(Rectangle((left, 0), right-left, g(right),
                          facecolor="#a7d6d0", edgecolor="#247f78", lw=1.2, alpha=.85))
    ax.plot(right, g(right), "o", color="#247f78", ms=4)
left, right = 1/4, 1/2
height = g(right)
ax.annotate("", xy=(right, -.35), xytext=(left, -.35),
            arrowprops={"arrowstyle": "<->", "color": "#247f78"}, annotation_clip=False)
ax.text((left+right)/2, -.50, r"$\delta_{m+1}/2$", ha="center", color="#247f78")
ax.annotate(r"height $g(\delta_{m+1})$", xy=(.34, height), xytext=(.58, 1.5),
            arrowprops={"arrowstyle": "->", "color": "#247f78"}, color="#247f78")
ax.text(.65, 1.0, "Every rectangle lies\nbelow the curve.", color="#163d65")
ax.set_xticks([0, 1/8, 1/4, 1/2, 1],
              [r"$0$", r"$\cdots$", r"$\delta_{m+2}$", r"$\delta_{m+1}$", r"$D$"])
ax.set_yticks([])
ax.set_xlim(0, 1.04)
ax.set_ylim(0, 2.25)
ax.set_xlabel(r"$\epsilon$", loc="right")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper right", frameon=False)
fig.subplots_adjust(left=.05, right=.97, bottom=.23, top=.94)
fig.savefig(out / "lec6-dyadic-integral.pdf", bbox_inches="tight")
fig.savefig(out / "lec6-dyadic-integral.png", dpi=220, bbox_inches="tight")
plt.close(fig)
