from django import template

register = template.Library()


@register.filter
def get_avg_rating(product):
    total_reviews = 0
    total_rating = 0
    for review in product.productreview_set.all():
        total_rating += review.rating
        total_reviews += 1
    if total_reviews == 0:
        return 0
    else:
        avg_rating = int(round(float(float(total_rating)/float(total_reviews))/5*100, -1))
        return avg_rating


# function to covert scores out of 5 to multiples of 10 to work with stars css
@register.filter
def convert_score_for_stars(review):
    return (review * 2) * 10



