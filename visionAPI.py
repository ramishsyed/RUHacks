import os
import io
from google.cloud import vision
import pandas as pd

def image_description(path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"serviceaccount.json"

    client = vision.ImageAnnotatorClient()

    image_path = path

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # construct an image instance
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    df = pd.DataFrame(columns=['description', 'score', 'topicality'])

    for label in labels:
        df = df.append(
            dict(
                description=label.description,
                score=label.score,
                topicality=label.topicality
            ), ignore_index=True)
    return df.description
