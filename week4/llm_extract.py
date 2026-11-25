# 구조가 제각각인 페이지에서 필요한 필드만 LLM으로 뽑습니다.
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from playwright.sync_api import sync_playwright

load_dotenv()
client = OpenAI()

class Book(BaseModel):
    title: str
    price: str
    in_stock: int

with sync_playwright() as p:
    page = p.chromium.launch().new_page()
    page.goto("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
    text = page.locator("article.product_page").inner_text()

r = client.beta.chat.completions.parse(model="gpt-4o-mini", response_format=Book,
    messages=[{"role": "user", "content": f"다음 상품 페이지에서 정보를 추출해:\n{text[:3000]}"}])
print(r.choices[0].message.parsed)
