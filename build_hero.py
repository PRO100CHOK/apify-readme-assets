#!/usr/bin/env python
"""Build an Apify README hero banner: JSON config -> HTML -> 2x PNG.

    python build_hero.py <config.json> <outdir>

Writes <outdir>/<actor>/hero.html and <outdir>/<actor>/hero.png (760 CSS px wide,
rendered at device_scale_factor=2). Commit both into the public assets repo and use
    https://raw.githubusercontent.com/PRO100CHOK/apify-readme-assets/main/<actor>/hero.png

Config keys
-----------
actor      str   actor name, used for the directory and the terminal path
accent     str   primary accent hex (headline line 2, rails, pill, eyebrow)
accent2    str   secondary glow hex, usually the platform's second brand colour
eyebrow    [str, str]        e.g. ["AHREFS", "16 SEO TOOLS"]
headline   [str, str, str]   3 short shout lines; line 3 is the grey punchline
lede       str   HTML: <b> white, <i> accent, <u> accent2
pill       str   badge text, " * " renders as a bullet separator
code       [str] plain-text JSON lines, auto-highlighted; prefix a line with ">" to
                 give it the accent left-rail highlight
"""
import html
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- highlighting

_TOKEN = re.compile(
    r'(?P<comment>//.*$)'
    r'|(?P<key>"(?:[^"\\]|\\.)*")(?=\s*:)'
    r'|(?P<str>"(?:[^"\\]|\\.)*")'
    r'|(?P<num>-?\b\d+(?:\.\d+)?\b)'
    r'|(?P<bool>\b(?:true|false|null)\b)'
)


def highlight(line: str) -> str:
    """Colourise one line of JSON-ish text into <span>s."""
    out, pos = [], 0
    for m in _TOKEN.finditer(line):
        if m.start() > pos:
            out.append(f'<span class="p">{html.escape(line[pos:m.start()])}</span>')
        kind = m.lastgroup
        cls = {"comment": "c", "key": "k", "str": "s", "num": "n", "bool": "n"}[kind]
        out.append(f'<span class="{cls}">{html.escape(m.group())}</span>')
        pos = m.end()
    if pos < len(line):
        out.append(f'<span class="p">{html.escape(line[pos:])}</span>')
    return "".join(out) or "&nbsp;"


def code_block(lines):
    """Join lines as block spans with no stray blank rows (see visuals.md).

    Each span is emitted unterminated (`</span`) and the joiner puts the newline
    *inside* the closing tag, so no literal newline ever lands between two
    display:block spans -- that is what would render as an empty extra row.
    """
    spans = []
    for raw in lines:
        hl = raw.startswith(">")
        text = raw[1:] if hl else raw
        cls = "ln hl" if hl else "ln"
        spans.append(f'<span class="{cls}">{highlight(text)}</span')
    return "\n        >".join(spans) + ">"


# ---------------------------------------------------------------------- render

TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:760px; }}
  body {{ background:#08090B; font-family:"Helvetica Neue", Arial, "Segoe UI", sans-serif;
         -webkit-font-smoothing:antialiased; position:relative; overflow:hidden; }}
  .grid {{ position:absolute; inset:0;
    background-image:linear-gradient(rgba(255,255,255,.028) 1px, transparent 1px),
                     linear-gradient(90deg, rgba(255,255,255,.028) 1px, transparent 1px);
    background-size:38px 38px; }}
  .glow {{ position:absolute; top:-190px; left:-170px; width:660px; height:560px;
    background:radial-gradient(closest-side, {accent}38, {accent}00); }}
  .glow2 {{ position:absolute; top:230px; right:-220px; width:540px; height:480px;
    background:radial-gradient(closest-side, {accent2}1E, {accent2}00); }}
  .wrap {{ position:relative; padding:44px 45px 46px; }}

  .eyebrow {{ display:flex; align-items:center; gap:11px; margin-bottom:22px; }}
  .dot {{ width:9px; height:9px; border-radius:50%; background:{accent};
         box-shadow:0 0 14px 3px {accent}A6; }}
  .eyebrow span {{ font-family:"Cascadia Mono", Consolas, "Courier New", monospace;
    font-size:13px; font-weight:700; letter-spacing:.20em; color:{accent}; }}
  .eyebrow span em {{ font-style:normal; color:#6E7681; }}

  h1 {{ line-height:.94; letter-spacing:-.035em; font-weight:800; }}
  h1 div {{ font-size:{h1size}px; }}
  .l1 {{ color:#FFFFFF; }} .l2 {{ color:{accent}; }} .l3 {{ color:#6E7681; }}

  p.lede {{ margin-top:28px; font-size:17.5px; line-height:1.52; color:#C9CDD3; max-width:655px; }}
  p.lede b {{ color:#FFFFFF; font-weight:700; }}
  p.lede i {{ font-style:normal; color:{accent}; font-weight:700; }}
  p.lede u {{ text-decoration:none; color:{accent2}; font-weight:700; }}

  .badges {{ margin-top:30px; display:flex; align-items:center; gap:16px; }}
  .pill {{ border:1px solid {accent}73; border-radius:999px; padding:9px 18px;
    font-family:"Cascadia Mono", Consolas, monospace; font-size:12px; font-weight:700;
    letter-spacing:.11em; color:{accent}; background:{accent}12; }}
  .runs {{ font-family:"Cascadia Mono", Consolas, monospace; font-size:12px;
    letter-spacing:.11em; color:#6E7681; }}
  .runs b {{ color:#E6E8EB; }} .sep {{ color:#3A3F46; }}

  .term {{ margin-top:42px; border:1px solid #23262B; border-radius:12px;
    background:#0C0E11; overflow:hidden; }}
  .bar {{ display:flex; align-items:center; gap:9px; padding:12px 16px;
    border-bottom:1px solid #1B1E23; background:#101317; }}
  .b {{ width:11px; height:11px; border-radius:50%; }}
  .b1{{background:#FF5F57}} .b2{{background:#FEBC2E}} .b3{{background:#28C840}}
  .path {{ margin-left:9px; font-family:"Cascadia Mono", Consolas, monospace;
    font-size:12.5px; letter-spacing:.05em; color:#6E7681; }}
  .live {{ margin-left:auto; display:flex; align-items:center; gap:6px;
    border:1px solid rgba(40,200,64,.35); border-radius:999px; padding:4px 11px;
    background:rgba(40,200,64,.08); font-family:"Cascadia Mono", Consolas, monospace;
    font-size:10.5px; font-weight:700; letter-spacing:.11em; color:#28C840; }}
  .live .d {{ width:6px; height:6px; border-radius:50%; background:#28C840; }}

  pre {{ padding:18px 20px 20px; font-family:"Cascadia Mono", Consolas, "Courier New", monospace;
    font-size:{codesize}px; line-height:1.76; color:#C9CDD3; white-space:normal; }}
  /* every source line is its own block, so no stray blank rows */
  .ln {{ display:block; white-space:pre; }}
  .hl {{ background:{accent}1C; box-shadow:inset 3px 0 0 {accent}; margin:0 -20px;
        padding:0 20px 0 17px; }}
  .c {{ color:#5A616B; }} .k {{ color:#79C0FF; }} .s {{ color:#7EE787; }}
  .n {{ color:#FFA657; }} .p {{ color:#8B949E; }}
</style></head>
<body>
  <div class="grid"></div><div class="glow"></div><div class="glow2"></div>
  <div class="wrap">
    <div class="eyebrow"><div class="dot"></div>
      <span>{eyebrow0} <em>/</em> {eyebrow1}</span></div>
    <h1><div class="l1">{hl0}</div><div class="l2">{hl1}</div><div class="l3">{hl2}</div></h1>
    <p class="lede">{lede}</p>
    <div class="badges">
      <div class="pill">{pill}</div><div class="sep">&bull;</div>
      <div class="runs">RUNS ON <b>APIFY</b></div>
    </div>
    <div class="term">
      <div class="bar">
        <div class="b b1"></div><div class="b b2"></div><div class="b b3"></div>
        <div class="path">~/{actor}</div>
        <div class="live"><div class="d"></div>LIVE</div>
      </div>
      <pre>{code}</pre>
    </div>
  </div>
</body></html>
"""


def build_html(cfg: dict) -> str:
    return TEMPLATE.format(
        accent=cfg["accent"],
        accent2=cfg.get("accent2", "#FF8A00"),
        h1size=cfg.get("h1size", 59),
        codesize=cfg.get("codesize", 13.2),
        eyebrow0=html.escape(cfg["eyebrow"][0]),
        eyebrow1=html.escape(cfg["eyebrow"][1]),
        hl0=html.escape(cfg["headline"][0]),
        hl1=html.escape(cfg["headline"][1]),
        hl2=html.escape(cfg["headline"][2]),
        lede=cfg["lede"],
        pill=html.escape(cfg["pill"]).replace(" * ", " &bull; "),
        actor=cfg["actor"],
        code=code_block(cfg["code"]),
    )


def render(html_path: Path, png_path: Path, width: int = 760) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        page = b.new_page(viewport={"width": width, "height": 800}, device_scale_factor=2)
        page.goto(html_path.resolve().as_uri())
        page.wait_for_timeout(350)
        h = page.evaluate("document.body.scrollHeight")
        page.set_viewport_size({"width": width, "height": int(h)})
        page.wait_for_timeout(150)
        page.screenshot(path=str(png_path))
        b.close()


def main() -> None:
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    outdir = Path(sys.argv[2]) / cfg["actor"]
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "hero.html").write_text(build_html(cfg), encoding="utf-8")
    render(outdir / "hero.html", outdir / "hero.png")
    print(f"{cfg['actor']}: {outdir / 'hero.png'}")


if __name__ == "__main__":
    main()
