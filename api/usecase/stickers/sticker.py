from models import stickers


def get_sticker():
    try:
        stickers_data = stickers.get_trending_sticker()
        sticker_list_info = []
        for sticker in stickers_data:
            sticker_dict = {}
            sticker_dict['name'] = sticker.name
            sticker_dict['image_url'] = sticker.image_url
            sticker_list_info.append(sticker_dict)

        return sticker_list_info
    except Exception as e:
        print(e)
        return None