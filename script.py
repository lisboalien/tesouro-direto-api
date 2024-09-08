import json
from playwright.sync_api import sync_playwright # type: ignore

def fetch_tesouro_direto():
    url = 'https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json'
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for the page to load      
        content = page.inner_text("pre")
        
        browser.close()
        
    data = json.loads(content)
    return data

def save_to_json(data, filename = "tesouro_direto.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)
        
if __name__ == '__main__':
    data = fetch_tesouro_direto()
    save_to_json(data)
    print('Data saved to tesouro_direto.json')