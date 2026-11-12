from playwright.sync_api import sync_playwright
import pathlib, json
html = pathlib.Path("visual-complex-analysis学习伴侣.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/local/bin/chromium")
    pg = b.new_page()
    errs=[]
    pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(html)
    pg.wait_for_timeout(3000)
    pg.evaluate("location.hash='#/chapter/ch02'")
    pg.wait_for_timeout(9000)
    k2 = pg.eval_on_selector_all(".katex", "e=>e.length")
    m2 = pg.eval_on_selector_all(".mermaid svg", "e=>e.length")
    raw = pg.eval_on_selector_all(".katex-inline", "e=>e.length")
    pg.evaluate("location.hash='#/chapter/ch01'")
    pg.wait_for_timeout(1500)
    k1 = pg.eval_on_selector_all(".katex", "e=>e.length")
    total_k = pg.eval_on_selector_all(".katex", "e=>e.length")
    stats = pg.evaluate("()=>document.body.innerText.slice(0,0)")
    print(json.dumps(dict(ch02_katex=k2, ch02_mermaid=m2, ch02_inline_slots=raw, ch01_katex=k1, console_errors=errs[:5]), ensure_ascii=False))
    b.close()
