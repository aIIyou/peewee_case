from model.model import Pet

herb_mittens = Pet.get(Pet.name == "Mittens")
herb_mittens.delete_instance()