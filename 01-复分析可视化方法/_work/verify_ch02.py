from playwright.sync_api import sync_playwright
import pathlib, json
html = pathlib.Path("visual-complex-analysis学习伴侣.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/local/bin/chromium")
    pg = b.new_page()
    errs=[]
    pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(html)
    pg.wait_for_timeout(9000)
    katex = pg.eval_on_selector_all(".katex", "e=>e.length")
    mermaid = pg.eval_on_selector_all(".mermaid svg", "e=>e.length")
    pg.evaluate("location.hash='#/chapter/ch02'")
    pg.wait_for_timeout(600)
    has_ch2 = "作为变换看的复函数" in pg.inner_text("#view")
    pg.evaluate("location.hash='#/concept/c07'")
    pg.wait_for_timeout(600)
    depth = pg.eval_on_selector_all("details.depth-fragment", "e=>e.length")
    opened=False
    if depth:
        pg.eval_on_selector("details.depth-fragment", "e=>e.open=true")
        pg.wait_for_timeout(200)
        opened = pg.eval_on_selector("details.depth-fragment", "e=>e.open")
    pg.evaluate("location.hash='#/concept/c09'")
    pg.wait_for_timeout(600)
    depth9 = pg.eval_on_selector_all("details.depth-fragment", "e=>e.length")
    print(json.dumps(dict(katex=katex, mermaid=mermaid, ch2=has_ch2, depth_c07=depth, opened=opened, depth_c09=depth9, console_errors=errs[:5]), ensure_ascii=False))
    b.close()
