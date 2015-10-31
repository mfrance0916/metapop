#!/usr/bin/python
import random
import numpy as np
import os
import math

#function for rounding up to 10 always, not proper round just always round up 
def roundup(x):

    return int(math.ceil(x / 10.0)) * 10



class Population(object):
    
    ## defines the following parameters that are needed for the simulation
    ## pop_dens = density of bacterial population in cells/ml
    ## n_generations = numberical number of generations to run the simulation for
    ## gd_mut_rate = growth dependent mutation rate
    ## gi_mut_rate = growth independent mutation rate
    ## volume = volume of the chemostat in mL
    ## flow_rate = rate of flow of new media into the chemostat 
    ## gd_ab_mut_rate = rate of mutation towards antibiotic resistance dependent on growth
    ## gi_ab_mut_rate = rate of mutation towards antibiotic resistance independent of growth
    ## num_met = Number of metapopulations
    ## grid_width = grid width

    def __init__(self, pop_dens, n_generations, gd_mut_rate, gi_mut_rate, volume, flow_rate, gd_ab_mut_rate, gi_ab_mut_rate,num_met,grid_width):
        self.pop_dens = pop_dens
        self. n_generations = n_generations
        self.gd_mut_rate = gd_mut_rate
        self.gi_mut_rate = gi_mut_rate
        self.volume = volume
        self.flow_rate = flow_rate
        self.gd_ab_mut_rate = gd_ab_mut_rate
        self.gi_ab_mut_rate = gi_ab_mut_rate
        self.num_met = num_met
        self.grid_width = grid_width

    def initialize(self):

        #calculate population size
        self.pop_size = self.pop_dens*self.volume

        #calculate population size within each subpopulation

        self.subpop_size = roundup(self.pop_size/self.num_met)

        print self.subpop_size



exp_evol = Population(50000000,1000,0.0006,0.00015,10,1.5,0.00000012,0.0000000055,100,5)

exp_evol.initialize()

