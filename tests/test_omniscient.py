#import pytest
#
#if __name__=="__main__": pytest.main(args=[__file__,'-s'])

import os.path
if __name__=='__main__':
    folder=os.path.join(os.path.dirname(__file__),'knowledge')


    from omniscient.omniscient import Brain
    brain=Brain(folder)

    #brain.read("VM2003.txt")
    #print(brain('GaN.relaxed.lattice.u'))

    brain.read("FET8.txt")
    #print(brain._dict)
    print(brain['FET8.dev=DC13r.Lsdm'])
    print(brain('FET8.Lsdm',dev=["DC13r"]))
    print(brain['FET8'])
    print(brain['FET5'])
    print(brain['FET4.sam'])
    try:
        print(brain['FET4.joh'])
        print("I FAILED")
    except Exception as e:
        print("Good: ",e)
    #print(brain._dict)

