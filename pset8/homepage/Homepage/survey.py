class Task:
    def __init__(self, name, tag, esttime, deadline):
        self.name = name
        self.tag = tag              #creative, informational
        self.esttime = esttime         #in hours
        self.deadline = deadline    #number between 0-24
        

class Instruction:
    def __init__(self, social, starttime, endtime):
        self.social = social
        self.starttime = starttime
        self.endtime = endtime
        self.tasks = []
        
    def addTask(self, task):
        self.tasks.append(task)
        return self.tasks
        
    def removeTask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return self.tasks
        else:
            print("That task is not in the list")
            return None
            
    def removeAllTasks(self):
        self.tasks.clear()
        return self.tasks
        
    def sortTasks(self):
        self.tasks.sort(key=lambda x: x.deadline)
        self.tasks.sort(key=lambda x: x.tag)
        return self.tasks
        
        
class Schedule:
    def __init__(self, day, instructions):
        self.day = day
        self.dayplan = []
        self.makePlan(instructions)
    
    def makePlan(self, instructions):
        allocation = {}
        time = instructions.starttime
        count = 0
        alltasks = instructions.sortTasks()
        Break = Task("Break", "Break", 0.25, 25)

        while time <= instructions.endtime and count < len(alltasks):
            task = alltasks[count]
            estimate = task.esttime
            
            while estimate > 1:
                self.dayplan.append(dict(Task=task.name, Time=time))
                time += 1
                self.dayplan.append(dict(Task=Break.name, Time=time))
                time += 0.25
                estimate -= 1
            
            self.dayplan.append(dict(Task=task.name, Time=time))
            time += estimate
            count += 1
        
        if count != len(alltasks):
            return -1
        else:
            return 0
    
    def showPlan(self):
        for task in self.dayplan:
        name = task["Task"]
        time = str(task["Time"])
        print(f"{name} at {time}")

    
        
class Main:
    def main():
    
    def createInstructions():
        
    
    def processTime(time):
        parts = time.split(":")
        if len(parts) != 2:
            print("Please input time in format hh:mm _M")
            return -1
        else:
            number = int(parts[0])
            
            if "pm" in parts[1].lower():
                number += 12
                
            moreparts = parts[1].split()
            return number + int(moreparts[0])/60
        
        
newtask = Task("Walking the Dog", "Relaxation", 2, 8)
newtaskx = Task("Feeding the Dog", "Relaxation", 1, 9)
newinstruction = Instruction(2, 7, 22)
newinstruction.addTask(newtask)
newinstruction.addTask(newtaskx)
print(newinstruction.tasks)
schedule = Schedule("today", newinstruction)
print("Flag")
print(schedule.dayplan)


    
        