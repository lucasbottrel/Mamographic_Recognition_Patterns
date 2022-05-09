from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(3, 1)

ds.addSample((1, 2, 2), (1))
ds.addSample((5, 6, 6), (2))
ds.addSample((8, 9, 9), (3))

nn = buildNetwork(3, 6, 1, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in xrange(2000):
    trainer.train()
    
result = nn.activate(1,2,1)

print(str(result))
    