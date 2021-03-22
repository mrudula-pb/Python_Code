# add member(s) in a set.

class add_members:
    def add_members(self):
        dataEngineers = {'Python', 'Java', 'C', 'R', 'Flask'}
        dataScientists = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

        # add takes only ONE value as argument, argument take strings and tuples which are ordered but not lists
        dataEngineers.add(('AWS', 9))
        print(dataEngineers)

        dataScientists.add(9)
        print(dataScientists)

solution = add_members()
solution.add_members()