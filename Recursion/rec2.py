def callme(x):
	if x<5:
		print('done')
	else:
		callme(x-2)
		print(x-1)
		callme(x-3)

callme(10)

# callme(8)
# callme(6)
# callme(4)
# print('done')
# print(5)
# callme(3)
# print('done')
# print(7)
# callme(5)
# callme(3)
# done
# print(4)
# callme(2)
# done
# print(9)
# callme(7)
# callme(5)
# callme(3)
# done
# print(4)
# print(6)
# callme(4)
# done


done
5
done
7
done
4
done
9
done
4
6
done