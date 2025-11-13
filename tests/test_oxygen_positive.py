from playwright.sync_api import sync_playwright

def test_earth_oxygen_percentage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Сразу открываем статью "Земля (планета)"
        page.goto("https://ru.wikipedia.org/wiki/Земля_(планета)", wait_until="networkidle")

        # Получаем текст всей страницы
        body_text = page.inner_text("body")

        # Проверяем наличие информации о содержании кислорода
        assert ("20,95" in body_text or "20.95" in body_text), "Ожидаемое значение 20,95% кислорода не найдено"

        browser.close()
