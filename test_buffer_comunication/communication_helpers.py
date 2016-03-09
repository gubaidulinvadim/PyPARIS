import numpy as np
from PyHEADTAIL.particles.particles import Particles


def list_of_strings_2_buffer(strlist):
	data = ''.join(map(lambda s:s+';', strlist))+'\n'
	buf_to_send = np.int_(np.array(map(ord, list(data))))
	return buf_to_send
	
def buffer_2_list_of_strings(buf):
	str_received = ''.join(map(unichr, list(buf)))
	strlist = map(str, str_received.split('\n')[0].split(';'))[:-1]
	return strlist


def beam_2_buffer(beam):
	if np.array(beam.particlenumber_per_mp).shape != ():
		raise ValueError('particlenumber_per_mp is a vector! Not implemented!')
	
	buf = np.concatenate((
		np.array([float(beam.macroparticlenumber)]),
		np.array([float(beam.particlenumber_per_mp)]), 
		np.array([beam.charge]),
		np.array([beam.mass]),
		np.array([beam.circumference]),
		np.array([beam.gamma]),
		np.float_(beam.id),
		beam.x, beam.xp, beam.y, beam.yp, beam.z, beam.dp))
	return buf
	
def buffer_2_beam(buf):
	
	i_buf = 0
	
	macroparticlenumber = int(buf[i_buf])
	i_buf += 1
	
	particlenumber_per_mp = buf[i_buf]
	i_buf += 1
	
	charge = buf[i_buf]
	i_buf += 1
	
	mass = buf[i_buf]
	i_buf += 1
	
	circumference = buf[i_buf]
	i_buf += 1
	
	gamma = buf[i_buf]
	i_buf += 1
	
	id_ = np.int_(buf[i_buf:i_buf+macroparticlenumber])
	i_buf += macroparticlenumber

	x =  buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber
	
	xp =  buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber
	
	y =  buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber
	
	yp =  buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber
	
	z =  buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber	
	
	dp = buf[i_buf:i_buf+macroparticlenumber]
	i_buf += macroparticlenumber
	
	beam = Particles(macroparticlenumber=macroparticlenumber,
                    particlenumber_per_mp=particlenumber_per_mp, charge=charge,
                    mass=mass, circumference=circumference, gamma=gamma, coords_n_momenta_dict={})

	beam.id = id_
	beam.x = x
	beam.xp = xp
	beam.y = y
	beam.yp = yp		
	beam.z = z
	beam.dp = dp
	
	return beam
