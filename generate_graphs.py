"""
IB Economics — All Diagrams (Units 2, 3, 4)
============================================
Generates 54 PNG diagrams into ./diagrams/

Usage:
    python3 draw_all_diagrams.py

Requirements:
    pip install matplotlib numpy

To adjust a diagram, find its section (search for the save() call or
the section comment) and edit the values there.
Colours, fonts, and figure sizes are all set via the constants at the top.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ── Output directory ──────────────────────────────────────────────────────────
OUT_DIR = r'C:\Users\SachaLawrenceJohnGré\Desktop\Personal\ib_econ_notes\graphs'
os.makedirs(OUT_DIR, exist_ok=True)

# ── Colour palette (edit here to restyle everything) ──────────────────────────
NAVY   = '#1B3A6B'   # unit headings, LRAS, main navy
BLUE   = '#2E75B6'   # demand curves, consumer surplus
RED    = '#C00000'   # supply curves, losses
GREEN  = '#375623'   # social optimum, government, gains
ORANGE = '#E36C09'   # welfare loss, warnings
GRAY   = '#888888'   # dashed guidelines, secondary
LGRAY  = '#CCCCCC'   # faint lines
PURPLE = '#7030A0'   # quota licence rent, financial flows

# ── Shared helpers ────────────────────────────────────────────────────────────

def base_ax(ax, xlabel='Quantity (Q)', ylabel='Price (P)', title='',
            xlim=(0, 10), ylim=(0, 10)):
    """Apply standard IB-style formatting to an axes object."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NAVY)
    ax.spines['bottom'].set_color(NAVY)
    ax.set_xlabel(xlabel, fontsize=10, color=NAVY, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=10, color=NAVY, fontweight='bold')
    if title:
        ax.set_title(title, fontsize=11, color=NAVY, fontweight='bold', pad=10)
    ax.tick_params(colors=NAVY)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([])
    ax.set_yticks([])


def save(name):
    """Tidy layout and save to OUT_DIR."""
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/{name}.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'  ✓  {name}.png')


# ═══════════════════════════════════════════════════════════════════════════════
# UNIT 2 — MICROECONOMICS
# ═══════════════════════════════════════════════════════════════════════════════

# ── 2.1  Market Equilibrium ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Market Equilibrium')
Q = np.linspace(1, 9, 100)
D = 10 - Q; S = Q
ax.plot(Q, D, color=BLUE, lw=2.2, label='Demand (D)')
ax.plot(Q, S, color=RED,  lw=2.2, label='Supply (S)')
ax.plot(5, 5, 'ko', ms=6)
ax.plot([5,5],[0,5], color=GRAY, lw=1, ls='--')
ax.plot([0,5],[5,5], color=GRAY, lw=1, ls='--')
ax.text(5.15, 0.3, 'Q*', fontsize=10, color=NAVY)
ax.text(0.15, 5.1, 'P*', fontsize=10, color=NAVY)
ax.text(9.1, 0.8, 'D', fontsize=11, color=BLUE, fontweight='bold')
ax.text(9.1, 9.0, 'S', fontsize=11, color=RED,  fontweight='bold')
ax.legend(loc='center right', fontsize=9, framealpha=0)
save('2_3a_market_equilibrium')

# ── 2.1a  Demand Curve + Movement Along ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Demand Curve & Movement Along')
Q = np.linspace(1, 9, 200)
D = 10 - Q
D1 = 12 - Q
D2 = 8 - Q
mask = (D >= 1) & (D <= 9)
ax.plot(Q[mask], D[mask], color=BLUE, lw=2.5, label='Demand (D)')
ax.plot(Q[(D1 >= 1) & (D1 <= 9)], D1[(D1 >= 1) & (D1 <= 9)],
        color=GREEN, lw=1.8, ls='--', label='D1 (increase)')
ax.plot(Q[(D2 >= 1) & (D2 <= 9)], D2[(D2 >= 1) & (D2 <= 9)],
        color=RED, lw=1.8, ls='--', label='D2 (decrease)')
q1, p1 = 3.0, 7.0
q2, p2 = 6.5, 3.5
ax.plot([q1, q1], [0, p1], color=GRAY, lw=1, ls=':')
ax.plot([0, q1], [p1, p1], color=GRAY, lw=1, ls=':')
ax.plot([q2, q2], [0, p2], color=GRAY, lw=1, ls=':')
ax.plot([0, q2], [p2, p2], color=GRAY, lw=1, ls=':')
ax.plot(q1, p1, 'o', ms=6, color=GREEN, zorder=5)
ax.plot(q2, p2, 'o', ms=6, color=ORANGE, zorder=5)
ax.annotate('', xy=(q2+0.1, p2+0.2), xytext=(q1+0.1, p1+0.2),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2))
ax.text((q1 + q2) / 2 + 0.3, (p1 + p2) / 2 + 0.6,
        'Movement along D\ncaused by ΔP', fontsize=8.2, color=PURPLE,
        ha='center', va='center', fontweight='bold', rotation=-36)
ax.text(q1 - 0.35, p1 + 0.28, 'A', fontsize=9, color=GREEN, fontweight='bold')
ax.text(q2 + 0.12, p2 - 0.42, 'B', fontsize=9, color=ORANGE, fontweight='bold')
ax.text(0.15, p1 + 0.1, 'P1', fontsize=8.5, color=NAVY)
ax.text(0.15, p2 + 0.1, 'P2', fontsize=8.5, color=NAVY)
ax.text(q1 - 0.1, 0.3, 'Q1', fontsize=8.5, color=NAVY)
ax.text(q2 - 0.1, 0.3, 'Q2', fontsize=8.5, color=NAVY)
ax.text(9.1, 1.0, 'D', fontsize=10, color=BLUE, fontweight='bold')
ax.text(9.1, 2.8, 'D1', fontsize=10, color=GREEN, fontweight='bold')
ax.text(7.0, 1.0, 'D2', fontsize=10, color=RED, fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='upper right')
save('2_1a_demand_shift')

# ── 2.2a  Supply Curve + Movement Along ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Supply Curve & Movement Along')
Q = np.linspace(1, 9, 200)
S = Q
S1 = Q - 2
S2 = Q + 2
mask = (S >= 1) & (S <= 9)
ax.plot(Q[mask], S[mask], color=RED, lw=2.5, label='Supply (S)')
ax.plot(Q[(S1 >= 1) & (S1 <= 9)], S1[(S1 >= 1) & (S1 <= 9)],
        color=GREEN, lw=1.8, ls='--', label='S1 (increase)')
ax.plot(Q[(S2 >= 1) & (S2 <= 9)], S2[(S2 >= 1) & (S2 <= 9)],
        color=BLUE, lw=1.8, ls='--', label='S2 (decrease)')
q1, p1 = 3.0, 3.0
q2, p2 = 6.5, 6.5
ax.plot([q1, q1], [0, p1], color=GRAY, lw=1, ls=':')
ax.plot([0, q1], [p1, p1], color=GRAY, lw=1, ls=':')
ax.plot([q2, q2], [0, p2], color=GRAY, lw=1, ls=':')
ax.plot([0, q2], [p2, p2], color=GRAY, lw=1, ls=':')
ax.plot(q1, p1, 'o', ms=6, color=GREEN, zorder=5)
ax.plot(q2, p2, 'o', ms=6, color=ORANGE, zorder=5)
ax.annotate('', xy=(q2-0.1, p2+0.2), xytext=(q1-0.1, p1+0.2),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2))
ax.text((q1 + q2) / 2 -0.5, (p1 + p2) / 2 + 0.5,
        'Movement along S\ncaused by ΔP', fontsize=8.2, color=PURPLE,
        ha='center', va='center', fontweight='bold',rotation=+36)
ax.text(q1 - 0.32, p1 + 0.22, 'A', fontsize=9, color=GREEN, fontweight='bold')
ax.text(q2 + 0.1, p2 + 0.18, 'B', fontsize=9, color=ORANGE, fontweight='bold')
ax.text(0.15, p1 + 0.1, 'P1', fontsize=8.5, color=NAVY)
ax.text(0.15, p2 + 0.1, 'P2', fontsize=8.5, color=NAVY)
ax.text(q1 - 0.1, 0.3, 'Q1', fontsize=8.5, color=NAVY)
ax.text(q2 - 0.1, 0.3, 'Q2', fontsize=8.5, color=NAVY)
ax.text(9.1, 9.0, 'S', fontsize=10, color=RED, fontweight='bold')
ax.text(9.1, 7.0, 'S1', fontsize=10, color=GREEN, fontweight='bold')
ax.text(7.0, 9.0, 'S2', fontsize=10, color=BLUE, fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='lower right')
save('2_2a_supply_shift')

# ── 2.3a  Change in Equilibrium After a Demand Shift ──────────────────────────
fig, ax = plt.subplots(figsize=(5.2, 4.2))
base_ax(ax, title='Change in Equilibrium After a Demand Shift')
Q = np.linspace(0.5, 9.5, 200)
D1 = 9 - Q
D2 = 11 - Q
S = 1 + 0.8 * Q
ax.plot(Q, D1, color=BLUE, lw=2.2, label='D')
ax.plot(Q, D2, color=BLUE, lw=2.2, ls='--', label='D₁')
ax.plot(Q, S, color=RED, lw=2.2, label='S')
q1 = 8 / 1.8; p1 = 9 - q1
q2 = 10 / 1.8; p2 = 11 - q2
ax.plot(q1, p1, 'o', ms=5.5, color=BLUE, zorder=6)
ax.plot(q2, p2, 'o', ms=5.5, color=GREEN, zorder=6)
for qv, pv, qlab, plab in [(q1, p1, 'Q*', 'P*'), (q2, p2, "Q*₁", "P*₁")]:
    ax.plot([qv, qv], [0, pv], color=GRAY, lw=1, ls=':')
    ax.plot([0, qv], [pv, pv], color=GRAY, lw=1, ls=':')
    ax.text(qv - 0.15, 0.3, qlab, fontsize=8.2, color=NAVY)
    ax.text(0.15, pv + 0.08, plab, fontsize=8.2, color=NAVY)
