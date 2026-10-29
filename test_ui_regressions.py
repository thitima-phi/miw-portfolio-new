"""UI regressions; run with the portfolio served on localhost:8771."""
import re
import unittest
from playwright.sync_api import sync_playwright


class PortfolioUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.page = self.browser.new_page()
        self.page.goto('http://127.0.0.1:8771', wait_until='networkidle')

    def tearDown(self):
        self.page.close()

    def test_arrows_are_svg_not_font_glyphs(self):
        self.assertIsNone(re.search('[↗↖↑↓←→▷]', self.page.locator('body').inner_text()))
        for selector in ['.nav-contact', '.round-link', '.caption-arrow', '.hero-bottom a', '.line-link', '.contact-section h2 a', '.contact-bottom a', 'footer a:last-child', '#previous', '#next']:
            icon = self.page.locator(f'{selector} svg')
            self.assertEqual(icon.count(), 1, selector)
            self.assertEqual(icon.get_attribute('aria-hidden'), 'true')
            self.assertEqual(icon.get_attribute('focusable'), 'false')
        self.assertEqual(self.page.locator('.project-cover svg').count(), 15)

    def test_work_matches_original_artwork_layout(self):
        sonar = self.page.locator('.company-group[data-company="sonar"] .project')
        merick = self.page.locator('.company-group[data-company="merick"] .project')
        self.assertEqual(sonar.nth(0).locator('.everyday-pair [data-gallery]').evaluate_all('els => els.map(el => el.dataset.gallery)'), ['everyday', 'everydaybeforeafter'])
        self.assertEqual(sonar.nth(1).locator('.everyday-pair [data-gallery]').evaluate_all('els => els.map(el => el.dataset.gallery)'), ['sherlock', 'america'])
        self.assertEqual(sonar.locator('[data-gallery]').evaluate_all('els => els.map(el => el.dataset.gallery)'), ['everyday', 'everydaybeforeafter', 'sherlock', 'america', 'poster', 'landscape', 'sonarcollection', 'sonareducation', 'sonaroffers', 'sonarbanners', 'sonarcarousel'])
        self.assertEqual(sonar.nth(8).locator('.collection-preview img').count(), 3)
        self.assertEqual(sonar.nth(9).locator('.video-series video[controls]').count(), 3)
        self.assertEqual(merick.nth(0).locator('.merick-art-grid img').count(), 4)
        self.assertEqual(merick.nth(1).locator('.page-update-pair img').count(), 2)
        self.assertEqual(merick.nth(4).locator('video[controls]').count(), 1)
        self.assertEqual(self.page.locator('.project-wide').count(), 6)
        for video in self.page.locator('.project video').all():
            self.assertEqual(video.get_attribute('preload'), 'none')
            self.assertIsNotNone(video.get_attribute('playsinline'))
            self.assertIsNone(video.get_attribute('autoplay'))
        self.page.locator('[data-filter="merick"]').click()
        self.assertEqual(self.page.locator('.project:visible').count(), 5)

    def test_motion_respects_reduced_motion(self):
        self.assertGreater(self.page.locator('.reveal-target').count(), 0)
        self.page.wait_for_function("document.querySelector('.hero h1').classList.contains('is-visible')")
        self.page.emulate_media(reduced_motion='reduce')
        self.page.reload(wait_until='networkidle')
        self.assertEqual(self.page.locator('.hero h1').evaluate('el => getComputedStyle(el).opacity'), '1')
        self.assertEqual(self.page.locator('.hero h1').evaluate('el => getComputedStyle(el).transform'), 'none')
        self.assertEqual(self.page.locator('.desk-art').first.evaluate('el => getComputedStyle(el).transitionDuration'), '0s')

    def test_noticeable_motion_can_be_paused_and_resumed(self):
        self.assertEqual(self.page.locator('.hero-line-inner').count(), 2)
        self.assertIn('headline-enter', self.page.locator('.hero-line-inner').first.evaluate('el => getComputedStyle(el).animationName'))
        self.assertIn('artwork-float', self.page.locator('.desk-art').first.evaluate('el => getComputedStyle(el).animationName'))
        toggle = self.page.get_by_role('button', name='Pause motion', exact=True)
        toggle.click()
        self.assertTrue(self.page.locator('body').evaluate('el => el.classList.contains("motion-paused")'))
        for card in self.page.locator('.desk-art').all():
            self.assertTrue(all(state.strip() == 'paused' for state in card.evaluate('el => getComputedStyle(el).animationPlayState').split(',')))
        self.page.get_by_role('button', name='Resume motion', exact=True).click()
        self.assertFalse(self.page.locator('body').evaluate('el => el.classList.contains("motion-paused")'))
        self.page.emulate_media(reduced_motion='reduce')
        self.assertTrue(self.page.locator('#motion-toggle').is_hidden())
        self.assertEqual(self.page.locator('.desk-art').first.evaluate('el => getComputedStyle(el).animationName'), 'none')

    def test_companies_have_separate_project_sections(self):
        groups = self.page.locator('.company-group')
        self.assertEqual(groups.count(), 2)
        for company, heading, count in [('sonar', 'Sonar Audiobooks', 10), ('merick', 'Merick Polymers & Leaf Pac', 5)]:
            group = self.page.locator(f'.company-group[data-company="{company}"]')
            self.assertEqual(group.locator('h3').inner_text(), heading)
            self.assertEqual(group.locator('.project').count(), count)
            self.assertEqual(group.locator(f'.project:not([data-company="{company}"])').count(), 0)
            self.page.locator(f'[data-filter="{company}"]').click()
            self.assertEqual(self.page.locator('.company-group:visible').count(), 1)
            self.assertTrue(group.is_visible())
        self.page.locator('[data-filter="all"]').click()
        self.assertEqual(self.page.locator('.company-group:visible').count(), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
