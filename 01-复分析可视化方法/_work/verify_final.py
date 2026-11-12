from playwright.sync_api import sync_playwright
import os, json
path=os.path.abspath("visual-complex-analysis学习伴侣.html")
out={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/local/bin/chromium",headless=True)
    pg=b.new_page()
    errs=[]; pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto("file://"+path); pg.wait_for_timeout(4000)
    pg.evaluate("location.hash='#/chapter/ch12'"); pg.wait_for_timeout(6000)
    out["ch12_katex"]=pg.eval_on_selector_all(".katex","e=>e.length")
    out["ch12_mermaid"]=pg.eval_on_selector_all(".mermaid svg","e=>e.length")
    pg.evaluate("location.hash='#/concept/c48'"); pg.wait_for_timeout(3000)
    out["c48_depth"]=pg.eval_on_selector_all("details.depth-fragment","e=>e.length")
    if out["c48_depth"]:
        pg.eval_on_selector("details.depth-fragment","e=>e.open=true")
        pg.wait_for_timeout(300)
        out["c48_open"]=pg.eval_on_selector("details.depth-fragment","e=>e.open")
    out["console_errors"]=errs
    b.close()
print(json.dumps(out,ensure_ascii=False,indent=2))
