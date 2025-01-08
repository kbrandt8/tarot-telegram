from PIL import Image


class TarotImage:
    def __init__(self, reading):
        self.reading = reading
        self.card_size = (100, 175)
        self.img_size = (500, 300)

    def create_image(self):
        # Tarot image settings depend on the reading type
        image_path = "tarot.jpg"
        padding = 20 if len(self.reading) == 4 else 50
        box_x = padding
        box_y = 63

        # Create the blank background
        image = Image.new("RGB", self.img_size, "#fff")
        for card in self.reading:
            card_image = self.create_card(card)
            image.paste(card_image, (box_x, box_y))
            box_x += self.card_size[0] + padding
        image.save(image_path)

    def create_card(self, card):
        card_image = Image.open(card['url'])
        card_image.thumbnail(self.card_size)
        # Check is card is reversed
        if card.get('is_reversed'):
            card_image = card_image.transpose(Image.Transpose.ROTATE_180)
        return card_image
