"""
Proset has some advantages over Set/Triology.

- It's easier to explain.
- Prosets can be any number of cards (including the entire board).
- One is guaranteed a proset in 7 cards.
- The deck should end in a set.
- It's a fresher game.

Try to find a set (any number) of cards with an even number of every color.

"""

from __future__ import annotations
import math
import shutil
import subprocess
from typing import Union
from pathlib import Path

import svgwrite

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Union[Point, int]) -> Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __radd__(self, other: int) -> Point:
        return self + other

    def __neg__(self) -> Point:
        return Point(-self.x, -self.y)

    def __sub__(self, other: Union[Point, int]) -> Point:
        return self + -other

    def __rsub__(self, other: int) -> Point:
        return -self + other

    def __mul__(self, other: Union[Point, int]) -> Point:
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> Point:
        return self * other

    def __floordiv__(self, other: Point) -> Point:
        """How many times could this rectangle be tiled inside another rectangle?"""
        return Point(self.x // other.x, self.y // other.y)

    def __iter__(self) -> Iterator[int]:
        yield self.x
        yield self.y

    def __setitem__(self, index: int, val: int) -> int:
        if index == 0:
            self.x = val
        elif index == 1:
            self.y = val
        else:
            raise IndexError(index)

    def __getitem__(self, index: int) -> int:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError(index)

    def range(self) -> Iterator[Point]:
        for x in range(self.x):
            for y in range(self.y):
                yield Point(x, y)

    def count(self) -> int:
        """How many points are contained in this rectangle?"""
        return self.x * self.y

########################################
# Parameters
# Change these
########################################

golden_ratio = (1 + math.sqrt(5)) / 2
page = Point(850, 1100)
margin = 8
page_margin = 8
card_size = Point(195, int(195 * golden_ratio))
card_radius = 20
card_color = svgwrite.rgb(r=255, g=255, b=255)
card_color_alpha = 0.0 # completely transparent
card_border_color = svgwrite.rgb(r=0, g=0, b=0)
card_border_color_alpha = 0.05
card_border_width = 1
pips_on_card = Point(2, 3)
pip_radius = 20
pip_colors = {
    0: svgwrite.rgb(189, 19, 84),
    1: svgwrite.rgb(228, 108, 33),
    2: svgwrite.rgb(226, 166, 29),
    3: svgwrite.rgb(46, 163, 44),
    4: svgwrite.rgb(54, 83, 238),
    5: svgwrite.rgb(87, 32, 131),
}
output = Path("output")

########################################
# End parameters
# Don't change unless you know what you are doing
########################################

cards_on_page = (page - margin - 2 * page_margin) // (card_size + margin)
num_pages = int(math.ceil(2**pips_on_card.count() / cards_on_page.count()))

if output.exists():
    shutil.rmtree(output)
output.mkdir()

print(f"{num_pages} pages")
for page_idx in range(num_pages):
    drawing = svgwrite.drawing.Drawing(filename=output / f"page-{page_idx}.svg", size=page)

    for card_pos in cards_on_page.range():
        value = card_pos.x * cards_on_page.y + card_pos.y + page_idx * cards_on_page.count()
        card_corner = page_margin + card_pos * (card_size + margin) + margin
        if value >= 2**pips_on_card.count():
            break
        drawing.add(
            drawing.rect(
                card_corner,
                card_size,
                rx=card_radius,
                ry=card_radius,
            ).fill(
                color=card_color,
                opacity=card_color_alpha,
            ).stroke(
                color=card_border_color,
                opacity=card_border_color_alpha,
            )
        )

        for pip_pos in pips_on_card.range():
            pip_value = pip_pos.x * pips_on_card.y + pip_pos.y
            pip_set = value & (1 << pip_value)
            if pip_set:
                drawing.add(
                    drawing.circle(
                        card_corner + ((pip_pos + 1) * card_size) // (pips_on_card + 1),
                        # One 'phantom' pip at the lower extreme.
                        r=pip_radius,
                        fill=pip_colors[pip_value]
                    )
                )

    drawing.save()

for page_idx in range(num_pages):
    subprocess.run([
        "rsvg-convert", "--zoom=0.72", "--keep-aspect-ratio", "--format=pdf", f"--output={output!s}/page-{page_idx}.pdf", f"{output!s}/page-{page_idx}.svg"
    ], check=True)
subprocess.run([
    "pdftk", *[f"{output!s}/page-{page_idx}.pdf" for page_idx in range(num_pages)], "cat", "output", f"{output!s}/pages.pdf",
], check=True)
