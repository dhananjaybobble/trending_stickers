from api.usecase.stickers import sticker


def get_trending_stickers():
    sticker_data = sticker.get_sticker()

    return {
                "data": sticker_data,
                "status": "success",
            }, 200
