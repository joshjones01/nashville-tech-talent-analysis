import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import pi
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuals")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Shared styling ──
plt.rcParams.update({
    "figure.facecolor": "#0d1117",
    "axes.facecolor": "#0d1117",
    "axes.edgecolor": "#30363d",
    "axes.labelcolor": "#c9d1d9",
    "text.color": "#c9d1d9",
    "xtick.color": "#8b949e",
    "ytick.color": "#8b949e",
    "grid.color": "#21262d",
    "font.family": "sans-serif",
    "font.size": 11,
})

ACCENT = "#58a6ff"
GOLD = "#f0c040"
GREEN = "#3fb950"
RED = "#f85149"


# ═══════════════════════════════════════════════════════════════════════
#  1. SALARY GAP CHART
# ═══════════════════════════════════════════════════════════════════════

def create_salary_gap_chart():
    categories = [
        "Data Analyst",
        "Python Developer",
        "AI / ML Engineer",
        "BI Analyst / Power BI",
        "MCP / AI Automation",
        "Node.js / JavaScript",
        "Data Scientist",
        "Data Engineer",
    ]
    lows =  [56, 83, 80, 62, 80, 101, 97, 48]
    highs = [213, 286, 257, 184, 237, 380, 237, 223]
    asking = 60

    fig, ax = plt.subplots(figsize=(12, 6))

    y_pos = np.arange(len(categories))
    bar_height = 0.5

    # Gradient-style bars: low to high
    for i, (lo, hi) in enumerate(zip(lows, highs)):
        ax.barh(i, hi - lo, left=lo, height=bar_height, color=ACCENT, alpha=0.7, edgecolor="none")
        ax.text(lo - 2, i, f"${lo}K", ha="right", va="center", fontsize=9, color="#8b949e")
        ax.text(hi + 2, i, f"${hi}K", ha="left", va="center", fontsize=9, color="#8b949e")

    # Joshua's asking salary line
    ax.axvline(x=asking, color=GOLD, linewidth=2.5, linestyle="--", zorder=5)
    ax.text(asking + 3, len(categories) - 0.15, f"Joshua's ask: ${asking}K",
            color=GOLD, fontsize=11, fontweight="bold", va="bottom")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=11)
    ax.set_xlabel("Annual Salary (thousands)", fontsize=12)
    ax.set_title("Market Salary Ranges vs. Joshua's $60K Ask", fontsize=15, fontweight="bold", pad=15)
    ax.set_xlim(0, 410)
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)
    ax.tick_params(left=False)

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "salary_gap_chart.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  2. SKILL RARITY BAR CHART
# ═══════════════════════════════════════════════════════════════════════

def create_rarity_chart():
    skills = [
        "JavaScript / Node.js",
        "API Integration",
        "Python (Data/Analytics)",
        "Power BI / Visualization",
        "Revenue Forecasting",
        "CompTIA Quad-Stack",
        "AI/ML + Data Analytics",
        "Model Context Protocol",
    ]
    scores = [5, 6, 6, 7, 7, 8, 8, 10]

    # Color gradient: green (common) → gold (moderate) → red (rare)
    def rarity_color(score):
        if score <= 5:
            return GREEN
        elif score <= 7:
            return GOLD
        else:
            return RED

    colors = [rarity_color(s) for s in scores]

    fig, ax = plt.subplots(figsize=(11, 6))

    y_pos = np.arange(len(skills))
    bars = ax.barh(y_pos, scores, height=0.6, color=colors, edgecolor="none", alpha=0.85)

    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(bar.get_width() + 0.15, i, f"{score}/10", va="center", fontsize=11, fontweight="bold",
                color=colors[i])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(skills, fontsize=11)
    ax.set_xlim(0, 11.5)
    ax.set_xlabel("Rarity Score", fontsize=12)
    ax.set_title("Skill Rarity Index — Joshua Jones", fontsize=15, fontweight="bold", pad=15)
    ax.invert_yaxis()

    # Legend
    legend_patches = [
        mpatches.Patch(color=GREEN, label="In-Demand (5–6)"),
        mpatches.Patch(color=GOLD, label="Rare / Niche (7)"),
        mpatches.Patch(color=RED, label="Extremely Rare (8–10)"),
    ]
    ax.legend(handles=legend_patches, loc="lower right", fontsize=9,
              facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")

    ax.grid(axis="x", alpha=0.3)
    ax.tick_params(left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "skill_rarity_chart.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  3. MULTI-DISCIPLINE RADAR CHART
# ═══════════════════════════════════════════════════════════════════════

def create_radar_chart():
    dimensions = [
        "Data Analytics\n& Visualization",
        "AI / ML",
        "Software\nDevelopment",
        "Business\nIntelligence",
        "Cloud &\nInfrastructure",
        "MCP / Agentic\nAI",
    ]

    # Scores out of 10
    joshua =          [9, 8, 7, 8, 8, 10]
    typical_analyst = [7, 2, 3, 5, 2, 0]

    N = len(dimensions)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    joshua += joshua[:1]
    typical_analyst += typical_analyst[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_facecolor("#0d1117")
    fig.patch.set_facecolor("#0d1117")

    # Draw grid
    ax.set_rlabel_position(0)
    ax.set_rticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], color="#8b949e", fontsize=8)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=10, color="#c9d1d9")
    ax.set_ylim(0, 10.5)

    # Grid styling
    ax.spines["polar"].set_color("#30363d")
    ax.xaxis.grid(color="#21262d", linewidth=0.5)
    ax.yaxis.grid(color="#21262d", linewidth=0.5)

    # Typical analyst (filled gray)
    ax.fill(angles, typical_analyst, alpha=0.15, color="#8b949e")
    ax.plot(angles, typical_analyst, color="#8b949e", linewidth=1.5, linestyle="--", label="Typical Data Analyst")

    # Joshua (filled blue)
    ax.fill(angles, joshua, alpha=0.2, color=ACCENT)
    ax.plot(angles, joshua, color=ACCENT, linewidth=2.5, label="Joshua Jones")

    # Dots on Joshua's points
    for angle, val in zip(angles[:-1], joshua[:-1]):
        ax.plot(angle, val, "o", color=ACCENT, markersize=7, zorder=5)

    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), fontsize=10,
              facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")

    ax.set_title("Multi-Discipline Coverage\nJoshua Jones vs. Typical Data Analyst",
                 fontsize=14, fontweight="bold", pad=25, color="#c9d1d9")

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "radar_chart.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  4. SKILL RARITY BUBBLE CHART  (rarity × demand × salary)
# ═══════════════════════════════════════════════════════════════════════

