"""
You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list with the first element equal to the name of the ingredient and all of the other elements equal to the names of dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically. The result array should be sorted lexicographically by the names of the ingredients in its elements.

Example

For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
"""
from operator import itemgetter

def groupingDishes(dishes):
    dishDict = {}
    allIngredients = []
    for dish in dishes:
        dishDict[dish[0]] = []
        for ingredient in range(1, len(dish)):
            dishDict[dish[0]].append(dish[ingredient])
            if dish[ingredient] not in allIngredients:
                allIngredients.append(dish[ingredient])
    
    finalList = []
    for ingredient in allIngredients:
        finalIngredients = []
        finalIngredients.append(ingredient)
        for dish in dishDict:
            if ingredient in dishDict[dish]:
                finalIngredients.append(dish)
        
        if len(finalIngredients) > 2:
            finalList.append(finalIngredients)
            
    print(finalList)
    finalList = sorted(finalList, key = itemgetter(0))
    
    for lst in finalList:
        lst = sorted(lst, key = itemgetter(0))
               
    return finalList