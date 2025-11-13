import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ru.wikipedia.org/wiki/Равшан_и_Джамшут", wait_until="networkidle")
        yield page
        browser.close()

def test_names_present(page):
    body_text = page.inner_text("body")
    assert "Равшан" in body_text
    assert "Джамшут" in body_text

def test_keywords_present(page):
    body_text = page.inner_text("body")
    assert ("гастарбайтер" in body_text or "эмигрант" in body_text)

def test_negative_oxygen_absent(page):
    body_text = page.inner_text("body")
    assert "кислород" not in body_text
