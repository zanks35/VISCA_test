import time
from common import port_connect


power_on = [0x81, 0x01, 0x04, 0x00, 0x02, 0xff]                                                       # power打开
power_off = [0x81, 0x01, 0x04, 0x00, 0x03, 0xff]                                                       # power关闭
power_quire = [0x81, 0x09, 0x04, 0x00, 0xff]                                                             # 查询电源状态
PT_Home = [0x81, 0x01, 0x06, 0x04, 0xFF]
PT_Quire = [0x81, 0x09, 0x06, 0x12, 0xff]
PT_Reset = [0x81, 0x01, 0x06, 0x05, 0xff]
Zoom_Quire= [0x81,0x09,0x04,0x47,0xff]                                                                     # 查询zoom位置
zoom_t_standard = [0X81, 0x01, 0x04, 0x07, 0x02, 0xff]                                                     # ZOOM Tele定速
zoom_w_standard = [0X81, 0x01, 0x04, 0x07, 0x03, 0xff]                                                     # ZOOM Wide定速
zoom_t_variable_0= [0X81, 0x01, 0x04, 0x07, 0x20, 0xff]                                                    # ZOOM Tele变速:0
zoom_t_variable_7= [0X81, 0x01, 0x04, 0x07, 0x27, 0xff]                                                    # ZOOM Tele变速:7
zoom_t_variable_5= [0X81, 0x01, 0x04, 0x07, 0x25, 0xff]                                                    # ZOOM Tele变速:5
zoom_w_variable_0 = [0X81, 0x01, 0x04, 0x07, 0x30, 0xff]                                                   # ZOOM Wide变速:0
zoom_w_variable_7 = [0X81, 0x01, 0x04, 0x07, 0x37, 0xff]                                                   # ZOOM Wide变速:7
zoom_w_variable_5 = [0X81, 0x01, 0x04, 0x07, 0x35, 0xff]                                                   # ZOOM Wide变速:5
zoom_position_4000 = [0X81, 0x01, 0x04, 0x47, 0x04, 0x00, 0x00, 0x00, 0xff]                                # ZOOM 直接到达指定位置:4000
zoom_position_2000 = [0X81, 0x01, 0x04, 0x47, 0x02, 0x00, 0x00, 0x00, 0xff]                                # ZOOM 直接到达指定位置:2000
zoom_position_0000 = [0X81, 0x01, 0x04, 0x47, 0x00, 0x00, 0x00, 0x00, 0xff]                                # ZOOM 直接到达指定位置:0000
zoom_stop = [0X81, 0x01, 0x04, 0x07, 0x00, 0xff]
Dzoom_stus_qurie = [0X81, 0x09, 0x04, 0x06, 0xff]
Dzoom_qurie = [0X81, 0x09, 0x04, 0x26, 0xff]
# Dzoom_on = [0X81, 0x01, 0x04, 0x06, 0x02, 0xff]
# Dzoom_off = [0X81, 0x01, 0x04, 0x06, 0x03, 0xff]
Dzoom_x1 = [0X81, 0x01, 0x04, 0x26, 0x00, 0xff]
Dzoom_x8 = [0X81, 0x01, 0x04, 0x26, 0x07, 0xff]
Dzoom_x12 = [0X81, 0x01, 0x04, 0x26, 0x0b, 0xff]
zoom0000_focus3bdf = [0X81, 0x01, 0x04, 0x47,0x00,0x00,0x00,0x00,0x03,0x0b,0x0d,0x0f, 0xff]
zoom2000_focus4000 = [0X81, 0x01, 0x04, 0x47,0x02,0x00,0x00,0x00,0x04,0x00,0x00,0x00, 0xff]
zoom4000_focus4280 = [0X81, 0x01, 0x04, 0x47,0x04,0x00,0x00,0x00,0x04,0x02,0x08,0x00, 0xff]
Focus_Quire= [0x81,0x09,0x04,0x48,0xff]                                                                    # Focus 位置查询
Focus_mode_Quire= [0x81,0x09,0x04,0x38,0xff]                                                                    # Focus mode 位置查询
focus_manual_auto = [0X81, 0x01, 0x04, 0x38, 0x10, 0xff]                                                   # Focus 手动自动切换
focus_one_push_trigger = [0X81, 0x01, 0x04, 0x18, 0x01, 0xff]                                                   # Focus 一键触发
focus_manual = [0X81, 0x01, 0x04, 0x38, 0x03, 0xff]                                                     # FOCUS 手动
focus_auto = [0X81, 0x01, 0x04, 0x38, 0x02, 0xff]                                                     # FOCUS 自动
focus_far_standard = [0X81, 0x01, 0x04, 0x08, 0x02, 0xff]                                                     # FOCUS 定速far
focus_near_standard = [0X81, 0x01, 0x04, 0x08, 0x03, 0xff]                                                     # FOCUS 定速near
focus_far_0 = [0X81, 0x01, 0x04, 0x08, 0x20, 0xff]                                                   # FOCUS 变速速far:0
focus_far_7 = [0X81, 0x01, 0x04, 0x08, 0x27, 0xff]                                                   # FOCUS 变速速far:7
focus_far_5 = [0X81, 0x01, 0x04, 0x08, 0x25, 0xff]                                                   # FOCUS 变速速far:5
focus_near_0 = [0X81, 0x01, 0x04, 0x08, 0x30, 0xff]                                                   # FOCUS 变速 near:0
focus_near_7= [0X81, 0x01, 0x04, 0x08, 0x37, 0xff]                                                    # FOCUS 变速 near:7
focus_near_5= [0X81, 0x01, 0x04, 0x08, 0x35, 0xff]                                                    # FOCUS 变速 near:5
focus_stop = [0X81, 0x01, 0x04, 0x08, 0x00, 0xff]                                                     # FOCUS 停止
focus_3bdf = [0X81, 0x01, 0x04, 0x48, 0x03, 0x0b, 0x0d, 0x0f, 0xff]                                   # FOCUS 直接到指定位置
focus_4BDF = [0X81, 0x01, 0x04, 0x48, 0x04, 0x0B, 0x0D, 0x0F, 0xff]                              # FOCUS 直接到指定位置
focus_5494 = [0X81, 0x01, 0x04, 0x48, 0x05, 0x04, 0x09, 0x04, 0xff]                              # FOCUS 直接到指定位置
WB_manual = [0x81, 0x01, 0x04, 0x35, 0x05, 0xFF]                                                     # 设置手动白平衡模式
WB_Quire = [0x81, 0x09, 0x04, 0x35, 0xff]                                                           # 查询白平衡模式
WB_auto = [0x81, 0x01, 0x04, 0x35, 0x00, 0xFF]                                                     #设置自动白平衡模式
WB_indoor = [0x81, 0x01, 0x04, 0x35, 0x01, 0xFF]                                                   # 白平衡 室内
WB_outdoor = [0x81, 0x01, 0x04, 0x35, 0x02, 0xFF]                                                   # 白平衡 户外
WB_one_push = [0x81, 0x01, 0x04, 0x35, 0x03, 0xFF]                                                     # 白平衡一键白平衡
WB_AWB = [0x81, 0x01, 0x04, 0x35, 0x05, 0xFF]                                                   # 白平衡AWB
WB_sodium_lamp = [0x81, 0x01, 0x04, 0x35, 0x0C, 0xFF]                                                   # 白平衡钠灯
WB_one_push_trigger = [0x81, 0x01, 0x04, 0x10, 0x05, 0xFF]                                                   # 白平衡one push trigger
# data_coordinate41 = [0x81, 0x01, 0x04, 0x35, 0x05, 0xFF]                                                   # 白平衡日光灯2
# data_coordinate42 = [0x81, 0x01, 0x04, 0x35, 0x06, 0xFF]                                                   # 白平衡白炽灯
# data_coordinate43 = [0x81, 0x01, 0x04, 0x35, 0x07, 0xFF]                                                   # 白平衡闪光灯

