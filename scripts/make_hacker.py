#!/usr/bin/env python3
"""Turn a photo into ascii.svg — a self-typing, monochrome ASCII portrait.

    pip install pillow numpy
    python3 scripts/make_hacker.py scripts/source.jpg
    python3 scripts/embed_portrait_font.py      # inline the font, see below

Run it once; it is not on a schedule, unlike scripts/generate_stats.py.

The source is the hooded-figure photograph at
https://pixabay.com/photos/mask-hoodie-hacker-attack-2883635/ — Pixabay
Content License, free to use, no attribution required, and kept alongside this
script as scripts/source.jpg so the portrait stays reproducible. CROP is cut to
that image at its original 1280x853; point this at a different photo and the
crop and both curve constants need redoing.

Three things decide whether the output is any good.

  * Polarity. Most ASCII portraits map dark to dense, because most portraits
    are a lit subject on a light ground. This one is the opposite — a lit hood
    and a pale mask against black — so here BRIGHTNESS is the ink. Map it the
    usual way round and the backdrop floods the whole frame with '@'.
  * GAMMA. At 1.0 the hood's cloth falls below the ramp's first step and the
    figure renders as a hollow arch: a bright outline with nothing inside it.
    Pulling it to ~0.55 lifts the cloth into the low end of the ramp.
  * The enclosed-shadow fill, below. Without it the hood has a hole in it.

The grid bakes in an advance width of exactly 0.600 em (CHAR_W / FONT_SIZE), so
after generating, run scripts/embed_portrait_font.py to inline JetBrains Mono.
Otherwise a viewer whose default monospace is narrower — Consolas is about 0.55
— sees the portrait roughly 7% too narrow.

Motion is SMIL, because GitHub strips <script> from READMEs: each row is
revealed by a clipPath wipe with a cursor block riding its edge, staggered top
to bottom, frozen at the end so it prints once and stops.
"""
import argparse
import sys
from collections import deque

import numpy as np
from PIL import Image

RAMP = " .`:-=+*cs#%@"     # sparse/dark -> dense/bright; leading space = blank
COLS = 90                  # below ~80 the mask's features stop separating
ROW_RATIO = 0.48           # monospace cells are about twice as tall as wide
CROP = (185, 15, 1010, 690)   # tight to the hood, cut above the shoulders

BLACK, WHITE = 22.0, 248.0    # input black and white points, 0-255
GAMMA = 0.55                  # see above; this is the difference-maker
FADE0, FADE1 = 0.76, 0.90     # dissolve the last rows, as a fraction of height

# The shadow inside the hood is not dark, it is *empty*: those pixels read
# exactly 0, the same value as the backdrop, so no curve can recover them.
# It has to be drawn instead, and these say how.
WALL = 0.12                # at or below this, a cell counts as unlit
NEAR, FAR = 0.30, 0.09     # ink at the hood's inner wall, and deep inside it
DEPTH = 7.0                # cells over which NEAR falls off to FAR
GRAIN = 0.03               # jitter, so the drawn shadow isn't a flat slab

FG_LIGHT = "#6e7681"       # the stat graphics' ink, so the page is one material
FG_DARK = "#c9d1d9"
CHAR_W = 7.74              # 0.600 em at FONT_SIZE — keep these in step
FONT_SIZE = 12.9
LINE_H = 15
ROW_DELAY = 0.09           # per-row stagger, seconds
FAMILY = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def sample(path, cols=COLS, crop=CROP):
    """Crop, resize onto the character grid, and put the curve through it."""
    im = Image.open(path).convert("L")
    if crop:
        im = im.crop(crop)
    w, h = im.size
    rows = max(1, int(round(cols * (h / w) * ROW_RATIO)))
    im = im.resize((cols, rows), Image.LANCZOS)
    a = np.asarray(im, dtype=float)
    return np.clip((a - BLACK) / (WHITE - BLACK), 0.0, 1.0) ** GAMMA


def backdrop(dark):
    """Which unlit cells belong to the backdrop rather than to the hood.

    Brightness cannot tell them apart — both are zero. Topology can: the
    backdrop is the darkness that reaches the edge of the frame, and the hood's
    shadow is darkness walled in by the lit hood around it. So flood the
    darkness inward from the border; whatever it fails to reach is subject.

    The flood is seeded from the top and the two sides but NOT the bottom: the
    hood's shadow runs off the bottom of the crop, and a seed there seeps
    straight up inside the hood and empties it out again. The backdrop still
    reaches a seed by going around the outside of the hood.
    """
    rows, cols = dark.shape
    seen = np.zeros_like(dark)
    q = deque()

    def push(r, c):
        if dark[r, c] and not seen[r, c]:
            seen[r, c] = True
            q.append((r, c))

    for r in range(rows):
        push(r, 0)
        push(r, cols - 1)
    for c in range(cols):
        push(0, c)

    while q:
        r, c = q.popleft()
        for dr, dc in STEPS:
            y, x = r + dr, c + dc
            if 0 <= y < rows and 0 <= x < cols:
                push(y, x)
    return seen


