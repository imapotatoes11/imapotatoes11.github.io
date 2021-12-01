#https://edabit.com/challenge/QgSMSMpfcEebAyCye
def time_saved(s_lim, s_avg, d):
	t_lim=d/s_lim
	t_avg=d/s_avg
	return round(((d/s_lim)-(d/s_avg))*60,1)