# Color_Temperature = [0x81, 0x01, 0x04, 0x35, 0x0b, 0xFF]
# CAM_WB_Color_Temperature_quire = [0x81, 0x09, 0x0e, 0x24, 0x49, 0xFF]
# CAM_WB_Color_Temperature_0 = [0x81, 0x01, 0x0e, 0x24, 0x49, 0x00, 0x00, 0xFF]
# CAM_WB_Color_Temperature_11 = [0x81, 0x01, 0x0e, 0x24, 0x49, 0x01, 0x01, 0xFF]
# CAM_WB_Color_Temperature_25 = [0x81, 0x01, 0x0e, 0x24, 0x49, 0x02, 0x05, 0xFF]

WB_R_Gain_default = [0x81, 0x01, 0x04, 0x03, 0x00, 0xFF]                                                     # 白平衡 RGAIN恢复默认
WB_R_Gain_up= [0x81, 0x01, 0x04, 0x03, 0x02, 0xFF]                                                      # 白平衡 R增益向上调节
WB_R_Gain_down = [0x81, 0x01, 0x04, 0x03, 0x03, 0xFF]                                                     # 白平衡 R增益向下调节
WB_R_Gain_0 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x00, 0x00, 0xFF]                                   # 白平衡 R增益指定到达的位置:0
WB_R_Gain_16 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x01, 0x00, 0xFF]                                # 白平衡 R增益指定到达的位置:16
WB_R_Gain_7 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x00, 0x07, 0xFF]                                # 白平衡 R增益指定到达的位置:17
WB_R_Gain_Quire = [0x81, 0x09, 0x04, 0x43, 0xFF]                                                           # 查询红色增益值
WB_B_Gain_Quire = [0x81, 0x09, 0x04, 0x44, 0xFF]                                                           #查询蓝色增益值
WB_B_Gain_default = [0x81, 0x01, 0x04, 0x04, 0x00, 0xFF]                                                     # 白平衡 BGAIN恢复默认
WB_B_Gain_up = [0x81, 0x01, 0x04, 0x04, 0x02, 0xFF]                                                     # 白平衡 B向上调节
WB_B_Gain_down = [0x81, 0x01, 0x04, 0x04, 0x03, 0xFF]                                                     # 白平衡 B向下调节
WB_B_Gain_0 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x00, 0x00, 0xFF]                                   # 白平衡 B指定到达的位置:0
WB_B_Gain_16 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x01, 0x00, 0xFF]                                   # 白平衡 B指定到达的位置:16
WB_B_Gain_7 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x00, 0x01, 0xFF]                                   # 白平衡 B指定到达的位置:17

CAM_AWB_RGain_quire = [0x81, 0x09, 0x0e, 0x24, 0x46, 0xFF]
CAM_AWB_RGain_0 = [0x81, 0x01, 0x0e, 0x24, 0x46, 0x00, 0x00, 0xFF]
CAM_AWB_RGain_9 = [0x81, 0x01, 0x0e, 0x24, 0x46, 0x00, 0x09, 0xFF]
CAM_AWB_RGain_14 = [0x81, 0x01, 0x0e, 0x24, 0x46, 0x00, 0x0e, 0xFF]

CAM_AWB_BGain_quire = [0x81, 0x09, 0x0e, 0x24, 0x47, 0xFF]
CAM_AWB_BGain_0 = [0x81, 0x01, 0x0e, 0x24, 0x47, 0x00, 0x00, 0xFF]
CAM_AWB_BGain_9 = [0x81, 0x01, 0x0e, 0x24, 0x47, 0x00, 0x09, 0xFF]
CAM_AWB_BGain_14 = [0x81, 0x01, 0x0e, 0x24, 0x47, 0x00, 0x0e, 0xFF]

CAM_AWB_GGain_quire = [0x81, 0x09, 0x0e, 0x24, 0x48, 0xFF]
CAM_AWB_GGain_0 = [0x81, 0x01, 0x0e, 0x24, 0x48, 0x00, 0x00, 0xFF]
CAM_AWB_GGain_9 = [0x81, 0x01, 0x0e, 0x24, 0x48, 0x00, 0x09, 0xFF]
CAM_AWB_GGain_14 = [0x81, 0x01, 0x0e, 0x24, 0x48, 0x00, 0x0e, 0xFF]

Gain_quire = [0x81, 0x09, 0x04, 0x4c, 0xFF]
Gain_12 = [0x81, 0x01, 0x04, 0x2c, 0x04, 0xFF]
Gain_24 = [0x81, 0x01, 0x04, 0x2c, 0x08, 0xFF]
Gain_45 = [0x81, 0x01, 0x04, 0x2c, 0x0f, 0xFF]
exposure_auto = [0x81, 0x01, 0x04, 0x39, 0x00, 0xFF]                                                     # 设置自动曝光模式
exposure_manual = [0x81, 0x01, 0x04, 0x39, 0x03, 0xFF]                                                     # 设置手动曝光模式
exposure_iris = [0x81, 0x01, 0x04, 0x39, 0x0B, 0xFF]                                                     # 设置光圈优先模式
exposure_shutter = [0x81, 0x01, 0x04, 0x39, 0x0A, 0xFF]                                                     # 设置快门优先模式
exposure_white_board = [0x81, 0x01, 0x04, 0x39, 0x5F, 0xFF]                                                     # 设置白板模式
exposure_bright = [0x81, 0x01, 0x04, 0x39, 0x0D, 0xFF]                                                     # 设置亮度优先模式
exposure_Quire = [0x81, 0x09, 0x04, 0x39, 0xFF]                                                           # 曝光模式查询命令

exposure_shutter_default = [0x81, 0x01, 0x04, 0x0A, 0x00,0xFF]                                                      # 快门数值恢复默认
exposure_shutter_up = [0x81, 0x01, 0x04, 0x0A, 0x02, 0xFF]                                                     # 快门数值向上调整
exposure_shutter_down = [0x81, 0x01, 0x04, 0x0A, 0x03, 0xFF]                                                     # 快门数值向下调整
exposure_shutter_Quire = [0x81, 0x09, 0x04, 0x4A, 0xFF]                                                           #快门数值查询
exposure_shutter_6 = [0x81, 0x01, 0x04, 0x4A,0x00, 0x00,0x00,0x0F,0xFF]                                       # 快门直接调整到：1/60
exposure_shutter_1_90 = [0x81, 0x01, 0x04, 0x4A,0x00, 0x00,0x00,0x07,0xFF]

exposure_iris_Quire = [0x81, 0x09, 0x04, 0x4B, 0xFF]                                                            #光圈数值查询
exposure_iris_default = [0x81, 0x01, 0x04, 0x0B,0x00,0xFF]                                                        #光圈恢复默认值
exposure_iris_up = [0x81, 0x01, 0x04, 0x0B,0x02,0xFF]                                                        #光圈数值向上
exposure_iris_down = [0x81, 0x01, 0x04, 0x0B,0x03,0xFF]                                                        #光圈数值向下
exposure_iris_close = [0x81, 0x01, 0x04, 0x4B,0x00,0x00,0x00,0x00,0xFF]                                         #光圈数值到绝对位置：close
exposure_iris_F1_6 = [0x81, 0x01, 0x04, 0x4B,0x00,0x00,0x00,0x0D,0xFF]                                      #光圈数值到绝对位置：F1.6

exposure_bright_Qurie = [0x81, 0x09, 0x04, 0x4D, 0xFF]                                                             #亮度数值查询
exposure_bright_up = [0x81, 0x01, 0x04, 0x0D, 0x02,0xFF]                                                         #亮度数值向上调整
exposure_bright_down = [0x81, 0x01, 0x04, 0x0D, 0x03,0xFF]                                                         #亮度数值向下调整
exposure_bright_default = [0x81, 0x01, 0x04, 0x0D, 0x00,0xFF]                                                         #亮度数值恢复默认值
exposure_bright_0 = [0x81, 0x01, 0x04, 0x4D, 0x00,0x00,0x00,0x00,0xFF]                                          #亮度数值到指定位置：0
exposure_bright_15 = [0x81, 0x01, 0x04, 0x4D, 0x00,0x00,0x00,0x0F,0xFF]                                       #亮度数值到指定位置：28
Image_Mode_default = [0x81, 0x01, 0x04, 0x3F, 0x04, 0x00,0xFF]                                                         #亮度数值恢复默认值
Image_Mode_Custom = [0x81, 0x01, 0x04, 0x3F, 0x04, 0x01,0xFF]                                                        #亮度数值恢复默认值


