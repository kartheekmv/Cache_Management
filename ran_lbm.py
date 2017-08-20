#!/usr/bin/python
#lbm
import os
count=1
for ld in [128,64]:        # Second Example
   for li in [64,32]:
         if ld >= li:
	 	    for l in [1]:
		    		   for ls in [32,64]:
				   			if 1 :
										   for s in [1,4,8]:
										   		
												for sr in [1,4,8]:
													     print "Iteration=",count
													     count=count+1
										   			     file_name = '470.lbm_'+str(li)+'kB_'+str(ld)+'kB_'+str(sr)+'_'+str(l)+'MB_'+str(s)+'_'+str(ls)+'B'
										   			     cmd="time ~/gem5/build/X86/gem5.opt -d ~/Downloads/Project1_SPEC-master/470.lbm/AllOutputs/{9} ~/gem5/configs/example/se.py -c ./src/benchmark -o \"20 reference.dat 0 1 ./data/100_100_130_cf_a.of\" -I 500000000 --cpu-type=TimingSimpleCPU --caches --l2cache --l1d_size={0}{8} --l1i_size={1}{8} --l2_size={2}{7} --l1d_assoc={3} --l1i_assoc={4} --l2_assoc={5} --cacheline_size={6}".format(ld,li,l,sr,sr,s,ls,"MB","kB",file_name) 
													     os.system(cmd)
