
class remove_item:
    def remove_item(self):
        dataEngineers = {'Python', 'Java', 'C', 'R', 'Flask'}
        dataScientists = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

        print(dataScientists)
        print(dataEngineers)

        # remove one item at a time
        dataEngineers.remove('Python')
        print(dataEngineers)

        # program to remove an item from a set if it is present in the set.
        item = 'Flask'
        if item in dataEngineers:
            dataEngineers.remove(item)

        print(dataEngineers)



solution = remove_item()
solution.remove_item()