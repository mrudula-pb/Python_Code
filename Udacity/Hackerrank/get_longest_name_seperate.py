


names = ['Rhoda Hajduk', 'Armanda Pilling', 'Lahoma Mondragon', 'Angle Rase', 'Dave Cudd', 'Dawna Estey', 'Jone Jiron', 'Karina Vandyne', 'Calista Overbay', 'Cherise Retana', 'Pearly Breece', 'Lashanda Demoura', 'Jannie Hickey', 'Tommie Leung', 'Bong Humbertson', 'Clifton Nees', 'Maxwell Coupe', 'Maryam Lyons', 'Vasiliki Stonge', 'Danita Vallance', 'Trisha Belin', 'Salena Dulmage', 'Kellie Acord', 'Rogelio Ponds', 'Sergio Cockrill', 'Elidia Grote', 'Dalia Forth', 'Delaine Creamer', 'Chu Nelson', 'Jenell Henson', 'Serina Watkin', 'Hellen Farley', 'Clarita Jetter', 'Candra Barros', 'Maren Plouffe', 'Tanesha Finkbeiner', 'Mi Vanpelt', 'Leonore Cushman', 'Dwain Mccotter', 'Usha Lurry', 'Alphonse Bellomy', 'Deadra Bisceglia', 'Josefine Montijo', 'Danyel Zeng', 'Cristi Graff', 'Brittanie Talamantes', 'Carolina Powel', 'Voncile Borey', 'Octavio Trumbull', 'Ruth Boxer']

def seperate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def get_longest(namelist):
    value = seperate_names(names)
    full_names = (name.strip() for name in value)
    lengths = ((name, len(name)) for name in full_names)
    longest = max(lengths, key=lambda x: x[1])
    return longest


values = get_longest('names.txt')
print(values)

#full_names = (name.strip() for name in open('names.txt'))
#print(list(full_names))