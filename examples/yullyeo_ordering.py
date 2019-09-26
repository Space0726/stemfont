""" This is example of setting attribute values in order using by Yullyeo font data.

Last modified date: 2019/09/11

Created by Seongju Woo.
"""
from stemfont import ordering as od

class YullyeoOrdering(od.Ordering):
    def __init__(self, glyph, *attributes, padding=0):
        super().__init__(glyph, *attributes, padding=padding)

    def calculate_padding(self):
        font = self.glyph.font
        if self.glyph.name.endswith('C'):
            return None
        elif self.glyph.name.endswith('V'):
            padding_glyphs = font.getGlyph(self.glyph.name[:-1] + 'C'),
        elif self.glyph.name.endswith('F'):
            padding_glyphs = font.getGlyph(self.glyph.name[:-1] + 'C'), \
                             font.getGlyph(self.glyph.name[:-1] + 'V')
        for padding_glyph in padding_glyphs:
            if od.get_min_penpair(padding_glyph) == 1:
                self.padding += od.get_max_penpair(padding_glyph)
            else:
                self.padding = od.get_max_penpair(padding_glyph)
                break


if __name__ == '__main__':
    font = CurrentFont()
    for o in font.glyphOrder:
        glyph = font.getGlyph(o)
        if glyph.name.find('uni') == -1:
            print(glyph.name)
            YullyeoOrdering(glyph, 'penPair').attributes_ordering()