import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9})
P=np.linspace(0.01,0.99,197)
fee=7*P*(1-P)
fig,ax=plt.subplots(figsize=(5.2,3.3))
ax.fill_between(P*100,0,fee+1.2,color="#dde6f0",label="No-profit band for takers (fee + 1.2¢ half-spread)")
ax.plot(P*100,fee,color="#1f4e79",lw=1.6,label="Kalshi taker fee, 0.07·P(1−P)")
pts=[(1,0.57,"1¢, taker fills"),(5,0.82,"5¢, all fills"),(50,1.33,"50¢, taker fills"),(95,0.83,"95¢, all fills")]
offs={1:(6,-10),5:(6,4),50:(6,-12),95:(-62,-12)}
for x,y,l in pts:
    ax.plot(x,y,"o",color="#b03a2e",ms=5)
    ax.annotate(l,(x,y),xytext=offs[x],textcoords="offset points",fontsize=7.5)
ax.plot([],[],"o",color="#b03a2e",ms=5,label="Observed gap between win rate and price (Becker 2026)")
ax.set_xlabel("Contract price P (cents)"); ax.set_ylabel("Cents per contract")
ax.set_xlim(0,100); ax.set_ylim(0,3.1)
ax.legend(fontsize=7,loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=1,frameon=False)
for s in ["top","right"]: ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig("fig1.pdf"); fig.savefig("fig1.png",dpi=200)