def create_rarity_bubble_chart():
    skills = [
        "MCP",
        "AI/ML +\nData Analytics",
        "CompTIA\nQuad-Stack",
        "Power BI /\nVisualization",
        "Revenue\nForecasting",
        "Python\n(Analytics)",
        "API\nIntegration",
        "JavaScript /\nNode.js",
    ]
    rarity_scores =   [10,   8,    8,    7,    7,    6,    6,    5]
    dice_listings =   [10,  1062,  50,   29,    5,   83,  200,  105]  # approximate Dice presence
    salary_ceiling_k = [237, 257,  135,  166,  120,  286,  184,  380]  # high end of range (K)

    # Bubble size proportional to salary ceiling
    sizes = [s * 2.2 for s in salary_ceiling_k]

    # Color by rarity tier
    def rarity_color(score):
        if score <= 5:
            return GREEN
        elif score <= 7:
            return GOLD
        else:
            return RED

    colors = [rarity_color(s) for s in rarity_scores]

    fig, ax = plt.subplots(figsize=(13, 8))

    # Use log scale for x-axis (demand) since values span 5 → 1,062
    for i in range(len(skills)):
        ax.scatter(dice_listings[i], rarity_scores[i], s=sizes[i],
                   color=colors[i], alpha=0.7, edgecolors="white", linewidths=0.8, zorder=5)
        # Label each bubble
        x_off = 8 if dice_listings[i] < 500 else -15
        ha = "left" if dice_listings[i] < 500 else "right"
        ax.annotate(f"{skills[i]}\n${salary_ceiling_k[i]}K+",
                    (dice_listings[i], rarity_scores[i]),
                    textcoords="offset points", xytext=(x_off, 18), ha=ha,
                    fontsize=9, color="#c9d1d9", fontweight="bold",
                    arrowprops=dict(arrowstyle="-", color="#30363d", lw=0.5))

    ax.set_xscale("log")
    ax.set_xlabel("Market Demand (Dice.com listings, log scale)", fontsize=12)
    ax.set_ylabel("Skill Rarity Score (1–10)", fontsize=12)
    ax.set_title("Skill Rarity vs. Market Demand\nBubble size = salary ceiling",
                 fontsize=15, fontweight="bold", pad=15)
    ax.set_ylim(3.5, 11.5)
    ax.set_xlim(3, 2000)
    ax.set_yticks(range(4, 11))

    # Quadrant annotations
    ax.axhline(y=7.5, color="#30363d", linewidth=1, linestyle=":", alpha=0.6)
    ax.axvline(x=70, color="#30363d", linewidth=1, linestyle=":", alpha=0.6)
    ax.text(4.5, 10.8, "RARE + NICHE\n(hardest to hire)", fontsize=8, color="#8b949e", style="italic")
    ax.text(300, 10.8, "RARE + HIGH DEMAND\n(unicorn zone)", fontsize=8, color=RED, style="italic", fontweight="bold")
    ax.text(4.5, 4.0, "COMMON + NICHE", fontsize=8, color="#8b949e", style="italic")
    ax.text(300, 4.0, "COMMON + HIGH DEMAND\n(competitive market)", fontsize=8, color="#8b949e", style="italic")

    # Legend for bubble size
    for ref_salary, ref_label in [(100, "$100K"), (200, "$200K"), (350, "$350K")]:
        ax.scatter([], [], s=ref_salary * 2.2, color="#8b949e", alpha=0.4,
                   edgecolors="white", linewidths=0.5, label=f"{ref_label}+ ceiling")

    legend_patches = [
        mpatches.Patch(color=GREEN, label="In-Demand (5–6)"),
        mpatches.Patch(color=GOLD, label="Rare / Niche (7)"),
        mpatches.Patch(color=RED, label="Extremely Rare (8–10)"),
    ]

    leg1 = ax.legend(handles=legend_patches, loc="lower left", fontsize=8,
                     facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9",
                     title="Rarity Tier", title_fontsize=9)
    leg1.get_title().set_color("#c9d1d9")
    ax.add_artist(leg1)

    ax.grid(alpha=0.2)
    ax.tick_params(left=False, bottom=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "skill_rarity_bubble.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    create_salary_gap_chart()
    create_rarity_chart()
    create_radar_chart()
    create_rarity_bubble_chart()
    print("\n🎨 All visualizations generated.")

