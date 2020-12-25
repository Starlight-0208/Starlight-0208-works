import wmi
import psutil
import time

#获取每秒数据量(动态)
def VariablePerSecond():
    #磁盘IO-初状态量
    ReadBit0 = psutil.disk_io_counters().read_bytes
    ReadCounts0 = psutil.disk_io_counters().read_count
    WriteBit0 = psutil.disk_io_counters().write_bytes
    WriteCounts0 = psutil.disk_io_counters().write_count
    #网络-初状态量
    BytesSent0 = psutil.net_io_counters().bytes_sent
    BytesRecv0 = psutil.net_io_counters().bytes_recv
    PacketsSent0 = psutil.net_io_counters().packets_sent
    PacketsRecv0 = psutil.net_io_counters().packets_recv
    time.sleep(1)
    #磁盘IO-末状态量
    ReadBit1 = psutil.disk_io_counters().read_bytes
    ReadCounts1 = psutil.disk_io_counters().read_count
    WriteBit1 = psutil.disk_io_counters().write_bytes
    WriteCounts1 = psutil.disk_io_counters().write_count
    #网络-末状态量
    BytesSent1 = psutil.net_io_counters().bytes_sent
    BytesRecv1 = psutil.net_io_counters().bytes_recv
    PacketsSent1 = psutil.net_io_counters().packets_sent
    PacketsRecv1 = psutil.net_io_counters().packets_recv
    #result
    #磁盘IO-结果
    ReadBitPerSec = ReadBit1 - ReadBit0
    ReadCountsPerSec = ReadCounts1 - ReadCounts0
    WriteBitPerSec = WriteBit1 - WriteBit0
    WriteCountsPerSec = WriteCounts1 - WriteCounts0
    diskpersec = {'RBPS' : ReadBitPerSec, 'RCPS' : ReadCountsPerSec, 'WBPC' : WriteBitPerSec, 'WCPS' : WriteCountsPerSec}
    #网络-结果
    BytesSentPevSec = BytesSent1 - BytesSent0
    BytesRecvPevSec = BytesRecv1 - BytesRecv0
    PacketsSentPevSec = PacketsSent1 - PacketsSent0
    PacketsRecvPevSec = PacketsRecv1 - PacketsRecv0
    netiopersec = {'BSPS' : BytesSentPevSec, 'BRPS' : BytesRecvPevSec, 'PSPS' : PacketsSentPevSec, 'PRPS' : PacketsRecvPevSec}
    #结果打包
    VariPerSec = {'DISKIO' : diskpersec, 'NETIO' : netiopersec}
    return VariPerSec


#磁盘IO获取
def diskioinfo():
    Usage = psutil.disk_usage('/').used
    Free = psutil.disk_usage('/').free
    Total = psutil.disk_usage('/').total
    Percent = psutil.disk_usage('/').percent
    passive = VariablePerSecond()
    diskinfo = {'RBPS' : passive['DISKIO']['RBPS'], 'RCPS' : passive['DISKIO']['RCPS'], 'WBPC' : passive['DISKIO']['WBPS'], 'WCPS' : passive['DISKIO']['WCPS'], 'Usage' : Usage, 'Free' : Free, 'Total' : Total, 'Percents' : Percent}
    return diskinfo
    

#网络IO
def networkio():
    UpBitTotal = psutil.net_io_counters().bytes_sent
    DnBitTotal = psutil.net_io_counters().bytes_recv
    UpPacTotal = psutil.net_io_counters().packets_sent
    DnPacTotal = psutil.net_io_counters().packets_recv
    #errin = psutil.net_io_counters().errin
    #errout = psutil.net_io_counters().errin
    #dropin =  psutil.net_io_counters().dropin
    #dropout = psutil.net_io_counters().dropout
    psutil.net_if_addrs

    passive = VariablePerSecond()
    netinfo = {'BSPS' : passive['NETIO']['BSPS'], 'BRPS' : passive['NETIO']['BRPS'], 'PSPS' : passive['NETIO']['PSPS'], 'PRPS' : passive['NETIO']['PRPS'], 'UBT' : UpBitTotal, 'UPT' : UpPacTotal, 'DBT' : DnBitTotal, 'DPT' : DnPacTotal}
    return netinfo

#内存信息
def RAMinfo():
    RAMUsed = psutil.virtual_memory().used
    RAMAvail = psutil.virtual_memory().available
    RAMFree = psutil.virtual_memory().free
    RAMTotal = psutil.virtual_memory().total
    RAMUsedPercent = psutil.virtual_memory().percent
    RAMinfo1 = {'Used' : RAMUsed, 'Avail' : RAMAvail, 'Free' : RAMFree, 'Total' : RAMTotal, 'Percent' : RAMUsedPercent}
    return RAMinfo1

#CPU信息
def cpuinfo():
    cpu_counts = psutil.cpu_count() #cpu逻辑核心数
    cpu_freqent = psutil.cpu_freq().current #实时频率
    cpu_freqent_max = psutil.cpu_freq().max #最大频率
    cpu_freqent_min = psutil.cpu_freq().min #最小频率
    cpu_percents = psutil.cpu_percent() #CPU利用率
    cpuinfo1 = {'counts' : cpu_counts, 'freq' : cpu_freqent, 'maxfreq' : cpu_freqent_max, 'minfreq' : cpu_freqent_min, 'percent' : cpu_percents}
    return cpuinfo1

#获取系统详细配置信息（限制Windows）
def unit():
    w = wmi.WMI() 
    cpus = w.Win32_Processor() #cpu
    for cpu in cpus:
        CpuModel = cpu.Name    #CPU型号
        SystemName = cpu.SystemName    #主机名称
        ThreadCount = cpu.ThreadCount   #线程数
        NumberOfCores = cpu.NumberOfCores    #物理核心数
        NumberOfEnabledCore = cpu.NumberOfEnabledCore   #启用的物理核心数
        NumberOfLogicalProcessors = cpu.NumberOfLogicalProcessors   #逻辑处理器核心数
        DataWidth = cpu.DataWidth    #处理器位宽
    harddisk = w.Win32_