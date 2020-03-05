import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer

# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db", "labels", sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db", "images", sortKey=True)

# Process Logic.
labelDataset = ParseTriple.ParseTriples('./datasets/labels_en.ttl')
imageDataset = ParseTriple.ParseTriples('./datasets/images.ttl')

for i in range(1, 1000):
    label = labelDataset.getNext()
    stemmer = Stemmer.stem(label[2])
    for x in stemmer.split(' '):
        print("category: " + label[0] + " ____________ label:" + x)
        kv_labels.putSort(x, i, label[0])

for i in range(0, 1000):
    images = imageDataset.getNextImage()
    print("category: " + images[0] + " _________ imgPath: " + images[2])
    kv_images.putSort(images[0], i, images[2])

# Close KeyValues Storages
kv_labels.close()
kv_images.close()
