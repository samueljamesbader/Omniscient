#import pytest
#
#if __name__=="__main__": pytest.main(args=[__file__,'-s'])

import os.path
if __name__=='__main__':
    folder=os.path.join(os.path.dirname(__file__),'knowledge')


    from omniscient.omniscient import Brain
    brain=Brain(folder)

    brain.read("VM2003.txt")
    print(brain('GaN.relaxed.lattice.u'))

