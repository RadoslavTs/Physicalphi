import datetime
from hashlib import sha256


# function to calculate the persons age
def calculateAge(dob):
    converted = datetime.datetime.strptime(dob, '%d %B %Y')
    today = datetime.date.today()
    age = today.year - converted.year - ((today.month, today.day) <
                                         (converted.month, converted.day))

    return age


# function to return the current day (for calendar purposes)
def get_today():
    today = datetime.date.today()

    return today


# function to hash a password that was provided
def get_password_hash(password):
    hash_object = sha256(password.encode())

    return str(hash_object.hexdigest())


def provide_color_scheme():
    button_color = '#91bf76'
    hover_color = '#5a8640'
    inner_frame_bg_color = '#eaf3e7'
    inner_frame_fg_color = '#eaf3e7'
    outer_frame_bg_color = '#eaf3e7'
    outer_frame_fg_color = '#eaf3e7'
    button_text_color = '#163807'
    button_disabled_color_text = '#79818b'
    entry_placeholder_color = 'gray'
    button_font = ('Nirmala UI', 13)
    menu_color = '#f4f6f8'
    entry_color = 'white'
    corner_radius = 30
    colors = {'button_color': button_color,
              'hover_color': hover_color,
              'inner_frame_bg_color': inner_frame_bg_color,
              'inner_frame_fg_color': inner_frame_fg_color,
              'outer_frame_bg_color': outer_frame_bg_color,
              'outer_frame_fg_color': outer_frame_fg_color,
              'button_text_color': button_text_color,
              'button_disabled_color_text': button_disabled_color_text,
              'corner_radius': corner_radius,
              'entry_color': entry_color,
              'entry_placeholder_color': entry_placeholder_color,
              'menu_color': menu_color,
              'text_font': button_font}
    return colors
