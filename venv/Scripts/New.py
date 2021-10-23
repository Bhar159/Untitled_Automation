import matplotlib.pyplot as plt
from random import choice
class Randomwalk:
    def __init__(self,num_point=5000):
        self.num_point=num_point
        self.x_value=[0]
        self.y_value=[0]

    def fill_walk(self):
        while len(self.x_value) < self.num_point:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_value[0]+x_step
            next_y=self.y_value[0]+y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

while True:
    rw=Randomwalk()
    rw.fill_walk()
    point=list(range(rw.num_point))
    plt.scatter(rw.x_value, rw.y_value,c=point,cmap=plt.cm.Reds, s=2)
    #plt.plot(rw.x_value,rw.y_value,linewidth=2)
    plt.show()
    keep_running =input("Do you want to run? (Y/N)")

    if keep_running=='n'or keep_running=='N':
     break







