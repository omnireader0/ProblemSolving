ff, fs, sf, ss = map(int, input().split())
if not ff and not fs:
    if not sf: max_cnt = ss
    else: max_cnt = ss + 1
elif not fs: max_cnt = ff    
else:    
    if fs <= sf: max_cnt = ff + fs + fs + ss
    else: max_cnt = ff + sf + sf + ss + 1
print(max_cnt)
    