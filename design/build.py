"""Rebuild site/index.html from design/template.html by embedding images as base64.

Run from the "Stora Photographie" project root:
    python design/build.py
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "design" / "template.html"
OUTPUT = ROOT / "site" / "index.html"

MAPPING = {
    "__CAMERA_FULL__": "design/assets/camera-full.png",
    "__LENS_FULL__": "design/assets/lens-full.png",
    "__STUDIOLIGHT_FULL__": "design/assets/studiolight-full.png",
    "__ICON_LIGHT__": "design/assets/icon-light.png",
}

def main():
    html = TEMPLATE.read_text(encoding="utf-8")
    for placeholder, rel_path in MAPPING.items():
        path = ROOT / rel_path
        ext = path.suffix.lstrip(".")
        b64 = base64.b64encode(path.read_bytes()).decode()
        html = html.replace(placeholder, f"data:image/{ext};base64,{b64}")
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"OK: {OUTPUT} ({len(html)} caracteres)")

if __name__ == "__main__":
    main()