exposure_Gain_Quire = [0x81, 0x09, 0x04, 0x4C, 0xFF]                                                             #曝光增益查询
exposure_Gain_up = [0x81, 0x01, 0x04, 0x0C, 0x02,0xFF]                                                         #曝光增益向上调整
exposure_Gain_down = [0x81, 0x01, 0x04, 0x0C, 0x03,0xFF]                                                         #曝光增益向下调整
exposure_Gain_default = [0x81, 0x01, 0x04, 0x0C, 0x00,0xFF]                                                         #曝光增益恢复默认值
exposure_Gain_0 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x00,0xFF]                                          #曝光增益数值到指定位置：0
exposure_Gain_14 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x0E,0xFF]                                          #曝光增益数值到指定位置：14
exposure_Gain_8 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x08,0xFF]                                          #曝光增益数值到指定位置：8
exposure_Gain_9 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x09,0xFF]                                          #曝光增益数值到指定位置：9

ExpComp_on= [0x81, 0x01, 0x04, 0x3E, 0x02, 0xFF]                                                        #曝光补偿打开
ExpComp_off= [0x81, 0x01, 0x04, 0x3E, 0x03, 0xFF]                                                       #曝光补偿关闭
ExpComp_default= [0x81, 0x01, 0x04, 0x0E, 0x00, 0xFF]                                                       #曝光补偿恢复默认值
ExpComp_up= [0x81, 0x01, 0x04, 0x0E, 0x02, 0xFF]                                                       #曝光补偿数值向上
ExpComp_down= [0x81, 0x01, 0x04, 0x0E, 0x03, 0xFF]                                                       #曝光补偿数值向下
ExpComp_status_quire= [0x81, 0x09, 0x04, 0x3E,0xFF]                                                              #曝光补偿状态查询
ExpComp_value_quire= [0x81, 0x09, 0x04, 0x4E,0xFF]                                                              #曝光补偿数值查询
ExpComp_value_0= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x00,0xFF]                                     #曝光补偿数值设置为0
ExpComp_value_2= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x02,0xFF]                                     #曝光补偿数值设置为2
ExpComp_value_4= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x04,0xFF]                                    #曝光补偿数值设置为4

BackLight_Quire= [0x81, 0x09, 0x04, 0x33, 0xFF]                                                             #背光补偿状态查询
BackLight_on= [0x81, 0x01, 0x04, 0x33, 0x02, 0xFF]                                                       #背光补偿打开
BackLight_off= [0x81, 0x01, 0x04, 0x33, 0x03, 0xFF]                                                       #背光补偿关闭

WDR_Quire =[0x81, 0x09, 0x04, 0x2D, 0xFF]                    #宽动态查询
WDR_3 =[0x81, 0x01, 0x04, 0x2D, 0x03, 0xFF]                  #宽动态3
WDR_2 =[0x81, 0x01, 0x04, 0x2D, 0x02, 0xFF]                  #宽动态2
WDR_1 =[0x81, 0x01, 0x04, 0x2D, 0x01, 0xFF]                  #宽动态1
WDR_OFF =[0x81, 0x01, 0x04, 0x2D, 0x00, 0xFF]                #宽动态关闭

Sharpness_default=[0x81, 0x01, 0x04, 0x02, 0x00, 0xFF]             #锐度值恢复默认值
Sharpness_up=[0x81, 0x01, 0x04, 0x02, 0x02, 0xFF]                  #锐度值增加
Sharpness_down=[0x81, 0x01, 0x04, 0x02, 0x03, 0xFF]                #锐度值减小
Sharpness_Quire=[0x81, 0x09, 0x04, 0x42, 0xFF]                     #查询锐度值
Sharpness_0=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x00,0xFF]                #设置锐度值0
Sharpness_1=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x01,0xFF]                #设置锐度值1
Sharpness_8=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x08,0xFF]                #设置锐度值8
Sharpness_14=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x0E,0xFF]                #设置锐度值14

CAM_2DNR_Quire =[0x81, 0x09, 0x04, 0x53, 0xFF]                 #2DNR值查询
CAM_2DNR_0ff =[0x81, 0x01, 0x04, 0x53, 0x00,0xFF]              #2DNR关闭
CAM_2DNR_1 =[0x81, 0x01, 0x04, 0x53, 0x01,0xFF]                #2DNR值为1
CAM_2DNR_2 =[0x81, 0x01, 0x04, 0x53, 0x02,0xFF]                #2DNR值为2
CAM_2DNR_3 =[0x81, 0x01, 0x04, 0x53, 0x03,0xFF]                #2DNR值为3

CAM_3DNR_Quire =[0x81, 0x09, 0x04, 0x54, 0xFF]                 #3DNR值查询
CAM_3DNR_0ff =[0x81, 0x01, 0x04, 0x54, 0x00,0xFF]              #3DNR关闭
CAM_3DNR_1 =[0x81, 0x01, 0x04, 0x54, 0x01,0xFF]                #3DNR值为1
CAM_3DNR_2 =[0x81, 0x01, 0x04, 0x54, 0x02,0xFF]                #3DNR值为2
CAM_3DNR_3 =[0x81, 0x01, 0x04, 0x54, 0x03,0xFF]                #3DNR值为3

clear_0 = [0x81,0x01,0x04,0x3f,0x00,0x00,0xff]                                                       # 清除0预置位
set_0 = [0x81,0x01,0x04,0x3f,0x01,0x00,0xff]                                                       # 设置0预置位
call_0 = [0x81,0x01,0x04,0x3f,0x02,0x00,0xff]                                                       # 调用0预置位


data_up = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x01, 0xff]  # 云台向上
data_down = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x02, 0xff]  # 云台向下
data_left = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x03, 0xff]  # 云台向左
data_right = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x03, 0xff]  # 云台向右
data_stop = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x03, 0xff]  # 云台停止
PT_UpLeft = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x01, 0xff]  # 云台左上
PT_UpRight = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x01, 0xff]  # 云台右上
PT_DownLeft = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x02, 0xff]  # 云台左下
PT_DownRight = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x02, 0xff]  # 云台右下

video_format_quire = [0x81, 0x09, 0x06, 0x23, 0xFF]                                                           # 视频格式查询命令
video_format_1080p60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x00, 0xFF]                                               # 视频格式设置：1080p60
video_format_1080p30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x01, 0xFF]                                               # 视频格式设置：1080p30
video_format_1080i60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x02, 0xFF]                                               # 视频格式设置：1080i60
video_format_720p60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x03, 0xFF]                                               # 视频格式设置：720p60
video_format_720p30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x04, 0xFF]                                               # 视频格式设置：720p30
video_format_4kp60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x06, 0xFF]                                               # 视频格式设置：4kp60
video_format_4kp30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x07, 0xFF]                                               # 视频格式设置：4kp30
video_format_1080p50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x08, 0xFF]                                               # 视频格式设置：1080p50
video_format_1080p25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x09, 0xFF]                                               # 视频格式设置：1080p25
video_format_1080i50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0A, 0xFF]                                               # 视频格式设置：1080i50
video_format_720p50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0B, 0xFF]                                               # 视频格式设置：720p50
video_format_720p25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0C, 0xFF]                                               # 视频格式设置：720p25
video_format_4Kp50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0E, 0xFF]                                               # 视频格式设置：4Kp50
video_format_4Kp25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0F, 0xFF]                                               # 视频格式设置：4Kp25

