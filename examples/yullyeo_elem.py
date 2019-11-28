from stemfont.tools import attributetools as at, iterfont
from fontParts.world import CurrentFont, OpenFont

def _is_inside_point(glyph, point):
    for contour in glyph.contours:
        if contour.pointInside(point.position):
            if contour == point.contour:
                continue
            return True
    return False

def add_elem_attr(glyph):
    for contour in glyph.contours:
        is_stem = True
        for point in contour.points:
            if point.type == 'offcurve':
                continue
            if _is_inside_point(glyph, point):
                is_stem = False
                break
        if is_stem:
            at.add_attr(contour.points[0], 'elem', 'stem')
        else:
            at.add_attr(contour.points[0], 'elem', 'branch')

def need_elem(glyph):
    return not glyph.name.startswith('uni') and glyph.name.endswith('V')

if __name__ == '__main__':
    iterfont.glyph_generator(CurrentFont(), add_elem_attr, add_elem_attr=need_elem)