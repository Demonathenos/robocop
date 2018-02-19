import io
N = input("What is the size of the problem")
config = io.open("problem.def", 'w')
for line in io.open('problem.def.templ', 'r'):
  line = line.replace('$state.dimension', str(int(N)+1))
  line = line.replace('$boundarycond.dimension', str(int(N)+1))
  if "$stateconditions" in line:
      x = 0
      line=''
      while x < int(str(N)):
          x += 1
          row = 'state.' + str(int(x))+" "+"string state."+str(int(x))+"\n"
          config.write(row)
  if "$boundaryconditions" in line:
      line=''
      x = 0
      while x < int(str(N)):
          x += 1
          row = 'boundarycond.' + str(int(x))+" "+"string boundarycond."+str(int(x))+"\n"
          config.write(row)
  config.write(line)
config.close()

config1 = io.open('problem.bounds', 'w')
for line in io.open('problem.bounds.tmpl', 'r'):
  line = line.replace('$dimension1', str(int(N)+1))
  line = line.replace('$dimension2', str(int(N) + 1))
  if "$statevariablebounds" in line:
      x = 0
      line=''
      while x < (int(str(N))+1):
          x+= 1
          row = '0 0 free'+'\n'
          config1.write(row)
  if "$initandfinconditions" in line:
      x = 0
      line=''
      while x < (int(str(N))+1):
          x+= 1
          row = '1 1 equal'+'\n'
          config1.write(row)
  config1.write(line)

config1.close()


