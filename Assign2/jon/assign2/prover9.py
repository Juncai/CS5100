'''
Created on Feb 17, 2014

@author: Jon
'''

import os
import subprocess


class Prover9(object):
    """
    A class contains the functionality required to implement 
    a TELL/ASK interface with the knowledge base which is 
    implemented with Prover-9 theorem prover.
    
    This class is revised from NLTK source.
    """
    _filename = None
    
    
    def config_prover9(self, filename, verbose=False):
        assert isinstance(filename, basestring)
        # File exists, no magic
        if os.path.isfile(filename):
            if verbose: print '[Found %s: %s]' % (filename, filename)
            self._filename = filename
        else:
            msg = ("Unable to find the %s file!" % filename)
            raise Prover9Exception(msg)
    
    def _prove(self, goal=None, assumptions=None, verbose=False):
        """
        Use Prover9 to prove a theorem.
        :return: A pair whose first element is a boolean indicating if the
        proof was successful (i.e. return value of 0) and whose second element
        is the output of the prover.
        """
        if not assumptions:
            assumptions = []
            
        stdout, returncode = self._call_prover9(self.prover9_input(goal, assumptions),
                                                verbose=verbose)
        return (returncode == 0, stdout)
    
     
    def prover9_input(self, goal, assumptions):
        """
        :return: The input string that should be provided to the 
        prover9 binary. This string is formed based on the goal,
        assumptions.
        """
        s = ''
        s += 'set(binary_resolution).\n'
        s += 'clear(print_initial_clauses).\n'
        s += 'clear(print_kept).\n'
        s += 'clear(print_given).\n'
        s += 'clear(auto_denials).\n' #only one proof required
        s += 'assign(max_seconds,1).\n'
        s += 'assign(stats,none).\n'
        
        if assumptions:
            s += 'formulas(assumptions).\n'
            for p9_assumption in assumptions:
                s += '    %s\n' % p9_assumption
            s += 'end_of_list.\n\n'
        
        if goal:
            s += 'formulas(goals).\n'
            s += '    %s\n' % goal
            s += 'end_of_list.\n\n'
        
        return s
        
    
    def _call_prover9(self, input_str, args=[], verbose=False):
        """
        Call the "prover9" binary with the given input.
        
        :param input_str: A string whose contents are used as stdin.
        :param args: A list of command-line arguments.
        :return: A tuple (stdout, returncode)        
        """
        if verbose:
            print('Calling:', self._filename)
            print('Args:', args)
            print('Input:\n', input_str, '\n')
            
        # Call prover9 via a subprocess
        cmd = [self._filename] + args
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             stdin=subprocess.PIPE)
        (stdout, stderr) = p.communicate(input=input_str)
        
        if verbose:
            print ('Return code', p.returncode)
            if stdout: print ('stdout:\n', stdout, '\n')
            if stderr: print ('stderr:\n', stderr, '\n')
        
        returncode = p.returncode
        if returncode not in [0,2]:
            errormsgprefix = '%%ERROR:'
            if errormsgprefix in stdout:
                msgstart = stdout.index(errormsgprefix)
                errormsg = stdout[msgstart:].strip()
            else:
                errormsg = None
            if returncode in [3,4,5,6]:
                raise Prover9LimitExceededException(returncode, errormsg)
            else:
                raise Prover9FatalException(returncode, errormsg)
        
        return stdout, returncode
        
        
    
class Prover9Exception (Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        
class Prover9LimitExceededException (Prover9Exception):
    pass

class Prover9FatalException (Prover9Exception):
    pass
