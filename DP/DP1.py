tile_list= [-1] * 1000
tile_list[0], tile_list[1], tile_list[2]= 0, 1, 2

for i in range(3, 10):
	tile_list[i]=tile_list[i-1] + tile_list[i-2]


x=int(input())
print(tile_list[:10])
