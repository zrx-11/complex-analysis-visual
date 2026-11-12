from playwright.sync_api import sync_playwright
import pathlib, json
html = pathlib.Path("visual-complex-analysis学习伴侣.html").resolve().as_uri()
depth = {}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/local/bin/chromium")
    pg = b.new_page(); errs=[]
    pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(html); pg.wait_for_timeout(2500)
    for cid in ["c02","c03","c07","c08","c09"]:
        pg.evaluate(f"location.hash='#/concept/{cid}'"); pg.wait_for_timeout(700)
        n = pg.eval_on_selector_all("details.depth-fragment", "e=>e.length")
        chars = 0
        if n:
            pg.eval_on_selector("details.depth-fragment", "e=>e.open=true"); pg.wait_for_timeout(150)
            chars = len(pg.eval_on_selector("details.depth-fragment", "e=>e.innerText"))
        depth[cid] = [n, chars]
    print(json.dumps({"depth": depth, "errs": errs[:3]}, ensure_ascii=False))
    b.close()
