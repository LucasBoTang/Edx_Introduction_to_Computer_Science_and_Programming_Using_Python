class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)