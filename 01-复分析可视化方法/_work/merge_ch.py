"""把一章的数据合并进 manifest.json。
用法：python3 _work/merge_ch.py _work/ch03_data.py
数据文件需定义 DATA = {chapter, concepts, quizzes, flashcards, glossary, path}
"""
import json, sys, importlib.util, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("chdata", sys.argv[1])
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
d = mod.DATA

path = os.path.join(BASE, "manifest.json")
m = json.load(open(path, encoding="utf-8"))

def ids(lst):
    return {x["id"] for x in lst}

m["chapters"].append(d["chapter"])
for c in d["concepts"]:
    if c["id"] not in ids(m["concepts"]):
        m["concepts"].append(c)
for q in d["quizzes"]:
    if q["id"] not in ids(m["quizzes"]):
        m["quizzes"].append(q)
for f in d["flashcards"]:
    if f["id"] not in ids(m["flashcards"]):
        m["flashcards"].append(f)
for g in d["glossary"]:
    m["glossary"].append(g)
if d.get("path"):
    m["learningPath"].append(d["path"])

json.dump(m, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("merged", d["chapter"]["id"], "chapters", len(m["chapters"]), "concepts", len(m["concepts"]),
      "quizzes", len(m["quizzes"]), "cards", len(m["flashcards"]), "glossary", len(m["glossary"]))
