dist = {'AY':51,
	'AS':89,
	'AC':125,
	'AX':232,
	'YS':123,
	'YC':172,
	'YX':279,
	'SC':112,
	'SX':231,
	'CX':106}

def functionVal(path):
	total_dist = 0
	x = path[0]
	for city in path[1:]:
		if x+city in dist:
			total_dist += dist[x+city]
		else:
			total_dist += dist[city+x]
		x = city
	return -1 * total_dist
