import wmi
import psutil
import time

#获取每秒磁盘IO数据量
def diskioPerSecond():
    ReadBit0 = psutil.disk_io_counters().read_bytes
    ReadCounts0 = psutil.disk_io_counters().read_count
    WriteBit0 = psutil.disk_io_counters().write_bytes
    WriteCounts0 = psutil.disk_io_counters().write_count
    time.sleep(1)
    ReadBit1 = psutil.disk_io_counters().read_bytes
    ReadCounts1 = psutil.disk_io_counters().read_count
    WriteBit1 = psutil.disk_io_counters().write_bytes
    WriteCounts1 = psutil.disk_io_counters().write_count
    #result
    ReadBitPerSec = ReadBit1 - ReadBit0
    ReadCountsPerSec = ReadCounts1 - ReadCounts0
    WriteBitPerSec = WriteBit1 - WriteBit0
    WriteCountsPerSec = WriteCounts1 - WriteCounts0
    diskpersec = {'RBPS' : ReadBitPerSec, 'RCPS' : ReadCountsPerSec, 'WBPC' : WriteBitPerSec, 'WCPS' : WriteCountsPerSec}
    return diskpersec


#获取实时网速
def netioPerSecond():
    BytesSent0 = psutil.net_io_counters().bytes_sent
    BytesRecv0 = psutil.net_io_counters().bytes_recv
    PacketsSent0 = psutil.net_io_counters().packets_sent
    PacketsRecv0 = psutil.net_io_counters().packets_recv
    time.sleep(1)
    BytesSent1 = psutil.net_io_counters().bytes_sent
    BytesRecv1 = psutil.net_io_counters().bytes_recv
    PacketsSent1 = psutil.net_io_counters().packets_sent
    PacketsRecv1 = psutil.net_io_counters().packets_recv
    #result
    BytesSentPevSec = BytesSent1 - BytesSent0
    BytesRecvPevSec = BytesRecv1 - BytesRecv0
    PacketsSentPevSec = PacketsSent1 - PacketsSent0
    PacketsRecvPevSec = PacketsRecv1 - PacketsRecv0
    netiopersec = {'BSPS' : BytesSentPevSec, 'BRPS' : BytesRecvPevSec, 'PSPS' : PacketsSentPevSec, 'PRPS' : PacketsRecvPevSec}
    return netiopersec
    
#
#

#磁盘IO获取
def diskioinfo():
    pass

#网络IO
def networkio():
    pass

#内存信息
def RAMinfo():
    RAMUsed = psutil.virtual_memory().used
    RAMAvail = psutil.virtual_memory().available
    RAMFree = psutil.virtual_memory().free
    RAMTotal = psutil.virtual_memory().total
    RAMUsedPercent = psutil.virtual_memory().percent


#CPU信息
def cpuio():
    cpu_counts = psutil.cpu_count() #cpu逻辑核心数
    cpu_freqent = psutil.cpu_freq().current #实时频率
    cpu_freqent_max = psutil.cpu_freq().max #最大频率
    cpu_freqent_min = psutil.cpu_freq().min #最小频率
    cpu_percents = psutil.cpu_percent() #CPU利用率

#获取系统详细配置信息（限制Windows）
def unit():
    w=wmi.WMI() 
    cpus=w.Win32_Processor() #cpu
    for 