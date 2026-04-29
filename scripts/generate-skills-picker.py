#!/usr/bin/env python3
"""
Build the interactive skills picker for Dharma.

Reads each top-level */SKILL.md under the repository root and writes
docs/index.html for GitHub Pages (or local opening).

Usage:
  python3 scripts/generate-skills-picker.py
  python3 scripts/generate-skills-picker.py /path/to/skills-root
"""

from __future__ import annotations

import re
import sys
from html import escape
from pathlib import Path


def category_for(folder: str) -> str:
    if folder.startswith("00-"):
        return "Orchestrator"
    if folder.startswith("pm-") or folder in ("churney-os", "goal-driven-execution"):
        return "Layer 1 — Product & Planning"
    if folder in (
        "karpathy-discipline",
        "think-before-coding",
        "simplicity-first",
        "surgical-changes",
    ):
        return "Layer 2 — Engineering Discipline"
    if folder.startswith("superpowers"):
        return "Layer 3 — Execution Methodology"
    if folder.startswith("uiux-"):
        return "Layer 4 — Experience Quality"
    if folder.startswith(
        ("ai-", "inference-", "prompt-", "model-", "benchmark-")
    ):
        return "Layer 5 — AI & Economics"
    return "Other"


def layer_slug(category: str) -> str:
    if category == "Orchestrator":
        return "orchestrator"
    if category.startswith("Layer 1"):
        return "l1"
    if category.startswith("Layer 2"):
        return "l2"
    if category.startswith("Layer 3"):
        return "l3"
    if category.startswith("Layer 4"):
        return "l4"
    if category.startswith("Layer 5"):
        return "l5"
    return "other"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (fields, body). Minimal YAML subset: key: value and key: | blocks."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw_fm = parts[1].strip("\n")
    body = parts[2].lstrip("\n")

    fields: dict[str, str] = {}
    lines = raw_fm.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        if rest == "|":
            block: list[str] = []
            i += 1
            while i < len(lines):
                ln = lines[i]
                if ln.startswith("  "):
                    block.append(ln[2:].rstrip())
                    i += 1
                elif ln.strip() == "":
                    block.append("")
                    i += 1
                else:
                    break
            fields[key] = "\n".join(block).strip()
            continue
        if rest.startswith('"') and rest.endswith('"'):
            rest = rest[1:-1]
        fields[key] = rest
        i += 1

    return fields, body


def extract_core_snippet(body: str, max_chars: int = 1200) -> str:
    """Prefer 'Core rule' / 'Core Operating Rule' / first bold line after H1."""
    patterns = [
        r"##\s+Core rule\s*\n+((?:.|\n)+?)(?=\n## |\Z)",
        r"##\s+Core Operating Rule\s*\n+((?:.|\n)+?)(?=\n## |\Z)",
        r"##\s+The Non-Negotiable Rule[^\n]*\s*\n+((?:.|\n)+?)(?=\n## |\Z)",
        r"#\s+[^\n]+\n+((?:\*\*[^*]+\*\*(?:.|\n))+?)(?=\n## |\Z)",
    ]
    for pat in patterns:
        m = re.search(pat, body, re.IGNORECASE)
        if m:
            chunk = m.group(1).strip()
            if len(chunk) > max_chars:
                chunk = chunk[: max_chars - 3].rsplit(" ", 1)[0] + "..."
            return chunk
    # Fallback: skip title, take first substantive paragraphs
    lines = body.split("\n")
    buf: list[str] = []
    started = False
    for ln in lines:
        if ln.startswith("# ") and not started:
            started = True
            continue
        if not started:
            continue
        if ln.startswith("## "):
            break
        if ln.strip():
            buf.append(ln)
    out = "\n".join(buf).strip()
    if len(out) > max_chars:
        out = out[: max_chars - 3].rsplit(" ", 1)[0] + "..."
    return out or "(See full SKILL.md for body.)"


def md_inline_to_html(text: str) -> str:
    """Minimal **bold** and newlines to <br>/<strong>. Avoid backticks for JS safety."""
    text = escape(text).replace("`", "&#96;")
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = text.replace("\n\n", "</p><p>")
    text = text.replace("\n", "<br>\n")
    return f"<p>{text}</p>" if text else ""


