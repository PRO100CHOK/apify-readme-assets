# apify-readme-assets

Hero images and other static assets used in the READMEs of my Apify actors.

Layout: `<actor-name>/hero.png` + the `hero.html` it was rendered from.

Re-render: `python render_hero.py <actor>/hero.html <actor>/hero.png 760` (Playwright, 2x device scale).
