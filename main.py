import numpy as np
import math as math 

#n = 3 # numero de salidas
#m = 5 # numero de entradas

red = [5,7,4,3]


#omega= weigths.dot(input_) - bias # pesos* entradas - sesgos 

def sigmoide(t):
    s = []
    for i in t :
        s.append(pow(1+math.exp(-i), -1))
    return s

class capa:
    def __init__(self, n, input):
        self.input = input # entradas
        self.weights = np.random.rand(n,len(self.input)) # peso
        self.bias = np.random.rand(n) # sesgos 
    def dprint(self):
        print(' input: ',self.input,'\n','weigths:','\n',self.weights,'\n','bias:',self.bias)
        return   

class network:
    def __init__(self, neuron_for_layer, input):
        self.input = input
        self.neuron_for_layer = neuron_for_layer
        self.layers = []
        for t in range(0,len(self.neuron_for_layer)-1):
            #print(self.neuron_for_layer[t+1])
            if not t == 0: 
                self.layers.append(capa(self.neuron_for_layer[t+1],self.layers[t-1].bias))
            else:
                self.layers.append(capa(self.neuron_for_layer[t+1],self.input))

    def sprint(self):
        for i in range(0,len(self.layers)):
            print('capa_',i,'----------')
            self.layers[i].dprint()
    def run(self):
        for i in range(0,len(self.layers)):
            if not i == 0 : 
                self.layers[i].input = sigmoide(np.add(self.layers[i-1].weights.dot(self.layers[i-1].input),self.layers[i-1].bias))
            else:
                print('luke es bonito ')


input_ = np.random.rand(5) # sesgos 
network_1=network(red, input_)
network_1.run()
network_1.sprint()
#print(omega) 