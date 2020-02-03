from gnuradio import gr
import numpy as np

####################################################
##     clase e_add_ff                             ##
####################################################
class e_add_ff(gr.sync_block):  
    """consiste en un bloque para una suma escalada de dos senales reales. Por lo tanto hay dos senales de entrada y una de salida. Si escala=0.5 lo que se logra es promediar las dos senales"""
     
    def __init__(self, escala=0.5):
 
        gr.sync_block.__init__(
            self,
            name='e_add_ff', 
            in_sig=[np.float32,np.float32], 
            out_sig=[np.float32]
        )
        self.escala=escala
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala
        return len(out0)