def build_html(skills: list[dict], source_label: str) -> str:
    import json

    data_json = json.dumps(skills, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Dharma — Skills picker</title>
  <style>
    :root {{
      --bg: #0c0f14;
      --surface: #141a24;
      --elevated: #1c2533;
      --text: #eef2f8;
      --muted: #8a9ab0;
      --border: #2a3548;
      --glow: rgba(91, 155, 213, 0.35);
      --orch: #e8b84a;
      --l1: #6bcf7f;
      --l2: #5eb8e8;
      --l3: #a78bfa;
      --l4: #f472b6;
      --l5: #fb923c;
      --other: #94a3b8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: "DM Sans", ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      background: radial-gradient(1200px 600px at 20% -10%, rgba(91,155,213,0.12), transparent),
        radial-gradient(900px 500px at 90% 30%, rgba(167,139,250,0.1), transparent),
        var(--bg);
      color: var(--text);
      margin: 0;
      line-height: 1.45;
      font-size: 15px;
      padding-bottom: 10rem;
    }}
    header {{
      padding: 1.5rem clamp(1rem, 4vw, 2rem) 1.25rem;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(28,37,51,0.95), rgba(20,26,36,0.85));
      backdrop-filter: blur(12px);
    }}
    header h1 {{
      margin: 0 0 0.4rem;
      font-size: clamp(1.35rem, 3vw, 1.75rem);
      font-weight: 700;
      letter-spacing: -0.02em;
    }}
    header p {{ margin: 0; color: var(--muted); font-size: 0.92rem; max-width: 62ch; }}
    .toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      align-items: center;
      padding: 0.9rem clamp(1rem, 4vw, 2rem);
      border-bottom: 1px solid var(--border);
      background: rgba(20, 26, 36, 0.6);
      position: sticky;
      top: 0;
      z-index: 40;
      backdrop-filter: blur(10px);
    }}
    .toolbar input[type="search"] {{
      flex: 1;
      min-width: 220px;
      padding: 0.6rem 1rem;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .toolbar input:focus {{
      border-color: #5b9bd5;
      box-shadow: 0 0 0 3px var(--glow);
    }}
    .toolbar select {{
      padding: 0.55rem 0.75rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
    }}
    .btn {{
      font: inherit;
      cursor: pointer;
      padding: 0.5rem 0.9rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--elevated);
      color: var(--text);
      transition: background 0.15s, transform 0.1s;
    }}
    .btn:hover {{ background: #243044; }}
    .btn:active {{ transform: scale(0.98); }}
    .btn-primary {{
      background: linear-gradient(135deg, #3d6fa8, #5b9bd5);
      border-color: transparent;
      color: #fff;
    }}
    .btn-primary:hover {{ filter: brightness(1.06); }}
    .count {{ color: var(--muted); font-size: 0.88rem; white-space: nowrap; }}
    .hint {{ color: var(--muted); font-size: 0.8rem; width: 100%; margin-top: 0.15rem; }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
      gap: 1.1rem;
      padding: 1.25rem clamp(1rem, 4vw, 2rem) 2rem;
      max-width: 1400px;
      margin: 0 auto;
    }}

    .skill-card {{
      position: relative;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s;
      display: flex;
      flex-direction: column;
      min-height: 220px;
      outline: none;
    }}
    .skill-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 12px 40px rgba(0,0,0,0.35);
      border-color: rgba(91,155,213,0.35);
    }}
    .skill-card:focus-visible {{
      box-shadow: 0 0 0 3px var(--glow);
    }}
    .skill-card.is-selected {{
      border-color: #5b9bd5;
      box-shadow: 0 0 0 1px #5b9bd5, 0 8px 32px rgba(91,155,213,0.2);
    }}
    .skill-card .accent {{
      height: 4px;
      width: 100%;
    }}
    .layer-orchestrator .accent {{ background: linear-gradient(90deg, var(--orch), #f4d03f); }}
    .layer-l1 .accent {{ background: linear-gradient(90deg, #4ade80, var(--l1)); }}
    .layer-l2 .accent {{ background: linear-gradient(90deg, #38bdf8, var(--l2)); }}
    .layer-l3 .accent {{ background: linear-gradient(90deg, #818cf8, var(--l3)); }}
    .layer-l4 .accent {{ background: linear-gradient(90deg, #f472b6, #fb7185); }}
    .layer-l5 .accent {{ background: linear-gradient(90deg, #fb923c, #f59e0b); }}
    .layer-other .accent {{ background: var(--other); }}

    .card-inner {{ padding: 1rem 1.1rem 1.1rem; flex: 1; display: flex; flex-direction: column; gap: 0.5rem; }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 0.5rem;
    }}
    .skill-name {{
      font-weight: 650;
      font-size: 1.02rem;
      letter-spacing: -0.02em;
      margin: 0;
      font-family: "JetBrains Mono", ui-monospace, monospace;
      color: #c8d7ea;
    }}
    .pick-indicator {{
      flex-shrink: 0;
      width: 22px;
      height: 22px;
      border-radius: 6px;
      border: 2px solid var(--border);
      background: rgba(0,0,0,0.25);
      display: grid;
      place-items: center;
      transition: border-color 0.15s, background 0.15s;
    }}
    .skill-card.is-selected .pick-indicator {{
      background: linear-gradient(135deg, #3d6fa8, #5b9bd5);
      border-color: transparent;
    }}
    .pick-indicator svg {{ width: 14px; height: 14px; opacity: 0; }}
    .skill-card.is-selected .pick-indicator svg {{ opacity: 1; }}

    .layer-pill {{
      font-size: 0.65rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
      background: rgba(0,0,0,0.25);
      padding: 0.25rem 0.55rem;
      border-radius: 999px;
      align-self: flex-start;
    }}
    .folder-tag {{
      font-size: 0.72rem;
      color: var(--muted);
      font-family: ui-monospace, monospace;
    }}
    .preview-label {{
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #7dd3fc;
      margin-top: 0.25rem;
    }}
    .preview-text {{
      font-size: 0.86rem;
      color: #b8c5d8;
      line-clamp: 4;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      -webkit-box-orient: vertical;
      overflow: hidden;
      flex: 1;
    }}
    .preview-text p {{ margin: 0; display: inline; }}
    .card-actions {{
      margin-top: auto;
      padding-top: 0.5rem;
    }}
    details.card-details {{
      font-size: 0.82rem;
    }}
    details.card-details summary {{
      cursor: pointer;
      color: #7dd3fc;
      list-style: none;
    }}
    details.card-details summary::-webkit-details-marker {{ display: none; }}
    details.card-details .detail-body {{
      margin-top: 0.6rem;
      padding: 0.65rem 0.75rem;
      background: rgba(0,0,0,0.22);
      border-radius: 10px;
      max-height: 200px;
      overflow-y: auto;
      font-size: 0.8rem;
      color: #aebccf;
    }}

    .tray {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 50;
      background: linear-gradient(180deg, transparent, rgba(12,15,20,0.92) 18%);
      padding: 0.75rem clamp(1rem, 3vw, 2rem) 1rem;
      pointer-events: none;
    }}
    .tray-inner {{
      pointer-events: auto;
      max-width: 900px;
      margin: 0 auto;
      background: var(--elevated);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1rem 1.15rem;
      box-shadow: 0 -8px 40px rgba(0,0,0,0.45);
    }}
    .tray-head {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 0.65rem;
    }}
    .tray-head strong {{ font-size: 1rem; }}
    .tray-head span {{ color: var(--muted); font-size: 0.9rem; }}
    .chip-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
      max-height: 88px;
      overflow-y: auto;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.28rem 0.55rem 0.28rem 0.65rem;
      background: rgba(91,155,213,0.15);
      border: 1px solid rgba(91,155,213,0.35);
      border-radius: 999px;
      font-size: 0.78rem;
      font-family: ui-monospace, monospace;
      color: #b8d4f0;
    }}
    .chip button {{
      border: none;
      background: transparent;
      color: var(--muted);
      cursor: pointer;
      padding: 0 0.15rem;
      font-size: 1rem;
      line-height: 1;
    }}
    .chip button:hover {{ color: #f87171; }}
    .tray-actions {{ display: flex; flex-wrap: wrap; gap: 0.45rem; }}

    .toast {{
      position: fixed;
      bottom: 6.5rem;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: #1e293b;
      color: #e2e8f0;
      padding: 0.55rem 1rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s, transform 0.2s;
      z-index: 60;
      font-size: 0.88rem;
    }}
    .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
  </style>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet" />
</head>
<body>
  <header>
    <h1>Skill cards</h1>
    <p>Tap a card to select skills for your next build. Your picks are remembered on this device. Skills source: {escape(source_label)}</p>
  </header>
  <div class="toolbar">
    <input type="search" id="q" placeholder="Search name, folder, triggers…" autocomplete="off" aria-label="Filter skills" />
    <select id="layer" aria-label="Filter by layer">
      <option value="">All layers</option>
    </select>
    <button type="button" class="btn" id="selectVisible" title="Select all cards currently visible">Select visible</button>
    <button type="button" class="btn" id="clearVisible">Clear visible</button>
    <span class="count" id="count"></span>
    <span class="hint">Click a card to toggle. Use “Copy for chat” to paste into Cursor.</span>
  </div>
  <main class="grid" id="root" role="list"></main>

  <div class="tray" aria-live="polite">
    <div class="tray-inner">
      <div class="tray-head">
        <div>
          <strong>Your selection</strong>
          <span id="traySub">No skills selected</span>
        </div>
      </div>
      <div class="chip-row" id="chipRow"></div>
      <div class="tray-actions">
        <button type="button" class="btn btn-primary" id="copyChat">Copy for chat</button>
        <button type="button" class="btn" id="copyFolders">Copy folder names</button>
        <button type="button" class="btn" id="clearAll">Clear all</button>
      </div>
    </div>
  </div>
  <div class="toast" id="toast" role="status"></div>

  <script>
    const LS_KEY = "dharmaSkillCardPick";
    const skills = {data_json};
    let selected = new Set();

    try {{
      const saved = JSON.parse(localStorage.getItem(LS_KEY) || "[]");
      if (Array.isArray(saved)) saved.forEach((x) => selected.add(x));
    }} catch (e) {{}}

    function persist() {{
      localStorage.setItem(LS_KEY, JSON.stringify([...selected]));
    }}

    const layers = [...new Set(skills.map(s => s.category))].sort();
    const layerSel = document.getElementById("layer");
    for (const L of layers) {{
      const o = document.createElement("option");
      o.value = L;
      o.textContent = L;
      layerSel.appendChild(o);
    }}

    function escapeHtml(t) {{
      const d = document.createElement("div");
      d.textContent = t;
      return d.innerHTML;
    }}
    function escapeAttr(t) {{
      return String(t).replace(/"/g, '&quot;');
    }}

    function skillByFolder(f) {{
      return skills.find((s) => s.folder === f);
    }}

    function cardHtml(s) {{
      const layerClass = "layer-" + (s.layer_slug || "other");
      const isOn = selected.has(s.folder) ? "is-selected" : "";
      return `<article role="listitem" tabindex="0" class="skill-card ${{layerClass}} ${{isOn}}"
        data-folder="${{escapeAttr(s.folder)}}"
        data-search="${{escapeAttr(s.searchBlob)}}"
        data-layer="${{escapeAttr(s.category)}}"
        aria-pressed="${{selected.has(s.folder)}}">
        <div class="accent" aria-hidden="true"></div>
        <div class="card-inner">
          <div class="card-top">
            <h2 class="skill-name">${{escapeHtml(s.name)}}</h2>
            <div class="pick-indicator" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg>
            </div>
          </div>
          <div class="layer-pill">${{escapeHtml(s.category)}}</div>
          <div class="folder-tag">${{escapeHtml(s.rel_path)}}</div>
          <div class="preview-label">Core rule / excerpt</div>
          <div class="preview-text">${{s.snippet_html}}</div>
          <div class="card-actions">
            <details class="card-details" onclick="event.stopPropagation()">
              <summary>Full trigger text &amp; description</summary>
              <div class="detail-body">${{s.description_html}}</div>
            </details>
          </div>
        </div>
      </article>`;
    }}

    function updateTray() {{
      const chipRow = document.getElementById("chipRow");
      const sub = document.getElementById("traySub");
      chipRow.replaceChildren();
      if (selected.size === 0) {{
        sub.textContent = "No skills selected";
        return;
      }}
      sub.textContent = selected.size + " skill" + (selected.size === 1 ? "" : "s") + " selected";
      [...selected].sort().forEach((folder) => {{
        const s = skillByFolder(folder);
        const label = s ? s.name : folder;
        const span = document.createElement("span");
        span.className = "chip";
        span.innerHTML = escapeHtml(label) +
          '<button type="button" aria-label="Remove ' + escapeAttr(label) + '" data-remove="' + escapeAttr(folder) + '">×</button>';
        chipRow.appendChild(span);
      }});
      chipRow.querySelectorAll("button[data-remove]").forEach((btn) => {{
        btn.addEventListener("click", (ev) => {{
          ev.stopPropagation();
          selected.delete(btn.getAttribute("data-remove"));
          persist();
          render();
          updateTray();
        }});
      }});
    }}

    function toggleFolder(folder) {{
      if (selected.has(folder)) selected.delete(folder);
      else selected.add(folder);
      persist();
    }}

    function render() {{
      const q = document.getElementById("q").value.trim().toLowerCase();
      const layer = document.getElementById("layer").value;
      const root = document.getElementById("root");
      let n = 0;
      const frag = document.createDocumentFragment();
      for (const s of skills) {{
        const matchQ = !q || s.searchBlob.includes(q);
        const matchL = !layer || s.category === layer;
        if (!matchQ || !matchL) continue;
        n++;
        const wrap = document.createElement("div");
        wrap.innerHTML = cardHtml(s).trim();
        frag.appendChild(wrap.firstElementChild);
      }}
      root.replaceChildren(frag);
      document.getElementById("count").textContent = n + " cards";

      root.querySelectorAll(".skill-card").forEach((card) => {{
        const folder = card.getAttribute("data-folder");
        card.classList.toggle("is-selected", selected.has(folder));
        card.setAttribute("aria-pressed", selected.has(folder) ? "true" : "false");
        const onActivate = (e) => {{
          if (e.type === "keydown" && e.key !== "Enter" && e.key !== " ") return;
          e.preventDefault();
          toggleFolder(folder);
          render();
          updateTray();
        }};
        card.addEventListener("click", (e) => {{
          if (e.target.closest("details, summary, button, a")) return;
          toggleFolder(folder);
          render();
          updateTray();
        }});
        card.addEventListener("keydown", onActivate);
      }});
    }}

    function toast(msg) {{
      const t = document.getElementById("toast");
      t.textContent = msg;
      t.classList.add("show");
      clearTimeout(toast._id);
      toast._id = setTimeout(() => t.classList.remove("show"), 2200);
    }}

    function copyText(text) {{
      navigator.clipboard.writeText(text).then(() => toast("Copied to clipboard")).catch(() => toast("Copy failed — select text manually"));
    }}

    document.getElementById("copyChat").addEventListener("click", () => {{
      if (selected.size === 0) return toast("No skills selected");
      const lines = [...selected].sort().map((f) => {{
        const s = skillByFolder(f);
        return "- " + (s ? s.name + " (`" + f + "`) — " + s.category : f);
      }});
      const body = [
        "For this task, apply these Cursor/Dharma skills (read SKILL.md for each):",
        "",
        ...lines,
        "",
        "Start with `lifecycle-orchestrator` if the task is new or ambiguous."
      ].join("\\n");
      copyText(body);
    }});

    document.getElementById("copyFolders").addEventListener("click", () => {{
      if (selected.size === 0) return toast("No skills selected");
      copyText([...selected].sort().join("\\n"));
    }});

    document.getElementById("clearAll").addEventListener("click", () => {{
      selected.clear();
      persist();
      render();
      updateTray();
    }});

    document.getElementById("selectVisible").addEventListener("click", () => {{
      const q = document.getElementById("q").value.trim().toLowerCase();
      const layer = document.getElementById("layer").value;
      skills.forEach((s) => {{
        const matchQ = !q || s.searchBlob.includes(q);
        const matchL = !layer || s.category === layer;
        if (matchQ && matchL) selected.add(s.folder);
      }});
      persist();
      render();
      updateTray();
    }});

    document.getElementById("clearVisible").addEventListener("click", () => {{
      const q = document.getElementById("q").value.trim().toLowerCase();
      const layer = document.getElementById("layer").value;
      skills.forEach((s) => {{
        const matchQ = !q || s.searchBlob.includes(q);
        const matchL = !layer || s.category === layer;
        if (matchQ && matchL) selected.delete(s.folder);
      }});
      persist();
      render();
      updateTray();
    }});

    document.getElementById("q").addEventListener("input", render);
    document.getElementById("layer").addEventListener("change", render);
    updateTray();
    render();
  </script>
</body>
</html>
"""


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skills_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo_root
    if not skills_root.is_dir():
        print(f"Skills directory not found: {skills_root}", file=sys.stderr)
        return 1

    skills: list[dict] = []
    for skill_dir in sorted(skills_root.iterdir()):
        if not skill_dir.is_dir():
            continue
        md = skill_dir / "SKILL.md"
        if not md.is_file():
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        fields, body = parse_frontmatter(text)
        name = fields.get("name", skill_dir.name)
        desc_raw = fields.get("description", "(no description in frontmatter)").strip()
        snippet_raw = extract_core_snippet(body)
        cat = category_for(skill_dir.name)
        rel = f"{skill_dir.name}/SKILL.md"

        search_blob = " ".join(
            [
                name,
                skill_dir.name,
                cat,
                desc_raw,
                snippet_raw,
            ]
        ).lower()

        skills.append(
            {
                "folder": skill_dir.name,
                "name": name,
                "category": cat,
                "layer_slug": layer_slug(cat),
                "rel_path": rel,
                "description_raw": desc_raw,
                "description_html": md_inline_to_html(desc_raw),
                "snippet_html": md_inline_to_html(snippet_raw),
                "searchBlob": search_blob,
            }
        )

    docs_dir = repo_root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    out_file = docs_dir / "index.html"
    source_note = "github.com/SahuDilip1356/Dharma — regenerate: python3 scripts/generate-skills-picker.py"
    html = build_html(skills, source_note)
    out_file.write_text(html, encoding="utf-8")
    print(f"Wrote {out_file} ({len(skills)} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
