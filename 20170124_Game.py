
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


class Answer:
    def ask(self):
        print self.text
        if int(raw_input('0 or 1')):
           raise win(self)
        else:
            if not self.no:
                raise loose(self, False)
            self.no.ask()


root = 'ask question'
try:
    root.ask()
except loose as ans:
    print ans.res.text
    # ...
    # ...
except win as ans:
    print ans.res.text