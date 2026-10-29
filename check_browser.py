"""Browser smoke checks. Run while the portfolio is served on port 8771."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1080}, device_scale_factor=1, reduced_motion="reduce")
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto("http://127.0.0.1:8771", wait_until="networkidle")
    assert page.locator(".project").count() == 15
    assert page.locator("#result-count").inner_text() == "15 projects"
    page.locator('img[loading="lazy"]').evaluate_all("images => images.forEach(img => img.loading = 'eager')")
    page.wait_for_function("Array.from(document.querySelectorAll('img[src]')).every(img => img.complete && img.naturalWidth > 0)")
    page.screenshot(path=str(ROOT / "preview-desktop.png"))
    page.screenshot(path=str(ROOT / "preview-full.png"), full_page=True)
    for company, expected in [("sonar", 10), ("merick", 5), ("all", 15)]:
        page.locator(f'[data-filter="{company}"]').click()
        assert page.locator(".project:visible").count() == expected
    for button in page.locator("button.project-cover").all():
        button.click()
        assert page.locator("#gallery").evaluate("el => el.open")
        image = page.locator("#gallery-image")
        assert image.is_visible()
        page.wait_for_function("document.querySelector('#gallery-image').complete && document.querySelector('#gallery-image').naturalWidth > 0")
        if page.locator("#next").is_enabled():
            first = page.locator("#gallery-count").inner_text()
            page.keyboard.press("ArrowRight")
            assert first != page.locator("#gallery-count").inner_text()
            page.keyboard.press("ArrowLeft")
            assert first == page.locator("#gallery-count").inner_text(), (button.get_attribute('data-gallery'), first, page.locator('#gallery-count').inner_text(), page.evaluate('document.activeElement.outerHTML'))
        page.keyboard.press("Escape")
        assert not page.locator("#gallery").evaluate("el => el.open")
    clips = page.locator('.project video')
    assert clips.count() == 4
    clips.nth(0).evaluate('async el => { el.muted = true; await el.play(); }')
    assert not clips.nth(0).evaluate('el => el.paused')
    clips.nth(1).evaluate('async el => { el.muted = true; await el.play(); }')
    assert clips.nth(0).evaluate('el => el.paused')
    page.locator('[data-filter="merick"]').click()
    assert clips.nth(1).evaluate('el => el.paused')
    page.locator('[data-filter="all"]').click()
    for width in [320, 390, 768, 1024, 1440]:
        page.set_viewport_size({"width": width, "height": 900})
        page.goto("http://127.0.0.1:8771", wait_until="networkidle")
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at {width}px"
        if width == 390:
            page.screenshot(path=str(ROOT / "preview-mobile.png"))
            page.locator('[data-gallery="sonarcollection"]').first.click()
            assert page.locator("#gallery-close").is_visible()
            page.locator("#gallery-close").click()
    assert not errors, errors
    assert page.request.get("http://127.0.0.1:8771/assets/Thitima-Phimsen-Resume.pdf").ok
    # Every collection path must exist, including items beyond the first slide.
    paths = page.evaluate("Object.values(collections).flatMap(c => c.items.flatMap(i => [i[0], ...(i[2] ? [i[2]] : [])]))")
    for path in paths:
        assert (ROOT / path).is_file(), path
    for src in page.locator('.project video source').evaluate_all('els => els.map(el => el.getAttribute("src"))'):
        assert (ROOT / src).is_file(), src
    print("PASS: 15 image galleries, 3 filters, keyboard navigation, inline playback and video pausing, resume, all collection assets, and overflow checks at 5 widths; no JavaScript errors.")
    browser.close()
