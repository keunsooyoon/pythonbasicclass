class Korean:
    country = "korea"

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print("domastic")
        else:
            print("abroad")

Korean.trip('korea')
Korean.trip('usa')

