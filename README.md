# Can a trader make money consistently on Kalshi?

**Inside the Fee Band: Why Takers Cannot Beat Kalshi and Who Profits Anyway**

Reed Ostrov, Denison University. November 2026.

## Result

A trader who buys at the posted price and uses only public prices cannot make money on Kalshi in the long run. Kalshi's fee at a 50 cent price is 1.75 cents per contract, and the measured mispricing for those buyers is 1.33 cents. The fee is larger. Makers, who post resting orders and pay no fee on most series, earned +1.12% per trade across 72.1 million trades. So the strong claim "no one can profit on Kalshi" is false, and the narrow claim "takers using public prices cannot profit" is supported. Polymarket shows the same shape with taker fees 57% to 100% of Kalshi's.

The paper collects no new trade data. All inputs come from the cited studies and the published fee schedules.

## Break-even test

For a taker buying YES, expected profit per contract is

    q - P - 0.07 * P * (1 - P) - s / 2

where q is the true probability, P the price in dollars, and s the bid-ask spread. Compute it on out-of-sample resolved markets, and count events, not contracts, as observations.

## Files

- `paper.pdf`: typeset paper, 5 pages
- `paper.tex`: LaTeX source
- `paper.md`: Markdown version
- `fig1.pdf`, `fig1.png`, `fig.py`: figure and the script that draws it

## Cite

Ostrov, R. (2026). Inside the Fee Band: Why Takers Cannot Beat Kalshi and Who Profits Anyway. https://github.com/Questboy23/kalshi-impossibility

## Disclosure

Drafting used Claude, an AI model made by Anthropic. All empirical figures come from or are computed from the cited sources.

## License

Text: CC BY 4.0. See `LICENSE`.
