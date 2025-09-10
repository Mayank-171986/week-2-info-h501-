import numpy as np


# update/add code below ...
"""
This funtion will calculate the number of ways one can make change for a given amount of cents `n` 
in the combination of nickels and pennies
Parameters:
 n: cents for which need to find out the combination nikels and pennies
Returns:
 This fuction will return the number of ways to yield `n` cents using only pennies and nickels.
"""
#This function yeild the numbers of pennis and nickels 
def combination_of_change(n):
   # find out possible combinations of nickels and pennies  
    for nickels in range(n//5, -1, -1):
        pennies = n-(5 * nickels)
        yield(pennies, nickels)
def ways(n):
    # find out count of the all possible change combination
    number_of_ways = len(list(combination_of_change(n)))
    return number_of_ways


"""
This funtion will list the name of student with the lowest test score.
Parameters:
 names: name of the the students: numpy array
 scores: corrsponding student's score: numpy array

Returns:
 This fuction will return name of the student with the lowest test score

"""
def lowest_score(names, scores):
    names = np.array(names)
    scores = np.array(scores)
    #reveal the index of the lowest score via np.argmin() 
    lowest_result_index = np.unravel_index(np.argmin(scores), scores.shape)

    #return the name of the student corresponding to the lowest_result_index with score 
    return names[lowest_result_index], scores[lowest_result_index]




"""
This funtion will list the names of students in *descending* order of test score.
Parameters:
 names: name of the the students: numpy array
 scores: corrsponding student's score: numpy array

Returns:
 This fuction will return the students list with score in descending order of test score

"""
def sort_names(names, scores):

    names = np.array(names)
    scores = np.array(scores)

    #Sort the indices in desending order of scores
    score_sort_index = np.argsort(scores)[::-1]

    #sorting the score based on sorted index
    sorted_scores = scores[score_sort_index]

    #sorting the names based on sorted index
    sorted_names = names[score_sort_index]

    #creating 2d array with name and corresponding score
    return list(zip(sorted_names.tolist(), sorted_scores.tolist()))

