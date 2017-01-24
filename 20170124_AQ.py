
class Question:
    def ask(self):
        print self.text
        if int(raw_input('0 or 1')):
            if not self.yes:
                raise loose(self, True)
            self.yes.ask()
        else:
            if not self.no:
                raise loose(self, False)
            self.no.ask()


class Question:
    def ask(self):
        print self.text
        if int(raw_input('0 or 1')):
            if not self.yes:
                raise loose(self, True)
            self.yes.ask()
        else:
            if not self.no:
                raise loose(self, False)
            self.no.ask()