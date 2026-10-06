"""Tile for 'Every Ablation Is a Dose' (arXiv:2610.02173): a high-resolution
redraw of the paper's two-panel dose figure (reference screenshot in
figures_src/dose_paper_figure.png). Panel (a): the dose axis and where
conventional ablations land on it. Panel (b): one direction's response is
affine in the dose; held-out doses at +-1/2 fall on the fit. Values in (b)
are read off the paper's figure. Run from the repo root."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 14, "axes.linewidth": 0.8})
INK, BAND = "#1f2a3a", "#ebebeb"
BLUE, ORANGE, GREY = "#4f86c6", "#e8743b", "#8c8c8c"
GREEN, RED = "#2a9d6b", "#d8432c"

fig = plt.figure(figsize=(8, 5), dpi=150)
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.08], left=0.03, right=0.985, top=0.93, bottom=0.14, wspace=0.28)

# ---------- (a) the dose axis ----------
ax = fig.add_subplot(gs[0])
ax.set_xlim(1.8, -1.55); ax.set_ylim(0, 1); ax.axis("off")
ax.axvspan(1, -1, color=BAND, zorder=0)
ax.text(1.78, 0.98, "a", fontsize=17, fontweight="bold", va="top", ha="left", color=INK)

y_dose = 0.88
ax.plot([1, -1], [y_dose, y_dose], color=INK, lw=1.8, zorder=2)
ax.plot([-1, -1.35], [y_dose, y_dose], color=INK, lw=1.4, ls=(0, (3, 2.5)), zorder=2)
ax.annotate("", (-1.42, y_dose), (-1.35, y_dose), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2, mutation_scale=12))
ax.plot([1, -1], [y_dose, y_dose], "o", color=INK, ms=8, zorder=3)
ax.plot([0], [y_dose], "D", mfc="white", mec=INK, mew=1.4, ms=8, zorder=3)

y_ax = 0.745
ax.annotate("", (-1.5, y_ax), (1.2, y_ax), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, mutation_scale=12))
ax.text(-1.46, y_ax + 0.035, r"$\lambda$", fontsize=15, ha="right", va="bottom", color=INK)
for x, top, bot in [(1, "+1", "clean"), (0, "0", "neutral"), (-1, "−1", "inverted")]:
    ax.plot([x, x], [y_ax - 0.015, y_ax + 0.015], color=INK, lw=1)
    ax.text(x, y_ax - 0.035, top, ha="center", va="top", fontsize=13, color=INK)
    ax.text(x, y_ax - 0.105, bot, ha="center", va="top", fontsize=13, color=INK)

xs = np.linspace(1.3, -1.55, 600)
def gauss(mu, sd): return np.exp(-0.5 * ((xs - mu) / sd) ** 2)
rows = [("zero", BLUE, gauss(0.02, 0.17), True, 0.02),
        ("mean", ORANGE, gauss(0.03, 0.19), True, 0.03),
        ("resample", GREY, 0.85 * (gauss(0.9, 0.17) + gauss(-0.9, 0.17)), False, None)]
y0, h = 0.42, 0.12
for i, (name, col, ys, filled, mode) in enumerate(rows):
    base = y0 - i * 0.165
    ax.plot([1.3, -1.55], [base, base], color=col if filled else GREY, lw=0.9, zorder=1)
    if filled:
        ax.fill_between(xs, base, base + h * ys, color=col, alpha=0.35, lw=0, zorder=2)
        ax.plot(xs, base + h * ys, color=col, lw=1.3, zorder=3)
        ax.plot([mode, mode], [base, base + h], color=col, lw=1.6, zorder=4)
        ax.text(1.78, base + 0.04, name, fontsize=13, style="italic", color=col, ha="left", va="bottom")
    else:
        ax.plot(xs, base + h * ys, color=GREY, lw=1.2, ls=(0, (4, 3)), zorder=3)
        ax.text(1.78, base + 0.055, name, fontsize=13, style="italic", color=GREY, ha="left", va="bottom")
        ax.text(1.78, base + 0.008, "predicted", fontsize=9.5, color=GREY, ha="left", va="bottom")

# ---------- (b) affine response in the dose ----------
bx = fig.add_subplot(gs[1])
bx.text(-0.2, 0.985, "b", transform=bx.transAxes, fontsize=17, fontweight="bold", va="top", color=INK)
bx.axvspan(1, -1, color=BAND, zorder=0)
bx.axhline(0, color=INK, lw=0.9, zorder=1)
lam_fit, lam_held = np.array([1, 0, -1]), np.array([0.5, -0.5])
# values read off the paper's figure
ET = lambda l: -0.35 - 0.78 * l
EF = lambda l: -0.125 - 0.725 * l
ll = np.array([1.05, -1.05])
for f, col in [(ET, GREEN), (EF, RED)]:
    bx.plot(ll, f(ll), color=col, lw=2.2, zorder=2)
    bx.errorbar(lam_fit, f(lam_fit), yerr=[0.03, 0.07, 0.03], fmt="o", color=col, ms=7, ecolor=col, elinewidth=1.3, capsize=0, zorder=4)
    bx.plot(lam_held, f(lam_held), "o", mfc="white", mec=col, mew=1.6, ms=7, zorder=4)
bx.set_xlim(1.15, -1.15); bx.set_ylim(-1.3, 0.85)
bx.set_xticks([1, 0.5, 0, -0.5, -1]); bx.set_xticklabels(["+1", "+½", "0", "−½", "−1"])
bx.set_yticks([-1.0, -0.5, 0.0, 0.5])
bx.tick_params(labelsize=12.5, length=3, colors=INK)
bx.set_xlabel(r"dose $\lambda$", fontsize=14, color=INK)
bx.set_ylabel(r"$E_r$", fontsize=15, color=INK, rotation=0, labelpad=14, va="center")
for s in ("top", "right"): bx.spines[s].set_visible(False)
for s in ("left", "bottom"): bx.spines[s].set_color(INK)
bx.legend(handles=[Line2D([], [], color=GREEN, lw=2, marker="o", ms=6, label=r"true side $E_T$"),
                   Line2D([], [], color=RED, lw=2, marker="o", ms=6, label=r"false side $E_F$"),
                   Line2D([], [], color="none", marker="o", mfc="white", mec=INK, mew=1.4, ms=6.5, label="held-out dose")],
          loc="lower right", frameon=False, fontsize=12, handlelength=2.2, borderaxespad=0.3)
fig.savefig("figures/dose.png", dpi=150, facecolor="white")
print("ok")