ax.annotate('', xy=(q2+0.1, p2 - 0.2), xytext=(q1+0.1, p1 - 0.2),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.text((q1 + q2) / 2 + 2.1, (p1 + p2) / 2, 'Demand increases\nE → E₁',
        ha='center', fontsize=8.3, color=GREEN, fontweight='bold')
ax.text(9.1, 0.3, 'D', fontsize=10, color=BLUE, fontweight='bold')
ax.text(9.1, 2.3, 'D₁', fontsize=10, color=BLUE, fontweight='bold')
ax.text(9.1, 8.8, 'S', fontsize=10, color=RED, fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='center right')
save('2_3b_change_in_equilibrium')

# ── 2.3  Consumer & Producer Surplus ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Consumer & Producer Surplus')
Q = np.linspace(0, 9, 100)
D = 10 - Q; S = Q
Qe, Pe = 5, 5
ax.fill_between(np.linspace(0,Qe,50), 10-np.linspace(0,Qe,50), Pe, alpha=0.35, color=BLUE, label='Consumer Surplus (CS)')
ax.fill_between(np.linspace(0,Qe,50), np.linspace(0,Qe,50), Pe, alpha=0.35, color=RED,  label='Producer Surplus (PS)')
ax.plot(Q, D, color=BLUE, lw=2.2)
ax.plot(Q, S, color=RED,  lw=2.2)
ax.plot(Qe, Pe, 'ko', ms=6)
ax.plot([Qe,Qe],[0,Pe], color=GRAY, lw=1, ls='--')
ax.plot([0,Qe],[Pe,Pe], color=GRAY, lw=1, ls='--')
ax.text(Qe+0.1,0.3,'Q*',fontsize=10,color=NAVY)
ax.text(0.15,Pe+0.1,'P*',fontsize=10,color=NAVY)
ax.text(1.2,6,'CS',fontsize=12,color=BLUE,fontweight='bold')
ax.text(1.2,3.5,'PS',fontsize=12,color=RED,fontweight='bold')
ax.text(9.1,0.7,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,9.0,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='center right')
save('2_3c_surplus')

# ── 2.5  PED Elastic vs Inelastic ────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
for ax, label, slope, col in zip(axes,
        ['Elastic Demand (|PED| > 1)', 'Inelastic Demand (|PED| < 1)'],
        [0.5, 2.5], [BLUE, RED]):
    base_ax(ax, title=label)
    Q = np.linspace(0.5, 9.5, 100)
    P = 10 - slope * Q
    mask = P > 0
    ax.plot(Q[mask], P[mask], color=col, lw=2.5)
    ax.text(Q[mask][-1]+0.2, P[mask][-1], 'D', fontsize=11, color=col, fontweight='bold')
plt.suptitle('Price Elasticity of Demand', fontsize=11, color=NAVY, fontweight='bold', y=1.02)
save('2_5a_PED')

# ── 2.5a  PED Special Cases ───────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(10, 3.5))
for ax, (title, kind, col) in zip(axes, [
        ('Perfectly Elastic |PED|=∞', 'horiz', BLUE),
        ('Perfectly Inelastic |PED|=0', 'vert',  RED),
        ('Unit Elastic |PED|=1',        'unit',  GREEN)]):
    base_ax(ax, title=title)
    if kind == 'horiz':
        ax.axhline(5, color=col, lw=2.5)
        ax.text(9.2,5.2,'D',fontsize=11,color=col,fontweight='bold')
        ax.text(0.2,5.2,'P*',fontsize=9,color=NAVY)
    elif kind == 'vert':
        ax.axvline(5, color=col, lw=2.5)
        ax.text(5.2,9.3,'D',fontsize=11,color=col,fontweight='bold')
        ax.text(5.2,0.3,'Q*',fontsize=9,color=NAVY)
    else:
        Q = np.linspace(0.5, 9.5, 100); P = 10 / Q; m = P < 10
        ax.plot(Q[m], P[m], color=col, lw=2.5)
        ax.text(9,1.4,'D',fontsize=11,color=col,fontweight='bold')
        ax.text(4,5,'TR = constant',fontsize=8.5,color=GRAY,style='italic')
plt.suptitle('Constant PED Demand Curves', fontsize=11, color=NAVY, fontweight='bold')
save('2_5b_PED_special')

# ── 2.5b  PED Along Straight-Line Demand + TR (HL) ───────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
ax1, ax2 = axes
base_ax(ax1, title='PED Along a Demand Curve (HL)')
Q = np.linspace(0, 10, 200)
P = 10 - Q
ax1.plot(Q, P, color=BLUE, lw=2.5)
ax1.fill_between(Q[Q<5], 0, P[Q<5], alpha=0.1, color=RED)
ax1.fill_between(Q[Q>5], 0, P[Q>5], alpha=0.1, color=GREEN)
ax1.plot(5, 5, 'ko', ms=7)
ax1.text(2.5,3,'Inelastic\n|PED|<1',ha='center',fontsize=9,color=RED)
ax1.text(6.8,1.3,'Elastic\n|PED|>1',ha='center',fontsize=9,color=GREEN)
ax1.text(5.2,5.3,'Unit elastic',fontsize=8,color=NAVY)
ax1.text(9.1,1,'D',fontsize=11,color=BLUE,fontweight='bold')
ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(NAVY); ax2.spines['bottom'].set_color(NAVY)
ax2.set_xlabel('Q',fontsize=10,color=NAVY,fontweight='bold')
ax2.set_ylabel('TR',fontsize=10,color=NAVY,fontweight='bold')
ax2.set_title('Total Revenue Curve',fontsize=11,color=NAVY,fontweight='bold')
ax2.set_xticks([]); ax2.set_yticks([])
TR = Q*(10-Q)
ax2.plot(Q, TR, color=ORANGE, lw=2.5)
ax2.axvline(5, color=GRAY, lw=1, ls='--')
ax2.text(5.2,25.4,'Max TR',fontsize=8.5,color=NAVY)
ax2.text(3.3,18,'Elastic:\n↓P→↑TR',fontsize=8,color=GREEN,style='italic')
ax2.text(5.5,18,'Inelastic:\n↓P→↓TR',fontsize=8,color=RED,style='italic')
save('2_5c_PED_straight_line')

# ── 2.5bb  PED Revenue Rectangles ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9.2, 4))
for ax, title, slope, p_old, p_new, col in [
        (axes[0], 'Elastic Demand: Price Falls → TR Rises', 0.6, 6.5, 4.5, GREEN),
        (axes[1], 'Inelastic Demand: Price Falls → TR Falls', 1.6, 6.5, 4.5, RED)]:
    base_ax(ax, title=title)
    Q = np.linspace(0.5, 9.5, 200)
    P = 10 - slope * Q
    mask = P > 0
    ax.plot(Q[mask], P[mask], color=BLUE, lw=2.2, label='D')
    q_old = (10 - p_old) / slope
    q_new = (10 - p_new) / slope
    ax.fill_between([0, q_old], [0, 0], [p_old, p_old], color=ORANGE, alpha=0.22, label='Initial TR')
    ax.fill_between([0, q_new], [0, 0], [p_new, p_new], color=col, alpha=0.22, label='New TR')
    ax.plot([q_old, q_old], [0, p_old], color=GRAY, lw=1, ls=':')
    ax.plot([q_new, q_new], [0, p_new], color=GRAY, lw=1, ls=':')
    ax.plot([0, q_old], [p_old, p_old], color=GRAY, lw=1, ls=':')
    ax.plot([0, q_new], [p_new, p_new], color=GRAY, lw=1, ls=':')
    ax.text(0.15, p_old + 0.08, 'P1', fontsize=8, color=NAVY)
    ax.text(0.15, p_new + 0.08, 'P2', fontsize=8, color=NAVY)
    ax.text(q_old - 0.12, 0.3, 'Q1', fontsize=8, color=NAVY)
    ax.text(q_new - 0.12, 0.3, 'Q2', fontsize=8, color=NAVY)
    ax.text(q_old / 2, p_old / 2+2, 'TR1', ha='center', va='center', fontsize=9, color=ORANGE, fontweight='bold')
    ax.text(q_new / 2+ 1.8 * (q_new - q_old) / 2, p_new / 2, 'TR2', ha='center', va='center', fontsize=9, color=col, fontweight='bold')
    ax.text(9.1, max(P[mask][-1], 0.6), 'D', fontsize=10, color=BLUE, fontweight='bold')
    ax.legend(fontsize=7.4, framealpha=0, loc='upper right')
plt.suptitle('PED and Total Revenue Rectangles', fontsize=11, color=NAVY, fontweight='bold', y=1.02)
save('2_5d_PED_revenue_rectangles')

# ── 2.5c  Engel Curves ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
ax.spines['top'].set_visible(False); ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(False); ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Income (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Quantity Demanded (Q)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Engel Curves (YED)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Y = np.linspace(1, 9, 100)
ax.plot(Y, 0.35*Y+3.25,   color=BLUE,   lw=2.2, label='Normal good (YED>0)')
ax.plot(Y, 2.0*Y-5.0,     color=GREEN,  lw=2.2, ls='--', label='Luxury good (YED>1)')
ax.plot(Y, -0.5*Y+7.5,    color=RED,    lw=2.2, ls=':',  label='Inferior good (YED<0)')
# Visual benchmark for YED = 1
ax.plot(Y, Y,             color=LGRAY,  lw=1.2, ls=':')
# Horizontal reference through common intersection
ax.axhline(5,             color=LGRAY,  lw=1.0, ls=':')
ax.text(9.0,6.6,'Normal', fontsize=8.5,color=BLUE, fontweight='bold')
ax.text(7.4,9.2,'Luxury', fontsize=8.5,color=GREEN,fontweight='bold')
ax.text(9.2,2.6,'Inferior',fontsize=8.5,color=RED,  fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='upper left')
save('2_5e_engel_curve')

# ── 2.6a  PES Elastic vs Inelastic ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Price Elasticity of Supply')
Q = np.linspace(0, 9, 100)
ax.plot(Q, 0.5+0.5*Q, color=GREEN, lw=2.5, label='Elastic supply (PES>1)')
ax.plot(Q, -0.2+1.7*Q,     color=RED,   lw=2.5, label='Inelastic supply (PES<1)')
ax.text(9.2,5.0,'Elastic S',  fontsize=9,color=GREEN,fontweight='bold')
ax.text(6,9.2,'Inelastic S',fontsize=9,color=RED,  fontweight='bold')
ax.legend(fontsize=9, framealpha=0, loc='upper left')
save('2_6a_PES_curves')

# ── 2.6b  PES Special Cases ───────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(10, 3.5))
for ax, (title, kind, col) in zip(axes, [
        ('Perfectly Elastic PES=∞','horiz', GREEN),
        ('Perfectly Inelastic PES=0','vert', RED),
        ('Unit Elastic PES=1',      'unit',  BLUE)]):
    base_ax(ax, title=title)
    Q = np.linspace(0.5, 9.5, 100)
    if kind == 'horiz':
        ax.axhline(5,color=col,lw=2.5)
        ax.text(9.2,5.2,'S',fontsize=11,color=col,fontweight='bold')
    elif kind == 'vert':
        ax.axvline(5,color=col,lw=2.5)
        ax.text(5.2,9.3,'S',fontsize=11,color=col,fontweight='bold')
    else:
        ax.plot(Q, Q, color=col, lw=2.5)
        ax.text(8.7,9.2,'S',fontsize=11,color=col,fontweight='bold')
        ax.text(4,6,'Through\norigin',fontsize=8,color=GRAY,style='italic')
plt.suptitle('Constant PES Supply Curves', fontsize=11, color=NAVY, fontweight='bold')
save('2_6b_PES_special')

# ── 2.7a  Price Ceiling ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Price Ceiling (Maximum Price)')
Q = np.linspace(0.5, 9.5, 100)
D = 10-Q; S = Q
ax.plot(Q,D,color=BLUE,lw=2.2); ax.plot(Q,S,color=RED,lw=2.2)
ax.plot(5,5,'ko',ms=4)
Pc = 3
ax.axhline(Pc,color=GREEN,lw=2,label='Price ceiling (Pmax)')
Qd_c = 10-Pc; Qs_c = Pc
ax.plot(Qs_c,Pc,'ko',ms=4)
ax.plot([Qs_c,Qs_c],[0,Pc],GRAY,lw=1,ls='--'); ax.plot([Qd_c,Qd_c],[0,Pc],GRAY,lw=1,ls='--')
ax.fill([Qs_c, Qs_c, 5], [10-Qs_c, Qs_c, 5],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.annotate('',xy=(Qd_c,1),xytext=(Qs_c,1),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qs_c+Qd_c)/2,1.3,'Shortage',ha='center',fontsize=9,color=ORANGE,fontweight='bold')
ax.text(3.45,5.25,'DWL',fontsize=8.5,color=ORANGE,fontweight='bold')
ax.text(0.15,Pc+0.15,'Pmax',fontsize=9,color=GREEN,fontweight='bold')
ax.text(0.15,5.1,'P*',fontsize=9,color=NAVY)
ax.text(Qs_c+0.1,0.3,'Qs',fontsize=9,color=NAVY); ax.text(Qd_c+0.1,0.3,'Qd',fontsize=9,color=NAVY)
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='center right')
save('2_7a_price_ceiling')

# ── 2.7b  Price Floor ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Price Floor (Minimum Price)')
Q = np.linspace(0.5, 9.5, 100)
D = 10-Q; S = Q
ax.plot(Q,D,color=BLUE,lw=2.2); ax.plot(Q,S,color=RED,lw=2.2)
ax.plot(5,5,'ko',ms=4)
Pf = 7
ax.axhline(Pf,color=GREEN,lw=2,label='Price floor (Pmin)')
Qd_f = 10-Pf; Qs_f = Pf
ax.plot(Qd_f,Pf,'ko',ms=4)
ax.plot([Qd_f,Qd_f],[0,Pf],GRAY,lw=1,ls='--'); ax.plot([Qs_f,Qs_f],[0,Pf],GRAY,lw=1,ls='--')
ax.fill([Qd_f, Qd_f, 5], [10-Qd_f, Qd_f, 5],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.annotate('',xy=(Qs_f,1),xytext=(Qd_f,1),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qd_f+Qs_f)/2,1.3,'Surplus',ha='center',fontsize=9,color=ORANGE,fontweight='bold')
ax.text(3.45,5.25,'DWL',fontsize=8.5,color=ORANGE,fontweight='bold')
ax.text(0.15,Pf+0.15,'Pmin',fontsize=9,color=GREEN,fontweight='bold')
ax.text(0.15,5.1,'P*',fontsize=9,color=NAVY)
ax.text(Qd_f+0.1,0.3,'Qd',fontsize=9,color=NAVY); ax.text(Qs_f+0.1,0.3,'Qs',fontsize=9,color=NAVY)
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=8, framealpha=0, loc='center right')
save('2_7b_price_floor')

