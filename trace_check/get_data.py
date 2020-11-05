def get_all_input_with_sensors(HMI):
    input_vector=[HMI.P1.State,HMI.P2.State,HMI.P3.State,HMI.P4.State,HMI.P5.State,HMI.P6.State,
    HMI.P101.Status,HMI.P102.Status,HMI.MV101.Status,HMI.MV201.Status,
    HMI.FIT101.Pv,HMI.LIT101.Pv,HMI.LS201.Alarm, HMI.LS202.Alarm, HMI.LSL203.Alarm, HMI.LSLL203.Alarm, HMI.P201.Status, HMI.P202.Status, HMI.P203.Status,
    HMI.P204.Status,HMI.P205.Status,HMI.P206.Status,HMI.P207.Status,HMI.P208.Status,
    HMI.FIT201.Pv,HMI.AIT201.Pv,HMI.AIT202.Pv,HMI.AIT203.Pv, HMI.P301.Status, HMI.P302.Status,HMI.FIT301.Pv, HMI.LIT301.Pv,
    HMI.PSH301.Alarm,HMI.DPSH301.Alarm,HMI.DPIT301.Pv, HMI.MV301.Status,HMI.MV302.Status,HMI.MV303.Status,HMI.MV304.Status,
    HMI.LS401.Alarm,HMI.LIT401.Pv, HMI.P401.Status, HMI.P402.Status, HMI.P403.Status,  HMI.P404.Status,
    HMI.UV401.Status,HMI.AIT401.Pv,HMI.AIT402.Pv,HMI.FIT401.Pv, HMI.AIT501.Pv,HMI.AIT502.Pv,HMI.AIT503.Pv,HMI.AIT504.Pv,
    HMI.FIT501.Pv,HMI.FIT502.Pv,HMI.FIT503.Pv,HMI.FIT504.Pv,HMI.MV501.Status, HMI.MV502.Status, HMI.MV503.Status, HMI.MV504.Status,
    HMI.P501.Status,HMI.P502.Status, HMI.LSL601.Alarm, HMI.LSL602.Alarm, HMI.LSL603.Alarm, HMI.LSH601.Alarm, HMI.LSH602.Alarm, HMI.LSH603.Alarm,
    HMI.P601.Status, HMI.P602.Status, HMI.P603.Status]

    return input_vector


def print_all_output(P1,P2,P3,P4,P5,P6):
    plc1_output_vector = [P1.MV101.DO_Open, P1.MV101.DO_Close, P1.P101.DO_Start, P1.P102.DO_Start]
    plc2_output_vector= [P2.MV201.DO_Open, P2.MV201.DO_Close, P2.P201.DO_Start, P2.P202.DO_Start, P2.P203.DO_Start, P2.P204.DO_Start, P2.P205.DO_Start, P2.P206.DO_Start]
    plc3_output_vector = [P3.MV301.DO_Open, P3.MV301.DO_Close,P3.MV302.DO_Open, P3.MV302.DO_Close,P3.MV303.DO_Open, P3.MV303.DO_Close,P3.MV304.DO_Open, P3.MV304.DO_Close, P3.P301.DO_Start, P3.P302.DO_Start]
    plc4_output_vector = [P4.P401.DO_Start,P4.P402.DO_Start,P4.P403.DO_Start,P4.P404.DO_Start,P4.UV401.DO_Start]
    plc5_output_vector = [P5.MV501.DO_Open,P5.MV501.DO_Close,P5.MV502.DO_Open,P5.MV502.DO_Close,P5.MV503.DO_Open,P5.MV503.DO_Close,P5.MV504.DO_Open,P5.MV504.DO_Close]
    plc6_output_vector = [P6.P601.DO_Start,P6.P602.DO_Start]
    return plc1_output_vector,plc2_output_vector,plc3_output_vector,plc4_output_vector,plc5_output_vector,plc6_output_vector