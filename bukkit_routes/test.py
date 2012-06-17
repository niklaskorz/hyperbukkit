def init(bottle, webapp):
    @webapp.get("/test")
    def test():
        return "Hello World"
