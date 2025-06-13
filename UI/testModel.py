from database.DAO import DAO
from model.model import Model

model = Model()

obj = model.allExhibitions()

model.buildGraph()

print(model.getNumEdges())
print(model.getNumNodes())

model.getInfoConnessa(1234)