def depth_from_wall(enclosed, dark):
    """Cells of distance from the lit wall, across the enclosed shadow."""
    rows, cols = enclosed.shape
    dist = np.full(enclosed.shape, np.inf)
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if not enclosed[r, c]:
                continue
            for dr, dc in STEPS:                 # touching anything lit,
                y, x = r + dr, c + dc            # or running off the frame
                if not (0 <= y < rows and 0 <= x < cols) or not dark[y, x]:
                    dist[r, c] = 1.0
                    q.append((r, c))
                    break
    while q:
        r, c = q.popleft()
        for dr, dc in STEPS:
            y, x = r + dr, c + dc
            if (0 <= y < rows and 0 <= x < cols and enclosed[y, x]
                    and dist[y, x] > dist[r, c] + 1):
                dist[y, x] = dist[r, c] + 1
                q.append((y, x))
    return dist


def light_the_hood(a):
    """Draw the shadow the photograph does not contain, and fade the hem."""
    rows, cols = a.shape
    dark = a <= WALL
    enclosed = dark & ~backdrop(dark)

    t = np.clip(depth_from_wall(enclosed, dark) / DEPTH, 0.0, 1.0)
    shade = NEAR + (FAR - NEAR) * t
    # A deterministic jitter, not a random one: the SVG is committed, and a
    # random fill would rewrite it on every run.
    r = np.arange(rows)[:, None]
    c = np.arange(cols)[None, :]
    shade = shade + GRAIN * np.sin(r * 12.9 + c * 7.7) * 0.5

    a = np.where(enclosed, np.maximum(a, shade), a)

    y = np.linspace(0.0, 1.0, rows)[:, None]
    f = np.clip((y - FADE0) / (FADE1 - FADE0), 0.0, 1.0)
    return np.clip(a * (1.0 - f * f * (3 - 2 * f)), 0.0, 1.0)


def to_lines(a):
    n = len(RAMP)
    out = ["".join(RAMP[min(n - 1, int(v * n))] for v in row).rstrip()
           for row in a]
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


def build_svg(lines, cols=COLS):
    pad = 14
    width = int(cols * CHAR_W + pad * 2)
    height = len(lines) * LINE_H + pad * 2

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
         f'height="{height}" viewBox="0 0 {width} {height}" '
         f'font-family="{FAMILY}">',
         f'<style>.a{{fill:{FG_LIGHT}}}'
         f'@media(prefers-color-scheme:dark){{.a{{fill:{FG_DARK}}}}}</style>']

    for i, line in enumerate(lines):
        y = pad + i * LINE_H
        begin = f"{i * ROW_DELAY:.2f}s"
        end = f"{(i + 1) * ROW_DELAY:.2f}s"
        w = max(len(line), 1) * CHAR_W
        safe = (line.replace("&", "&amp;").replace("<", "&lt;")
                    .replace(">", "&gt;"))

        p.append(f'<clipPath id="c{i}"><rect x="{pad}" y="{y}" '
                 f'height="{LINE_H}" width="0">'
                 f'<animate attributeName="width" from="0" to="{w:.1f}" '
                 f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
                 f'</rect></clipPath>')
        p.append(f'<g clip-path="url(#c{i})"><text xml:space="preserve" '
                 f'x="{pad}" y="{y + 11.2:.1f}" class="a" '
                 f'font-size="{FONT_SIZE}">{safe}</text></g>')
        # the cursor: a small block riding the wipe edge, gone once the row lands
        p.append(f'<rect y="{y + 1}" width="6" height="12" class="a" '
                 f'opacity="0">'
                 f'<animate attributeName="x" from="{pad}" to="{pad + w:.1f}" '
                 f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
                 f'<set attributeName="opacity" to="0.8" begin="{begin}"/>'
                 f'<set attributeName="opacity" to="0" begin="{end}"/></rect>')

    p.append("</svg>")
    return "".join(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("photo")
    ap.add_argument("out", nargs="?", default="ascii.svg")
    ap.add_argument("--crop", help="left,top,right,bottom, applied first; "
                                   "defaults to the crop for the source photo")
    ap.add_argument("--cols", type=int, default=COLS)
    ap.add_argument("--preview", action="store_true",
                    help="print the ASCII to the terminal as well")
    args = ap.parse_args()

    crop = CROP
    if args.crop:
        parts = [int(v) for v in args.crop.split(",")]
        if len(parts) != 4:
            sys.exit("--crop needs four numbers: left,top,right,bottom")
        crop = tuple(parts)

    lines = to_lines(light_the_hood(sample(args.photo, args.cols, crop)))
    if args.preview:
        print("\n".join(lines))

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(build_svg(lines, cols=args.cols))
    print(f"wrote {args.out} — {len(lines)} rows, {args.cols} columns")
    print("next: python3 scripts/embed_portrait_font.py")


if __name__ == "__main__":
    main()
