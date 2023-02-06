# Generated by Django 4.1.6 on 2023-02-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("file_name", models.CharField(max_length=140)),
                ("file_url", models.CharField(max_length=999)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("apple", "Apple"),
                            ("aquarium_fish", "Aquarium Fish"),
                            ("baby", "Baby"),
                            ("bear", "Bear"),
                            ("beaver", "Beaver"),
                            ("bed", "Bed"),
                            ("bee", "Bee"),
                            ("beetle", "Beetle"),
                            ("bicycle", "Bicycle"),
                            ("bottle", "Bottle"),
                            ("bowl", "Bowl"),
                            ("boy", "Boy"),
                            ("bridge", "Bridge"),
                            ("bus", "Bus"),
                            ("butterfly", "Butterfly"),
                            ("camel", "Camel"),
                            ("can", "Can"),
                            ("castle", "Castle"),
                            ("caterpillar", "Caterpillar"),
                            ("cattle", "Cattle"),
                            ("chair", "Chair"),
                            ("chimpanzee", "Chimpanzee"),
                            ("clock", "Clock"),
                            ("cloud", "Cloud"),
                            ("cockroach", "Cockroach"),
                            ("couch", "Couch"),
                            ("cra", "Cra"),
                            ("crocodile", "Crocodile"),
                            ("cup", "Cup"),
                            ("dinosaur", "Dinosaur"),
                            ("dolphin", "Dolphin"),
                            ("elephant", "Elephant"),
                            ("flatfish", "Flatfish"),
                            ("forest", "Forest"),
                            ("fox", "Fox"),
                            ("girl", "Girl"),
                            ("hamster", "Hamster"),
                            ("house", "House"),
                            ("kangaroo", "Kangaroo"),
                            ("keyboard", "Keyboard"),
                            ("lamp", "Lamp"),
                            ("lawn_mower", "Lawn Mower"),
                            ("leopard", "Leopard"),
                            ("lion", "Lion"),
                            ("lizard", "Lizard"),
                            ("lobster", "Lobster"),
                            ("man", "Man"),
                            ("maple_tree", "Maple Tree"),
                            ("motorcycle", "Motorcycle"),
                            ("mountain", "Mountain"),
                            ("mouse", "Mouse"),
                            ("mushroom", "Mushroom"),
                            ("oak_tree", "Oak Tree"),
                            ("orange", "Orange"),
                            ("orchid", "Orchid"),
                            ("otter", "Otter"),
                            ("palm_tree", "Palm Tree"),
                            ("pear", "Pear"),
                            ("pickup_truck", "Pickup Truck"),
                            ("pine_tree", "Pine Tree"),
                            ("plain", "Plain"),
                            ("plate", "Plate"),
                            ("poppy", "Poppy"),
                            ("porcupine", "Porcupine"),
                            ("possum", "Possum"),
                            ("rabbit", "Rabbit"),
                            ("raccoon", "Raccoon"),
                            ("ray", "Ray"),
                            ("road", "Road"),
                            ("rocket", "Rocket"),
                            ("rose", "Rose"),
                            ("sea", "Sea"),
                            ("seal", "Seal"),
                            ("shark", "Shark"),
                            ("shrew", "Shrew"),
                            ("skunk", "Skunk"),
                            ("skyscraper", "Skyscraper"),
                            ("snail", "Snail"),
                            ("snake", "Snake"),
                            ("spider", "Spider"),
                            ("squirrel", "Squirrel"),
                            ("streetcar", "Streetcar"),
                            ("sunflower", "Sunflower"),
                            ("sweet_pepper", "Sweet Pepper"),
                            ("table", "Table"),
                            ("tank", "Tank"),
                            ("telephone", "Telephone"),
                            ("television", "Television"),
                            ("tiger", "Tiger"),
                            ("tractor", "Tractor"),
                            ("train", "Train"),
                            ("trout", "Trout"),
                            ("tulip", "Tulip"),
                            ("turtle", "Turtle"),
                            ("wardrobe", "Wardrobe"),
                            ("whale", "Whale"),
                            ("willow_tree", "Willow Tree"),
                            ("wolf", "Wolf"),
                            ("woman", "Woman"),
                            ("worm", "Worm"),
                        ],
                        max_length=140,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
