
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

# Inputs
plt.scatter([0,0],[1,-1],s=2500)
plt.text(0,1,"Salary\nx1",ha='center',va='center')
plt.text(0,-1,"Experience\nx2",ha='center',va='center')

# Hidden neuron
plt.scatter([3],[0],s=3000)
plt.text(3,0,"Hidden\nNeuron\nσ(z)",ha='center',va='center')

# Output neuron
plt.scatter([6],[0],s=3000)
plt.text(6,0,"Output\nNeuron\nσ(z)",ha='center',va='center')

# Connections
plt.arrow(0.4,0.8,2.1,-0.6,width=0.01,length_includes_head=True)
plt.arrow(0.4,-0.8,2.1,0.6,width=0.01,length_includes_head=True)
plt.arrow(3.5,0,2,0,width=0.01,length_includes_head=True)

# Weight labels
plt.text(1.3,0.55,"w1=0.4")
plt.text(1.3,-0.55,"w2=0.7")
plt.text(4.4,0.15,"w=0.9")


# Bias labels
plt.text(3,-0.7,"b=0.2")
plt.text(6,-0.7,"b=0.1")

plt.title("2-1-1 Neural Network Architecture")
plt.axis('off')
plt.show()