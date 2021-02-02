import epics

im = epics.PV('XF:17IDB-ES:AMX{Cam:9}cam1:ImageMode')
trig = epics.PV('XF:17IDB-ES:AMX{Cam:9}cam1:TriggerMode')
dt = epics.PV('XF:17IDB-ES:AMX{Cam:9}cam1:DataType')
acq = epics.PV('XF:17IDB-ES:AMX{Cam:9}cam1:Acquire')
file_path = epics.PV('XF:17IDB-ES:AMX{Cam:9}JPEG1:FilePath')
file_name = epics.PV('XF:17IDB-ES:AMX{Cam:9}JPEG1:FileName')
file_number = epics.PV('XF:17IDB-ES:AMX{Cam:9}JPEG1:FileNumber')
write_file = epics.PV('XF:17IDB-ES:AMX{Cam:9}JPEG1:WriteFile')
