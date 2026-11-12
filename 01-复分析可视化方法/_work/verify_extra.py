import asyncio, os, json
from playwright.async_api import async_playwright

ROOT = "/home/user/Doubao/chats/38453413604796930/复分析可视化学习系统"
INDEX = "file://" + os.path.join(ROOT, "index.html")
BOOK = "file://" + os.path.join(ROOT, "01-复分析可视化方法", "visual-complex-analysis学习伴侣.html")


async def main():
    rows, errs = [], []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/local/bin/chromium", args=["--no-sandbox"])
        pg = await b.new_page()
        pg.on("console", lambda m: errs.append(m.type + ":" + m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror:" + str(e)))

        # --- 总入口 ---
        await pg.goto(INDEX, wait_until="load"); await pg.wait_for_timeout(1500)
        rows.append(("首页书本卡片", await pg.locator("text=复分析：可视化方法").count()))
        await pg.click("text=进入学习 →"); await pg.wait_for_timeout(1200)
        rows.append(("进入后导航项", await pg.eval_on_selector_all("#nav a", "e=>e.length")))
        await pg.click("text=第 1 章：几何和复算术"); await pg.wait_for_timeout(3000)
        rows.append(("总入口章节页字符", len(await pg.inner_html("body"))))
        rows.append(("总入口 KaTeX 数", await pg.locator(".katex").count()))

        # --- 单书伴侣 ---
        await pg.goto(BOOK, wait_until="load"); await pg.wait_for_timeout(2500)
        rows.append(("伴侣导航项", await pg.eval_on_selector_all("#nav a", "e=>e.length")))
        await pg.click("text=第 1 章：几何和复算术"); await pg.wait_for_timeout(3500)
        rows.append(("伴侣章节 KaTeX", await pg.locator(".katex").count()))
        rows.append(("伴侣章节 Mermaid SVG", await pg.locator(".mermaid svg").count()))
        rows.append(("章节正文长度", len(await pg.inner_text("body"))))

        # 概念页 + 深度片段
        await pg.click("text=复数乘法：旋转加放大"); await pg.wait_for_timeout(1800)
        rows.append(("概念页深度片段", await pg.locator("details.depth-fragment").count()))
        rows.append(("概念页 KaTeX", await pg.locator(".katex").count()))
        if await pg.locator("details.depth-fragment").count():
            await pg.click("details.depth-fragment summary"); await pg.wait_for_timeout(600)
            rows.append(("展开后正文长度", len(await pg.inner_text("body"))))

        # 诊断页
        navs = await pg.eval_on_selector_all("#nav a", "e=>e.map(x=>x.innerText)")
        diag = [n for n in navs if "诊断" in n]
        rows.append(("诊断导航项", diag))
        if diag:
            await pg.click(f"text={diag[0]}"); await pg.wait_for_timeout(800)
            await pg.click("#diag-start"); await pg.wait_for_timeout(1500)
            rows.append(("诊断抽题数", await pg.locator("#diag-stage .quiz-item").count()))

        # 测验作答
        navs = await pg.eval_on_selector_all("#nav a", "e=>e.map(x=>x.innerText)")
        quiz = [n for n in navs if n.startswith("测验")][0]
        await pg.click(f"text={quiz}"); await pg.wait_for_timeout(900)
        it = pg.locator(".quiz-item").first
        await it.locator("input").nth(1).check(); await pg.click(".quiz-item .quiz-check")
        await pg.wait_for_timeout(700)
        rows.append(("答题反馈", (await it.locator(".quiz-feedback").inner_text()).strip()[:20]))

        # 深色
        before = await pg.evaluate("document.documentElement.getAttribute('data-theme')||document.body.getAttribute('data-theme')")
        await pg.click("text=🌙 深色") if await pg.locator("text=🌙 深色").count() else None
        await pg.wait_for_timeout(500)
        after = await pg.evaluate("document.documentElement.getAttribute('data-theme')||document.body.getAttribute('data-theme')")
        rows.append(("深色切换", f"{before}->{after}"))

        # 进度持久化
        keys = await pg.evaluate("Object.keys(localStorage)")
        rows.append(("localStorage 键", keys))
        await b.close()
    for k, v in rows:
        print(f"{k}: {v}")
    print("CONSOLE_ERRORS:", json.dumps(errs[:8], ensure_ascii=False))

asyncio.run(main())
