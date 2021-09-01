"""Grids and Hexes
By Al Sweigart al@inventwithpython.com

A Python module for producing PNG and PDF files of customized graph paper."""

__version__ = '0.1.0'

from PIL import Image, ImageDraw, ImageColor

CM_PER_INCH = 2.54

class GridsAndHexesException(Exception):
    """This class represents any exceptions raised by the gridsandhexes module. If a function in this module raises
    an exception that is not GridsAndHexesException or its subclass, it's likely caused by a bug in the module."""
    pass


class GridsAndHexesValueError(GridsAndHexesException):
    """TODO"""
    pass


def grid(filename=None, cols=10, rows=10, width=40, height=40, dpi=72,
         background='white', style='solid', thickness=1, color='black',
         secondaryInterval=None, secondaryHorizontalInterval=None, secondaryVerticalInterval=None,
         secondaryStyle=None, secondaryThickness=None, secondaryColor=None):
    """TODO

    """

    # Check the `filename` argument's type and value:
    if not isinstance(filename, str) and filename is not None:
        raise GridsAndHexesValueError("filename arg must be a str or None, not " + type(filename).__qualname__)
    if filename == '':
        raise GridsAndHexesValueError("filename arg cannot be a blank string")

    # Check the `cols`, `rows`, `width`, and `height` arguments' types and values:
    if secondaryThickness is None:
        secondaryThickness = thickness  # secondaryThickness "inherits" thickness
    for var, varName in ((cols, 'cols'), (rows, 'rows'), (width, 'width'), (height, 'height'), (thickness, 'thickness'), (secondaryThickness, 'secondaryThickness')):
        if not isinstance(var, int):
            raise GridsAndHexesValueError(varName + " arg must be an int, not a " + type(var).__qualname__)
        if var < 1:
            raise GridsAndHexesValueError(varName + " arg must be a positive, nonzero integer")

    # Check the `dpi` argument's type and value:
    if not isinstance(dpi, int):
        raise GridsAndHexesValueError("dpi arg must be a int, not " + type(dpi).__qualname__)
    if dpi <= 0:
        raise GridsAndHexesValueError("dpi arg must be greater than 0")

    # The color arguments can be a color name ('black') or RGB tuple ((0, 0, 0)).
    # The background argument can be None (in which case, it's a transparent background).
    # Check the `background`, `color`, and `secondaryColor` arguments' types and values:
    if secondaryColor is None:
        secondaryColor = color  # secondaryColor "inherits" color
    for var, varName in ((background, 'background'), (color, 'color'), (secondaryColor, 'secondaryColor')):
        if not isinstance(var, (str, list, tuple)):
            if varName != 'background':  # Unlike color and secondaryColor, background can be None.
                raise GridsAndHexesValueError(varName + " arg must be a str, list, or tuple, not " + type(var).__qualname__)
            elif var is not None:
                raise GridsAndHexesValueError(varName + " arg must be a str, list, tuple, or None, not " + type(var).__qualname__)
        if isinstance(var, str):
            try:
                ImageColor.getrgb(var)
            except ValueError:
                raise GridsAndHexesValueError(varName + " arg is an unknown color")
        elif isinstance(var, (list, tuple)):
            if len(var) != 3:
                raise GridsAndHexesValueError(varName + " arg must have a length of three for the R, G, and B values")
            for i in range(3):
                if not isinstance(var[i], int) or not (0 <= var[0] <= 255):
                    raise GridsAndHexesValueError("element " + str(i) + " of " + varName + " must be an integer between 0 and 255")

    # Make sure `color` is a tuple:
    if isinstance(color, str):
        color = ImageColor.getrgb(color)
    else:
        color = tuple(color)
    # Make sure `background` is a tuple or None:
    if isinstance(background, str):
        background = ImageColor.getrgb(background)
    elif background is not None:
        background = tuple(background)
    elif background is None:
        pass # TODO how do we set this for transparent?
    # Make sure `secondaryColor` is a tuple:
    if isinstance(secondaryColor, str):
        secondaryColor = ImageColor.getrgb(secondaryColor)
    else:
        secondaryColor = tuple(secondaryColor)


    # Check the `style`, `borderStyle`, and `interiorStyle` arguments' types and values:
    if secondaryStyle is None:
        secondaryStyle = style  # secondaryStyle "inherits" style
    for var, varName in ((style, 'style'), (secondaryStyle, 'secondaryStyle')):
        if not isinstance(var, str):
            raise GridsAndHexesValueError(varName + " arg must be a str, not " + type(var).__qualname__)

    style = style.lower()
    secondaryStyle = secondaryStyle.lower()

    for var, varName in ((style, 'style'), (secondaryStyle, 'secondaryStyle')):
        if var not in ('dotted', 'solid', 'double', 'dashed'):
            raise GridsAndHexesValueError(varName + " arg must be 'dotted', 'solid', 'double', or 'dashed'")

    # Check the `secondaryInterval`, `secondaryHorizontalInterval`, and `secondaryVerticalInterval` arguments' types and values:
    if secondaryInterval is not None:
        secondaryHorizontalInterval = secondaryInterval
        secondaryVerticalInterval = secondaryInterval
    # LEFT OFF

    # Create the image object that we'll draw the grid on:
    totalImageWidth = cols * width + thickness  # The `+ thickness` is for the line at the right edge
    totalImageHeight = rows * height + thickness  # The `+ thickness` is for the line at the bottom edge
    if background is not None:
        im = Image.new('RGB', (totalImageWidth, totalImageHeight), background)
    else:
        im = Image.new('RGBA', (totalImageWidth, totalImageHeight))  # Transparent background.

    # Draw the grid lines onto the image object:
    draw = ImageDraw.Draw(im)
    for x in range(0, totalImageWidth, width):
        for y in range(0, totalImageHeight, height):
            # Draw the left side of the box:
            draw.rectangle((x, y, x + thickness - 1, y + (height) - 1), fill=color)
            # Draw the top side of the box:
            draw.rectangle((x, y, x + (width) - 1, y + thickness - 1), fill=color)

    if filename is None:
        return im
    else:
        im.save(filename, dpi=(dpi, dpi))

