print(sum(n in(sorted(n),sorted(n,reverse=True))and all(1<=abs(n[i+1]-n[i])<=3for i in range(len(n)-1))for n in[[*map(int,line.split())]for line in open(0)]))
