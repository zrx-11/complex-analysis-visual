from playwright.sync_api import sync_playwright
import json
url="https://zrx-11.github.io/complex-analysis-visual/"
out={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/local/bin/chromium",headless=True)
    pg=b.new_page(); errs=[]; pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(url,timeout=60000); pg.wait_for_timeout(4000)
    out["title"]=pg.title()
    pg.evaluate("location.hash='#/book/visual-complex-analysis/chapter/ch12'"); pg.wait_for_timeout(6000)
    out["ch12_chars"]=len(pg.inner_text("#view"))
    out["ch12_katex"]=pg.eval_on_selector_all(".katex","e=>e.length")
    out["ch12_mermaid"]=pg.eval_on_selector_all(".mermaid svg","e=>e.length")
    pg.evaluate("location.hash='#/book/visual-complex-analysis/concept/c48'"); pg.wait_for_timeout(3000)
    out["c48_depth"]=pg.eval_on_selector_all("details.depth-fragment","e=>e.length")
    out["errors"]=errs
    b.close()
print(json.dumps(out,ensure_ascii=False,indent=2))
