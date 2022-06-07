class MyMixin:
    mixin_reg = "Чтобы добавлять посты и комментарии авторизуйтесь"

    def get_reg(self):
        return self.mixin_reg.upper()