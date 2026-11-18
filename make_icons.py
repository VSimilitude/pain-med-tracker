#!/usr/bin/env python3
"""Generate the PWA / apple-touch icons for Pain Med Log.
Draws a tilted two-tone capsule on the app's blue background. Rendered at 4x
and downsampled with LANCZOS for smooth edges. No external assets."""
from PIL import Image, ImageDraw

BLUE = (59, 91, 138, 255)     # --tyl   #3B5B8A
CREAM = (255, 253, 248, 255)  # --card  #FFFDF8
RUST = (224, 140, 100, 255)   # lighter --ibu, readable on blue
SS = 4  # supersample factor


def draw_pill(size):
    C = size * SS
    L, T = 0.60 * C, 0.26 * C          # capsule length / thickness
    pill = Image.new("RGBA", (C, C), (0, 0, 0, 0))
    d = ImageDraw.Draw(pill)
    x0, y0 = (C - L) / 2, (C - T) / 2
    d.rounded_rectangle([x0, y0, x0 + L, y0 + T], radius=T / 2, fill=CREAM)
    # colour the right half: draw a rust capsule, then keep only its right side
    half = Image.new("RGBA", (C, C), (0, 0, 0, 0))
    ImageDraw.Draw(half).rounded_rectangle([x0, y0, x0 + L, y0 + T], radius=T / 2, fill=RUST)
    half.paste((0, 0, 0, 0), [0, 0, C // 2, C])
    pill.alpha_composite(half)
    pill = pill.rotate(40, resample=Image.BICUBIC)

    img = Image.new("RGBA", (C, C), BLUE)
    img.alpha_composite(pill)
    return img.resize((size, size), Image.LANCZOS)


for size, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    draw_pill(size).save(name)
    print("wrote", name, f"({size}x{size})")
