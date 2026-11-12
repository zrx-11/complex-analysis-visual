import json
m=json.load(open("manifest.json",encoding="utf-8"))
chapters={c["id"]:c["title"] for c in m["chapters"]}
def num(cid): return int(cid[2:])
def letter(i): return "ABCD"[i]
lines=["# 《复分析：可视化方法》测验",""]
for ch in sorted(m["chapters"],key=lambda c:num(c["id"])):
    cid=ch["id"]; qs=[q for q in m["quizzes"] if q["chapterId"]==cid]
    if not qs: continue
    n=num(cid)
    lines.append(f"## 第 {n} 章测验（检查点）"); lines.append("")
    for q in qs:
        typ={"single":"单选","multi":"多选"}.get(q["type"],q["type"])
        lines.append(f"### {q['id'].upper()}.（{typ}）{q['question']}")
        if q.get("options"):
            opts=q["options"]; lines.append("- "+" B. ".join(f"{letter(i)}. {o}" for i,o in enumerate(opts)) if len(opts)>1 else "- A. "+opts[0])
        if isinstance(q["answer"],list):
            ans="、".join(letter(i) for i in q["answer"])
        else:
            ans=letter(q["answer"])
        lines.append(f"**答案**：{ans}")
        lines.append(f"**解析**：{q['explain']}")
        lines.append("")
open("quiz.md","w",encoding="utf-8").write("\n".join(lines).rstrip()+"\n")

lines=["# 《复分析：可视化方法》抽认卡",""]
for ch in sorted(m["chapters"],key=lambda c:num(c["id"])):
    cid=ch["id"]; fs=[f for f in m["flashcards"] if f["chapterId"]==cid]
    if not fs: continue
    lines.append(f"## 第 {num(cid)} 章"); lines.append("")
    for f in fs:
        lines.append(f"### 卡片：{f['front']}")
        lines.append(f"- **背面**：{f['back']}")
        lines.append(f"- **标签**：{', '.join(f.get('tags',[]))}")
        lines.append(f"- **章节**：{cid}")
        lines.append("")
open("flashcards.md","w",encoding="utf-8").write("\n".join(lines).rstrip()+"\n")

lines=["# 术语表","","| 术语 | 白话定义 | 首次出现 | 章节 |","|---|---|---|---|"]
for ch in sorted(m["chapters"],key=lambda c:num(c["id"])):
    cid=ch["id"]
    for g in m["glossary"]:
        if g["chapterId"]==cid:
            lines.append(f"| {g['term']} | {g['def']} | {cid} | 第 {num(cid)} 章 |")
open("glossary.md","w",encoding="utf-8").write("\n".join(lines)+"\n")
print("synced",len(m["quizzes"]),len(m["flashcards"]),len(m["glossary"]))
