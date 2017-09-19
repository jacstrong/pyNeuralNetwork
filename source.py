import sys
import random
import math

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

    def set_weight(self, input):
        self.__node_weight = input

    def get_node_weight(self):
        return self.__node_weight

    def get_connection_weight(self, index):
        return self.__connection_weight_list[index]

    def print_node(self):
        print("Node weight: %s" % self.__node_weight)


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
        self.__input_nodes.append(node(numHiddenNodes, 1)) #bias node
        for j in range(0, numHiddenNodes):
            self.__hidden_nodes.append(node(numOutputs, 0))
        self.__hidden_nodes.append(node(numOutputs, 1)) #bias node
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

    def output_print(self):
        for i in range(0, self.__number_outputs):
            print("Output %s " % (i+1), end="")
            self.__output_nodes[i].print_node()

    def input_print(self):
        for i in range(0, self.__number_inputs):
            print("Input %s " % (i+1), end="")
            self.__input_nodes[i].print_node()

    def hidden_print(self):
        for i in range(0, self.__number_hidden_nodes + 1):
            print("Hidden %s " % (i+1), end="")
            self.__hidden_nodes[i].print_node()

    def set_inputs(self, inputs):
        for i in range(0, self.__number_inputs):
            self.__input_nodes[i].set_weight(inputs[i])

    def feed_forward(self, inputs):
        self.set_inputs(inputs)
        for i in range(0, self.__number_hidden_nodes):
            for j in range(0, self.__number_inputs + 1):
                self.__hidden_nodes[i].set_weight(self.__input_nodes[j].get_node_weight() * self.__input_nodes[j].get_connection_weight(i))
            self.__hidden_nodes[i].set_weight(math.tanh(self.__hidden_nodes[i].get_node_weight()))








net = neural_network(4,2,3)

net.get_layers()

net.hidden_print()
net.input_print()

inputs = [1,2,3,4]

net.feed_forward(inputs)

net.hidden_print()
net.input_print()
