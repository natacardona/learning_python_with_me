from sum import sum
from div import div
import times

print("This will be our new calculator")
print("Now we have submodules")

print("-----------------------------------")
print("Our first operation will be a sum")
print("How much is 1 + 2 = " + str(sum(1,2)))

print("-----------------------------------")
print("Now let's do a times operation")
print("How much is 3 * 1 = " + str(times.times(1,3)))

print("-----------------------------------")
print("Now let's do a div")
print("How much is 3 * 1 = " + div(1,0))