# ── 2.7c  Indirect Tax ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Indirect Tax Effect')
Q = np.linspace(0.5, 9, 100)
D = 10-Q; S1 = Q; tax = 2; S2 = S1+tax
ax.plot(Q,D, color=BLUE,lw=2.2,label='D')
ax.plot(Q,S1,color=RED, lw=2.2,label='S (before tax)')
ax.plot(Q,S2,color=RED, lw=2.2,ls='--',label="S + tax")
ax.plot(5,5,'ko',ms=5,zorder=10); ax.plot(4,6,'ko',ms=5,zorder=10)
ax.plot([5,5],[0,5],GRAY,lw=1,ls=(0,(1,2)))
ax.plot([0,5],[5,5],GRAY,lw=1,ls=(0,(1,2)))
ax.plot([4,4],[0,6],GRAY,lw=1,ls=':'); ax.plot([0,4],[6,6],GRAY,lw=1,ls=':')
ax.plot([0,4],[4,4],GRAY,lw=1,ls=':')
ax.fill_between([0,4],[4,4],[6,6],alpha=0.3,color=GREEN,label='Tax revenue')
ax.fill([4,4,5],[6,4,5],alpha=0.4,color=ORANGE,label='Welfare loss (DWL)')
ax.text(0.15,6.1,'Pc',fontsize=9,color=NAVY); ax.text(0.15,4.1,'Pp',fontsize=9,color=NAVY)
ax.text(0.15,5.1,'P*',fontsize=9,color=GRAY)
ax.text(4.1,0.3,'Qt',fontsize=9,color=NAVY); ax.text(5.1,0.3,'Q*',fontsize=9,color=GRAY)
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,"S",fontsize=11,color=RED,fontweight='bold')
ax.text(8.1,9.8,"S+tax",fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_7c_indirect_tax')

# ── 2.7d  Subsidy ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Subsidy Effect on Market')
Q = np.linspace(1, 9, 100)
D = 10-Q; S1 = Q; S2 = S1-2
ax.plot(Q,D, color=BLUE,lw=2.2,label='D')
ax.plot(Q,S1,color=RED, lw=2.2,label='S (before subsidy)')
ax.plot(Q[S2>0],S2[S2>0],color=RED,lw=2.2,ls='--',label="S (after subsidy)")
ax.annotate('', xy=(8.0,6.0), xytext=(6.0,6.0),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2, shrinkA=8, shrinkB=8))
Q1,P1 = 5,5; Q2,P2 = 6,4; Pp2 = P2+2
ax.plot(Q1,P1,'ko',ms=5); ax.plot(Q2,P2,'ko',ms=5)
ax.plot([Q1,Q1],[0,P1],GRAY,lw=1,ls=(0,(1,2)))
ax.plot([0,Q1],[P1,P1],GRAY,lw=1,ls=(0,(1,2)))
ax.plot([Q2,Q2],[0,Pp2],GRAY,lw=1,ls=':')
ax.plot([0,Q2],[P2,P2], GRAY,lw=1,ls=':')
ax.plot([0,Q2],[Pp2,Pp2],GRAY,lw=1,ls=':')
ax.fill_between([0,Q2],[P2,P2],[Pp2,Pp2],alpha=0.3,color=GREEN,label='Gov. subsidy cost')
ax.fill([Q1, Q2, Q2], [P1, P2, Pp2],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.text(5.68,5.1,'DWL',fontsize=8.5,color=ORANGE,fontweight='bold')
ax.text(0.1,P2+0.1,'Pc',fontsize=9,color=NAVY)
ax.text(0.1,Pp2+0.1,'Pp',fontsize=9,color=NAVY)
ax.text(0.1,P1+0.1,'P*',fontsize=9,color=GRAY)
ax.text(Q1+0.1,0.3,'Q*',fontsize=9,color=GRAY)
ax.text(Q2+0.1,0.3,'Qs',fontsize=9,color=NAVY)
ax.text(9.1,0.6,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,7.2,'S+Sub',fontsize=10,color=RED,fontweight='bold')
ax.text(9.1,9.1,"S",fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('2_7d_subsidy')

# ── 2.8a  Negative Externality of Production ─────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Negative Externality of Production')
Q = np.linspace(0.5, 9, 100)
D = 9-Q; MPC = 1+Q; MSC = MPC+1.5
ax.plot(Q,D,  color=BLUE,lw=2.2,label='D = MPB = MSB')
ax.plot(Q,MPC,color=RED, lw=2.2,label='S = MPC')
ax.plot(Q,MSC,color=NAVY,lw=2.2,ls='--',label='MSC = MPC + MEC')
Qm,Pm = 4,5; Qs,Ps = 3.25,5.75
ax.plot(Qm,Pm,'ro',ms=6); ax.plot(Qs,Ps,'bo',ms=6)
ax.fill([Qs, Qm, Qm], [Ps, Pm, MSC[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls='--'); ax.plot([Qs,Qs],[0,Ps],GRAY,lw=1,ls='--')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls='--'); ax.plot([0,Qs],[Ps,Ps],GRAY,lw=1,ls='--')
ax.text(Qm+0.1,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs-0.6,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Ps+0.1,'Ps*',fontsize=9,color=BLUE)
ax.text(7.5,1.9,'D = MPB = MSB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(7.5,7.8,'S = MPC',fontsize=8.5,color=RED,fontweight='bold')
ax.text(6,9.5,'MSC',fontsize=8.5,color=NAVY,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_8a_neg_ext_production')

# ── 2.8b  Positive Externality of Consumption ────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Positive Externality of Consumption')
Q = np.linspace(0.5, 9, 100)
S = 1+Q; MPB = 8-Q; MSB = MPB+1.5
ax.plot(Q,S,  color=RED, lw=2.2,label='S = MPC = MSC')
ax.plot(Q,MPB,color=BLUE,lw=2.2,label='D = MPB')
ax.plot(Q,MSB,color=NAVY,lw=2.2,ls='--',label='MSB = MPB + MEB')
Qm,Pm = 3.5,4.5; Qs,Ps = 4.25,5.25
ax.plot(Qm,Pm,'ro',ms=6); ax.plot(Qs,Ps,'bo',ms=6)
ax.fill([Qm, Qs, Qm], [Pm, Ps, MSB[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls='--'); ax.plot([Qs,Qs],[0,Ps],GRAY,lw=1,ls='--')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls='--'); ax.plot([0,Qs],[Ps,Ps],GRAY,lw=1,ls='--')
ax.text(Qm-0.5,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs+0.1,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Ps+0.1,'Ps*',fontsize=9,color=BLUE)
ax.text(5.4,0.9,'D = MPB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(7.2,7.4,'S = MPC = MSC',fontsize=8.5,color=RED,fontweight='bold')
ax.text(8.3,1.5,'MSB',fontsize=8.5,color=NAVY,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_8b_pos_ext_consumption')

# ── 2.8c  Negative Externality of Consumption ────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Negative Externality of Consumption')
Q = np.linspace(0.5, 9, 100)
S = 1+Q; MPB = 9-Q; MSB = MPB-1.5
ax.plot(Q,S,  color=RED, lw=2.2,label='S = MSC = MPC')
ax.plot(Q,MPB,color=BLUE,lw=2.2,label='D = MPB')
ax.plot(Q[MSB>0],MSB[MSB>0],color=NAVY,lw=2.2,ls='--',label='MSB = MPB − MEC')
Qm,Pm = 4,5; Qs,Ps = 3.25,4.25
ax.plot(Qm,Pm,'ro',ms=6); ax.plot(Qs,Ps,'bo',ms=6)
ax.fill([Qs, Qm, Qm], [Ps, Pm, MSB[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls='--'); ax.plot([Qs,Qs],[0,Ps],GRAY,lw=1,ls='--')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls='--'); ax.plot([0,Qs],[Ps,Ps],GRAY,lw=1,ls='--')
ax.text(Qm+0.1,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs-0.7,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Ps+0.1,'Ps*',fontsize=9,color=BLUE)
ax.text(7.5,1.9,'D = MPB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(5.5,0.8,'MSB',fontsize=8.5,color=NAVY,fontweight='bold')
ax.text(7.5,7.8,'S = MSC = MPC',fontsize=8.5,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_8c_neg_ext_consumption')

# ── 2.8d  Positive Externality of Production ─────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Positive Externality of Production')
Q = np.linspace(0.5, 9, 100)
D = 9-Q; MPC = 3+Q; MSC = MPC-1.5
ax.plot(Q,D,  color=BLUE,lw=2.2,label='D = MPB = MSB')
ax.plot(Q,MPC,color=RED, lw=2.2,label='S = MPC')
ax.plot(Q[MSC>0],MSC[MSC>0],color=NAVY,lw=2.2,ls='--',label='MSC = MPC − MEB')
Qm,Pm = 3,6; Qs,Ps = 3.75,5.25
ax.plot(Qm,Pm,'ro',ms=6); ax.plot(Qs,Ps,'bo',ms=6)
ax.fill([Qm, Qs, Qm], [Pm, Ps, MSC[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls='--'); ax.plot([Qs,Qs],[0,Ps],GRAY,lw=1,ls='--')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls='--'); ax.plot([0,Qs],[Ps,Ps],GRAY,lw=1,ls='--')
ax.text(Qm-0.5,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs+0.1,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Ps+0.1,'Ps*',fontsize=9,color=BLUE)
ax.text(7,2.5,'D = MPB = MSB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(4.4,8.9,'S = MPC',fontsize=8.5,color=RED,fontweight='bold')
ax.text(7,7.7,'MSC',fontsize=8.5,color=NAVY,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_8d_pos_ext_production')

# ── 2.8e  Pigouvian Tax ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Pigouvian Tax: Correcting Negative Externality')
Q = np.linspace(0.5, 9, 100)
D = 9-Q; MPC = 1+Q; MSC = MPC+1.5
ax.plot(Q,D,  color=BLUE,lw=2.2,label='D = MSB = MPB')
ax.plot(Q,MPC,color=RED, lw=2.2,label='S = MPC (before tax)')
ax.plot(Q,MSC,color=NAVY,lw=2.2,ls='--',label='S + Tax = MSC')
Qm,Pm = 4,5; Qs,Ps = 3.25,5.75
ax.plot(Qm,Pm,'ro',ms=6,label='Market output (too high)')
ax.plot(Qs,Ps,'gs',ms=7,label='Social optimum after tax')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls=':'); ax.plot([Qs,Qs],[0,Ps],GRAY,lw=1,ls=':')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls=':'); ax.plot([0,Qs],[Ps,Ps],GRAY,lw=1,ls=':')
ax.fill([Qs, Qm, Qm], [Ps, Pm, MSC[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
tx, ty = 3.8, 7.4
ax.annotate('', xy=(tx + 0.35, ty - 0.65), xytext=(tx + 1.10, ty - 1.40),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.text(tx, ty-0.5, 'Tax shifts S\nto MSC', ha='center', fontsize=8, color=GREEN)
ax.text(Qm+0.1,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs-0.7,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Ps+0.1,'Ps*',fontsize=9,color=BLUE)
ax.text(7.5,1.9,'D = MSB = MPB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(7.5,7.8,'S = MPC',fontsize=8.5,color=RED,fontweight='bold')
ax.text(6.0,9.5,'S + Tax = MSC',fontsize=8.5,color=NAVY,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('2_8e_pigouvian_tax')

# ── 2.8f  Subsidy Correcting Positive Externality ────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Subsidy: Correcting Positive Externality of Consumption')
Q = np.linspace(0.5, 9, 100)
S = 1+Q; MPB = 8-Q; sub = 1.5; MSB = MPB+sub; S_sub = S-sub
ax.plot(Q,S,  color=RED, lw=2.2,label='S = MPC = MSC')
ax.plot(Q,MPB,color=BLUE,lw=2.2,label='D = MPB')
ax.plot(Q,MSB,color=NAVY,lw=2.2,ls='--',label='MSB')
ax.plot(Q[S_sub>0],S_sub[S_sub>0],color=RED,lw=2.2,ls='--',label='S + subsidy')
Qm,Pm = 3.5,4.5; Qs,Pp = 4.25,5.25
Pc = Pp - sub
ax.plot(Qm,Pm,'ro',ms=6)
ax.plot(Qs,Pp,'bo',ms=6)
ax.plot(Qs,Pc,'ko',ms=5)
ax.fill([Qm, Qs, Qm], [Pm, Pp, MSB[np.argmin(np.abs(Q-Qm))]],
        alpha=0.35, color=ORANGE, label='Welfare loss (DWL)')
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls='--')
ax.plot([Qs,Qs],[0,Pp],GRAY,lw=1,ls='--')
ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls='--')
ax.plot([0,Qs],[Pp,Pp],GRAY,lw=1,ls='--')
ax.plot([0,Qs],[Pc,Pc],GRAY,lw=1,ls='--')
ax.annotate('', xy=(Qs+1.7,Pc+2.0), xytext=(Qm+1.55,Pc+2.0),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.8))
ax.text(Qm-0.5,0.3,'Qm',fontsize=9,color=RED); ax.text(Qs+0.1,0.3,'Qs*',fontsize=9,color=BLUE)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=RED)
ax.text(0.1,Pp+0.1,'Pp',fontsize=9,color=NAVY)
ax.text(0.1,Pc+0.1,'Pc',fontsize=9,color=GREEN)
ax.text(5.4,0.9,'D = MPB',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(9.3,8.9,'S = MPC\n= MSC',fontsize=8.3,color=RED,fontweight='bold',ha='center')
ax.text(8.15,1.5,'MSB',fontsize=8.5,color=NAVY,fontweight='bold')
ax.text(6.6,5.6,'S + subsidy',fontsize=8.2,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('2_8f_subsidy_pos_ext')

# ── 2.11a  Perfect Competition: Market + Firm ─────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
ax_m, ax_f = axes
base_ax(ax_m, title='PC Market')
Q = np.linspace(0.5, 9.5, 100)
ax_m.plot(Q,10-Q,color=BLUE,lw=2.2,label='D'); ax_m.plot(Q,Q,color=RED,lw=2.2,label='S')
ax_m.plot(5,5,'ko',ms=6); ax_m.axhline(5,color=GRAY,lw=1,ls='--')
ax_m.text(0.1,5.2,'P*=Pm',fontsize=9,color=NAVY)
ax_m.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax_m.text(9.1,9.0,'S',fontsize=11,color=RED,fontweight='bold')
ax_m.legend(fontsize=9,framealpha=0)
base_ax(ax_f, title='PC Firm (price taker)')
q = np.linspace(0.5,9.5,100)
# Curved MC while keeping a single MC=MR crossing near q=4.
MC = 0.08*q**2 + 0.7*q + 0.92
ATC = 3/q+0.5*q+1
ax_f.plot(q,MC, color=RED,   lw=2.2,label='MC')
ax_f.plot(q[(q>0.5)&(q<9)],ATC[(q>0.5)&(q<9)],color=ORANGE,lw=2.2,ls='-.',label='AC')
ax_f.axhline(5,color=BLUE,lw=2.5,label='P=D=AR=MR')
qstar = q[np.argmin(np.abs(MC - 5))]
atc_s=3/qstar+0.5*qstar+1
ax_f.plot(qstar,5,'ko',ms=6)
ax_f.plot([qstar,qstar],[0,5],GRAY,lw=1,ls=':')
ax_f.fill_between([0,qstar],[atc_s,atc_s],[5,5],alpha=0.25,color=GREEN,label='Abnormal profit')
ax_f.text(0.1,5.2,'P=MR',fontsize=8.5,color=BLUE)
ax_f.text(8,4.5, 'P=D=MR=AR',fontsize=9,color=BLUE,fontweight='bold')
ax_f.text(7,9.2,'MC',fontsize=9,color=RED,fontweight='bold')
ax_f.text(9.1,5.9,'AC',fontsize=9,color=ORANGE,fontweight='bold')
ax_f.text(qstar-1.5,5.2,'MC=MR\n(profit max)',fontsize=8,color=NAVY)
ax_f.text(qstar+0.1,0.3,'Q* (MC=MR)',fontsize=8,color=NAVY)
ax_f.legend(fontsize=7.5,framealpha=0,loc='lower right')
plt.suptitle('Perfect Competition: Market & Firm',fontsize=11,color=NAVY,fontweight='bold')
save('2_11a_PC_price_taker')

# ── 2.11b  PC Firm: Loss & Normal Profit ─────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, (mode, title) in zip(axes, [
        ('loss','PC Firm: Making a Loss'),
        ('normal','PC Firm: Normal Profit (LR)')]):
    base_ax(ax, title=title)
    q = np.linspace(0.5,9,100)
    MC = 0.08*q**2 + 0.7*q + 0.92
    ATC = 6/q+0.5*q+1
    ax.plot(q,MC, color=RED,   lw=2.2,label='MC')
    ax.plot(q[(q>0.5)&(q<9)],ATC[(q>0.5)&(q<9)],color=ORANGE,lw=2.2,ls='-.',label='AC')
    if mode == 'loss':
        P_level = 3.8
        qstar = q[np.argmin(np.abs(MC - P_level))]
        atc_s = 6/qstar+0.5*qstar+1
    else:
        # Normal profit occurs where MC and ATC meet.
        i_eq = np.argmin(np.abs(MC - ATC))
        qstar = q[i_eq]
        P_level = MC[i_eq]
        atc_s = ATC[i_eq]
    ax.axhline(P_level,color=BLUE,lw=2.5,label=f'P=MR=AR=D')
    ax.plot(qstar,P_level,'ko',ms=6)
    ax.plot([qstar,qstar],[0,P_level],GRAY,lw=1,ls=':')
    ax.text(0.1,P_level+0.1,'Pm',fontsize=9,color=NAVY)
    ax.text(qstar+0.1,0.3,'Qm',fontsize=9,color=NAVY)
    ax.text(qstar+0.15,P_level-0.4,'MC=MR',fontsize=8,color=NAVY)
    if mode == 'loss':
        ax.fill_between([0,qstar],[P_level,P_level],[atc_s,atc_s],alpha=0.3,color=RED,label='Loss')
        ax.text(qstar/2,(P_level+atc_s)/2-0.15,'Loss',ha='center',fontsize=10,color=RED,fontweight='bold')
    else:
        ax.text(qstar/2+0.3,P_level-0.4,'Normal Profit\n(AR=AC)',ha='center',fontsize=9,color=GREEN)
    ax.legend(fontsize=7.5,framealpha=0,loc='lower right')
save('2_11b_PC_normal_losses')

# ── 2.11c  Natural Monopoly ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, title='Natural Monopoly')
q = np.linspace(0.5,9.5,200)
AR = 9-q; MR = 9-2*q; LRAC = 8/q+0.3+0.015*q; MC_nm = 0.55 + 0.04*q + 0.0018*q**2
ax.plot(q,AR,   color=BLUE,  lw=2.2,label='D=AR')
ax.plot(q[MR>0],MR[MR>0],color=BLUE,lw=2.2,ls='--',label='MR')
ax.plot(q,LRAC, color=ORANGE,lw=2.2,ls='-.',label='LRAC (slight upturn)')
ax.plot(q,MC_nm,color=RED,   lw=2.2,label='MC')
qpm = q[np.argmin(np.abs(MR - MC_nm))]
Ppm = 9 - qpm
# Allocative efficiency where AR = MC.
qac = q[np.argmin(np.abs(AR - MC_nm))]
Pac = 9 - qac
ax.plot(qpm,Ppm,'ko',ms=6); ax.plot(qac,Pac,'gs',ms=7)
ax.plot([qpm,qpm],[0,Ppm],GRAY,lw=1,ls=':'); ax.plot([qac,qac],[0,Pac],GRAY,lw=1,ls=':')
ax.plot([0,qpm],[Ppm,Ppm],GRAY,lw=1,ls=':'); ax.plot([0,qac],[Pac,Pac],GRAY,lw=1,ls=':')
# Profit box at monopoly output: (Pm - LRAC at Qm) * Qm
LRAC_qpm = 8/qpm + 0.3 + 0.015*qpm
ax.fill_between([0, qpm], [LRAC_qpm, LRAC_qpm], [Ppm, Ppm],
                alpha=0.2, color=GREEN, label='Profit box')
# Loss box at allocative pricing Pac: (LRAC - AR) * Qac
LRAC_qac = 8/qac + 0.3 + 0.015*qac
ax.fill_between([0, qac], [Pac, Pac], [LRAC_qac, LRAC_qac],
                alpha=0.2, color=RED, label='Loss box')
ax.text(0.1,Ppm+0.1,'Pm',fontsize=8.5,color=NAVY); ax.text(0.1,Pac+0.1,'Pac',fontsize=8.5,color=GREEN)
ax.text(qpm+0.1,0.3,'Qm',fontsize=9,color=NAVY); ax.text(qac-0.7,0.3,'Qac',fontsize=9,color=GREEN)
ax.text(qpm+0.2,Ppm+0.25,'Profit-Maximizing\nMC=MR',fontsize=8,color=NAVY)
ax.text(qac+0.1,Pac+0.65,'Allocative Efficiency\nMC=AR',fontsize=8,color=GREEN)
ax.text(9.1,0.3,'D=AR',fontsize=9,color=BLUE,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper right')
save('2_11d_natural_monopoly')

# ── 2.11d  Game Theory Payoff Matrix ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.set_xlim(0.2,9.6); ax.set_ylim(0.8,8.0); ax.axis('off')
ax.set_title("Game Theory: Prisoners' Dilemma (Oligopoly)",fontsize=11,color=NAVY,fontweight='bold')
import matplotlib.patches as patches
# Consistent matrix geometry so the 2x2 payoff table aligns cleanly.
x_row, row_w = 0.6, 2.2
x1, cell_w = 2.9, 3.2
x2 = x1 + cell_w
y_bottom, row_h = 1.2, 2.4
y_top = y_bottom + row_h
hdr_h = 1.3
y_hdr = y_top + row_h

for x, label in [(x1, 'Firm B: Collude'), (x2, 'Firm B: Cheat')]:
    r = patches.FancyBboxPatch((x, y_hdr), cell_w, hdr_h,
                               boxstyle='round,pad=0.05',
                               facecolor=NAVY, edgecolor='white', lw=1.5)
    ax.add_patch(r)
    ax.text(x + cell_w/2, y_hdr + hdr_h/2, label, ha='center', va='center',
            fontsize=9.5, color='white', fontweight='bold')

for y, label in [(y_top, 'Firm A:\nCollude'), (y_bottom, 'Firm A:\nCheat')]:
    r = patches.FancyBboxPatch((x_row, y), row_w, row_h,
                               boxstyle='round,pad=0.05',
                               facecolor=NAVY, edgecolor='white', lw=1.5)
    ax.add_patch(r)
    ax.text(x_row + row_w/2, y + row_h/2, label, ha='center', va='center',
            fontsize=9.5, color='white', fontweight='bold')

cells = [
    (x1, y_top,    cell_w, row_h, 'A: $8m\nB: $8m',  '#EBF5EB', GREEN,  'Pareto optimal\n(unstable: incentive to defect)'),
    (x2, y_top,    cell_w, row_h, 'A: $2m\nB: $12m', '#FDECEA', RED,    'B cheats, A suffers'),
    (x1, y_bottom, cell_w, row_h, 'A: $12m\nB: $2m', '#FFF8E1', ORANGE, 'A cheats, B suffers'),
    (x2, y_bottom, cell_w, row_h, 'A: $4m\nB: $4m',  '#FDECEA', RED,    'Nash Equilibrium\n(dominant strategy)'),
]
for x, y, w, h, main, fill, tcol, sub in cells:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05',
                               facecolor=fill, edgecolor='white', lw=1.5)
    ax.add_patch(r)
    ax.text(x + w/2, y + h*0.62, main, ha='center', va='center',
            fontsize=10, color=NAVY, fontweight='bold')
    ax.text(x + w/2, y + h*0.20, sub, ha='center', va='center',
            fontsize=7.5, color=tcol, style='italic')
save('2_11e_game_theory')

# ── 2.11e  Monopolistic Competition SR & LR ───────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, (title, P_offset) in zip(axes, [
        ('Monopolistic Comp. — SR\n(Abnormal Profit)', 1.5),
        ('Monopolistic Comp. — LR\n(Normal Profit)',   0)]):
    base_ax(ax, title=title)
    q = np.linspace(0.3,9,200)
    AR=8.5-0.9*q; MR=8.5-1.8*q; MC=0.06*q**2 + 0.45*q + 0.9
    qstar = q[np.argmin(np.abs(MC - MR))]
    Pstar = 8.5 - 0.9*qstar
    # Base AC shape, then shift:
    # SR keeps exogenous upward shift; LR is adjusted to satisfy AR=AC at MC=MR.
    ATC_base = 4/q + 0.5*q + 0.8
    if P_offset > 0:
        ATC = ATC_base + P_offset
    else:
        atc_at_qstar = 4/qstar + 0.5*qstar + 0.8
        ATC = ATC_base + (Pstar - atc_at_qstar)
    ax.plot(q,AR,color=BLUE,lw=2.2,label='D=AR')
    ax.plot(q[MR>0],MR[MR>0],color=BLUE,lw=2.2,ls='--',label='MR')
    ax.plot(q,MC,color=RED,lw=2.2,label='MC')
    ax.plot(q[(q>0.3)&(q<8.5)],ATC[(q>0.3)&(q<8.5)],color=ORANGE,lw=2.2,ls='-.',label='AC')
    atc_s = ATC[np.argmin(np.abs(q - qstar))]
    ax.plot(qstar,Pstar,'ko',ms=6)
    ax.plot([qstar,qstar],[0,Pstar],GRAY,lw=1,ls=':')
    ax.plot([0,qstar],[Pstar,Pstar],GRAY,lw=1,ls=':')
    ax.text(qstar+0.15,Pstar+0.15,'MC=MR\n(Profit max)',fontsize=8,color=NAVY)
    if P_offset > 0:
        ax.fill_between([0,qstar],[atc_s,atc_s],[Pstar,Pstar],alpha=0.25,color=GREEN,label='Abnormal\nprofit')
        ax.text(qstar/2,(Pstar+atc_s)/2-0.15,'Profit',ha='center',fontsize=9,color=GREEN,fontweight='bold')
    else:
        ax.text(qstar/2+0.3,Pstar-0.3,'Normal profit\n(AR=ATC)',ha='center',fontsize=8.5,color=GRAY,style='italic')
    ax.text(9.2,0.3,'D=AR',fontsize=9,color=BLUE,fontweight='bold')
    ax.text(4.4,1.1,'MR',fontsize=9,color=BLUE,fontweight='bold')
    ax.text(7.2,8.2,'MC',fontsize=9,color=RED,fontweight='bold')
    ax.text(8.7,7.5-0.35*P_offset,'AC',fontsize=9,color=ORANGE,fontweight='bold')
    ax.legend(fontsize=7.5, framealpha=0, loc='center right', bbox_to_anchor=(1.0, 0.44))
plt.suptitle('Monopolistic Competition',fontsize=11,color=NAVY,fontweight='bold')
save('2_11f_monopolistic_comp')

# ── 2.11f  Monopoly ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, title='Monopoly: Profit Maximisation & Welfare Loss')
q = np.linspace(0.3,9,200)
AR=9-q; MR=9-2*q; MC=0.07*q**2 + 0.35*q + 0.95; ATC=4/q+1+0.25*q
Qm = q[np.argmin(np.abs(MR - MC))]
Pm = 9 - Qm
MC_at_Qm = MC[np.argmin(np.abs(q - Qm))]
ATC_at_Qm = 4/Qm+1+0.25*Qm
Qpc = q[np.argmin(np.abs(AR - MC))]
Ppc = 9 - Qpc
Par_qm = 9 - Qm
ax.plot(q[q<9],AR[q<9],color=BLUE,lw=2.2,label='D=AR')
ax.plot(q[MR>0],MR[MR>0],color=BLUE,lw=2.2,ls='--',label='MR')
ax.plot(q[(MC>=0)&(MC<=9)],MC[(MC>=0)&(MC<=9)],color=RED,lw=2.2,label='MC')
ax.plot(q[(q>1)&(q<9)],ATC[(q>1)&(q<9)],color=ORANGE,lw=2.2,ls='-.',label='AC')
ax.fill_between([0,Qm],[ATC_at_Qm,ATC_at_Qm],[Pm,Pm],alpha=0.25,color=GREEN,label='Abnormal profit')
ax.fill([Qm,Qpc,Qm],[Pm,Ppc,MC_at_Qm],alpha=0.35,color=ORANGE,label='Welfare loss (DWL)')
ax.plot(Qm,Par_qm,'ko',ms=5)
ax.plot(Qpc,Ppc,marker='o',ms=5,mfc='white',mec=GREEN,mew=1.6)
ax.plot([Qm,Qm],[0,Pm],GRAY,lw=1,ls=':'); ax.plot([0,Qm],[Pm,Pm],GRAY,lw=1,ls=':')
ax.plot([0,Qm],[ATC_at_Qm,ATC_at_Qm],GRAY,lw=1,ls=':')
ax.plot([Qpc,Qpc],[0,Ppc],GRAY,lw=1,ls=':'); ax.plot([0,Qpc],[Ppc,Ppc],GRAY,lw=1,ls=':')
ax.text(Qm+0.1,0.3,'Qm',fontsize=9,color=NAVY); ax.text(Qpc+0.1,0.3,'Qpc',fontsize=9,color=NAVY)
ax.text(0.1,Pm+0.1,'Pm',fontsize=9,color=NAVY); ax.text(0.1,Ppc+0.1,'Ppc',fontsize=9,color=GRAY)
ax.text(9.1,0.3,'D=AR',fontsize=9,color=BLUE,fontweight='bold')
ax.text(4.1,1.1,'MR',fontsize=9,color=BLUE,fontweight='bold')
ax.text(7.3,8.0,'MC',fontsize=9,color=RED,fontweight='bold')
ax.text(9.2,3.7,'AC',fontsize=9,color=ORANGE,fontweight='bold')
ax.text(Qm+0.2,Pm+0.2,'MC=MR\nProfit max',fontsize=8,color=NAVY)
ax.text(Qpc+0.5,Ppc-0.2,'MC=AR\nAllocative Efficiency',fontsize=8,color=GREEN)
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('2_11c_monopoly')

# ── 2.12  Circular Flow & Inequality ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
ax.set_title('Circular Flow of Income',fontsize=11,color=NAVY,fontweight='bold')

# Main sectors (IB two-sector structure)
house_x, house_y, box_w, box_h = 0.9, 3.9, 2.7, 2.7
firm_x, firm_y = 6.4, 3.9
for (x,y,label,col) in [
    (house_x, house_y, 'Households', BLUE),
    (firm_x,  firm_y,  'Firms', RED)]:
    rect = mpatches.FancyBboxPatch((x,y),box_w,box_h,boxstyle='round,pad=0.08',
        facecolor=col,edgecolor='white',linewidth=1.3,alpha=0.92)
    ax.add_patch(rect)
    ax.text(x+box_w/2,y+box_h/2,label,ha='center',va='center',fontsize=17,color='white',fontweight='bold')

# Outer loop: real flow (goods/services and factors of production)
left_outer, right_outer = 1.5, 8.5
top_outer, bottom_outer = 8.3, 2.2
top_box, bottom_box = house_y + box_h, house_y

arrow_flow = dict(arrowstyle='-|>', color=GREEN, lw=2.25, mutation_scale=12)
arrow_money = dict(arrowstyle='-|>', color=ORANGE, lw=2.25, mutation_scale=12)
head_stub = 0.34

ax.plot([right_outer, left_outer], [top_outer, top_outer], color=GREEN, lw=2.25)
ax.plot([right_outer, right_outer], [top_box, top_outer], color=GREEN, lw=2.25)
ax.plot([left_outer, left_outer], [top_outer, top_box+head_stub], color=GREEN, lw=2.25)
ax.annotate('', xy=(left_outer, top_box), xytext=(left_outer, top_box+head_stub), arrowprops=arrow_flow)
ax.text(5.0, 8.56, 'Goods and Services', fontsize=12, color=NAVY, ha='center')

ax.plot([left_outer, left_outer], [bottom_box, bottom_outer], color=GREEN, lw=2.25)
ax.plot([left_outer, right_outer], [bottom_outer, bottom_outer], color=GREEN, lw=2.25)
ax.plot([right_outer, right_outer], [bottom_outer, bottom_box-head_stub], color=GREEN, lw=2.25)
ax.annotate('', xy=(right_outer, bottom_box), xytext=(right_outer, bottom_box-head_stub), arrowprops=arrow_flow)
ax.text(5.0, 1.62, 'Factors of Production', fontsize=12, color=NAVY, ha='center')

# Inner loop: money flow (expenditure and income)
left_inner, right_inner = 2.2, 7.8
top_inner, bottom_inner = 7.2, 3.2

ax.plot([left_inner, right_inner], [top_inner, top_inner], color=ORANGE, lw=2.25)
ax.plot([left_inner, left_inner], [top_box, top_inner], color=ORANGE, lw=2.25)
ax.plot([right_inner, right_inner], [top_inner, top_box+head_stub], color=ORANGE, lw=2.25)
ax.annotate('', xy=(right_inner, top_box), xytext=(right_inner, top_box+head_stub), arrowprops=arrow_money)
ax.text(5.0, 7.46, 'Expenditure', fontsize=12, color=NAVY, ha='center')

ax.plot([right_inner, right_inner], [bottom_box, bottom_inner], color=ORANGE, lw=2.25)
ax.plot([right_inner, left_inner], [bottom_inner, bottom_inner], color=ORANGE, lw=2.25)
ax.plot([left_inner, left_inner], [bottom_inner, bottom_box-head_stub], color=ORANGE, lw=2.25)
ax.annotate('', xy=(left_inner, bottom_box), xytext=(left_inner, bottom_box-head_stub), arrowprops=arrow_money)
ax.text(5.0, 2.75, 'Income', fontsize=12, color=NAVY, ha='center')

ax.text(0.3,0.25,'Inequality link: unequal factor of production ownership -> unequal incomes',
    fontsize=8,color=NAVY,style='italic')
save('2_12a_circular_flow')


# ═══════════════════════════════════════════════════════════════════════════════
# UNIT 3 — MACROECONOMICS
# ═══════════════════════════════════════════════════════════════════════════════

# ── 3.1a  Business Cycle ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY);   ax.spines['bottom'].set_color(NAVY)
t = np.linspace(0, 4*np.pi, 300)
trend = 0.4*t+2; cycle = np.sin(t)*1.2; actual = trend+cycle
ax.plot(t,trend, color=RED, lw=2,ls='--',label='Potential output (trend)')
ax.plot(t,actual,color=BLUE,lw=2.5,label='Actual real GDP')
ax.text(np.pi*0.5+0.2,actual[int(0.5*300/4)]+0.2,'Peak',fontsize=9,color=NAVY,ha='center')
ax.text(np.pi*1.5-0.3,actual[int(1.5*300/4)]-0.4,'Trough',fontsize=9,color=NAVY,ha='center')
ax.text(np.pi*1.0-0.2,actual[int(1.0*300/4)]-0.6,'Recession',fontsize=9,color=RED,ha='center',style='italic')
ax.text(np.pi*0.25-0.5,actual[int(0.25*300/4)]+0.4,'Expansion',fontsize=9,color=GREEN,ha='center',style='italic')
ax.annotate('',xy=(np.pi*0.5,trend[int(0.5*300/4)]),xytext=(np.pi*0.5,actual[int(0.5*300/4)]),
    arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=1.5))
ax.text(np.pi*0.5+0.05,(trend[int(0.5*300/4)]+actual[int(0.5*300/4)])/2-0.2,
    'Inflationary\ngap',fontsize=6.5,color=ORANGE)
ax.set_xlabel('Time',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Real GDP',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('The Business Cycle',fontsize=11,color=NAVY,fontweight='bold')
ax.set_xticks([]); ax.set_yticks([])
ax.legend(fontsize=9,framealpha=0)
save('3_1a_business_cycle')

# ── 3.1b  Circular Flow: Leakages & Injections ───────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
ax.set_title('Circular Flow: Leakages & Injections',fontsize=11,color=NAVY,fontweight='bold')

# Same core structure as 2.12 circular flow
house_x, house_y, box_w, box_h = 0.9, 3.9, 2.7, 2.7
firm_x, firm_y = 6.4, 3.9
for (x,y,label,col) in [(house_x, house_y, 'Households', BLUE), (firm_x, firm_y, 'Firms', RED)]:
    rect = mpatches.FancyBboxPatch((x,y),box_w,box_h,boxstyle='round,pad=0.08',
        facecolor=col,edgecolor='white',linewidth=1.32,alpha=0.92)
    ax.add_patch(rect)
    ax.text(x+box_w/2,y+box_h/2,label,ha='center',va='center',fontsize=14,color='white',fontweight='bold')

left_outer, right_outer = 1.5, 8.5
top_outer, bottom_outer = 8.3, 2.2
top_box, bottom_box = house_y + box_h, house_y
left_inner, right_inner = 2.2, 7.8
top_inner, bottom_inner = 7.2, 3.2
head_stub = 0.34
arrow_flow = dict(arrowstyle='-|>', color=GREEN, lw=2.25, mutation_scale=12)
arrow_money = dict(arrowstyle='-|>', color=ORANGE, lw=2.25, mutation_scale=12)

# Real flow (outer loop)
ax.plot([right_outer, left_outer], [top_outer, top_outer], color=GREEN, lw=2.25)
ax.plot([right_outer, right_outer], [top_box, top_outer], color=GREEN, lw=2.25)
ax.plot([left_outer, left_outer], [top_outer, top_box+head_stub], color=GREEN, lw=2.25)
ax.annotate('', xy=(left_outer, top_box), xytext=(left_outer, top_box+head_stub), arrowprops=arrow_flow)
ax.text(5.0, 8.56, 'Goods and Services', fontsize=12, color=NAVY, ha='center')

ax.plot([left_outer, left_outer], [bottom_box, bottom_outer], color=GREEN, lw=2.25)
ax.plot([left_outer, right_outer], [bottom_outer, bottom_outer], color=GREEN, lw=2.25)
ax.plot([right_outer, right_outer], [bottom_outer, bottom_box-head_stub], color=GREEN, lw=2.25)
ax.annotate('', xy=(right_outer, bottom_box), xytext=(right_outer, bottom_box-head_stub), arrowprops=arrow_flow)
ax.text(5.0, 1.62, 'Factors of Production', fontsize=12, color=NAVY, ha='center')

# Inner loop: money flow (expenditure and income)
left_inner, right_inner = 2.2, 7.8
top_inner, bottom_inner = 7.2, 3.2

ax.plot([left_inner, right_inner], [top_inner, top_inner], color=ORANGE, lw=2.25)
ax.plot([left_inner, left_inner], [top_box, top_inner], color=ORANGE, lw=2.25)
ax.plot([right_inner, right_inner], [top_inner, top_box+head_stub], color=ORANGE, lw=2.25)
ax.annotate('', xy=(right_inner, top_box), xytext=(right_inner, top_box+head_stub), arrowprops=arrow_money)
ax.text(5.0, 7.46, 'Expenditure', fontsize=12, color=NAVY, ha='center')

ax.plot([right_inner, right_inner], [bottom_box, bottom_inner], color=ORANGE, lw=2.25)
ax.plot([right_inner, left_inner], [bottom_inner, bottom_inner], color=ORANGE, lw=2.25)
ax.plot([left_inner, left_inner], [bottom_inner, bottom_box-head_stub], color=ORANGE, lw=2.25)
ax.annotate('', xy=(left_inner, bottom_box), xytext=(left_inner, bottom_box-head_stub), arrowprops=arrow_money)
ax.text(5.0, 2.75, 'Income', fontsize=12, color=NAVY, ha='center')

# Leakages/Withdrawals from money flow
ax.text(-0.6, 6.25, 'Leakages', fontsize=9.5, color=RED, fontweight='bold', ha='left')
for y,lbl,col in [(6.45,'S',RED),(5.90,'T',ORANGE),(5.35,'M',PURPLE)]:
    ax.annotate('', xy=(0.18,y-0.7), xytext=(0.76,y-0.7),
        arrowprops=dict(arrowstyle='-|>', color=col, lw=2, mutation_scale=10))
    ax.text(0,y-0.85,lbl,fontsize=10,color=col,fontweight='bold',ha='center',va='bottom')

# Injections into money flow
ax.text(10, 6.25, 'Injections', fontsize=9.5, color=GREEN, fontweight='bold', ha='center')
for y,lbl,col in [(6.45,'I',GREEN),(5.90,'G',BLUE),(5.35,'X',NAVY)]:
    ax.annotate('', xy=(9.24,y-0.7), xytext=(9.86,y-0.7),
        arrowprops=dict(arrowstyle='-|>', color=col, lw=2, mutation_scale=10))
    ax.text(10,y-0.85,lbl,fontsize=10,color=col,fontweight='bold',ha='center',va='bottom')

ax.text(5.0,0.58,'Equilibrium condition:  S + T + M = I + G + X',
    fontsize=9.3,color=NAVY,style='italic',fontweight='bold',ha='center')
save('3_1b_circular_flow_leakages')

# ── 3.2a  AD / AS Model ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4.5))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY);   ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Real GDP (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Price Level (PL)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('AD / AS Model',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9,100)
AD1=9-Q; AD2=11-Q; SRAS=1+0.8*Q; Yf=10/1.8
ax.plot(Q,AD1,color=BLUE,lw=2.2,label='AD₁')
ax.plot(Q,AD2,color=BLUE,lw=2.2,ls='--',label='AD₂ (↑AD)')
ax.plot(Q,SRAS,color=RED, lw=2.2,label='SRAS')
ax.axvline(Yf,color=NAVY,lw=2.2,label='LRAS')
Q1=8/1.8; P1=9-Q1; Q2=10/1.8; P2=11-Q2
ax.plot(Q1,P1,'bo',ms=5); ax.plot(Q2,P2,'bo',ms=5)
ax.plot([Q1,Q1],[0,P1],GRAY,lw=1,ls=':')
ax.plot([0,Q1],[P1,P1],GRAY,lw=1,ls=':'); ax.plot([0,Q2],[P2,P2],GRAY,lw=1,ls=':')
ax.text(Q1-0.2,0.3,'Y₁',fontsize=9,color=NAVY)
ax.text(Yf+0.1,0.3,'Yf',fontsize=9,color=NAVY)
ax.text(0.1,P1+0.1,'PL₁',fontsize=9,color=NAVY); ax.text(0.1,P2+0.1,'PL₂',fontsize=9,color=NAVY)
ax.text(9.1,0.3,'AD₁',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,1.8,'AD₂',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,8.5,'SRAS',fontsize=8,color=RED,fontweight='bold')
ax.text(Yf+0.1,9.3,'LRAS',fontsize=9,color=NAVY,fontweight='bold')
ax.annotate('',xy=(Yf,1.5),xytext=(Q1,1.5),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=1.5))
ax.text((Yf+Q1)/2,1.8,'Recessionary gap',fontsize=7.5,color=ORANGE,ha='center')
ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('3_2a_AD_AS')

# ── 3.2b  Keynesian vs Monetarist AS ──────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

for ax, (title, model) in zip(axes, [
        ('Monetarist / New Classical Model', 'monetarist'),
        ('Keynesian Model',                  'keynesian')]):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
    ax.set_xlabel('Real GDP (Y)', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_ylabel('Price Level',  fontsize=10, color=NAVY, fontweight='bold')
    ax.set_title(title, fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xticks([]); ax.set_yticks([])

    Q = np.linspace(0.5, 9.5, 300)
    ax.plot(Q, 9-Q, color=BLUE, lw=2.2, label='AD')
    ax.text(9.1, 0.3, 'AD', fontsize=9, color=BLUE, fontweight='bold')

    if model == 'monetarist':
        # SRAS upward sloping, then vertical LRAS
        ax.plot(Q, 1 + 0.7*Q, color=RED, lw=2.2, label='SRAS')
        ax.axvline(5.5, color=NAVY, lw=2.5, label='LRAS')
        ax.text(5.7, 0.3, 'Yf', fontsize=9, color=NAVY)
        ax.text(9.1, 7, 'SRAS', fontsize=9, color=RED, fontweight='bold')
        ax.text(5.6, 9.3, 'LRAS', fontsize=9, color=NAVY, fontweight='bold')
        ax.text(3.1, 2,
                'Self-correcting:\nwages flexible,\nauto-returns to Yf',
                fontsize=8.5, color=GREEN, style='italic')

    else:
        # Keynesian AS: flat, then smooth asymptotic rise toward Yf.
        Yf_shift = -1.5
        Yf     = 8.2 + Yf_shift   # full-capacity output (vertical asymptote location)
        P_flat = 2.5   # price level in the flat (Keynesian) zone
        Q_turn = 4.2   # where the curve starts to bend up

        # Segment 1 - flat section
        Q1 = np.linspace(0.3, Q_turn, 90, endpoint=False)
        P1 = np.full_like(Q1, P_flat)

        # Segment 2 - asymptotic branch approaching Yf from the left
        Q2 = np.linspace(Q_turn, Yf - 0.09, 260)
        u = (Q2 - Q_turn) / (Yf - Q_turn)  # 0 -> 1
        rise = (1.0 / (Yf - Q2)) - (1.0 / (Yf - Q_turn))
        P2 = P_flat + 0.82 * rise * (u**1.35)  # higher asymptote while keeping smooth approach

        # Stitch together
        Q_as = np.concatenate([Q1, Q2])
        P_as = np.concatenate([P1, P2])
        # Clip to visible window
        mask = (P_as <= 10) & (Q_as <= 10)

        ax.plot(Q_as[mask], P_as[mask], color=RED, lw=2.5, label='AS (Keynesian)')
        ax.axvline(Yf, color=NAVY, lw=2, ls='--', label='Full capacity (Yf)')
        ax.text(Yf + 0.15, 0.3, 'Yf', fontsize=9, color=NAVY)
        ax.text(Yf - 0.8, 8.0, 'AS', fontsize=9, color=RED, fontweight='bold')

        # Zone labels
        ax.text(3.5-0.5, 1.2,
                'Keynesian zone\n(spare capacity,\nsticky wages)',
                fontsize=8, color=ORANGE, style='italic', ha='center')
        ax.text(6.7-1.5, 3,
                'Intermediate\nzone',
                fontsize=8, color=GRAY, style='italic', ha='center')
        ax.text(7.2-1.5, 6, 'Classical\nzone', fontsize=8, color=NAVY,
                style='italic', ha='center')

    ax.legend(fontsize=8, framealpha=0, loc='upper right')

plt.suptitle('Keynesian vs Monetarist AS Model',
             fontsize=11, color=NAVY, fontweight='bold')
save('3_2b_keynesian_vs_monetarist')


# ── 3.3a  PPC: Actual vs Potential Growth ────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4.5))
ax.spines['top'].set_visible(False); ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(True); ax.spines['right'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Consumer Goods',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Capital Goods',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('PPC: Actual vs Potential Growth',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,12); ax.set_ylim(0,12); ax.set_xticks([]); ax.set_yticks([])
th = np.linspace(0,np.pi/2,100)
ax.plot(8*np.cos(th),8*np.sin(th),  color=NAVY, lw=2.5,label='PPC₁')
ax.plot(11*np.cos(th),11*np.sin(th),color=GREEN,lw=2.5,ls='--',label='PPC₂ (potential growth)')
ax.plot(3,3,'rx',ms=12,mew=2.5,label='A: below capacity')
ax.plot(5.65,5.65,'bo',ms=8,label='B: actual growth')
ax.annotate('',xy=(5.3,5.3),xytext=(3.4,3.4),arrowprops=dict(arrowstyle='->',color=BLUE,lw=2))
ax.text(3.2,4.5,'Actual\ngrowth',fontsize=8.5,color=BLUE,style='italic')
ax.annotate('',xy=(7.6,7.6),xytext=(5.9,5.9),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2))
ax.text(5.4,6.8,'Potential\ngrowth',fontsize=8.5,color=GREEN,style='italic')
ax.legend(fontsize=8,framealpha=0,loc='upper right')
save('3_3a_PPC_growth')

# ── 3.3b  LRAS Shifting Right ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Real GDP (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Price Level',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Long-Run Economic Growth\n(LRAS shifts right)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9.5,100)
yf1 = 8/1.8
ax.plot(Q,9-Q,color=BLUE,lw=2.2,label='AD')
ax.plot(Q,1+0.8*Q,color=RED,lw=2.2,label='SRAS')
ax.axvline(yf1,color=NAVY,lw=2.2,label='LRAS₁')
ax.axvline(7,color=GREEN,lw=2.5,ls='--',label='LRAS₂')
ax.annotate('',xy=(6.9,1.5),xytext=(4.7,1.5),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2.5))
ax.text(5.5,2.0,'Economic\ngrowth',ha='center',fontsize=9,color=GREEN,fontweight='bold')
ax.text(yf1+0.1,0.3,'Yf₁',fontsize=9,color=NAVY); ax.text(7.1,0.3,'Yf₂',fontsize=9,color=GREEN)
ax.legend(fontsize=8,framealpha=0,loc='center right')
save('3_3b_LRAS_growth')

# ── 3.3c  Demand-Pull vs Cost-Push Inflation ─────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, (title, ad_shift) in zip(axes, [
        ('Demand-Pull Inflation', True),
        ('Cost-Push Inflation',   False)]):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
    ax.set_xlabel('Real GDP (Y)',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_ylabel('Price Level',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_title(title,fontsize=10,color=NAVY,fontweight='bold')
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
    Q = np.linspace(0.5,9.5,100)
    AD=9-Q; AD2=11-Q; SR1=1+0.8*Q; SR2=3+0.8*Q
    ax.plot(Q,SR1,color=RED,lw=2.2,label='SRAS')
    ax.text(8.7, 7.55, 'SRAS', fontsize=8.5, color=RED, fontweight='bold')
    if ad_shift:
        ax.plot(Q,AD, color=BLUE,lw=2.2,label='AD')
        ax.plot(Q,AD2,color=BLUE,lw=2.2,ls='--',label='AD₁')
        Q1,P1=8/1.8,9-8/1.8; Q2,P2=10/1.8,11-10/1.8
        ax.plot(Q1,P1,'bo',ms=5); ax.plot(Q2,P2,'bo',ms=5)
        arrow_off = 0.23
        ax.annotate('', xy=(Q2-0.2,P2+arrow_off), xytext=(Q1-0.2,P1+arrow_off),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.6, shrinkA=5, shrinkB=5))
        ax.text((Q1+Q2)/2-0.7, (P1+P2)/2+0.5, '↑Y, ↑PL', ha='center', fontsize=8, color=GREEN)
        ax.text(9.1,0.2,'AD',fontsize=8.5,color=BLUE,fontweight='bold')
        ax.text(9.1,1,'AD₁',fontsize=8.5,color=BLUE,fontweight='bold')
    else:
        ax.plot(Q,SR2,color=RED,lw=2.2,ls='--',label='SRAS₁')
        ax.text(7.2, 8.3, 'SRAS₁', fontsize=8.5, color=RED, fontweight='bold')
        ax.plot(Q,AD, color=BLUE,lw=2.2,label='AD')
        Q1,P1=8/1.8,9-8/1.8; Q2,P2=6/1.8,9-6/1.8
        ax.plot(Q1,P1,'bo',ms=5); ax.plot(Q2,P2,'bo',ms=5)
        arrow_off = 0.23
        ax.annotate('', xy=(Q2+0.2,P2+arrow_off), xytext=(Q1+0.2,P1+arrow_off),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.6, shrinkA=5, shrinkB=5))
        ax.text((Q1+Q2)/2+0.9, (P1+P2)/2+0.5, '↓Y, ↑PL\n(Stagflation)', ha='center', fontsize=8, color=ORANGE)
        ax.text(9.1,0.2,'AD',fontsize=8.5,color=BLUE,fontweight='bold')
    ax.legend(fontsize=7.5,framealpha=0)
save('3_3c_inflation')

# ── 3.3d  Minimum Wage & Unemployment ────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, xlabel='Quantity of Labour (L)', ylabel='Wage Rate (W)',
        title='Minimum Wage & Unemployment')
Q = np.linspace(0.5,9.5,100)
ax.plot(Q,10-Q,color=BLUE,lw=2.2,label='Demand for labour')
ax.plot(Q,Q,color=RED, lw=2.2,label='Supply of labour')
ax.axhline(7,color=GREEN,lw=2.5,label='Minimum wage (Wmin)')
ax.plot(5,5,'ko',ms=5)
Ld=10-7; Ls=7
ax.plot([Ld,Ld],[0,7],GRAY,lw=1,ls='--'); ax.plot([Ls,Ls],[0,7],GRAY,lw=1,ls='--')
ax.annotate('',xy=(Ls,1),xytext=(Ld,1),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Ld+Ls)/2,1.4,'Unemployment',ha='center',fontsize=9,color=ORANGE,fontweight='bold')
ax.text(0.1,7.2,'Wmin',fontsize=9,color=GREEN,fontweight='bold')
ax.text(0.1,5.2,'W*',fontsize=9,color=NAVY)
ax.text(Ld+0.1,0.3,'Ld',fontsize=9,color=NAVY); ax.text(Ls+0.1,0.3,'Ls',fontsize=9,color=NAVY)
ax.text(9.1,0.2,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=8,framealpha=0)
save('3_3d_minimum_wage_unemployment')

# ── 3.3cc  Fall in Labour Demand & Local Unemployment ─────────────────────────
fig, ax = plt.subplots(figsize=(5.2, 4))
base_ax(ax, xlabel='Quantity of Labour (L)', ylabel='Wage Rate (W)',
        title='Fall in Labour Demand & Local Unemployment')
Q = np.linspace(0.5, 9.5, 120)
S_lab = Q
D1 = 10 - Q
D2 = 7.5 - Q
ax.plot(Q, D1, color=BLUE, lw=2.2, label='D for labour')
ax.plot(Q[D2 > 0], D2[D2 > 0], color=BLUE, lw=2.2, ls='--', label='D₁ for labour')
ax.plot(Q, S_lab, color=RED, lw=2.2, label='S of labour')
q1, w1 = 5.0, 5.0
q2, w2 = 3.75, 3.75
ax.plot(q1, w1, 'o', ms=5.5, color=BLUE, zorder=6)
ax.plot(q2, w2, 'o', ms=5.5, color=ORANGE, zorder=6)
ax.plot([q1, q1], [0, w1], color=GRAY, lw=1, ls=':')
ax.plot([q2, q2], [0, w2], color=GRAY, lw=1, ls=':')
ax.plot([0, q1], [w1, w1], color=GRAY, lw=1, ls=':')
ax.plot([0, q2], [w2, w2], color=GRAY, lw=1, ls=':')
ax.annotate('', xy=(q2, 1.05), xytext=(q1, 1.05),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
ax.text((q1 + q2) / 2, 1.35, 'Employment falls', ha='center',
        fontsize=8.4, color=ORANGE, fontweight='bold')
ax.text((q1 + q2) / 2 + 2.8, 4.6, 'Demand for labour falls\nin a sector / region',
        ha='center', fontsize=8.1, color=BLUE, fontweight='bold')
ax.text(0.15, w1 + 0.1, 'W1', fontsize=8.3, color=NAVY)
ax.text(0.15, w2 + 0.1, 'W2', fontsize=8.3, color=NAVY)
ax.text(q1 - 0.12, 0.3, 'L1', fontsize=8.3, color=NAVY)
ax.text(q2 - 0.12, 0.3, 'L2', fontsize=8.3, color=NAVY)
ax.text(9.1, 0.2, 'D', fontsize=10, color=BLUE, fontweight='bold')
ax.text(6.7, 0.2, 'D₁', fontsize=10, color=BLUE, fontweight='bold')
ax.text(9.1, 8.6, 'S', fontsize=10, color=RED, fontweight='bold')
ax.legend(fontsize=7.8, framealpha=0, loc='upper center')
save('3_3e_labour_demand_fall')

# ── 3.3e  Deflationary Gap ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Real GDP (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Price Level',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Deflationary Gap & Cyclical Unemployment',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9.5,100)
ax.plot(Q,7-Q,color=BLUE,lw=2.2,label='AD (below full\nemployment)')
ax.plot(Q,1+0.8*Q,color=RED,lw=2.2,label='SRAS')
ax.axvline(6,color=NAVY,lw=2.2,ls='--',label='LRAS (Yf)')
Ye=6/1.8; Pe=7-Ye
ax.plot(Ye,Pe,'bo',ms=6)
ax.plot([Ye,Ye],[0,Pe],GRAY,lw=1,ls=':'); ax.plot([0,Ye],[Pe,Pe],GRAY,lw=1,ls=':')
ax.text(0.1,Pe+0.1,'Pe',fontsize=9,color=NAVY)
ax.annotate('',xy=(6,1.2),xytext=(Ye,1.2),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((6+Ye)/2,0.4,'Deflationary gap\n(cyclical unemployment)',ha='center',fontsize=6,color=ORANGE,fontweight='bold')
ax.text(Ye-0.4,0.3,'Ye',fontsize=9,color=NAVY); ax.text(6.1,0.3,'Yf',fontsize=9,color=NAVY)
ax.legend(fontsize=8,framealpha=0,loc='center right')
save('3_3f_deflationary_gap')

# ── 3.3f  Deflation ───────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, (title, shift) in zip(axes, [
        ('Demand-Side Deflation\n(AD falls)',          'AD'),
        ('Supply-Side Deflation\n(SRAS rises — benign)','SRAS')]):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
    ax.set_xlabel('Real GDP',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_ylabel('Price Level',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_title(title,fontsize=10,color=NAVY,fontweight='bold')
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
    Q = np.linspace(0.5,9.5,100)
    if shift == 'AD':
        ax.plot(Q,9-Q,color=BLUE,lw=2,label='AD')
        ax.plot(Q,7-Q,color=BLUE,lw=2,ls='--',label='AD₁ (↓)')
        ax.plot(Q,1+0.8*Q,color=RED,lw=2.2,label='SRAS')
        Q1=8/1.8; P1=9-Q1; Q2=6/1.8; P2=7-Q2
        ax.plot(Q1,P1,'bo',ms=5); ax.plot(Q2,P2,'ro',ms=5)
        ax.annotate('',xy=(Q2-0.2,P2+0.1),xytext=(Q1-0.2,P1+0.1),arrowprops=dict(arrowstyle='->',color=RED,lw=1.5))
        ax.text((Q1+Q2)/2-0.65,P1,'↓Y, ↓PL\n(harmful)',ha='center',fontsize=8.5,color=RED,fontweight='bold')
        ax.text(9,0.3,'AD',fontsize=8.5,color=BLUE,fontweight='bold'); ax.text(7,0.3,'AD₁',fontsize=8.5,color=BLUE,fontweight='bold')
        ax.text(9,8.8,'SRAS',fontsize=8.5,color=RED,fontweight='bold')
    else:
        ax.plot(Q,9-Q,color=BLUE,lw=2.2,label='AD')
        ax.plot(Q,1+0.8*Q,color=RED,lw=2,label='SRAS')
        ax.plot(Q,-1+0.8*Q,color=RED,lw=2,ls='--',label='SRAS₁ (↑)')
        Q1=8/1.8; P1=9-Q1; Q2=10/1.8; P2=9-Q2
        ax.plot(Q1,P1,'ro',ms=5); ax.plot(Q2,P2,'go',ms=5)
        ax.annotate('',xy=(Q2+0.2,P2+0.1),xytext=(Q1+0.2,P1+0.1),arrowprops=dict(arrowstyle='->',color=GREEN,lw=1.5))
        ax.text((Q1+Q2)/2+0.85,P1-0.1,'↑Y, ↓PL\n(benign)',ha='center',fontsize=8.5,color=GREEN,fontweight='bold')
        ax.text(9.1,0.3,'AD',fontsize=8.5,color=BLUE,fontweight='bold')
        ax.text(9.1,8.8,'SRAS',fontsize=8,color=RED,fontweight='bold'); ax.text(9.1,6.8,'SRAS₁',fontsize=8,color=RED,fontweight='bold')
    ax.legend(fontsize=7.5,framealpha=0)
save('3_3g_deflation')

# ── 3.3g  Short-Run & Long-Run Phillips Curve (HL) ────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Unemployment Rate (%)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Inflation Rate (%)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Short-Run & Long-Run Phillips Curve (HL)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(-1,10); ax.set_xticks([]); ax.set_yticks([])
U = np.linspace(0.5,9.5,100)
SRPC1 = 8-U; SRPC2 = 12-U; NRU = 4
ax.plot(U[SRPC1>-0.5],SRPC1[SRPC1>-0.5],color=BLUE,lw=2.2,label='SRPC₁')
ax.plot(U[SRPC2>-0.5],SRPC2[SRPC2>-0.5],color=BLUE,lw=2.2,ls='--',label='SRPC₂ (higher expectations)')
ax.axvline(NRU,color=RED,lw=2.5,label='LRPC (= NRU)')
A_u,A_pi=4,4; B_u,B_pi=2,6; C_u,C_pi=4,8
ax.plot(A_u,A_pi,'bo',ms=7); ax.plot(B_u,B_pi,'go',ms=7); ax.plot(C_u,C_pi,'rs',ms=7)
ax.text(A_u+0.15,A_pi+0.2,'A',fontsize=10,color=BLUE,fontweight='bold')
ax.text(B_u-0.1,B_pi+0.4,'B',fontsize=10,color=GREEN,fontweight='bold')
ax.text(C_u+0.15,C_pi+0.2,'C',fontsize=10,color=RED,fontweight='bold')
ax.annotate('',xy=(B_u-0.1+0.05,B_pi-0.1-0.05),xytext=(A_u-0.1,A_pi-0.1),arrowprops=dict(arrowstyle='->',color=GREEN,lw=1.5))
ax.annotate('',xy=(C_u-0.1,C_pi-0.1),xytext=(B_u+0.1,B_pi+0.1),arrowprops=dict(arrowstyle='->',color=RED,lw=1.5))
ax.text(4.1,0.3,'NRU',fontsize=9,color=RED,fontweight='bold')
ax.legend(fontsize=8.5,framealpha=0)
save('3_3h_phillips_curve')

# ── 3.4  Lorenz Curve & Gini ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4.5))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(True); ax.spines['right'].set_color(NAVY)
ax.spines['left'].set_visible(False); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Cumulative % of Population',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Cumulative % of Income',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Lorenz Curve & Gini Coefficient',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,100); ax.set_ylim(0,100)
ax.set_xticks([0,20,40,60,80,100]); ax.set_yticks([0,20,40,60,80,100])
ax.yaxis.set_label_position('right'); ax.yaxis.tick_right()
ax.tick_params(axis='y', colors=NAVY, labelsize=8, left=False, right=True, labelleft=False, labelright=True)
ax.tick_params(axis='x', colors=NAVY, labelsize=8)
pop  = np.array([0,20,40,60,80,100])
inc1 = np.array([0, 5,15,30,55,100])
inc2 = np.array([0,12,28,48,72,100])
BLUE_DARK = NAVY
BLUE_LIGHT = BLUE
ax.plot([0,100],[0,100],color=GRAY,lw=1.5,ls='--',label='Line of perfect equality')
ax.plot(pop,inc1,color=BLUE_DARK, lw=2.2,marker='o',ms=5,label='Lorenz (high inequality)')
ax.plot(pop,inc2,color=BLUE_LIGHT,lw=2.2,marker='s',ms=5,label='Lorenz (lower inequality)')
ax.fill_between(pop,pop,inc1,alpha=0.15,color=BLUE_LIGHT)
ax.fill_between(pop,0,inc1,alpha=0.12,color=RED)
ax.text(60,40,'Area A',ha='center',fontsize=9,color=BLUE_DARK,style='italic')
ax.text(75,20,'Area B',ha='center',fontsize=9,color=RED,style='italic')
ax.text(30,60,'Gini = A/(A+B)',ha='center',fontsize=9,color='black',style='italic')
ax.legend(fontsize=7.5,framealpha=0,loc='upper left')
save('3_4a_lorenz_curve')

# ── 3.5a  Money Market (HL) ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Quantity of Money (M)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Nominal Interest Rate (i)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Money Market — Equilibrium Interest Rate (HL)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(1,9.5,100)
ax.plot(Q,9-Q,color=BLUE,lw=2.2,label='Md (money demand)')
ax.axvline(5,color=RED,lw=2.5,label='Ms (central bank)')
ax.axvline(7,color=RED,lw=2.5,ls='--',label='Ms₁ (↑ money supply)')
ax.plot(5,4,'ko',ms=6,zorder=6); ax.plot(7,2,'go',ms=6,zorder=6)
ax.plot([0,5],[4,4],GRAY,lw=1,ls='--'); ax.plot([0,7],[2,2],GRAY,lw=1,ls='--')
ax.annotate('',xy=(0.5,2),xytext=(0.5,4),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2))
ax.text(0.7,3,'↓i',fontsize=9,color=GREEN,fontweight='bold')
ax.text(0.1,4.2,'i',fontsize=9,color=NAVY); ax.text(0.1,2.2,'i₁',fontsize=9,color=GREEN)
ax.text(5.1,0.3,'Ms',fontsize=9,color=RED); ax.text(7.1,0.3,'Ms₁',fontsize=9,color=RED)
ax.text(9.1,0.3,'Md',fontsize=9,color=BLUE,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper left')
save('3_5a_money_market')

# ── 3.5b  Monetary Policy: AD/AS ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, (title, expand) in zip(axes, [
        ('Expansionary Monetary Policy\n(↓i → ↑AD)', True),
        ('Contractionary Monetary Policy\n(↑i → ↓AD)',False)]):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
    ax.set_xlabel('Real GDP (Y)',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_ylabel('Price Level',fontsize=9,color=NAVY,fontweight='bold')
    ax.set_title(title,fontsize=9.5,color=NAVY,fontweight='bold')
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
    Q = np.linspace(0.5,9.5,100)
    SRAS = 1+0.8*Q
    Yf = 4.0
    AD1_int = 6.6 if expand else 9.8
    AD2_int = 8.2
    AD1 = AD1_int-Q
    AD2 = AD2_int-Q
    ax.plot(Q,AD1,color=BLUE,lw=2,label='AD')
    ax.plot(Q,AD2,color=BLUE,lw=2.5,ls=':',label='AD₁')
    ax.plot(Q,SRAS,color=RED,lw=2.2,label='SRAS')
    ax.axvline(Yf,color=NAVY,lw=2.2,label='LRAS (Yf)')
    Q1 = (AD1_int-1) / 1.8
    Q2 = (AD2_int-1) / 1.8
    P1 = 1 + 0.8*Q1; P2 = 1 + 0.8*Q2
    ax.plot(Q1,P1,'o',ms=5,color=BLUE,zorder=6); ax.plot(Q2,P2,'o',ms=5,color=GREEN if expand else RED,zorder=6)
    ax.plot([Q1,Q1],[0,P1],color=GRAY,lw=1,ls='--'); ax.plot([0,Q1],[P1,P1],color=GRAY,lw=1,ls='--')
    if abs(Q2-Yf) > 1e-9:
        ax.plot([Q2,Q2],[0,P2],color=GRAY,lw=1,ls='--')
    ax.plot([0,Q2],[P2,P2],color=GRAY,lw=1,ls='--')
    ax.text(Q1-0.18,P1+0.25,'E',fontsize=8.5,color=BLUE,fontweight='bold')
    ax.text(Q2+0.22,P2-0.14,'E₁',fontsize=8.5,color=GREEN if expand else RED,fontweight='bold')
    col = GREEN if expand else RED
    ax.annotate('',xy=(Q2,1.0),xytext=(Q1,1.0),arrowprops=dict(arrowstyle='->',color=col,lw=2))
    ax.text(Yf+0.1,0.3,'Yf',fontsize=9,color=NAVY)
    ax.text(Q1-0.3,0.3,'Y₁',fontsize=8,color=BLUE)
    if abs(Q2-Yf) > 1e-9:
        ax.text(Q2-0.1,0.3,'Y₂',fontsize=8,color=GREEN if expand else RED)
    ax.text(0.15,P1+0.12,'PL',fontsize=8,color=BLUE)
    ax.text(0.15,P2+0.12,'PL₁',fontsize=8,color=GREEN if expand else RED)
    ax.text((Q1+Q2)/2,1.35,'Output rises' if expand else 'Output falls',ha='center',fontsize=8,color=col,fontweight='bold')
    x_ad1 = 6.6 if expand else 7.1
    x_ad2 = 7.7 if expand else 8.0
    ax.text(x_ad1,AD1_int-x_ad1+0.25,'AD',fontsize=8,color=BLUE,fontweight='bold')
    ax.text(x_ad2,AD2_int-x_ad2+0.2,'AD₁',fontsize=8,color=BLUE,fontweight='bold')
    ax.text(8.6,8.6,'SRAS',fontsize=8,color=RED,fontweight='bold')
    ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('3_5b_monetary_policy')

# ── 3.6a  Fiscal Policy & Keynesian Multiplier (HL) ──────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Real GDP (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Price Level',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Fiscal Policy & Keynesian Multiplier (HL)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9.5,100)
AD0 = 8-Q
ADg = 9-Q
AD1 = 10.5-Q
Yf = 9.5/1.6
ax.plot(Q,AD0,color=BLUE,lw=2.2,label='AD')
ax.plot(Q,ADg,color=BLUE,lw=2,ls=':',label='AD + ΔG')
ax.plot(Q,AD1,color=NAVY,lw=2.4,ls=':',label='AD₁ (after multiplier)')
ax.plot(Q,1+0.6*Q,color=RED,lw=2.2,label='SRAS')
ax.axvline(Yf,color=NAVY,lw=2.2,label='LRAS')
Q0=7/1.6; P0=8-Q0
Qg=8/1.6; Pg=9-Qg
Q1=9.5/1.6; P1=10.5-Q1
ax.plot(Q0,P0,'o',ms=5,color=BLUE,zorder=6)
ax.plot(Qg,Pg,'o',ms=5,color=ORANGE,zorder=6)
ax.plot(Q1,P1,'o',ms=5,color=NAVY,zorder=6)
ax.plot([Q0,Q0],[0,P0],GRAY,lw=1,ls=':')
ax.plot([Qg,Qg],[0,Pg],color=LGRAY,lw=1,ls=':')
ax.plot([0,Q0],[P0,P0],GRAY,lw=1,ls=':')
ax.plot([0,Yf],[P1,P1],GRAY,lw=1,ls=':')
ax.text(Q0,P0+0.22,'E',ha='center',fontsize=8.5,color=BLUE,fontweight='bold')
ax.text(Qg+0.05,Pg+0.2,"E'",ha='center',fontsize=8.5,color=ORANGE,fontweight='bold')
ax.text(Q1+0.05,P1+0.22,'E₁',fontsize=8.5,color=NAVY,fontweight='bold')
ax.annotate('',xy=(Qg,1.05),xytext=(Q0,1.05),arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.8))
ax.annotate('',xy=(Q1,1.45),xytext=(Q0,1.45),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2))
ax.text((Q0+Qg)/2,0.6,'Initial ΔG',fontsize=7.5,color=ORANGE,ha='center')
ax.text((Q0+Q1)/2,1.65,'ΔY > ΔG\n(multiplier)',fontsize=8,color=GREEN,ha='center',fontweight='bold')
ax.text(Q0-0.2,0.1,'Y',fontsize=9,color=NAVY)
ax.text(Yf+0.1,0.3,'Yf',fontsize=9,color=NAVY)
ax.text(0.12,P0+0.08,'PL',fontsize=8.5,color=BLUE)
ax.text(0.12,P1+0.08,'PL₁',fontsize=8.5,color=NAVY)
ax.text(7.25,0.85,'AD',fontsize=8,color=BLUE,fontweight='bold')
ax.text(7.9,1.25,'AD + ΔG',fontsize=7.5,color=BLUE,fontweight='bold')
ax.text(8.0,2.6,'AD₁',fontsize=8,color=NAVY,fontweight='bold')
ax.text(8.6,6.7,'SRAS',fontsize=8,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper right')
save('3_6a_multiplier')

# ── 3.6b  Crowding Out (HL) ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Quantity of Loanable Funds',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Interest Rate (i)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Crowding Out Effect (HL)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9.5,100)
ax.plot(Q,Q, color=GREEN,lw=2.2,label='S (savings)')
ax.plot(Q,10-Q, color=BLUE, lw=2.2,label='D (private investment)')
ax.plot(Q,12-Q,color=RED,  lw=2.2,ls='--',label='D₁ (+ govt borrowing)')
ax.plot(5,5,'bo',ms=6); ax.plot(6,6,'ro',ms=6)
ax.plot([5,5],[0,5],GRAY,lw=1,ls=':'); ax.plot([6,6],[0,6],GRAY,lw=1,ls=':')
ax.plot([0,5],[5,5],GRAY,lw=1,ls=':'); ax.plot([0,6],[6,6],GRAY,lw=1,ls=':')
ax.annotate('',xy=(0.5,6),xytext=(0.5,5),arrowprops=dict(arrowstyle='->',color=RED,lw=2))
ax.text(0.7,5.2,'↑i crowds out\nprivate investment',fontsize=8,color=RED)
ax.text(0.1,5.2,'i',fontsize=9,color=BLUE); ax.text(0.1,6.2,'i₁',fontsize=9,color=RED)
ax.text(9.1,8.7,'S',fontsize=11,color=GREEN,fontweight='bold')
ax.text(9.1,1.0,'D',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,3.0,'D₁',fontsize=9,color=RED,fontweight='bold')
ax.legend(fontsize=8,framealpha=0,loc='upper center',bbox_to_anchor=(0.62,1))
save('3_6b_crowding_out')

# ── 3.7  Supply-Side Policies: LRAS Shifts Right ─────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Real GDP (Y)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Price Level',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Supply-Side Policies: LRAS Shifts Right',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_xticks([]); ax.set_yticks([])
Q = np.linspace(0.5,9.5,100)
ax.plot(Q,9-Q,color=BLUE,lw=2.2,label='AD')
ax.plot(Q,1+0.8*Q,color=RED,lw=2.2,label='SRAS')
ax.axvline(4,color=NAVY,lw=2.2,label='LRAS')
ax.axvline(7,color=GREEN,lw=2.5,ls='--',label='LRAS₁ (after\nsupply-side policy)')
ax.annotate('',xy=(6.5,8.5),xytext=(4.5,8.5),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2.5))
ax.text(5.5,8.8,'↑ Productive capacity\ntraining, R&D\nderegulation',ha='center',fontsize=7,color=GREEN)
ax.text(4.1,0.3,'Yf',fontsize=9,color=NAVY); ax.text(7.1,0.3,'Yf₁',fontsize=9,color=GREEN)
ax.legend(fontsize=8,framealpha=0,bbox_to_anchor=(0.7,0.5))
save('3_7a_supply_side_LRAS')


# ═══════════════════════════════════════════════════════════════════════════════
# UNIT 4 — THE GLOBAL ECONOMY
# ═══════════════════════════════════════════════════════════════════════════════

# ── 4.1a  Free Trade: Imports ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Free Trade: Imports (Pw < Pd)')
Q = np.linspace(0,9.5,100)
D=10-Q; S=Q; Pw=3.5
ax.plot(Q,D,color=BLUE,lw=2.2,label='D'); ax.plot(Q,S,color=RED,lw=2.2,label='S')
ax.axhline(Pw,color=GREEN,lw=2,label='World price (Pw)')
Qs=Pw; Qd=10-Pw
ax.plot(Qd,Pw,'ko',ms=5,zorder=6)
ax.plot([Qs,Qs],[0,Pw],GRAY,lw=1,ls='--'); ax.plot([Qd,Qd],[0,Pw],GRAY,lw=1,ls='--')
ax.annotate('',xy=(Qd,Pw/2),xytext=(Qs,Pw/2),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qs+Qd)/2,Pw/2+0.3,'Imports',ha='center',fontsize=9,color=ORANGE,fontweight='bold')
ax.fill_between(Q[Q<=Qd],Pw,D[Q<=Qd],alpha=0.2,color=BLUE,label='↑ Consumer surplus')
ax.fill_between(Q[Q<=Qs],S[Q<=Qs],Pw,alpha=0.2,color=RED,label='↓ Producer surplus')
ax.text(0.1,Pw+0.1,'Pw',fontsize=9,color=GREEN,fontweight='bold')
ax.text(1.75,5,'CS',fontsize=11,color=BLUE,fontweight='bold')
ax.text(0.9,2.3,'PS',fontsize=11,color=RED,fontweight='bold')
ax.text(Qs+0.1,0.3,'Qs',fontsize=9,color=NAVY); ax.text(Qd+0.1,0.3,'Qd',fontsize=9,color=NAVY)
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.7,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_1a_free_trade_imports')

# ── 4.1b  Free Trade: Exports ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, title='Free Trade: Exports (Pw > Pd)')
Q = np.linspace(0,9.5,100)
D=10-Q; S=Q; Pw=6.5
ax.plot(Q,D,color=BLUE,lw=2.2,label='D'); ax.plot(Q,S,color=RED,lw=2.2,label='S')
ax.axhline(Pw,color=GREEN,lw=2,label='World price (Pw)')
Qs=Pw; Qd=10-Pw
ax.plot(Qs,Pw,'ko',ms=5,zorder=6)
ax.plot([Qs,Qs],[0,Pw],GRAY,lw=1,ls='--'); ax.plot([Qd,Qd],[0,Pw],GRAY,lw=1,ls='--')
ax.annotate('',xy=(Qs,Pw/2-1),xytext=(Qd,Pw/2-1),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qs+Qd)/2,Pw/2-0.6,'Exports',ha='center',fontsize=9,color=ORANGE,fontweight='bold')
ax.fill_between(Q[Q<=Qs],Pw,S[Q<=Qs],alpha=0.2,color=RED,label='↑ Producer surplus')
ax.fill_between(Q[Q<=Qd],D[Q<=Qd],Pw,alpha=0.2,color=BLUE,label='↓ Consumer surplus')
ax.text(0.1,Pw+0.1,'Pw',fontsize=9,color=GREEN,fontweight='bold')
ax.text(1.2,4,'PS',fontsize=11,color=RED,fontweight='bold')
ax.text(1.2,7.3,'CS',fontsize=11,color=BLUE,fontweight='bold')
ax.text(0.1,5.05,'Pd*',fontsize=9,color=GRAY)
ax.text(Qd+0.1,0.3,'Qd',fontsize=9,color=NAVY); ax.text(Qs+0.1,0.3,'Qs',fontsize=9,color=NAVY)
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_1b_free_trade_exports')

# ── 4.1c  Comparative Advantage: Linear PPCs (HL) ─────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 5))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Good X (e.g. cloth)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_ylabel('Good Y (e.g. wine)',fontsize=10,color=NAVY,fontweight='bold')
ax.set_title('Comparative Advantage: Linear PPCs (HL)',fontsize=11,color=NAVY,fontweight='bold',pad=10)
ax.set_xlim(0,12); ax.set_ylim(0,12); ax.set_xticks([]); ax.set_yticks([])
ax.plot([0,8],[6,0],color=BLUE,lw=2.5,label='Country A\n(CA in Good X)\nOC of X = ¾Y')
ax.plot([0,4],[8,0],color=RED, lw=2.5,label='Country B\n(CA in Good Y)\nOC of Y = ½X')
ax.text(8,0.2,'8',fontsize=9,color=BLUE); ax.text(0.1,6.2,'6',fontsize=9,color=BLUE)
ax.text(4,0.2,'4',fontsize=9,color=RED);  ax.text(0.1,8.2,'8',fontsize=9,color=RED)
Xi,Yi = 1.6,4.8
ax.plot(Xi,Yi,'ko',ms=5,zorder=6)
ax.text(Xi-0.2,Yi+0.25,'A',fontsize=8.5,color=NAVY,fontweight='bold')
ax.plot([0,8],[8,0],color=GRAY,lw=2.2,ls=':',label='Trade possibilities line')
ax.plot(2.3,5.8,'k*',ms=14,label='Consumption with specialisation')
ax.annotate('',xy=(2.2,5.7),xytext=(Xi+0.1,Yi+0.1),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2.2))
ax.text(2.3+0.2,5.8+0.2,'Specialisation and trade\nincrease global output',fontsize=8,color=GREEN,fontweight='bold')
ax.legend(fontsize=8,framealpha=0,loc='upper right')
save('4_1c_comparative_advantage')

# ── 4.2a  Tariff ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, title='Effect of a Tariff')
Q = np.linspace(0,9.5,100)
D=10-Q; S=Q; Pw=2.8; Pt=4.0; tariff=Pt-Pw
ax.plot(Q,D,color=BLUE,lw=2.2,label='D'); ax.plot(Q,S,color=RED,lw=2.2,label='S')
ax.axhline(Pw,color=GREEN,lw=1.8,label='World price (Pw)')
ax.axhline(Pt,color=NAVY, lw=2,  ls='-', label='Pw + tariff (Pt)')
Qs_w=Pw; Qd_w=10-Pw; Qs_t=Pt; Qd_t=10-Pt
for Qv in [Qs_w,Qd_w]:
    ax.plot([Qv,Qv],[0,Pw],GRAY,lw=0.8,ls=':')
for Qv in [Qs_t,Qd_t]:
    ax.plot([Qv,Qv],[0,Pt],GRAY,lw=0.8,ls=':')
ax.plot(Qd_w,Pw,'ko',ms=5,zorder=6)
ax.plot(Qd_t,Pt,'ko',ms=5,zorder=6)
ax.fill_between(Q[Q<=Qd_t],Pt,D[Q<=Qd_t],alpha=0.12,color=BLUE,label='Consumer surplus')
ax.fill_between(Q[Q<=Qs_t],S[Q<=Qs_t],Pt,alpha=0.22,color=RED,label='Producer surplus')
ax.fill_between([Qs_t,Qd_t],[Pw,Pw],[Pt,Pt],alpha=0.28,color=GREEN,label='Tariff revenue')
ax.fill([Qs_w,Qs_t,Qs_t],[Pw,Pw,Pt],alpha=0.35,color=ORANGE,label='Welfare loss (DWL)')
ax.fill([Qd_t,Qd_w,Qd_t],[Pt,Pw,Pw],alpha=0.35,color=ORANGE)
ax.text(0.1,Pw+0.1,'Pw',fontsize=9,color=GREEN); ax.text(0.1,Pt+0.1,'Pt',fontsize=9,color=NAVY)
ax.text(Qs_w,0.2,'Qs',fontsize=8,color=NAVY); ax.text(Qs_t,0.2,'Qs+t',fontsize=8,color=NAVY)
ax.text(Qd_t,0.2,'Qd+t',fontsize=8,color=NAVY); ax.text(Qd_w,0.2,'Qd',fontsize=8,color=NAVY)
ax.text(1.2,5.5,'CS',fontsize=11,color=BLUE,fontweight='bold')
ax.text(1.2,2.2,'PS',fontsize=11,color=RED,fontweight='bold')
ax.text((Qs_t+Qd_t)/2,Pt-0.29,'Tariff\nrevenue',ha='center',va='top',fontsize=8,color=GREEN,fontweight='bold')
ax.text(Qs_t-0.06,Pw+0.25,'DWL',fontsize=8,color=ORANGE,fontweight='bold',ha='right')
ax.text(Qd_t+0.06,Pw+0.25,'DWL',fontsize=8,color=ORANGE,fontweight='bold',ha='left')
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED, fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_2a_tariff')

# ── 4.2b  Import Quota ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, title='Effect of an Import Quota')
Q = np.linspace(0,9.5,300)
D=10-Q; S=Q; Pw=2.8; quota=2.0
Pq=(10-quota)/2; Qs_w=Pw; Qd_w=10-Pw; Qs_q=Pq; Qd_q=10-Pq
kink_x = Qs_w + quota
S_quota = Q - quota
ax.plot(Q,D,color=BLUE,lw=2.2,label='D')
ax.plot(Q,S,color=RED,lw=2.2,label='S')
ax.axhline(Pw,color=GREEN,lw=1.8,label='World price (Pw)')
ax.axhline(Pq,color=NAVY, lw=2,  ls='--', label='Price with quota (Pq)')
ax.plot([Qs_w,kink_x],[Pw,Pw],color=PURPLE,lw=2.2,ls='--')
ax.plot(Q[Q>=kink_x],S_quota[Q>=kink_x],color=PURPLE,lw=2.2,ls='--',label='S + quota')
for Qv in [Qs_w,Qd_w]:
    ax.plot([Qv,Qv],[0,Pw],GRAY,lw=0.8,ls=':')
ax.plot([kink_x,kink_x],[0,Pw],GRAY,lw=0.8,ls=':')
ax.plot([Qd_q,Qd_q],[0,Pq],GRAY,lw=0.8,ls=':')
ax.plot(Qd_q,Pq,'ko',ms=5,zorder=6)
ax.fill_between(Q[Q<=Qd_q],Pq,D[Q<=Qd_q],alpha=0.12,color=BLUE,label='Consumer surplus')
ax.fill_between(Q[Q<=Qs_q],S[Q<=Qs_q],Pq,alpha=0.22,color=RED,label='Producer surplus')
ax.fill_between([Qs_q,Qd_q],[Pw,Pw],[Pq,Pq],alpha=0.28,color=PURPLE,label='Quota rent')
ax.fill([Qs_w,Qs_q,Qs_q],[Pw,Pw,Pq],alpha=0.35,color=ORANGE,label='Welfare loss (DWL)')
ax.fill([Qd_q,Qd_w,Qd_q],[Pq,Pw,Pw],alpha=0.35,color=ORANGE)
ax.text(0.1,Pw+0.1,'Pw',fontsize=9,color=GREEN)
ax.text(0.1,Pq+0.1,'Pq',fontsize=9,color=NAVY)
ax.text(Qs_w,0.2,'Qs',fontsize=8,color=NAVY)
ax.text(kink_x+0.2,0.2,'Qx',fontsize=8,color=PURPLE,ha='center')
ax.text(Qd_q,0.2,'Qd+q',fontsize=8,color=NAVY)
ax.text(Qd_w,0.2,'Qd',fontsize=8,color=NAVY)
ax.text(1.2,5.5,'CS',fontsize=11,color=BLUE,fontweight='bold')
ax.text(1.2,2.2,'PS',fontsize=11,color=RED,fontweight='bold')
ax.text((Qs_q+Qd_q)/2,Pq-0.29,'Quota\nrent',ha='center',va='top',fontsize=8,color=PURPLE,fontweight='bold')
ax.text(Qs_q-0.06,Pw+0.25,'DWL',fontsize=8,color=ORANGE,fontweight='bold',ha='right')
ax.text(Qd_q+0.06,Pw+0.25,'DWL',fontsize=8,color=ORANGE,fontweight='bold',ha='left')
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED, fontweight='bold')
ax.text(7.1,4.7,'S + quota',fontsize=9,color=PURPLE,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_2b_quota')

# ── 4.2c  Domestic Production Subsidy (Trade) ─────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, title='Domestic Production Subsidy (Trade Context)')
Q = np.linspace(0,9.5,300)
D=10-Q; S=Q; subsidy=1.2; S_sub=S-subsidy; Pw=2.8; Pp=Pw+subsidy
Qs_w=Pw; Qd=10-Pw; Qs_s=Pp
ax.plot(Q,D, color=BLUE,lw=2.2,label='D')
ax.plot(Q,S,color=RED, lw=2.2,label='S')
ax.plot(Q[Q>=subsidy],S_sub[Q>=subsidy],color=RED,lw=2.2,ls='--',label='S with subsidy')
ax.axhline(Pw,color=GREEN,lw=1.8,label='World price (Pw)')
for Qv in [Qs_w,Qd]:
    ax.plot([Qv,Qv],[0,Pw],GRAY,lw=0.8,ls=':')
ax.plot([Qs_s,Qs_s],[0,Pp],GRAY,lw=0.8,ls=':')
ax.fill_between(Q[Q<=Qs_s],S[Q<=Qs_s],S_sub[Q<=Qs_s],alpha=0.24,color=RED,label='Producer gain')
ax.fill_between([0,Qs_s],[Pw,Pw],[Pp,Pp],alpha=0.14,color=PURPLE,label='Government subsidy cost')
ax.fill([Qs_w,Qs_s,Qs_s],[Pw,Pw,Pp],alpha=0.35,color=ORANGE,label='Welfare loss (DWL)')
ax.annotate('',xy=(Qs_s,1.45),xytext=(Qd,1.45),arrowprops=dict(arrowstyle='<->',color=BLUE,lw=2))
ax.text((Qs_s+Qd)/2,1.68,'Imports (after subsidy)',ha='center',fontsize=8.2,color=BLUE)
ax.annotate('',xy=(Qs_w,0.85),xytext=(Qd,0.85),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qs_w+Qd)/2,1.02,'Imports (before subsidy)',ha='center',fontsize=8.2,color=ORANGE)
ax.text(0.1,Pw+0.1,'Pw',fontsize=9,color=GREEN,fontweight='bold')
ax.text(Qs_w,0.2,'Qs',fontsize=8,color=NAVY)
ax.text(Qs_s,0.2,"Qs'",fontsize=8,color=NAVY)
ax.text(Qd,0.2,'Qd',fontsize=8,color=NAVY)
ax.text(Qs_s/2-1,1.4,'Producer\ngain',ha='center',fontsize=8,color=RED,fontweight='bold')
ax.text(Qs_s/2,Pw+subsidy/2,'Subsidy\ncost',ha='center',va='center',fontsize=8,color=PURPLE,fontweight='bold')
ax.text((Qs_w+Qs_s)/2+0.2,Pw+0.2,'DWL',ha='center',fontsize=8,color=ORANGE,fontweight='bold')
ax.text(9.1,0.3,'D',fontsize=11,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.text(8.0,6.4,'S with subsidy',fontsize=8.5,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_2c_subsidy_trade')

# ── 4.5a  Exchange Rate Determination ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4))
base_ax(ax, xlabel='Quantity of £', ylabel='Exchange Rate ($/£)',
        title='Exchange Rate Determination')
Q = np.linspace(1,9,100)
D1=10-Q; D2=12-Q; S=Q
ax.plot(Q,D1,color=BLUE,lw=2.2,label='D (£)')
ax.plot(Q,D2,color=BLUE,lw=2.2,ls='--',label='D₁ (£)\n↑ demand')
ax.plot(Q,S, color=RED, lw=2.2,label='S (£)')
Qe1,Pe1=5,5; Qe2,Pe2=6,6
ax.plot(Qe1,Pe1,'bo',ms=6,zorder=6); ax.plot(Qe2,Pe2,'bo',ms=6,zorder=6)
ax.plot([Qe1,Qe1],[0,Pe1],GRAY,lw=1,ls='--'); ax.plot([0,Qe1],[Pe1,Pe1],GRAY,lw=1,ls='--')
ax.plot([Qe2,Qe2],[0,Pe2],GRAY,lw=1,ls='--'); ax.plot([0,Qe2],[Pe2,Pe2],GRAY,lw=1,ls='--')
ax.annotate('',xy=(1.5,Pe2),xytext=(1.5,Pe1),arrowprops=dict(arrowstyle='->',color=GREEN,lw=2))
ax.text(1.65,(Pe1+Pe2)/2-0.3,'↑ ER\n(appreciation)',fontsize=8,color=GREEN)
ax.text(0.1,Pe1+0.1,'ER',fontsize=9,color=NAVY); ax.text(0.1,Pe2+0.1,'ER₁',fontsize=9,color=NAVY)
ax.text(Qe1+0.2,0.2,'Q',fontsize=9,color=NAVY,ha='center')
ax.text(Qe2+0.8,0.2,'Q₁ pounds',fontsize=9,color=NAVY,ha='center')
ax.text(9.1,1.0,'D',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,3.0,'D₁',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,9.0,'S', fontsize=11,color=RED, fontweight='bold')
ax.legend(fontsize=8,framealpha=0,bbox_to_anchor=(0.75,0.6))
save('4_5a_exchange_rate')

# ── 4.5b  Exchange Rate Changes: AD/AS Effects ────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, (title, deprec) in zip(axes, [
        ('Currency Depreciation\n(↑ exports, ↑ AD)', True),
        ('Currency Appreciation\n(↓ exports, ↓ AD)', False)]):
    base_ax(ax, xlabel='Real GDP (Y)', ylabel='Price Level', title=title)
    Q = np.linspace(0.5, 9.5, 100)
    SRAS = 1 + 0.8 * Q
    AD1 = 7 - Q if deprec else 9 - Q
    AD2 = 9 - Q if deprec else 7 - Q

    ax.plot(Q, AD1, color=BLUE, lw=2, ls='--', label='AD₁')
    ax.plot(Q, AD2, color=BLUE, lw=2.5, label='AD₂')
    ax.plot(Q, SRAS, color=RED, lw=2.2, label='SRAS')
    ax.axvline(6.5, color=NAVY, lw=2.3, ls='-', label='LRAS (Yf)')

    Q1, P1 = 6 / 1.8, 7 - (6 / 1.8)
    Q2, P2 = 8 / 1.8, 9 - (8 / 1.8)
    if not deprec:
        Q1, P1, Q2, P2 = Q2, P2, Q1, P1

    ax.plot(Q1, P1, 'o', ms=5.5, color=NAVY, zorder=5)
    ax.plot(Q2, P2, 'o', ms=5.5, color=NAVY, zorder=5)
    ax.text(Q1, P1 + 0.28, 'E₁', fontsize=8.5, color=NAVY, fontweight='bold', ha='center')
    ax.text(Q2, P2 + 0.28, 'E₂', fontsize=8.5, color=NAVY, fontweight='bold', ha='center')

    for q, p, qlab, plab in [(Q1, P1, 'Y₁', 'PL₁'), (Q2, P2, 'Y₂', 'PL₂')]:
        ax.plot([q, q], [0, p], color=LGRAY, lw=1, ls='--')
        ax.plot([0, q], [p, p], color=LGRAY, lw=1, ls='--')
        ax.text(q - 0.12, 0.25, qlab, fontsize=8, color=NAVY, ha='center')
        ax.text(0.18, p + 0.05, plab, fontsize=8, color=NAVY, va='bottom')

    shift_color = GREEN if deprec else RED
    outcome_text = ('Exports ↑, AD ↑\nY ↑, PL ↑'
                    if deprec else
                    'Exports ↓, AD ↓\nY ↓, PL ↓')

    ax.annotate('', xy=(Q2, 0.7), xytext=(Q1, 0.7),
                arrowprops=dict(arrowstyle='->', color=shift_color, lw=2))
    ax.text((Q1 + Q2) / 2, 1.08, outcome_text, ha='center',
            fontsize=8.2, color=shift_color, fontweight='bold')
    ax.text(6.62, 0.3, 'Yf', fontsize=9, color=NAVY)
    ax.legend(fontsize=7.5,framealpha=0,loc='center right')
save('4_5b_exchange_rate_ADAS')

# ── 4.5c  Fixed Exchange Rate ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
base_ax(ax, xlabel='Quantity of £', ylabel='Exchange Rate ($/£)',
        title='Fixed Exchange Rate: Defence Mechanisms')
Q = np.linspace(0.5,9.5,100)
D1=10-Q; D2=7-Q; S=Q
ax.plot(Q,D1,color=BLUE,lw=2.2,label='D (£)')
ax.plot(Q[D2>0],D2[D2>0],color=BLUE,lw=2.2,ls='--',label='D₁ (£) — falls')
ax.plot(Q,S,color=RED,lw=2.2,label='S (£)')
ax.axhline(5,color=GREEN,lw=2.5,ls='-',label='Fixed rate (ER*)')
Qm,ERm = 3.5,3.5
ax.plot(Qm,ERm,marker='*',color=RED,ms=12)
ax.plot([Qm,Qm],[0,ERm],GRAY,lw=1,ls=':')
ax.text(Qm + 0.25, ERm - 0.1, 'Free market ER\n(too low)', fontsize=8,
        color=RED, fontweight='bold', ha='left', va='center')
Qs_fix=5; Qd_fix=2
ax.plot([Qd_fix,Qd_fix],[0,5],GRAY,lw=1,ls='--'); ax.plot([Qs_fix,Qs_fix],[0,5],GRAY,lw=1,ls='--')
ax.annotate('',xy=(Qs_fix,1.0),xytext=(Qd_fix,1.0),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text((Qd_fix+Qs_fix)/2,1.5,'CB must buy £\n(use reserves)',ha='center',fontsize=8.5,color=ORANGE,fontweight='bold')
ax.text(0.1,5.2,'ER*',fontsize=9,color=GREEN,fontweight='bold')
ax.text(9.1,0.3,'D',fontsize=9,color=BLUE,fontweight='bold')
ax.text(6.8,0.3,'D₁',fontsize=9,color=BLUE,fontweight='bold')
ax.text(9.1,8.6,'S',fontsize=11,color=RED,fontweight='bold')
ax.legend(fontsize=7.5,framealpha=0,loc='upper center')
save('4_5c_fixed_exchange_rate')

# ── 4.5d  Managed (Dirty) Float ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
base_ax(ax, xlabel='Time', ylabel='Exchange Rate',
        title='Managed (Dirty) Float Exchange Rate',
        xlim=(0, 10), ylim=(2, 8))
t = np.linspace(0, 10, 400)
free = (5
        + 0.95 * np.sin(t * 0.9)
        + 0.55 * np.sin(t * 2.1)
        + 0.25 * np.cos(t * 3.4))
upper = np.full_like(t, 6.2)
lower = np.full_like(t, 3.8)
managed = np.clip(free, lower + 0.15, upper - 0.15)

ax.fill_between(t, lower, upper, alpha=0.1, color=GREEN)
ax.plot(t, free, color=GRAY, lw=1.6, ls='--', alpha=0.85, label='Free float')
ax.plot(t, managed, color=BLUE, lw=2.6, label='Managed float')
ax.plot(t, upper, color=GREEN, lw=1.5, ls=':', label='Intervention zone')
ax.plot(t, lower, color=GREEN, lw=1.5, ls=':')

high_idx = int(np.argmax(free))
low_idx = int(np.argmin(free))
mid_idx = int(np.argmax(free[220:320])) + 220

ax.plot(t[high_idx]-0.45, managed[high_idx], 'o', color=RED, ms=5.5, zorder=5)
ax.plot(t[low_idx]-0.45, managed[low_idx], 'o', color=ORANGE, ms=5.5, zorder=5)
ax.plot(t[mid_idx], managed[mid_idx], 'o', color=NAVY, ms=5.5, zorder=5)

ax.annotate('CB sells domestic currency\nlimits appreciation',
            xy=(t[high_idx]-0.4, managed[high_idx]-0.1), xytext=(6.8, 4.3),
            fontsize=8, color=RED, ha='left',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.8, relpos=(0.8, 0.5)))
ax.annotate('CB buys domestic currency\nlimits depreciation',
            xy=(t[low_idx]-0.45, managed[low_idx]-0.1), xytext=(2.5, 2.55),
            fontsize=8, color=ORANGE, ha='left',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.8))
ax.annotate('Occasional intervention,\nnot a fixed rate',
            xy=(t[mid_idx], managed[mid_idx]), xytext=(5.3, 6.5),
            fontsize=8, color=NAVY, ha='left',
            arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.6))

ax.text(2.0, 4.5, 'Mostly market-determined,\nbut smoothed by CB action',
        fontsize=8.2, color=NAVY, ha='center', va='center')
ax.legend(fontsize=8, framealpha=0, loc='lower right')
save('4_5d_managed_float')

# ── 4.6a  J-Curve (merged) ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(NAVY); ax.spines['bottom'].set_color(NAVY)
ax.set_xlabel('Time', fontsize=10, color=NAVY, fontweight='bold')
ax.set_ylabel('Current Account Balance', fontsize=10, color=NAVY, fontweight='bold')
ax.set_title('J-Curve Effect (HL)', fontsize=11, color=NAVY, fontweight='bold', pad=10)
ax.set_xticks([]); ax.set_yticks([])

# Keep the second graph's J-shape and SR/LR split.
x0 = 0.0
trough_x = 2.8
end_x = 9.2

t1 = np.linspace(0, 1, 140)
cx1 = x0 + t1 * (trough_x - x0) + 0.1
cy1 = -0.4 + -1.3 * np.sin(t1 * np.pi / 2)**1.45

t2 = np.linspace(0, 1, 320)
cx2 = trough_x + t2 * (end_x - trough_x) + 0.1
cy2 = -1.7 + 4.5 * t2**1.6

cx = np.concatenate([cx1, cx2])
cy = np.concatenate([cy1, cy2])

# Keep first graph styling/markers.
ax.axhline(0, color=GRAY, lw=1.2, ls='--')
ax.axvline(x0, color=RED, lw=1.8, ls='--', label='Depreciation occurs')
ax.plot(cx, cy, color=BLUE, lw=2.8, label='Current account balance')

bracket_y = 0.1
for (xa, xb, label) in [(x0, trough_x + 0.1, 'SR'), (trough_x + 0.1, end_x - 2.8, 'LR')]:
    ax.annotate('', xy=(xb, bracket_y), xytext=(xa, bracket_y),
                arrowprops=dict(arrowstyle='<->', color=RED, lw=2.0))
    ax.text((xa + xb) / 2, bracket_y + 0.18, label,
            ha='center', fontsize=10, color=RED, fontweight='bold')

ax.text(1.5, -2.25,
        'Short run:\nimport costs ↑\nbefore volumes adjust',
        fontsize=8, color=RED, style='italic', ha='center')
ax.text(6.6, -1.4,
        'Long run:\nvolumes adjust\n(M-L condition met)',
        fontsize=8, color=GREEN, style='italic', ha='center')

ax.set_xlim(-1.5, 10)
ax.set_ylim(-2.8, 3.2)
ax.legend(fontsize=8.5, framealpha=0, loc='lower right')

save('4_6a_j_curve')

# ── 4.6b  Current Account ↔ Exchange Rate flow diagram ───────────────────────
fig, ax = plt.subplots(figsize=(7.0, 5.8))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
ax.set_title('Current Account & Exchange Rate Relationship (HL)',
             fontsize=11, color=NAVY, fontweight='bold')

boxes = [
    (5.0, 8.6, 'Current Account\nDeficit'),
    (3.35, 6.5, 'Demand for foreign\ncurrency ↑'),
    (6.65, 6.5, 'Supply of domestic\ncurrency ↑'),
    (5.0, 4.4, 'Domestic currency\ndepreciates'),
    (5.0, 2.3, 'Exports cheaper ↑\nImports dearer ↓'),
]
box_colors = [RED, BLUE, BLUE, ORANGE, GREEN]
box_widths = [3.0, 2.75, 2.75, 3.0, 3.1]
BH = 1.1

for (cx, cy, label), col, bw in zip(boxes, box_colors, box_widths):
    rect = mpatches.FancyBboxPatch(
        (cx - bw / 2, cy - BH / 2), bw, BH,
        boxstyle='round,pad=0.13,rounding_size=0.14',
        facecolor=col, edgecolor='white', alpha=0.9, lw=1.5)
    ax.add_patch(rect)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')

top_y = boxes[0][1]
mid_y = boxes[1][1]
depr_y = boxes[3][1]
bottom_y = boxes[4][1]
left_x = boxes[1][0]
right_x = boxes[2][0]
center_x = boxes[0][0]
top_branch_dx = 0.83
lower_branch_dx = 0.83
arrow_start_offset = BH / 2
arrow_vertical_span = (top_y - mid_y) - BH

main_arrow = dict(arrowstyle='->', color=NAVY, lw=2.1, shrinkA=12, shrinkB=12)
ax.annotate('', xy=(left_x, mid_y + arrow_start_offset), xytext=(center_x - top_branch_dx, mid_y + arrow_start_offset + arrow_vertical_span), arrowprops=main_arrow)
ax.annotate('', xy=(right_x, mid_y + arrow_start_offset), xytext=(center_x + top_branch_dx, mid_y + arrow_start_offset + arrow_vertical_span), arrowprops=main_arrow)
ax.annotate('', xy=(center_x - lower_branch_dx, depr_y + arrow_start_offset), xytext=(left_x, depr_y + arrow_start_offset + arrow_vertical_span), arrowprops=main_arrow)
ax.annotate('', xy=(center_x + lower_branch_dx, depr_y + arrow_start_offset), xytext=(right_x, depr_y + arrow_start_offset + arrow_vertical_span), arrowprops=main_arrow)
ax.annotate('', xy=(center_x, bottom_y + arrow_start_offset), xytext=(center_x, bottom_y + arrow_start_offset + arrow_vertical_span), arrowprops=main_arrow)

ax.text(5.0, 0.65,
        'Over time: current account may improve if the Marshall-Lerner condition holds',
        fontsize=8, color=GREEN, style='italic', ha='center', va='center')

save('4_6b_current_account_ER')

# ── 4.9  Poverty Cycle ────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.1))
for ax, title, nodes, colors in [
    (
        axes[0],
        'Individual / Household Level',
        [
            (5.0, 8.8, 'Low income'),
            (8.15, 6.45, 'Low savings'),
            (6.95, 2.8, 'Low education &\nhealth spending'),
            (3.05, 2.8, 'Low skills &\nproductivity'),
            (1.85, 6.45, 'Low earning\npotential'),
        ],
        [RED, ORANGE, BLUE, BLUE, ORANGE],
    ),
    (
        axes[1],
        'National Level',
        [
            (5.0, 8.8, 'Low national\nincome'),
            (8.15, 6.45, 'Low savings'),
            (6.95, 2.8, 'Low capital\ninvestment'),
            (3.05, 2.8, 'Low productivity'),
            (1.85, 6.45, 'Low output /\nlow growth'),
        ],
        [RED, ORANGE, ORANGE, BLUE, BLUE],
    ),
]:
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.set_title(title, fontsize=10, color=NAVY, fontweight='bold', pad=8)
    radius = 1.16
    for (x, y, label), col in zip(nodes, colors):
        circle = plt.Circle((x, y), radius, color=col, alpha=0.88)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8.1, color='white', fontweight='bold')
    for (x1, y1, _), (x2, y2, _) in zip(nodes, nodes[1:] + [nodes[0]]):
        dx = x2 - x1; dy = y2 - y1; dist = np.sqrt(dx**2 + dy**2)
        ux, uy = dx / dist, dy / dist
        sx = x1 + radius * ux; sy = y1 + radius * uy
        ex = x2 - radius * ux; ey = y2 - radius * uy
        ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                    arrowprops=dict(arrowstyle='->', color=NAVY, lw=2))

fig.suptitle('Poverty Cycle', fontsize=11, color=NAVY, fontweight='bold', y=0.97)
fig.text(0.5, 0.05,
         'Breaking the cycle requires intervention: education, healthcare, infrastructure and investment.',
         ha='center', fontsize=7.8, color=GREEN, style='italic')
save('4_9a_poverty_cycle')


# ═══════════════════════════════════════════════════════════════════════════════
print(f'\n✅  All diagrams saved to {OUT_DIR}/')
print(f'    Total: {len([f for f in os.listdir(OUT_DIR) if f.endswith(".png")])} PNG files')
