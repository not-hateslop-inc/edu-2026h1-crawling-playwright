from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    page = p.chromium.launch().new_page()
    page.goto("https://quotes.toscrape.com/js/")
    rows = []
    for _ in range(3):
        page.wait_for_selector("div.quote")
        rows += page.locator("div.quote span.text").all_inner_texts()
        nxt = page.locator("li.next a")
        if nxt.count() == 0:
            break
        nxt.click()
    print(len(rows), rows[0])
