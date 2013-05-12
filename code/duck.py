class Duck(object):
    def walk(self):
        pass

    def quack(self):
        pass


def quack(duck):
    if isinstance(duck, Duck):
        duck.quack()


def quack(duck):
    if hasattr(duck, "quack"):
        duck.quack()
