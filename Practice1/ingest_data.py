import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice1.settings')

import django
django.setup()

## Ingesting fake data
from first_app import models
import random
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','games']


def add_topic():
    t = models.Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def ingest(n=5):
    for entry in range(n):
        topic = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = models.Webpage.objects.get_or_create(
            topic=topic, 
            url=fake_url,
            name=fake_name
        )[0]
        print(fake_url)
        webpg.save()

        acessRec = models.AcessRecords.objects.get_or_create(
            name=webpg,
            date=fake_date
        )[0]
        acessRec.save()


if __name__ == '__main__':
    print("Ingesting Data...")
    ingest(20)





