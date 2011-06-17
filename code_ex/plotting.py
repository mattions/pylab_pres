# plotting.py
# This use the console style.
# Do not use this stile on a program.

x = linspace(0,10)
# Plotting the exp
plot(x, exp(-x), label='exp')
# Plotting the sin
plot(x, sin(x), label='sin')
# Showing the legend
legend()
# Drawing the legend in a better location
legend(loc=0)

# Plotting in another figure
figure()
plot(x, cos(x), label='cos')
legend()

# Plotting in the firt plot
figure(1)
plot(x, cos(x), label='cos')
legend(loc=0)
title('Example plot')
ylabel('y Axis')
xlabel('x Axis')
# saving
savefig('example_plot.png')

