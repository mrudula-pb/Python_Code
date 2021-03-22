
class sets:
    def sets(self):
        # program to create an intersection of sets.
        dataEngineers = {'Python', 'Java', 'C', 'R', 'Flask'}
        dataScientists = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

        print(dataEngineers)
        print(dataScientists)

        print(dataEngineers.intersection(dataScientists))

        # disjoint: no common elements in both sets
        # Initialize a set
        graphicDesigner = {'Illustrator', 'InDesign', 'Photoshop'}
        # These sets have elements in common so it would return False
        print(dataScientists.isdisjoint(dataEngineers))
        # These sets have no elements in common so it would return True
        print(dataScientists.isdisjoint(graphicDesigner))

        # difference
        # Difference Operation
        print(dataScientists.difference(dataEngineers))
        # Equivalent Result
        dataScientists - dataEngineers

        # symetric difference
        # Symmetric Difference Operation
        print(dataScientists.symmetric_difference(dataEngineers))
        # Equivalent Result
        print(dataScientists ^ dataEngineers)


solution = sets()
solution.sets()