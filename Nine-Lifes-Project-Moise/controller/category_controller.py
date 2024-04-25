from model.category_model import Category


def save_category(category_name, nb_of_questions):
    category = Category(category_name=category_name, nb_of_questions=nb_of_questions)
    category.save()
    return category.toJSON()


def get_all_categories():
    category = Category()
    return category.read()


def get_category_with_id(id_category):
    category = Category()
    return category.read(id_category)


def update_category(id_category, category_name, nb_of_questions):
    category = Category(id_category=id_category, category_name=category_name, nb_of_questions=nb_of_questions)
    category.save()
    return category.toJSON()


def delete_category_with_id(id_category):
    category = Category(id_category=id_category)
    category.delete()
    return category.toJSON()


def delete_all_categories():
    category = Category()
    category.delete()
    return True