CATEGORIES_ATTRIBUTE = 'categories'

def categories_histogram(categories_list):
    return dict((x, categories_list.count(x)) for x in categories_list)

def aggregate_categories(businesses):
    result = []
    for business in businesses:
        result += business[CATEGORIES_ATTRIBUTE]
    return result

