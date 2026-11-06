# Kalshi Impossibility

Tests whether a taker using only public prices can profit on Kalshi, by comparing published calibration figures with the fee formula.

Paper: Reed Ostrov, "Inside the Fee Band: Why Takers Cannot Beat Kalshi and Who Profits Anyway", November 2026 (`paper.pdf`, `paper.md`, `paper.tex`).

## Result

- Kalshi's taker fee at a 50 cent price is 1.75 cents per contract. The average taker's pre-fee loss there is 1.33 cents (Becker 2026: -2.65% of a 50 cent stake). Taking the opposite side nets 1.33 - 1.75 = -0.42 cents.
- Makers earned +1.12% per trade across 72.1 million trades (Becker 2026, pre-fee, 2021 to November 2025).
- Supported: a taker who conditions only on price does not profit in the data used. Not proved: Proposition 2 is an equilibrium argument, not a theorem derived from data.
- The 95 cent row shows +0.50 cents per contract after fee for the average buyer, with about 5,100 independent bets needed to see it at one-sided 95% confidence.

## Run

The paper collects no new trade data. Every number comes from the cited studies and fee schedules.

1. `pip install numpy matplotlib`
2. `python fig.py` writes `fig1.pdf` and `fig1.png`.
3. `pdflatex paper.tex` (run twice) writes `paper.pdf`.

## Limitations

- Same-event contracts resolve together, so trade counts overstate independent observations.
- Data end in late 2025, before the 2026 fee revisions.
- The 1.2 cent half-spread in the figure is an assumption.
- The Kalshi fee schedule could not be re-fetched on 2026-11-06, so it was not re-verified. Becker (2026) and the Polymarket fee table were re-checked against their web pages.
- Maker and taker labels proxy imperfectly for sophistication.

## AI disclosure

The ideas and the question are Reed Ostrov's. Claude (Anthropic), run through Claude Code, did the literature and fee-schedule gathering, the break-even arithmetic, the figure script, the LaTeX typesetting and the first draft of the text from Reed's direction. Claude did not run any trades or collect trade data. Reed is responsible for all claims.

## Cite

Ostrov, R. (2026). Inside the Fee Band: Why Takers Cannot Beat Kalshi and Who Profits Anyway. https://github.com/Questboy23/kalshi-impossibility

License: text CC BY 4.0, see `LICENSE`.
