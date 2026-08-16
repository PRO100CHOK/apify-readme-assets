"""Render a README hero HTML to a 2x PNG (full page, exact content height)."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

src = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
width = int(sys.argv[3]) if len(sys.argv) > 3 else 760

with sync_playwright() as pw:
    b = pw.chromium.launch()
    page = b.new_page(viewport={"width": width, "height": 800}, device_scale_factor=2)
    page.goto(src.as_uri())
    page.wait_for_timeout(400)
    h = page.evaluate("document.body.scrollHeight")
    page.set_viewport_size({"width": width, "height": int(h)})
    page.wait_for_timeout(200)
    page.screenshot(path=str(out))
    b.close()

print(f"wrote {out} ({width}x{h} css -> {width*2}x{h*2} px)")
