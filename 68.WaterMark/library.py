from PIL import Image

WTM_PADDING_FACTOR = 1 / 30


def add_wtm(wtm: Image.Image, img: Image.Image, wtm_options: dict) -> Image.Image:
    # WTM resize
    new_wtm_width = int(wtm_options['resize_factor'] * img.width)
    # - WTM height relative to the new width
    coef = new_wtm_width / wtm.width
    new_wtm_height = int(wtm.height * coef)
    new_wtm = wtm.resize((new_wtm_width, new_wtm_height))

    # WTM position
    wtm_position = coord_wtm(new_wtm, img, wtm_options)

    # WTM opacity
    opacity_wtm(new_wtm, wtm_options)

    # Pasting WTM onto Image
    new_img = img.copy()
    new_img.paste(new_wtm, wtm_position, new_wtm)
    return new_img


def coord_wtm(resized_wtm: Image.Image, img: Image.Image, wtm_options: dict) -> tuple:
    position = wtm_options['position']
    padding = int(img.width // (1 / WTM_PADDING_FACTOR))
    if position == "Top Left":
        x_coord = padding
        y_coord = padding
    elif position == "Center":
        x_coord = int(img.width / 2 - resized_wtm.width / 2)
        y_coord = int(img.height / 2 - resized_wtm.height / 2)
    elif position == 'Bottom Right':
        x_coord = int(img.width - padding - resized_wtm.width)
        y_coord = int(img.height - padding - resized_wtm.height)
    elif position == 'Top Right':
        x_coord = int(img.width - padding - resized_wtm.width)
        y_coord = padding
    else:
        x_coord = padding
        y_coord = int(img.height - padding - resized_wtm.height)
    return x_coord, y_coord


def opacity_wtm(new_wtm: Image.Image, wtm_options: dict) -> None:
    opacity_level = int(wtm_options['opacity'] * 255)

    alpha = new_wtm.getchannel('A')
    # Filtering the transparent background and the opaque
    new_alpha = alpha.point(lambda i: opacity_level if i > 0 else 0)

    new_wtm.putalpha(new_alpha)
