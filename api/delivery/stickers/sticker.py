from api.usecase.stickers import sticker


def get_trending_stickers():
    sticker_data = sticker.get_sticker()

    for stickers in sticker_data:
        if len(stickers['name']) == 0 or len(stickers['image_url']) == 0:
            return {
                "status": "error",
            }, 404

    return {
                "status": "success",
            }, 200
