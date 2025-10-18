class Card:
    def __init__(self, mode, main_class):
        Mod=0
        """
        0=front+back
        1=front+back and back+front
        2=front+back,middle and back+front,middle and middle=
        
        """
        match mode:
            case 0:
                self.Mod=0
            case 1:
                self.Mod=1
            case 2:
                self.Mod=2
            case _:
                self.Mod=0








        day=main_class.global_day