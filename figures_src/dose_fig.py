import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
# Use the site's serif if present, else STIX (matplotlib's bundled Times-like)
plt.rcParams.update({"font.family":"STIXGeneral","mathtext.fontset":"stix","font.size":15,
                     "axes.linewidth":0.8,"xtick.major.width":0.8,"ytick.major.width":0.8})
rng=np.random.default_rng(7)
BLUE="#1f4e9c"; RED="#b4343c"; INK="#222"; GREY="#8a94a1"

fig,ax=plt.subplots(figsize=(8,5),dpi=150)
lam=np.linspace(-1,1,400)
samples=np.array([-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0])
# illustrative units (own_r, gamma_r)
units=[(0.52,-0.46),(0.14,-0.70),(-0.22,-0.28),(0.34,0.48),(-0.44,0.30)]
for own,g in units:
    c=BLUE if g<0 else RED
    ax.plot(lam,own+g*lam,color=c,lw=2,zorder=2)
    y=own+g*samples+rng.normal(0,0.025,samples.size)
    ax.scatter(samples,y,s=26,color=c,zorder=3,edgecolor="white",linewidth=0.6)
    ax.scatter([0],[own],s=48,facecolor="white",edgecolor=c,linewidth=1.3,zorder=4)

ax.axhline(0,color=INK,lw=0.8,zorder=1)
ax.axvline(0,color=GREY,lw=0.8,ls=(0,(4,3)),zorder=1)

# conventional ablations as uncalibrated points on the dose axis (positions illustrative)
for x,label in [(-1.0,"zero"),(-0.62,"mean"),(0.38,"resample")]:
    ax.plot([x],[-1.12],marker="^",color=INK,ms=8,zorder=5,clip_on=False)
    ax.annotate(label,(x,-1.17),ha="center",va="top",fontsize=13,color=INK)

# slope & intercept annotations on one blue unit
own,g=units[0]
ax.annotate(r"own$_r$",(0,own),xytext=(-0.36,0.80),fontsize=14,color=INK,
            arrowprops=dict(arrowstyle="-",color=GREY,lw=0.7))
x0,x1=0.62,0.82
ax.plot([x0,x1,x1],[own+g*x0,own+g*x0,own+g*x1],color=GREY,lw=0.7,zorder=1)
ax.annotate(r"slope $\gamma_r$",(x1,own+g*(x0+x1)/2),xytext=(6,0),textcoords="offset points",fontsize=14,color=INK,va="center")

ax.set_xlim(-1.08,1.08); ax.set_ylim(-1.3,1.05)
ax.set_xticks([-1,-0.5,0,0.5,1]); ax.set_yticks([-1,-0.5,0,0.5,1]); ax.tick_params(labelsize=13)
ax.set_xlabel(r"intervention strength $\lambda$ (signed counterfactual contrast)",fontsize=15)
ax.set_ylabel(r"response $E_r(\lambda)$",fontsize=15)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.tick_params(length=3)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([],[],color=BLUE,lw=2,label=r"counterweight, $\gamma_r<0$"),
                   Line2D([],[],color=RED,lw=2,label=r"reinforcer, $\gamma_r>0$")],
          loc="lower right",bbox_to_anchor=(1.0,1.0),ncol=2,frameon=False,fontsize=13,handlelength=1.6,columnspacing=1.2)
ax.set_title(r"$E_r(\lambda)=\mathrm{own}_r+\gamma_r\,\lambda$",fontsize=17,loc="left",pad=12)
fig.tight_layout()
fig.savefig("figures/dose.png",dpi=150,facecolor="white")
print("ok")
