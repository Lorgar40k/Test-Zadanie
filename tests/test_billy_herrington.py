from playwright.sync_api import sync_playwright

def test_billy_herrington_page_contains_name_and_birthdate():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ru.wikipedia.org/wiki/Херрингтон,_%D0%91%D0%B8%D0%BB%D0%BB%D0%B8", wait_until="networkidle")

        body_text = page.inner_text("body")
        assert "Билли Херрингтон" in body_text or "Billy Herrington" in body_text, "Имя Billy Herrington не найдено на странице"
        assert "14 июля 1969" in body_text or "1969" in body_text, "Дата рождения Billy Herrington не найдена на странице"

        browser.close()
