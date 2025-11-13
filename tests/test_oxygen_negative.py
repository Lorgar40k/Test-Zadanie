from playwright.sync_api import sync_playwright

def test_no_helium_in_earth_atmosphere():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Открываем ту же статью о Земле
        page.goto("https://ru.wikipedia.org/wiki/Земля_(планета)", wait_until="networkidle")

        body_text = page.inner_text("body")

        # Проверяем, что не указано 100% гелия
        assert "100% гелия" not in body_text, "Ошибка: В тексте указано 100% гелия!"

        browser.close()
