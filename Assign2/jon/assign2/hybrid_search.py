'''
Created on Feb 16, 2014

@author: Jon


pseudocode of a hybrid agent program for the wumpus world. 
It uses a propositional knowledge base to infer the state 
of the world, and a combination of problem-solving search 
and domain-specific code to decide what actions to take.

function HYBRID-WUMPUS-AGENT(percept) returns an action
    inputs: percept, a list, [stench,breeze,glitter,bump,scream]
    persistent: KB, a knowledge base, initially the atemporal "wumpus physics"
                t, a counter, initially 0, indicating time
                plan, an action sequence, initially empty
    
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    TELL the KB the temporal "physics" sentences for time t
    safe <- {[x,y] : ASK(KB, OK_xy^t)=true}
    
    if ASK(KB, Glitter^t) = true then
        plan <- [Grab] + PLAN-ROUTE(current,{[1,1]},safe)+[Climb]
    if plan is empty then
        unvisited <- {[x,y] : ASK(KB,L_x,y^t') = false for all t'<=t}
        plan <- PLAN-ROUTE(current,unvisited^safe,safe)
    if plan is empty and ASK(KB,HaveArrow^t) = true then
        possible_wumpus <- {[s,y] : ASK(KB,-W_x,y)=false}
        plan <- PLAN-SHOT(current,possible_wumpus,safe)
    if plan is empty then    // no choice but to take a risk
        not_unsafe <- {[x,y] : ASK(KB,-OK_x,y^t)=false}
        plan <- PLAN-ROUTE(current,unvisited^not_unsafe,safe)
    if plan is empty then
        plan <- PLAN-ROUTE(current,{[1,1]},safe) + [Climb]
    action <- POP(plan)
    TELL(KB,MAKE-ACTION-SENTENCE(action,t))
    t <- t + 1
    return action
    
function PLAN-ROUTE(current,goals,allowed) returns an action sequence
    input: current, the agent's current position
            goals, a set of squares; try to plan a route to one of them
            allowed, a set of squares that can form part of the route
    
    problem <- ROUTE-PROBLEM(current,goals,allowed)
    return A*-GRAPH-SEARCH(problem)
    
'''
from prover9 import Prover9








if __name__ == '__main__':
    pass
    