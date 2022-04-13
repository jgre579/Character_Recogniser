class MainController(object):
    def __init__(self, model):
        self.model = model

    def get_image(self, index):
        return self.model.get_image(index)
