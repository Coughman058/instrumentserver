# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:12:05 2020

@author: Chao
"""

from instrumentserver.proxy import InstrumentProxy, create_instrument
import qcodes
yoko = InstrumentProxy('yoko')

print(yoko.current(10))
print(yoko.current())

yoko.dac1()
yoko.multiply_addfunc(1,2,3)

yoko.multiply_method(1,2,3)
yoko.reset_method()

yoko.multiply_method(1,2,c=5)


# yoko2 = create_instrument(instrument_class = 'qc.tests.instrument_mocks.DummyInstrument',                          
                          # name = 'yoko2')
                          
                          
mydummy = InstrumentProxy('mydummy')                          