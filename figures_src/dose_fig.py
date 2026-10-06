"""Tile for 'Every Ablation Is a Dose' (arXiv:2610.02173): a redraw of the
paper's clean-world / dosed-world diagram (reference screenshot in
figures_src/dose_paper_worlds.png), stacked so each panel fills the tile
width. Run from the repo root."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix"})
INK, STREAM, GREY, GREYTXT = "#333333", "#b4b4b4", "#b8b8b8", "#8a8a8a"
RED, REDFILL, GREEN, GREENFILL = "#c92a1e", "#fbe9e6", "#2e8b57", "#e9f4ec"
YS = 1.9  # residual stream height

def box(ax, x, y, w, h, text, ec, fc="white", ls="-", fs=15, tc=None, lw=1.3):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                ec=ec, fc=fc, lw=lw, ls=ls, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc or ec, zorder=4)

def arrow(ax, x0, y0, x1, y1, color, ls="-", lw=1.2):
    ax.annotate("", (x1, y1), (x0, y0), zorder=3,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls, mutation_scale=11, shrinkA=0, shrinkB=0))

def switch(ax, x, y0, y1, color):
    """Open contact between y0 (stream side) and y1 (component side)."""
    ya, yb = y0 + 0.07, y1 - 0.07
    ax.plot([x], [ya], "o", color=color, ms=3.2, zorder=4)
    ax.plot([x], [yb], "o", color=color, ms=3.2, zorder=4)
    ax.plot([x, x - 0.2], [ya, ya + 0.62 * (yb - ya)], color=color, lw=1.2, zorder=4)

def grey_component(ax, x, y, above):
    box(ax, x, y, 0.95, 0.55, "· · ·", GREY, ls=(0, (2, 2)), fs=15, tc=GREYTXT)
    top, bot = (YS + 0.1, y - 0.3) if above else (y + 0.3, YS - 0.1)
    if above:
        arrow(ax, x - 0.2, top, x - 0.2, bot, GREY)          # stream -> component
        arrow(ax, x + 0.2, bot, x + 0.2, top, GREY)          # component -> stream
    else:
        arrow(ax, x - 0.2, bot, x - 0.2, top, GREY)
        arrow(ax, x + 0.2, top, x + 0.2, bot, GREY)

def world(ax, dosed):
    ax.set_xlim(0, 12); ax.set_ylim(0, 3.75); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.12, 0.08), 11.76, 3.6, boxstyle="round,pad=0,rounding_size=0.18",
                                ec="#9a9a9a", fc="white", lw=1.0, zorder=0))
    title = r"(b) dosed world, $b=\pi_\lambda$" if dosed else r"(a) clean world, $b=\varnothing$"
    ax.text(0.45, 3.33, title, fontsize=16, color=INK, va="center", zorder=4)

    # residual stream
    ax.plot([1.05, 10.55], [YS, YS], color=STREAM, lw=6, solid_capstyle="butt", zorder=1)
    arrow(ax, 10.5, YS, 10.95, YS, STREAM, lw=4)
    box(ax, 0.78, YS, 0.5, 0.5, r"$x$", GREEN, fc=GREENFILL, fs=16)
    ax.add_patch(Circle((11.3, YS), 0.33, ec=INK, fc="white", lw=1.2, zorder=3))
    ax.add_patch(Circle((11.3, YS), 0.26, ec=INK, fc="white", lw=1.2, zorder=3))
    ax.text(11.3, YS, r"$D$", ha="center", va="center", fontsize=15, color=INK, zorder=4)

    # upper row: a grey component, then the readout r with its activation written in
    grey_component(ax, 2.5, 2.85, above=True)
    ar = r"$a_r(x';\pi_\lambda)$" if dosed else r"$a_r(x';\varnothing)$"
    box(ax, 5.2, 2.85, 2.05, 0.55, ar, RED, fc=REDFILL, fs=15)
    box(ax, 7.6, 2.85, 0.75, 0.55, r"$r$", RED, fc=REDFILL, fs=16)
    arrow(ax, 6.26, 2.85, 7.2, 2.85, RED, ls=(0, (3, 2)))
    switch(ax, 7.4, YS + 0.1, 2.57, INK)                     # stream -> r cut
    arrow(ax, 7.8, 2.57, 7.8, YS + 0.1, RED)                 # r -> stream

    # lower row: the core c, then grey components
    cy = 0.95
    if dosed:
        box(ax, 4.5, cy, 0.8, 0.55, r"$c$", RED, fc=REDFILL, fs=16)
        box(ax, 1.95, cy, 2.55, 0.55, "$a_c$ \u2254 $m - \\frac{\\lambda}{2}\\Delta$", RED, fc=REDFILL, fs=15)
        arrow(ax, 3.25, cy, 4.08, cy, RED, ls=(0, (3, 2)))
        switch(ax, 4.3, cy + 0.28, YS - 0.1, INK)            # stream -> c cut
    else:
        box(ax, 4.5, cy, 0.8, 0.55, r"$c$", INK, fs=16)
        arrow(ax, 4.3, YS - 0.1, 4.3, cy + 0.28, INK)        # stream -> c
    arrow(ax, 4.7, cy + 0.28, 4.7, YS - 0.1, INK)            # c -> stream
    ax.text(4.5, 0.42, "core", ha="center", va="center", fontsize=14, color=GREYTXT, zorder=4)
    grey_component(ax, 6.9, cy, above=False)
    grey_component(ax, 9.1, cy, above=False)

fig, (a, b) = plt.subplots(2, 1, figsize=(8, 5), dpi=150,
                           gridspec_kw=dict(left=0.01, right=0.99, top=0.99, bottom=0.01, hspace=0.04))
world(a, dosed=False)
world(b, dosed=True)
fig.savefig("figures/dose.png", dpi=150, facecolor="white")
print("ok")
