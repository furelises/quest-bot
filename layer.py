from btn import Btn
import random

images_path = "./i"


class Layer:
    def __init__(self, id: str, title: str, desc: str, pictures: [str]):
        self.id = id
        self.title = title
        self.desc = desc
        self.pictures = list(map(lambda p: f"{images_path}/{p}", pictures))
        self.sub_layers = []

    def add_sub(self, sublayer: []):
        self.sub_layers.extend(sublayer)

    def to_button(self) -> Btn:
        return Btn(self.title, self.id)

    def is_last(self):
        return len(self.sub_layers) == 0

    def get_sub_buttons(self) -> [Btn]:
        return list(map(lambda l: l.to_button(), self.sub_layers))

    def get_picture(self):
        picture_rnd = random.choice(self.pictures)
        return open(picture_rnd, 'rb')


def find_layer_from(id: str, layer: Layer) -> Layer:
    if layer.id == id:
        return layer
    for l in layer.sub_layers:
        ll = find_layer_from(id, l)
        if ll is not None:
            return ll
