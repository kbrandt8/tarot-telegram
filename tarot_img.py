from PIL import Image


class TarotImage:
    def __init__(self, reading):
        self.reading = reading
        self.reading_type = len(self.reading)
        dimensions = self.width()
        width = int(dimensions["img_width"] / len(self.reading) - 15)
        size = (width, 300)
        box = (10, 25)
        image = Image.new("RGB", (dimensions["img_width"], dimensions["img_height"]), (255, 255, 255))
        for card in self.reading:
            card_im = Image.open(card['url'])
            card_im.thumbnail(size)
            if card['is_reversed']:
                card_im = card_im.transpose(Image.Transpose.ROTATE_180)
            image.paste(card_im, box)
            box = (box[0] + width + 15, 25)
        image.save("tarot.jpg")

    def width(self):
        if self.reading_type == 3:
            return {"img_width": 500, "img_height": 300}
        elif self.reading_type == 4:
            return {"img_width": 400, "img_height": 200}
        else:
            pass
