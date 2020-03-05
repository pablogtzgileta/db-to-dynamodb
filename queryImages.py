import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTripe
import keyvalue.stemmer as Stemmer

# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db", "labels", sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db", "images")


# Process Logic.

def searchlabels(key):
    return kv_labels.get(key)


def searchimg(key):
    if (key):
        return kv_images.get(key)
    return


print(
    "'Academy', 'america','Academic','Angola','Astronomer','Awards','acid','Algeria','Alchemy','Astronaut', 'Autism', "
    "'Android', 'Algorithm' ")

args = ['Academy', 'america', 'Academic', 'Angola', 'Astronomer', 'Awards', 'acid', 'Algeria', 'Alchemy', 'Astronaut',
        'Autism', 'Android', 'Algorithm']

for word in args:
    stem = Stemmer.stem(word)
    category = searchlabels(stem)
    img = searchimg(category)
    if (img):
        print(stem + " : " + img)

# Close KeyValues Storages
kv_labels.close()
kv_images.close()
