#Tool designed by ProNoob Sami-Colon
#remove the # sign to set recursion limit as per your need!

# import sys
# sys.setrecursionlimit(100000000)

def generate(inp,i,s):
	global ul
	global ll
	global ans
	if(i >= len(inp)):
		if(len(s)>=ll and s not in ans):
			global fp
			fp.write(s+"\n")
			# print(s)
			ans.append(s)
		return
	else:
		generate(inp,i+1,s)
		y=s
		s=s+str(inp[i])
		if(len(s) <=ul):
			generate(inp,i+1,s)
		y=str(inp[i])+y
		if(len(y) <=ul):
			generate(inp,i+1,y)
		return

inp = [int(x) for x in input("Enter Max limit and Min limit seperated by space\n").strip().split()]
ul,ll = max(inp[0],inp[1]), min(inp[0],inp[1])
del inp
inp = input("Enter words seperated by space!\n").strip().split()
file = input("Enter FileName to write to!\n").strip()
fp = open("./"+file+".txt",'a+')
ans = []
generate(inp,0,"")
print("Generated "+str(len(ans))+" words! Enjoy Noob!! HAHHAAaaaaaa")
print("_______________________________________________________________")

#only for debuging!
# for i in range(0,len(ans)):
# 	print(ans[i])
# print("_______________________________________________________________")
# print("Generated "+str(len(ans))+" words! Enjoy Noob!! HAHHAAaaaaaa")