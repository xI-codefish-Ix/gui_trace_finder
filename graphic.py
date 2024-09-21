import matplotlib.pyplot as plt
import numpy as np
import math
import os, shutil


class Get_trace:
    g = 9.8
    counter = 0
    def __init__(self, speed, angle):
        self.speed = speed
        self.angle = angle
        self.rad_angle = (math.pi*angle)/180
    
    def graph_init(self):
        Get_trace.counter+=1
        
        fig, ax = plt.subplots()
        
        ax.set_title(f'Траектория тела V0 = {self.speed} м/с a = {self.angle}`')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        l = int(self.speed**2 * math.sin(2*self.rad_angle)/self.g)
        h = int(self.speed**2 * (math.sin(self.rad_angle))**2/(2 * self.g))
        
        
        
        x = np.linspace(0, l+5, 100)
        t = x/(math.cos(self.rad_angle)*self.speed)
        y = self.speed*math.sin(self.rad_angle)*t - (self.g*t**2)/2
        
        
        ax.plot(x, y)
        plt.ylim(0, h+5)
        plt.xlim(0, l+5)
        plt.xticks(ticks=[x for x in range(0, l+5)], labels=[str(x) for x in range(0, l+5)])
        plt.yticks(ticks=[y for y in range(0, h+5)], labels=[str(y) for y in range(0, h+5)])
        plt.grid()
        
        
    def get_pic(self):
        if not os.path.isdir("pics"):
            os.mkdir("pics")
        
        plt.savefig(fname=f"pics/graphic{Get_trace.counter}.png")
        self.path = f"pics/graphic{Get_trace.counter}.png"

if __name__ == "__main__":    
    t1 = Get_trace(10, 90)
    t1.graph_init()
    t1.get_pic()
    plt.show()
