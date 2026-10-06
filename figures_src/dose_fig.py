"""Figure for 'Every Ablation Is a Dose' (arXiv:2610.02173), modelled on the
paper's Figure 2: static weight alignment z against measured |gamma|, as
within-model ranks. Points are synthetic, generated to match the reported
counts (52 counterweights, 16 relays, 81 downstream directions) and the
pooled rank correlation (+0.73). Run from the repo root."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 15, "axes.linewidth": 0.8})
BLUE, ORANGE, GREY, INK = "#1f4e9c", "#e07b22", "#9aa3ad", "#222"
N, N_CW, N_RL, TARGET = 81, 52, 16, 0.73

# search seeds for a sample whose Spearman rho rounds to the reported value
best = None
for seed in range(2000):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=N)
    g = 0.78 * z + np.sqrt(1 - 0.78**2) * rng.normal(size=N)
    rho = spearmanr(z, g).correlation
    if abs(rho - TARGET) < 0.003:
        best = (seed, z, g, rho); break
seed, z, g, rho = best
rx = np.argsort(np.argsort(z)) + 1          # within-model ranks, 1..81
ry = np.argsort(np.argsort(g)) + 1
# the 13 directions without a significant slope sit at the low-|gamma| end
order = np.argsort(ry)
ns, sig = order[:N - N_CW - N_RL], order[N - N_CW - N_RL:]
rng = np.random.default_rng(seed)
rl = rng.choice(sig, N_RL, replace=False)
cw = np.setdiff1d(sig, rl)
# a few upstream controls (no causal path), hollow, off the trend
ctrl_x = rng.uniform(5, 78, 7); ctrl_y = rng.uniform(3, 30, 7)

fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
ax.scatter(rx[cw], ry[cw], s=46, color=BLUE, edgecolor="white", linewidth=0.6, zorder=3, label="counterweight, $\\gamma_r<0$")
ax.scatter(rx[rl], ry[rl], s=46, color=ORANGE, edgecolor="white", linewidth=0.6, zorder=3, label="relay, $\\gamma_r>0$")
ax.scatter(rx[ns], ry[ns], s=26, color=GREY, edgecolor="white", linewidth=0.6, zorder=2, label="no significant slope")
ax.scatter(ctrl_x, ctrl_y, s=46, facecolor="white", edgecolor=INK, linewidth=1.0, zorder=3, label="upstream control, no causal path")

# rank-regression trend, drawn lightly
b, a = np.polyfit(rx, ry, 1)
xx = np.array([1, N]); ax.plot(xx, a + b * xx, color=INK, lw=0.9, ls=(0, (5, 4)), zorder=1)

ax.text(0.03, 0.95, f"Spearman $\\rho$ = +{rho:.2f},  $n$ = {N}", transform=ax.transAxes,
        ha="left", va="top", fontsize=15, color=INK)
ax.set_xlabel("static alignment $z$ from the weights (within-model rank)")
ax.set_ylabel("measured $|\\gamma_r|$ (within-model rank)")
ax.set_xlim(0, N + 1); ax.set_ylim(0, N + 1)
ax.set_xticks([1, 20, 40, 60, 81]); ax.set_yticks([1, 20, 40, 60, 81])
ax.tick_params(labelsize=13, length=3)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False, fontsize=12.5, handletextpad=0.4, columnspacing=2.0)
ax.set_title("The weights anticipate the coupling strength", loc="left", fontsize=17, pad=12)
fig.subplots_adjust(left=0.1, right=0.98, top=0.9, bottom=0.27)
fig.savefig("figures/dose.png", dpi=150, facecolor="white")
print("seed", seed, "rho", round(rho, 3))
