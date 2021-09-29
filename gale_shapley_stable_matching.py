from pprint import pprint  #Import pprint, sample and deepcopy libraries
from random import sample
from copy import deepcopy
from datetime import datetime


def gs_algo_team(n):    # Define a function to calculate the stable algo
  team1 = list(range(n))     #Create a team1 of n members
  team2 = list(range(n))     #Create a team2 of 8 members
  pref_team1 = dict((m,sample(range(0,len(team1)),len(team1))) for m in team1)     #Generate a sample preference list 1 for First Team
  #print("Printing First Team \n")
  pprint(pref_team1)
  print() #Generate a sample preference list 2 For Second Team                                 
  pref_team2 = dict((w, sample(range(0,len(team2)),len(team2))) for w in team2)
  #print("Printing second team\n")
  pprint(pref_team2)
  print()
  free_team1 = list(team1)
  free_team2 = list(team2)
  pairs = dict()
  #GS Algorithm
  while len(free_team1) :        # While there is some team member who is free 
      team1_mem = free_team1.pop(0)       # Pop the first element from 1 team
      team2_mem = pref_team1[team1_mem].pop(0)     # Pop the top element from team 2 who is top in the preference list of team 1
      if team2_mem in free_team2:                  # if that element is still in the team
          pairs[team2_mem] = team1_mem             # add that element to the stable pair, here, pairs dict 
          free_team2.remove(team2_mem)             # remove that member from the team2
      else :
          pref = pref_team2[team2_mem]             # if that person already paired with someone
          current_team_mem = pairs[team2_mem]       
          if pref.index(team1_mem)<pref.index(current_team_mem):   # Compare the index, If Less, then
              pairs[team2_mem] = team1_mem                    #add that member to the stable pair, here, pairs dict
              free_team1.append(current_team_mem)               
          else:
              free_team1.append(team1_mem)                   
  proper_pairs = [(team1[m],team2[w]) for (w,m) in pairs.items()]
  print("Perfect pairs is ",proper_pairs)


start_timer = datetime.now()
gs_algo_team(8)
end_timer = datetime.now()
cal_timer = end_timer - start_timer
print("Total Execution time ", cal_timer)

