# module nintendo
# -- encoding: utf-8 --

"""苦し紛れのブルートフォース"""
def brute_force_search(m):
	ans = ''
	for i in xrange(1,m):	
		ans = lets_take_tea_break(*[int(x) for x in (i, 17, 3569, 915)])
		if ans: print(ans)


def lets_take_tea_break(m, e, n, c):
	"""print(m, e, n, c)"""
    	if pow(m, e) % n == c: return str(m)
    	return ""

if __name__ == "__main__":
    	import sys
    	print("http://cp1.nintendo.co.jp/" +
    	  lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))


