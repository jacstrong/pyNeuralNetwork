import sys
import random

class node:
    __node_weight = 0
    __connection_weight_list =[]


    def __init__(self, nextLayerNumber, isBias):
        if isBias == 0 :
            self.__node_weight = random.uniform(-1.0, 1.0)
            for i in range(0,nextLayerNumber) :
                self.__connection_weight_list.append(random.randint(-1, 1))
        else :
            self.__node_weight = 1.0
            for i in range(0,nextLayerNumber) :
                self.__connection_weight_list.append(1.0)

class neural_network:
    __number_inputs = 0
    __number_hidden_nodes = 0
    __number_outputs = 0
    __input_nodes = []
    __hidden_nodes = []
    __output_nodes = []

    def __init__(self, numInputs, numHiddenNodes, numOutputs):
        self.__number_inputs = numInputs
        self.__number_hidden_nodes = numHiddenNodes
        self.__number_outputs = numOutputs

        for i in range(0, numInputs):
            self.__input_nodes.append(node(numHiddenNodes, 0))
        self.__input_nodes.append(node(numHiddenNodes, 1))
        for j in range(0, numHiddenNodes):
            self.__hidden_nodes.append(node(numOutputs, 0))
        self.__hidden_nodes.append(node(numOutputs, 1))
        for k in range(0, numOutputs):
            self.__output_nodes.append(node(0,0))




    def get_inputs(self):
        return self.__number_inputs

    def get_hidden(self):
        return self.__number_hidden_nodes

    def get_outputs(self):
        return self.__number_outputs

    def get_layers(self):
        print(self.__input_nodes)
        print(self.__hidden_nodes)
        print(self.__output_nodes)



net = neural_network(1,2,3)

net.get_layers()