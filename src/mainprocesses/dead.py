class DeadMenager:
    livest = 1

    @staticmethod
    def kill():
        DeadMenager.livest = 0
        exit()

    @staticmethod
    def alive():
        return DeadMenager.livest
