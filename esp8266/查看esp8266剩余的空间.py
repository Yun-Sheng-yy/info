# 终端输入
import ubinascii
import os
statvfs_fields = ['bsize','frsize','blocks','bfree','bavail','files','ffree',]
dict(zip(statvfs_fields, os.statvfs('/')))
import gc
gc.mem_free()