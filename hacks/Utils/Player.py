from system.misc import pixel

class Player:
    @staticmethod
    def hp():
        cc = 448; pot2 = 506
        try:
                for _ in range(10):
                    cc += 16
                    c = pixel(cc, 603, 620, 620, 235, 0, 16)
                    # print(c)
                    if c:
                        print(f"hp slot {_} is healthy!")
                print(f"Player has {_} hp ❤")
        except AttributeError:
            pass

    @staticmethod
    def protect():
        g = 0;
        f = 0;
        try:
            for __ in range(10):
              g += 16
              h = pixel(g)
              if h:
                f += 1
            return f
        except AttributeError:
            pass        