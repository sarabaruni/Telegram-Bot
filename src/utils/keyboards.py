from telebot import types

def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """
    create a keyboard from a list of keys.

    Example:
        keys = ['a', 'b', 'c', 'd']
    """
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
    )
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)

    return markup