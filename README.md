# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/suntoro1988/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/suntoro1988/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A program that writes one image summing up the world's news of Wednesday 18 November 2026 — the APEC summit in Shenzhen, the Quad meeting in Manila, Ukraine's strike on the Crimea bridge, Gulf drone interceptions, Nvidia's record quarter and Cyclone Akvan — to /output/entry.png.

## v2

v2 keeps the same six stories and 2×3 newspaper layout, but reworks the type for legibility at small (300px) sizes: headlines 28px → 36px, summaries trimmed to two lines at 21px, tags 15px → 19px, kicker 19px → 24px, subline 23px → 26px (no longer italic), footer 14.5px → 18px, and the pictogram icons removed. It also fixes four wordings from the v1 review: the Manila story is re-anchored on the Wednesday Marcos meeting (the Quad summit was a day earlier), the Crimea summary no longer says Russia hit Kyiv's bridges "in reply", the Gulf headline no longer attributes Kuwait's drones to Iran, and Nvidia's founder is "resigned", not "ousted". A follow-up tweak restored "Shenzhen" to the APEC summary (the host city had been cut when the headline was shortened to fit two lines); the summary still fits two lines.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sygna1z3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