IR_on = [0x81, 0x01, 0x06, 0x08, 0x02, 0xFF]                                               #
IR_off = [0x81, 0x01, 0x06, 0x08, 0x03, 0xFF]                                               #
IR_on_off = [0x81, 0x01, 0x06, 0x08, 0x10, 0xFF]                                               #
IR_quire = [0x81, 0x09, 0x06, 0x08, 0xFF]                                               #

audio_mode_on = [0x81, 0x01, 0x04, 0x68, 0x02, 0xFF]
audio_mode_off = [0x81, 0x01, 0x04, 0x68, 0x03, 0xFF]
audio_volume_quire = [0x81, 0x09, 0x04, 0x6e, 0xFF]
# audio_volume_reset = [0x81, 0x01, 0x04, 0x6e, 0x00, 0xFF]
# audio_volume_up = [0x81, 0x01, 0x04, 0x6e, 0x02, 0xFF]
# audio_volume_down = [0x81, 0x01, 0x04, 0x6e, 0x03, 0xFF]
audio_volume_00 = [0x81, 0x01, 0x04, 0x6e, 0x00, 0xFF]
audio_volume_03 = [0x81, 0x01, 0x04, 0x6e, 0x03, 0xFF]
audio_volume_08 = [0x81, 0x01, 0x04, 0x6e, 0x08, 0xFF]

IP_DHCP_quire = [0x81, 0x09, 0x7c, 0x01, 0xFF]
IP_DHCP_on = [0x81, 0x01, 0x7c, 0x01, 0x02, 0xFF]
IP_DHCP_off = [0x81, 0x01, 0x7c, 0x01, 0x03, 0xFF]

mirror_quire = [0x81, 0x09, 0x04, 0x61, 0xFF]
mirror_on = [0x81, 0x01, 0x04, 0x61, 0x02, 0xFF]
mirror_off = [0x81, 0x01, 0x04, 0x61, 0x03, 0xFF]

filp_quire = [0x81, 0x09, 0x04, 0x66, 0xFF]
filp_on = [0x81, 0x01, 0x04, 0x66, 0x02, 0xFF]
filp_off = [0x81, 0x01, 0x04, 0x66, 0x03, 0xFF]

anti_flicker_quire = [0x81, 0x09, 0x04, 0x3a, 0xFF]
anti_flicker_off = [0x81, 0x01, 0x04, 0x3a, 0x00, 0xFF]
anti_flicker_50Hz = [0x81, 0x01, 0x04, 0x3a, 0x01, 0xFF]
anti_flicker_60Hz = [0x81, 0x01, 0x04, 0x3a, 0x02, 0xFF]

gamma_quire = [0x81, 0x09, 0x04, 0x5b, 0xFF]
gamma_0 = [0x81, 0x01, 0x04, 0x5b, 0x00, 0xFF]
gamma_1 = [0x81, 0x01, 0x04, 0x5b, 0x01, 0xFF]
gamma_3 = [0x81, 0x01, 0x04, 0x5b, 0x03, 0xFF]

menu_factory = [0x81, 0x01, 0x04, 0x3f, 0x03, 0x00, 0xFF]

set_IP = [0x81, 0x01, 0x08, 0x07, 0x09,  0xFF]

IP_address_quire = [0x81, 0x09, 0x7c, 0x02, 0xFF]
set_IP_address_10_0_8_241 = [0x81, 0x01, 0x7c, 0x02, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x0f, 0x01, 0xFF]
set_IP_address_1_0_0_0 = [0x81, 0x01, 0x7c, 0x02,0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF]
set_IP_address_255_255_255_255 = [0x81, 0x01, 0x7c, 0x02,0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xFF]

IP_mask_quire = [0x81, 0x09, 0x7c, 0x03, 0xFF]

IP_gateway_quire = [0x81, 0x09, 0x7c, 0x04, 0xFF]

CAM_Sharpness_quire = [0x81, 0x09, 0x0e, 0x24, 0x40, 0xFF]
CAM_Sharpness_0 = [0x81, 0x01, 0x0e, 0x24, 0x40, 0x00, 0x00, 0xFF]
CAM_Sharpness_9 = [0x81, 0x01, 0x0e, 0x24, 0x40, 0x00, 0x09, 0xFF]
CAM_Sharpness_11 = [0x81, 0x01, 0x0e, 0x24, 0x40, 0x00, 0x0b, 0xFF]

CAM_Brightness_quire = [0x81, 0x09, 0x0e, 0x24, 0x41, 0xFF]
CAM_Brightness_0 = [0x81, 0x01, 0x0e, 0x24, 0x41, 0x00, 0x00, 0xFF]
CAM_Brightness_9 = [0x81, 0x01, 0x0e, 0x24, 0x41, 0x00, 0x09, 0xFF]
CAM_Brightness_14 = [0x81, 0x01, 0x0e, 0x24, 0x41, 0x00, 0x0e, 0xFF]

CAM_Contrast_quire = [0x81, 0x09, 0x0e, 0x24, 0x42, 0xFF]
CAM_Contrast_0 = [0x81, 0x01, 0x0e, 0x24, 0x42, 0x00, 0x00, 0xFF]
CAM_Contrast_9 = [0x81, 0x01, 0x0e, 0x24, 0x42, 0x00, 0x09, 0xFF]
CAM_Contrast_14 = [0x81, 0x01, 0x0e, 0x24, 0x42, 0x00, 0x0e, 0xFF]

CAM_Saturation_quire = [0x81, 0x09, 0x0e, 0x24, 0x43, 0xFF]
CAM_Saturation_0 = [0x81, 0x01, 0x0e, 0x24, 0x43, 0x00, 0x00, 0xFF]
CAM_Saturation_9 = [0x81, 0x01, 0x0e, 0x24, 0x43, 0x00, 0x09, 0xFF]
CAM_Saturation_14 = [0x81, 0x01, 0x0e, 0x24, 0x43, 0x00, 0x0e, 0xFF]

CAM_Hue_quire = [0x81, 0x09, 0x0e, 0x24, 0x44, 0xFF]
CAM_Hue_0 = [0x81, 0x01, 0x0e, 0x24, 0x44, 0x00, 0x00, 0xFF]
CAM_Hue_9 = [0x81, 0x01, 0x0e, 0x24, 0x44, 0x00, 0x09, 0xFF]
CAM_Hue_14 = [0x81, 0x01, 0x0e, 0x24, 0x44, 0x00, 0x0e, 0xFF]

preset_list = ['//*[@id="presetNum0ID"]','//*[@id="presetNum1ID"]','//*[@id="presetNum2ID"]',
                   '//*[@id="presetNum3ID"]','//*[@id="presetNum4ID"]','//*[@id="presetNum5ID"]',
                   '//*[@id="presetNum6ID"]','//*[@id="presetNum7ID"]','//*[@id="presetNum8ID"]',
                   '//*[@id="presetNum8ID"]']

port = port_connect.Port()

