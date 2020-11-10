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


class GridsAndHexesTypeError(GridsAndHexesException):
    """TODO"""
    pass


def grid(filename=None, format='png', cols=20, rows=80, width=1, height=1, unit='in',
         resolution=72, background='white', minorStyle='solid', minorThickness=1, minorColor='black',
         majorInterval=None, majorHorizontalInterval=None, majorVerticalInterval=None,
         majorStyle=None, majorThickness=None, majorColor=None):

    # Check the `filename` argument's type and value:
    if not isinstance(filename, str) and filename is not None:
        raise GridsAndHexesTypeError("filename arg must be a str or None, not " + type(filename).__qualname__)
    if filename == '':
        raise GridsAndHexesValueError("filename arg cannot be a blank string")

    # Check the `format` argument's type and value:
    if not isinstance(format, str):
        raise GridsAndHexesTypeError("format arg must be a str, not " + type(format).__qualname__)
    format = format.lower()
    if format not in ('png', 'pdf'):
        raise GridsAndHexesValueError("format arg must be a string of either 'png' or 'pdf'")

    # Check the `cols`, `rows`, `width`, `height`, and `resolution` arguments' types and values:
    if majorThickness is None:
        majorThickness = minorThickness  # majorThickness "inherits" minorThickness
    for var, varName in ((cols, 'cols'), (rows, 'rows'), (width, 'width'), (height, 'height'), (resolution, 'resolution'), (minorThickness, 'minorThickness'), (majorThickness, 'majorThickness')):
        if not isinstance(var, int):
            raise GridsAndHexesTypeError(varName + " arg must be an int, not a " + type(var).__qualname__)
        if var < 1:
            raise GridsAndHexesValueError(varName + " arg must be a positive, nonzero integer")

    # Check the `unit` argument's type and value:
    if not isinstance(unit, str):
        raise GridsAndHexesTypeError("unit arg must be a str, not " + type(unit).__qualname__)
    unit = unit.lower()
    if unit not in ('in', 'cm'):
        raise GridsAndHexesValueError("unit arg must be either 'in' or 'cm'")

    # Check the `background`, `minorColor`, and `majorColor` arguments' types and values:
    if majorColor is None:
        majorColor = minorColor  # majorColor "inherits" minorColor
    for var, varName in ((background, 'background'), (minorColor, 'minorColor'), (majorColor, 'majorColor')):
        if not isinstance(var, str):
            raise GridsAndHexesTypeError(varName + " arg must be a str, not " + type(var).__qualname__)
        try:
            ImageColor.getrgb(var)
        except ValueError:
            raise GridsAndHexesValueError(varName + " arg is an unknown color")

    # Check the `minorStyle`, `borderStyle`, and `interiorStyle` arguments' types and values:
    if majorStyle is None:
        majorStyle = minorStyle  # majorStyle "inherits" minorStyle
    for var, varName in ((minorStyle, 'minorStyle'), (majorStyle, 'majorStyle')):
        if not isinstance(var, str):
            raise GridsAndHexesTypeError(varName + " arg must be a str, not " + type(var).__qualname__)

    minorStyle = minorStyle.lower()
    majorStyle = majorStyle.lower()

    for var, varName in ((minorStyle, 'minorStyle'), (majorStyle, 'majorStyle')):
        if var not in ('dotted', 'solid', 'double', 'dashed'):
            raise GridsAndHexesValueError(varName + " arg must be 'dotted', 'solid', 'double', or 'dashed'")

    # Check the `majorInterval`, `majorHorizontalInterval`, and `majorVerticalInterval` arguments' types and values:
    if majorInterval is not None:
        majorHorizontalInterval = majorInterval
        majorVerticalInterval = majorInterval
    # LEFT OFF


    # Give the filename a default name if `filename` is `None`:
    if filename is None:
        filename = 'grid%sx%s.%s' % (cols, rows, format)

    boxWidthInPixels = width * resolution
    boxHeightInPixels = height * resolution

    # Create the image object that we'll draw the grid on:
    totalImageWidth = cols * boxWidthInPixels
    totalImageHeight = rows * boxHeightInPixels
    im = Image.new('RGBA', (totalImageWidth, totalImageHeight), background)

    # Draw the grid lines onto the image object:
    draw = ImageDraw.Draw(im)
    for x in range(0, totalImageWidth, boxWidthInPixels):
        for y in range(0, totalImageHeight, boxHeightInPixels):
            # Draw the left side of the box:
            draw.rectangle((x, y, x + minorThickness - 1, y + (boxHeightInPixels) - 1), fill=minorColor)
            # Draw the top side of the box:
            draw.rectangle((x, y, x + (boxWidthInPixels) - 1, y + minorThickness - 1), fill=minorColor)

    # Create the dpi metadata for the image:
    if unit == 'in':
        dpi = (resolution, resolution)
    elif unit == 'cm':
        dpi = (resolution * CM_PER_INCH, resolution * CM_PER_INCH)

    im.save(filename, dpi=(resolution, resolution))
