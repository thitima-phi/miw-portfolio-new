# Miw — Content desk edition

A separate redesign of Thitima Phimsen’s content and visual storytelling portfolio. The original portfolio remains unchanged.

GitHub Pages: https://thitima-phi.github.io/miw-portfolio-new/

## Preview

Open `index.html` directly, or serve this folder:

```sh
python3 -m http.server 8771 --bind 127.0.0.1
```

Visit http://127.0.0.1:8771.

## Design

- Paper `#faf9fc`, lilac desk `#dcd9f2`, plum ink `#292139`, raspberry marker `#a72e68`, orange tab `#f4a15f`, neutral artwork mount `#f0eff2`.
- Barlow Condensed display type and DM Sans body type, loaded through Google Fonts with local fallback stacks.
- The signature is a content desk of overlapping, clickable artwork prints. Quiet project mounts preserve artwork colours and proportions.
- Responsive layouts, visible keyboard focus, native modal focus management, Escape and arrow-key gallery controls, and reduced-motion support.

## Content and behaviour

15 project entries follow the original work-section layout, grouped into Sonar Audiobooks and Merick Polymers & Leaf Pac. Paired designs, multi-image previews, wide collections and four inline videos retain the original order and proportions. All 15 image galleries remain accessible. Project markup is in `index.html`; gallery records are in `collections.js`. Client filters, contribution notes, experience, university background, email links and the original resume are included. Assets are independent copies, not links back to the existing portfolio.

Arrows use SVG rather than font glyphs. The headline enters in staggered lines, the artwork fans into place and gently floats, and projects have stronger scroll reveals. A Pause motion / Resume motion control is available; floating stops while the desk is offscreen. Reduced-motion preferences disable animations and transitions and keep all content visible. Without JavaScript, all project content and native video controls remain available.

Published independently with GitHub Pages from the `main` branch. No claims of performance uplift, published research or authorship of third-party book covers and mascots are added.

## Browser checks

With the local server running and Python Playwright/Chromium available:

```sh
python3 check_browser.py
python3 test_ui_regressions.py
```

Checks cover project filters, every gallery, keyboard navigation, video cleanup, the resume, collection asset existence, JavaScript errors and horizontal overflow at 320, 390, 768, 1024 and 1440 pixels. The script also saves desktop, mobile and full-page screenshots. Preview screenshots and this Python check script are local review materials and need not be deployed.
