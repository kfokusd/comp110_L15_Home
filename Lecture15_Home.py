import Lecture15 as L15
import matplotlib.pyplot as pp

dict = L15.alphabet("Lecture15_article.txt")
print(dict.items())
pp.bar(dict.keys(), dict.values())
pp.show()


#Expected Output:
#dict_items([('A', 206), ('B', 45), ('C', 81), ('D', 91), ('E', 243), ('F', 49), 
# ('G', 52), ('H', 72), ('I', 148), ('J', 9), ('K', 13), ('L', 90), ('M', 73), 
# ('N', 180), ('O', 169), ('P', 73), ('Q', 1), ('R', 143), ('S', 149), ('T', 205), 
# ('U', 48), ('V', 18), ('W', 21), ('X', 10), ('Y', 52), ('Z', 1)])