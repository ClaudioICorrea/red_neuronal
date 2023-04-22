import numpy as np
import math as math 

#n = 3 # numero de salidas
#m = 5 # numero de entradas

red = [3,3,3]
output_ex = [3,3,3]


#omega= weigths.dot(input_) - bias # pesos* entradas - sesgos 

def sigmoide(t):
    s = []
    for i in t :
        s.append(pow(1+math.exp(-i), -1))
    return s


def dsigmoide(t):
    return sigmoide(t)*(np.ones(len(t))-sigmoide(t))
    

class layer:
    def __init__(self, n, input):
        self.a_i = input
        self.input = input # entradas
        self.weights = np.random.rand(n,len(self.input)) # peso
        self.bias = np.random.rand(n) # sesgos 
    def dprint(self):
        print('a_i:',self.a_i ,' input: ',self.input,'\n','weigths:','\n',self.weights,'\n','bias:',self.bias)
        return   

class network:
    def __init__(self, neuron_for_layer, input,output_ex):
        self.output_ex = np.array(output_ex)
        self.input = input
        self.neuron_for_layer = neuron_for_layer
        self.layers = []
        for t in range(0,len(self.neuron_for_layer)-1):
            #print(self.neuron_for_layer[t+1])
            if not t == 0: 
                self.layers.append(layer(self.neuron_for_layer[t+1],self.layers[t-1].bias))
            else:
                self.layers.append(layer(self.neuron_for_layer[t+1],self.input))

    def sprint(self):
        for i in range(0,len(self.layers)):
            print('capa_',i,'----------')
            self.layers[i].dprint()
    def run(self):
        for i in range(0,len(self.layers)):
            if not i == 0 : 
                self.layers[i].a_i = np.add(self.layers[i-1].weights.dot(self.layers[i-1].input),self.layers[i-1].bias)
                self.layers[i].input =sigmoide(self.layers[i].a_i)
            else:
                print('luke es bonito ')
    def learn(self):
        C=0
        for i in reversed(range(0,len(self.layers))):
            if not i == 0 :
                C= 2*(self.layers[i].a_i-self.output_ex)
                print('C es :',C,'------>',i)
            else :
                print('C:',np.multiply(np.multiply(self.layers[i+1].weights, dsigmoide(self.layers[i+1].a_i)),C),'------>',i)
                #print('C es :',C)
        # error: C = sum_j=0^nl (a_j^(l) - y_i)^2 ,  yi <- vector de valores esperados
        # where a_j^(l) := sigmoide(z_j^(l)) ,  z_j := sum_i^(nl-1 w_ij)
        return ''





input_ = np.random.rand(5) # sesgos 
network_1=network(red, input_, output_ex)
network_1.run()
network_1.sprint()
print('-----------Etapa-de-aprendizaje----------')
network_1.learn()
#print(omega) 