class Visca():
    # 电源
    def visca_power(self):
        port.send(power_on)
        time.sleep(20)
        power1 = port.send(power_quire)
        power1 = port.send(power_quire)
        # time.sleep(2)
        port.send(power_off)
        time.sleep(20)
        power2 = port.send(power_quire)
        power2 = port.send(power_quire)
        print(power1, power2)
        port.send(power_on)
        time.sleep(20)
        port.send(PT_Home)
        time.sleep(10)
        if power1 == ['0x90', '0x50', '0x2', '0xff'] and power2 == ['0x90', '0x50', '0x3', '0xff']:
            return True
        else:
            return False
    def visca_zoom_focus(self):
        # port.send(PT_Home)
        # time.sleep(10)
        port.send(zoom0000_focus3bdf)
        time.sleep(10)
        zoom1 = port.send(Zoom_Quire)
        zoom1 = port.send(Zoom_Quire)
        focus1 = port.send(Focus_Quire)
        focus1 = port.send(Focus_Quire)
        port.send(zoom2000_focus4000)
        time.sleep(2)
        zoom2 = port.send(Zoom_Quire)
        zoom2 = port.send(Zoom_Quire)
        zoom2 = port.send(Zoom_Quire)
        focus2 = port.send(Focus_Quire)
        focus2 = port.send(Focus_Quire)
        port.send(zoom4000_focus4280)
        time.sleep(2)
        zoom3 = port.send(Zoom_Quire)
        zoom3 = port.send(Zoom_Quire)
        zoom3 = port.send(Zoom_Quire)
        focus3 = port.send(Focus_Quire)
        focus3 = port.send(Focus_Quire)
        time.sleep(2)
        print('zoom1', zoom1)
        print('zoom2', zoom2)
        print('zoom3', zoom3)
        print('focus1', focus1)
        print('focus2', focus2)
        print('focus3', focus3)
        if zoom1 != zoom2 and zoom2 != zoom3 and zoom1 != zoom3 and focus1 != focus2 and focus1 != focus3 and focus3 != focus2:
            return True
        else:
            return False

    def visca_Dzoom(self):
        # port.send(Dzoom_on)
        # Dzoom1 = port.send(Dzoom_stus_qurie)
        # Dzoom1 = port.send(Dzoom_stus_qurie)
        # port.send(Dzoom_off)
        # Dzoom2 = port.send(Dzoom_stus_qurie)
        # Dzoom2 = port.send(Dzoom_stus_qurie)
        # port.send(Dzoom_on)
        port.send(Dzoom_x1)
        Dzoom3 = port.send(Dzoom_qurie)
        Dzoom3 = port.send(Dzoom_qurie)
        port.send(Dzoom_x8)
        Dzoom4 = port.send(Dzoom_qurie)
        Dzoom4 = port.send(Dzoom_qurie)
        port.send(Dzoom_x12)
        Dzoom5 = port.send(Dzoom_qurie)
        Dzoom5 = port.send(Dzoom_qurie)
        # print('Dzoom1',Dzoom1)
        # print('Dzoom2',Dzoom2)
        print('Dzoom3',Dzoom3)
        print('Dzoom4',Dzoom4)
        print('Dzoom5',Dzoom5)
        if Dzoom3 ==['0x90', '0x50', '0x0', '0xff'] and Dzoom4 ==['0x90', '0x50', '0x7', '0xff'] and Dzoom5 == ['0x90','0x50','0xb','0xff']:
            return True
        else:
            return False

    #     zoom调节
    def visca_zoom(self,zoom_value):
        # port.send(PT_Home)
        # time.sleep(10)
        port.send(zoom_position_2000)
        time.sleep(5)
        zoom1 = port.send(Zoom_Quire)
        zoom1 = port.send(Zoom_Quire)
        zoom1 = port.send(Zoom_Quire)
        time.sleep(2)
        print(zoom1)
        port.send(zoom_value)
        time.sleep(3)
        port.send(zoom_stop)
        time.sleep(1)
        zoom2 = port.send(Zoom_Quire)
        zoom2 = port.send(Zoom_Quire)
        time.sleep(2)
        print(zoom2)
        if zoom1 == zoom2:
            return False
        else:
            return True

    #     focus调节
    def visca_focus(self,focus_value):
        port.send(PT_Home)
        time.sleep(6)
        port.send(focus_manual)
        time.sleep(2)
        focus1 = port.send(Focus_Quire)
        focus1 = port.send(Focus_Quire)
        print('focus1',focus1)
        port.send(focus_value)
        time.sleep(2)
        port.send(focus_stop)
        time.sleep(2)
        focus2 = port.send(Focus_Quire)
        focus2 = port.send(Focus_Quire)
        print('focus2', focus2)
        port.send(focus_auto)

        time.sleep(2)
        focus4 = port.send(Focus_mode_Quire)
        focus4 = port.send(Focus_mode_Quire)
        port.send(focus_value)
        time.sleep(2)
        port.send(focus_stop)
        time.sleep(2)
        focus3 = port.send(Focus_Quire)
        focus3 = port.send(Focus_Quire)
        time.sleep(1)
        print('自动聚焦：')
        print('focus4',focus4)
        print('focus3',focus3)


        port.send(focus_manual)
        focus5 = port.check(3,focus_one_push_trigger)
        # focus5 = port.send(Focus_mode_Quire)
        port.send(focus_manual_auto)
        focus6 = port.send(Focus_mode_Quire)
        focus6 = port.send(Focus_mode_Quire)
        port.send(focus_manual_auto)
        focus7 = port.send(Focus_mode_Quire)
        focus7 = port.send(Focus_mode_Quire)
        # print(focus5)
        print('focus5', focus5)
        print('focus6', focus6)
        print('focus7', focus7)


        if focus1 != focus2 and focus4 == ['0x90', '0x50', '0x2', '0xff'] and focus6!=focus7 and focus5 == True:
            return True
        else:
            return False

    #     白平衡模式切换
    def visca_WB(self,WB_value,WB_return):
        port.send(WB_value)
        wb1 = port.send(WB_Quire)
        wb1 = port.send(WB_Quire)
        wb1 = port.send(WB_Quire)
        print(wb1)
        print(WB_return)
        if wb1 == WB_return:
            return True
        else:
            return False

    #     白平衡红色增益
    def visca_WB_R_gian(self,WB_R_Gain_value):
        port.send(WB_manual)
        port.send(WB_R_Gain_default)
        R1 = port.send(WB_R_Gain_Quire)
        R1 = port.send(WB_R_Gain_Quire)
        print(R1)
        port.send(WB_R_Gain_value)
        time.sleep(1)
        R2 = port.send(WB_R_Gain_Quire)
        R2 = port.send(WB_R_Gain_Quire)
        print(R2)
        port.send(WB_R_Gain_default)
        time.sleep(1)
        R3 = port.send(WB_R_Gain_Quire)
        R3 = port.send(WB_R_Gain_Quire)
        print(R3)
        if R1 != R2 and R2 != R3:
            return True
        else:
            return False

    #     白平衡蓝色增益
    def visca_WB_B_gian(self,WB_B_Gain_value):
        port.send(WB_manual)
        port.send(WB_B_Gain_default)
        B1 = port.send(WB_B_Gain_Quire)
        B1 = port.send(WB_B_Gain_Quire)
        print(B1)
        port.send(WB_B_Gain_value)
        time.sleep(1)
        B2 = port.send(WB_B_Gain_Quire)
        B2 = port.send(WB_B_Gain_Quire)
        print(B2)
        time.sleep(1)
        port.send(WB_B_Gain_default)
        B3 = port.send(WB_B_Gain_Quire)
        B3 = port.send(WB_B_Gain_Quire)
        print(B3)
        if B1 != B2 and B2 != B3 and B1 == B3:
            return True
        else:
            return False

    #     白平衡一键触发
    def visca_WB_One_Push_Trigger(self):

        port.send(WB_one_push)
        time.sleep(6)

        # port.send(WB_one_push_trigger)
        # time.sleep(4)

        t = port.check(6,WB_one_push_trigger)
        t = port.check(6, WB_one_push_trigger)
        if t == True:
            return True
        else:
            return False

    # 自动白平衡红色增益
    def AWB_RGain(self):
        port.send(WB_auto)
        port.send(CAM_AWB_RGain_0)
        port.send(CAM_AWB_RGain_quire)
        r1 = port.send(CAM_AWB_RGain_quire)
        r1 = port.send(CAM_AWB_RGain_quire)
        r1 = port.send(CAM_AWB_RGain_quire)
        port.send(CAM_AWB_RGain_9)
        port.send(CAM_AWB_RGain_quire)
        r2 = port.send(CAM_AWB_RGain_quire)
        r2 = port.send(CAM_AWB_RGain_quire)
        r2 = port.send(CAM_AWB_RGain_quire)
        r2 = port.send(CAM_AWB_RGain_quire)
        port.send(CAM_AWB_RGain_14)
        port.send(CAM_AWB_RGain_quire)
        r3 = port.send(CAM_AWB_RGain_quire)
        r3 = port.send(CAM_AWB_RGain_quire)
        r3 = port.send(CAM_AWB_RGain_quire)
        r3 = port.send(CAM_AWB_RGain_quire)
        print(r1)
        print(r2)
        print(r3)
        if r1!=r2 and r3!=r2 and r1!=r3:
            return True
        else:
            return False

    # 自动白平衡蓝色增益
    def AWB_BGain(self):
        port.send(WB_auto)
        port.send(CAM_AWB_BGain_0)
        port.send(CAM_AWB_BGain_quire)
        r1 = port.send(CAM_AWB_BGain_quire)
        port.send(CAM_AWB_BGain_9)
        port.send(CAM_AWB_BGain_quire)
        r2 = port.send(CAM_AWB_BGain_quire)
        port.send(CAM_AWB_BGain_14)
        port.send(CAM_AWB_BGain_quire)
        r3 = port.send(CAM_AWB_BGain_quire)
        print(r1)
        print(r2)
        print(r3)
        if r1!=r2 and r3!=r2 and r1!=r3:
            return True
        else:
            return False

    # # 色温调节
    # def Color_Temperature(self):
    #     port.send(Color_Temperature)
    #     port.send(CAM_WB_Color_Temperature_0)
    #     port.send(CAM_WB_Color_Temperature_quire)
    #     r1 = port.send(CAM_WB_Color_Temperature_quire)
    #     r1 = port.send(CAM_WB_Color_Temperature_quire)
    #     r1 = port.send(CAM_WB_Color_Temperature_quire)
    #     port.send(CAM_WB_Color_Temperature_11)
    #     port.send(CAM_WB_Color_Temperature_quire)
    #     r2 = port.send(CAM_WB_Color_Temperature_quire)
    #     r2 = port.send(CAM_WB_Color_Temperature_quire)
    #     r2 = port.send(CAM_WB_Color_Temperature_quire)
    #     port.send(CAM_WB_Color_Temperature_25)
    #     port.send(CAM_WB_Color_Temperature_quire)
    #     r3 = port.send(CAM_WB_Color_Temperature_quire)
    #     r3 = port.send(CAM_WB_Color_Temperature_quire)
    #     r3 = port.send(CAM_WB_Color_Temperature_quire)
    #     print(r1)
    #     print(r2)
    #     print(r3)
    #     if r1 != r2 and r3 != r2 and r1 != r3:
    #         return True
    #     else:
    #         return False
        # 自动白平衡绿色增益

    def AWB_GGain(self):
        port.send(WB_auto)
        port.send(CAM_AWB_GGain_0)
        port.send(CAM_AWB_GGain_quire)
        r1 = port.send(CAM_AWB_GGain_quire)
        port.send(CAM_AWB_GGain_9)
        port.send(CAM_AWB_GGain_quire)
        r2 = port.send(CAM_AWB_GGain_quire)
        port.send(CAM_AWB_GGain_14)
        port.send(CAM_AWB_GGain_quire)
        r3 = port.send(CAM_AWB_GGain_quire)
        print(r1)
        print(r2)
        print(r3)
        if r1!=r2 and r3!=r2 and r1!=r3:
            return True
        else:
            return False

    #     曝光模式切换
    def visca_exposure(self,exposure_value,exposure_return):
        port.send(exposure_value)
        time.sleep(1)
        e1 = port.send(exposure_Quire)
        e1 = port.send(exposure_Quire)
        e1 = port.send(exposure_Quire)
        e1 = port.send(exposure_Quire)
        e1 = port.send(exposure_Quire)
        print('e1',e1)
        print('exposure_return',exposure_return)
        # port.send(Gain_12)
        # time.sleep(1)
        # g1 = port.send(Gain_quire)
        # print('g1',g1)
        # port.send(Gain_24)
        # time.sleep(1)
        # g2 = port.send(Gain_quire)
        # print('g2', g2)
        # port.send(Gain_45)
        # time.sleep(1)
        # g3 = port.send(Gain_quire)
        # print('g3', g3)
        # and g1 != g2 and g2 != g3 and g1 != g3
        if e1 == exposure_return:
            return True
        else:
            return False

    #     快门调节
    def visca_exposure_shutter(self,shutter_value):
        port.send(exposure_shutter)
        port.send(exposure_shutter_1_90)
        time.sleep(1)
        s1 = port.send(exposure_shutter_Quire)
        s1 = port.send(exposure_shutter_Quire)
        s1 = port.send(exposure_shutter_Quire)
        s1 = port.send(exposure_shutter_Quire)
        port.send(shutter_value)
        time.sleep(1)
        s2 = port.send(exposure_shutter_Quire)
        s2 = port.send(exposure_shutter_Quire)
        s2 = port.send(exposure_shutter_Quire)
        s2 = port.send(exposure_shutter_Quire)
        port.send(exposure_shutter_1_90)
        time.sleep(1)
        s3 = port.send(exposure_shutter_Quire)
        s3 = port.send(exposure_shutter_Quire)
        s3 = port.send(exposure_shutter_Quire)
        s3 = port.send(exposure_shutter_Quire)
        port.send(exposure_shutter_default)
        print(s1)
        print(s2)
        print(s3)
        if s1 != s2 and s1 == s3:
            return True
        else:
            return False

    #     光圈调节
    def visca_exposure_iris(self,iris_value):
        port.send(exposure_iris)
        port.send(exposure_iris_default)
        time.sleep(1)
        s1 = port.send(exposure_iris_Quire)
        s1 = port.send(exposure_iris_Quire)
        s1 = port.send(exposure_iris_Quire)
        s1 = port.send(exposure_iris_Quire)
        port.send(iris_value)
        time.sleep(1)
        s2 = port.send(exposure_iris_Quire)
        s2 = port.send(exposure_iris_Quire)
        s2 = port.send(exposure_iris_Quire)
        s2 = port.send(exposure_iris_Quire)
        port.send(exposure_iris_default)
        time.sleep(1)
        s3 = port.send(exposure_iris_Quire)
        s3 = port.send(exposure_iris_Quire)
        s3 = port.send(exposure_iris_Quire)
        s3 = port.send(exposure_iris_Quire)
        port.send(exposure_iris_default)
        print(s1)
        print(s2)
        print(s3)
        if s1 != s2 and s2 != s3 and s1 == s3:
            return True
        else:
            return False

    #     亮度调节
    def visca_exposure_bright(self,bright_value):
        port.send(Image_Mode_Custom)
        port.send(exposure_bright_default)
        time.sleep(1)
        s1 = port.send(exposure_bright_Qurie)
        s1 = port.send(exposure_bright_Qurie)
        s1 = port.send(exposure_bright_Qurie)
        port.send(bright_value)
        time.sleep(1)
        s2 = port.send(exposure_bright_Qurie)
        s2 = port.send(exposure_bright_Qurie)
        s2 = port.send(exposure_bright_Qurie)
        port.send(exposure_bright_default)
        time.sleep(1)
        s3 = port.send(exposure_bright_Qurie)
        s3 = port.send(exposure_bright_Qurie)
        s3 = port.send(exposure_bright_Qurie)
        port.send(exposure_bright_default)
        print('亮度1：',s1)
        print('亮度2：',s2)
        print('亮度3：',s3)
        if s1 != s2 and s1 == s3:
            return True
        else:
            return False

    #     曝光补偿状态
    def visca_ExpComp_status(self):
        port.send(exposure_auto)
        time.sleep(1)
        port.send(ExpComp_default)
        time.sleep(1)
        # s3 = port.send(ExpComp_status_quire)
        # s3 = port.send(ExpComp_status_quire)
        # s3 = port.send(ExpComp_status_quire)    # 状态为on
        port.send(ExpComp_on)
        time.sleep(1)
        s1 = port.send(ExpComp_status_quire)
        s1 = port.send(ExpComp_status_quire)
        s1 = port.send(ExpComp_status_quire)    # 状态为on
        port.send(ExpComp_off)
        time.sleep(1)
        s2 = port.send(ExpComp_status_quire)
        s2 = port.send(ExpComp_status_quire)
        s2 = port.send(ExpComp_status_quire)    # 状态为off
        port.send(ExpComp_on)
        time.sleep(1)
        s3 = port.send(ExpComp_status_quire)
        s3 = port.send(ExpComp_status_quire)
        s3 = port.send(ExpComp_status_quire)  # 状态为on
        print(s1)
        print(s2)
        print(s3)
        if s2 != s1 and s2 != s3:
            return True
        else:
            return False

    #     曝光补偿调节
    def visca_ExpComp(self,ExpComp_value):
        port.send(ExpComp_on)
        time.sleep(1)
        port.send(ExpComp_default)
        port.send(ExpComp_value_2)
        time.sleep(1)
        s1 = port.send(ExpComp_value_quire)
        s1 = port.send(ExpComp_value_quire)
        s1 = port.send(ExpComp_value_quire)
        port.send(ExpComp_value)
        time.sleep(1)
        s2 = port.send(ExpComp_value_quire)
        s2 = port.send(ExpComp_value_quire)
        s2 = port.send(ExpComp_value_quire)
        print(s1)
        print(s2)
        if s1 != s2:
            return True
        else:
            return False

    #    曝光增益调节
    def visca_exposure_Gain(self,exposure_Gain):
        port.send(exposure_manual)
        port.send(exposure_Gain_9)
        time.sleep(1)
        s1 = port.send(exposure_Gain_Quire)
        s1 = port.send(exposure_Gain_Quire)
        s1 = port.send(exposure_Gain_Quire)
        port.send(exposure_Gain)
        time.sleep(1)
        s2 = port.send(exposure_Gain_Quire)
        s2 = port.send(exposure_Gain_Quire)
        s2 = port.send(exposure_Gain_Quire)
        port.send(exposure_auto)
        print(s1)
        print(s2)
        if s1 != s2:
            return True
        else:
            return False

    #     背光补偿
    def visca_BackLight(self):
        port.send(BackLight_on)
        bl1 = port.send(BackLight_Quire)
        bl1 = port.send(BackLight_Quire)
        port.send(BackLight_off)
        bl2 = port.send(BackLight_Quire)
        bl2 = port.send(BackLight_Quire)
        print(bl1)
        print(bl2)
        if bl1 != bl2:
            return True
        else:
            return False

    #     宽动态
    def visca_WDR(self):
        port.send(WDR_3)
        w1 = port.send(WDR_Quire)
        w1 = port.send(WDR_Quire)
        port.send(WDR_2)
        w2 = port.send(WDR_Quire)
        w2 = port.send(WDR_Quire)
        port.send(WDR_1)
        w3 = port.send(WDR_Quire)
        w3 = port.send(WDR_Quire)
        port.send(WDR_OFF)
        w4 = port.send(WDR_Quire)
        w4 = port.send(WDR_Quire)
        if w1 != w2 and w3 != w4 and w1 != w3 and w2 != w4 and w1 != w4:
            return True
        else:
            return False

    #     锐度值调节
    def visca_Sharpness(self,Sharpness_value):
        port.send(Image_Mode_Custom)
        port.send(Sharpness_default)
        s1 = port.send(Sharpness_Quire)
        s1 = port.send(Sharpness_Quire)
        port.send(Sharpness_value)
        s2 = port.send(Sharpness_Quire)
        s2 = port.send(Sharpness_Quire)
        print(s1)
        print(s2)

        if s1 != s2:
            return True
        else:
            return False

    #     2D降噪
    def visca_2DNR(self,CAM_2DNR):
        port.send(CAM_2DNR_0ff)
        d1 = port.send(CAM_2DNR_Quire)
        d1 = port.send(CAM_2DNR_Quire)
        port.send(CAM_2DNR)
        d2 = port.send(CAM_2DNR_Quire)
        d2 = port.send(CAM_2DNR_Quire)
        print(d1)
        print(d2)
        if d1 != d2:
            return True
        else:
            return False

    #     3D降噪
    def visca_3DNR(self,CAM_3DNR):
        port.send(CAM_3DNR_0ff)
        d1 = port.send(CAM_3DNR_Quire)
        d1 = port.send(CAM_3DNR_Quire)
        port.send(CAM_3DNR)
        d2 = port.send(CAM_3DNR_Quire)
        d2 = port.send(CAM_3DNR_Quire)
        print(d1)
        print(d2)
        if d1 != d2:
            return True
        else:
            return False

    #     预置点
    def visca_preset(self,set_value,call_value,clear_value):
        port.send(PT_Home)
        time.sleep(8)
        port.send(data_up)
        time.sleep(3)
        port.send(data_stop)
        time.sleep(1)
        port.send(set_value)
        time.sleep(1)
        P1 = port.send(PT_Quire)
        P1 = port.send(PT_Quire)
        port.send(PT_Home)
        time.sleep(2)
        port.send(call_value)
        time.sleep(10)
        P2 = port.send(PT_Quire)
        P2 = port.send(PT_Quire)
        print(P1)
        print(P2)
        port.send(PT_Home)
        time.sleep(10)
        P3 = port.send(PT_Quire)
        P3 = port.send(PT_Quire)
        time.sleep(2)
        port.send(clear_value)
        port.send(call_value)
        time.sleep(10)
        P4 = port.send(PT_Quire)
        P4 = port.send(PT_Quire)
        print(P4)
        if P1 == P2 and P4 == P3:
            return True
        else:
            return False

    #     云台运转
    def Visca_pt(self,pt_value):
        port.send(PT_Home)
        time.sleep(8)
        pt1 = port.send(PT_Quire)
        pt1 = port.send(PT_Quire)
        print('pt1:',pt1)
        port.send(pt_value)
        time.sleep(3)
        port.send(data_stop)
        time.sleep(1)
        pt2 = port.send(PT_Quire)
        pt2 = port.send(PT_Quire)
        print('pt2:', pt2)
        port.send(PT_Reset)
        time.sleep(11)
        pt3 = port.send(PT_Quire)
        pt3 = port.send(PT_Quire)
        print('pt3:', pt3)
        if pt1 != pt2 and pt3 != pt2:
            return True
        else:
            return False

    #     视频格式
    def Visca_video_format(self,value,result):
        port.send(value)
        time.sleep(40)
        port.send(video_format_quire)
        port.send(video_format_quire)
        port.send(video_format_quire)
        port.send(video_format_quire)
        time.sleep(2)
        v1 = port.send(video_format_quire)
        v1 = port.send(video_format_quire)
        v1 = port.send(video_format_quire)
        v1 = port.send(video_format_quire)
        time.sleep(3)

        print('返回值：',result)
        print('result',v1)
        if v1 == result:
            return True
        else:
            return False

    # 红外地址状态
    def Visca_IR_Receive(self):
        port.send(IR_on)
        i1 = port.send(IR_quire)
        i1 = port.send(IR_quire)
        port.send(IR_off)
        i2 = port.send(IR_quire)
        i2 = port.send(IR_quire)
        port.send(IR_on_off)
        i3 = port.send(IR_quire)
        i3 = port.send(IR_quire)
        port.send(IR_on_off)
        i4 = port.send(IR_quire)
        i4 = port.send(IR_quire)
        if i1 != i2 and i3 != i4:
            return True
        else:
            return False

    #音量
    def audio_volume(self):
        port.send(audio_mode_on)
        # port.send(audio_volume_reset)
        # v1 = port.send(audio_volume_quire)  # 6
        # v1 = port.send(audio_volume_quire)
        # port.send(audio_volume_up)
        # v2 = port.send(audio_volume_quire)  # 7
        # v2 = port.send(audio_volume_quire)
        # port.send(audio_volume_down)
        # v3 = port.send(audio_volume_quire)  # 6
        # v3 = port.send(audio_volume_quire)
        port.send(audio_volume_00)
        time.sleep(1)
        v4 = port.send(audio_volume_quire)  # 0
        v4 = port.send(audio_volume_quire)
        port.send(audio_volume_03)
        time.sleep(1)
        v5 = port.send(audio_volume_quire)  # 3
        v5 = port.send(audio_volume_quire)
        # port.send(audio_volume_up)
        port.send(audio_volume_08)     # 8
        time.sleep(1)
        v6 = port.send(audio_volume_quire)
        v6 = port.send(audio_volume_quire)
        if v4 != v6 and v5 != v4 and v6 != v5:
            return True
        else:
            return False

    #  动态IP
    def IP_DHCP(self):
        port.send(IP_DHCP_on)
        time.sleep(5)
        p1 = port.send(IP_DHCP_quire)
        time.sleep(0.5)
        p1 = port.send(IP_DHCP_quire)
        port.send(IP_DHCP_off)
        time.sleep(5)
        p2 = port.send(IP_DHCP_quire)
        time.sleep(0.5)
        p2 = port.send(IP_DHCP_quire)
        port.send(IP_DHCP_on)
        time.sleep(5)
        p3 = port.send(IP_DHCP_quire)
        time.sleep(0.5)
        p3 = port.send(IP_DHCP_quire)
        print('on', p1)
        print('off', p2)
        print('on', p3)
        if p1 != p2 and p2 != p3:
            return True
        else:
            return False

    #  水平镜像
    def mirror(self):
        port.send(mirror_on)
        p1 = port.send(mirror_quire)
        p1 = port.send(mirror_quire)
        port.send(mirror_off)
        p2 = port.send(mirror_quire)
        p2 = port.send(mirror_quire)
        if p1 != p2:
            return True
        else:
            return False

    # 垂直镜像
    def filp(self):
        port.send(filp_on)
        p1 = port.send(filp_quire)
        p1 = port.send(filp_quire)
        port.send(filp_off)
        p2 = port.send(filp_quire)
        p2 = port.send(filp_quire)
        if p1 != p2:
            return True
        else:
            return False

    # 抗闪烁
    # def anti_flicker(self):
    #     port.send(exposure_auto)
    #     port.send(anti_flicker_off)
    #     p1 = port.send(anti_flicker_quire)
    #     p1 = port.send(anti_flicker_quire)
    #     port.send(anti_flicker_50Hz)
    #     p2 = port.send(anti_flicker_quire)
    #     p2 = port.send(anti_flicker_quire)
    #     port.send(anti_flicker_60Hz)
    #     p3 = port.send(anti_flicker_quire)
    #     p3 = port.send(anti_flicker_quire)
    #     print('关闭',p1)
    #     print('50Hz',p2)
    #     print('60Hz',p3)
    #     if p1 != p2 and p2 != p3 and p1 != p3 :
    #         return True
    #     else:
    #         return False

    # 伽马
    def gamma(self):
        port.send(Image_Mode_Custom)
        port.send(gamma_0)
        p1 = port.send(gamma_quire)
        p1 = port.send(gamma_quire)
        port.send(gamma_1)
        p2 = port.send(gamma_quire)
        p2 = port.send(gamma_quire)
        port.send(gamma_3)
        p3 = port.send(gamma_quire)
        p3 = port.send(gamma_quire)
        if p1 != p2 and p2 != p3 and p1 != p3 :
            return True
        else:
            return False

    # IP地址设置
    def set_IP_address(self, value):
        port.send(IP_DHCP_off)
        time.sleep(3)
        p1 = port.send(IP_address_quire)
        p1 = port.send(IP_address_quire)
        port.send(value)
        port.send(set_IP)
        p2 = port.send(IP_address_quire)
        p2 = port.send(IP_address_quire)
        print('IP地址1',p1)
        print('IP地址2',p2)
        if p1 != p2:
            return True
        else:
            return False

    # IP子网掩码设置
    def set_IP_mask(self,value):
        port.send(IP_DHCP_off)
        p1 = port.send(IP_mask_quire)
        p1 = port.send(IP_mask_quire)
        time.sleep(1)
        port.send(value)
        time.sleep(1)
        port.send(set_IP)
        time.sleep(1)
        p2 = port.send(IP_mask_quire)
        p2 = port.send(IP_mask_quire)

        if p1 != p2:
            return True
        else:
            return False

    def IP_mask(self,value):
        port.send(IP_DHCP_off)
        p1 = port.send(IP_mask_quire)
        p1 = port.send(IP_mask_quire)
        port.send(value)
        port.send(set_IP)
        p2 = port.send(IP_mask_quire)
        p2 = port.send(IP_mask_quire)

        if p1 != p2:
            return True
        else:
            return False

    # IP网关设置
    def set_IP_gateway(self,value):
        port.send(IP_DHCP_off)
        p1 = port.send(IP_gateway_quire)
        p1 = port.send(IP_gateway_quire)
        port.send(value)
        port.send(set_IP)
        p2 = port.send(IP_gateway_quire)
        p2 = port.send(IP_gateway_quire)

        if p1 != p2:
            return True
        else:
            return False

    # 锐度调节
    def CAM_Sharpness(self):

        port.send(CAM_Sharpness_0)
        port.send(CAM_Sharpness_quire)
        r1 = port.send(CAM_Sharpness_quire)
        port.send(CAM_Sharpness_9)
        port.send(CAM_Sharpness_quire)
        r2 = port.send(CAM_Sharpness_quire)
        port.send(CAM_Sharpness_11)
        port.send(CAM_Sharpness_quire)
        r3 = port.send(CAM_Sharpness_quire)
        if r1!=r2 and r3!=r2 and r1!=r3:
            return True
        else:
            return False

    # 亮度调节
    def CAM_Brightness(self):

        port.send(CAM_Brightness_0)
        port.send(CAM_Brightness_quire)
        r1 = port.send(CAM_Brightness_quire)
        port.send(CAM_Brightness_9)
        port.send(CAM_Brightness_quire)
        r2 = port.send(CAM_Brightness_quire)
        port.send(CAM_Brightness_14)
        port.send(CAM_Brightness_quire)
        r3 = port.send(CAM_Brightness_quire)
        if r1!=r2 and r3!=r2 and r1!=r3:
            return True
        else:
            return False

    # 对比度调节
    def CAM_Contrast(self):

        port.send(CAM_Contrast_0)
        port.send(CAM_Contrast_quire)
        r1 = port.send(CAM_Contrast_quire)
        port.send(CAM_Contrast_9)
        port.send(CAM_Contrast_quire)
        r2 = port.send(CAM_Contrast_quire)
        port.send(CAM_Contrast_14)
        port.send(CAM_Contrast_quire)
        r3 = port.send(CAM_Contrast_quire)
        if r1 != r2 and r3 != r2 and r1 != r3:
            return True
        else:
            return False

    # 饱和度调节
    def CAM_Saturation(self):

        port.send(CAM_Saturation_0)
        port.send(CAM_Saturation_quire)
        r1 = port.send(CAM_Saturation_quire)
        port.send(CAM_Saturation_9)
        port.send(CAM_Saturation_quire)
        r2 = port.send(CAM_Saturation_quire)
        port.send(CAM_Saturation_14)
        port.send(CAM_Saturation_quire)
        r3 = port.send(CAM_Saturation_quire)
        if r1 != r2 and r3 != r2 and r1 != r3:
            return True
        else:
            return False

    # 色调调节
    def CAM_Hue(self):

        port.send(CAM_Hue_0)
        port.send(CAM_Hue_quire)
        r1 = port.send(CAM_Hue_quire)
        port.send(CAM_Hue_9)
        port.send(CAM_Hue_quire)
        r2 = port.send(CAM_Hue_quire)
        port.send(CAM_Hue_14)
        port.send(CAM_Hue_quire)
        r3 = port.send(CAM_Hue_quire)
        if r1 != r2 and r3 != r2 and r1 != r3:
            return True
        else:
            return False