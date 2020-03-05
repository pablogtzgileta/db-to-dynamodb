import keyvalue.dynamostorage as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer
from botocore.exceptions import ClientError

# Make connections to KeyValue
kv_labels = KeyValue.DynamoDB("labels")
kv_images = KeyValue.DynamoDB("images")

try:
    # Process Logic.
    print("-------------------------------------------")
    labelsDataset = ParseTriple.ParseTriples('./datasets/labels_en.ttl')

    for i in range(1, 1000):
        word = labelsDataset.getNext()
        category = word[0]
        label = word[2]
        steam = Stemmer.stem(label)
        for x in steam.split(' '):
            print("category: " + category + " ____________ labe:" + x)
            kv_labels.put(x, len(x), category)

    print("-------------------------------------------")

    print("-------------------------------------------")
    imagesDataset = ParseTriple.ParseTriples('./datasets/images.ttl')
    for i in range(0, 2000):
        img = imagesDataset.getNextImage()
        category = img[0]
        imgPath = img[2]
        print("category: " + category + " _________ imgPath: " + imgPath)
        kv_images.put(category, len(category), imgPath)
except ClientError as e:
    print(e.response['Error'])
    # kv_labels.close()
    # kv_images.close()

# Close KeyValues Storages
