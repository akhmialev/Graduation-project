class MyMixin:
    mixin_reg = "Чтобы добавить пост авторизуйтесь"

    def get_reg(self):
        return self.mixin_reg.upper()