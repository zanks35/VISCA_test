import allure
import pytest
from common import PT
zoom_t_standard = [0X81, 0x01, 0x04, 0x07, 0x02, 0xff]                                                     # ZOOM Tele定速
zoom_w_standard = [0X81, 0x01, 0x04, 0x07, 0x03, 0xff]                                                     # ZOOM Wide定速
zoom_t_variable_0= [0X81, 0x01, 0x04, 0x07, 0x20, 0xff]                                                    # ZOOM Tele变速:0
zoom_t_variable_7= [0X81, 0x01, 0x04, 0x07, 0x27, 0xff]                                                    # ZOOM Tele变速:7
zoom_t_variable_5= [0X81, 0x01, 0x04, 0x07, 0x25, 0xff]                                                    # ZOOM Tele变速:5
zoom_w_variable_0 = [0X81, 0x01, 0x04, 0x07, 0x30, 0xff]                                                   # ZOOM Wide变速:0
zoom_w_variable_7 = [0X81, 0x01, 0x04, 0x07, 0x37, 0xff]                                                   # ZOOM Wide变速:7
zoom_w_variable_5 = [0X81, 0x01, 0x04, 0x07, 0x35, 0xff]                                                   # ZOOM Wide变速:5
zoom_position_4000 = [0X81, 0x01, 0x04, 0x47, 0x04, 0x00, 0x00, 0x00, 0xff]  # ZOOM 直接到达指定位置:4000
zoom_position_2000 = [0X81, 0x01, 0x04, 0x47, 0x02, 0x00, 0x00, 0x00, 0xff]  # ZOOM 直接到达指定位置:2000
zoom_position_0000 = [0X81, 0x01, 0x04, 0x47, 0x00, 0x00, 0x00, 0x00, 0xff]  # ZOOM 直接到达指定位置:0000
focus_3bdf = [0X81, 0x01, 0x04, 0x48, 0x03, 0x0b, 0x0d, 0x0f, 0xff]                                   # FOCUS 直接到指定位置
focus_4778 = [0X81, 0x01, 0x04, 0x48, 0x04, 0x07, 0x07, 0x08, 0xff]                              # FOCUS 直接到指定位置
focus_far_standard = [0X81, 0x01, 0x04, 0x08, 0x02, 0xff]                                                     # FOCUS 定速far
focus_near_standard = [0X81, 0x01, 0x04, 0x08, 0x03, 0xff]                                                     # FOCUS 定速near
focus_far_0 = [0X81, 0x01, 0x04, 0x08, 0x20, 0xff]                                                   # FOCUS 变速速far:0
focus_far_7 = [0X81, 0x01, 0x04, 0x08, 0x27, 0xff]                                                   # FOCUS 变速速far:7
focus_far_5 = [0X81, 0x01, 0x04, 0x08, 0x25, 0xff]                                                   # FOCUS 变速速far:5
focus_near_0 = [0X81, 0x01, 0x04, 0x08, 0x30, 0xff]                                                   # FOCUS 变速 near:0
focus_near_7= [0X81, 0x01, 0x04, 0x08, 0x37, 0xff]                                                    # FOCUS 变速 near:7
focus_near_5= [0X81, 0x01, 0x04, 0x08, 0x35, 0xff]                                                    # FOCUS 变速 near:5
focus_stop = [0X81, 0x01, 0x04, 0x08, 0x00, 0xff]                                                     # FOCUS 停止
WB_manual = [0x81, 0x01, 0x04, 0x35, 0x05, 0xFF]                                                     # 设置手动白平衡模式
WB_Quire = [0x81, 0x09, 0x04, 0x35, 0xff]                                                           # 查询白平衡模式
WB_auto = [0x81, 0x01, 0x04, 0x35, 0x00, 0xFF]                                                     #设置自动白平衡模式
WB_indoor = [0x81, 0x01, 0x04, 0x35, 0x01, 0xFF]                                                   # 白平衡 室内
WB_outdoor = [0x81, 0x01, 0x04, 0x35, 0x02, 0xFF]                                                   # 白平衡 户外
WB_one_push = [0x81, 0x01, 0x04, 0x35, 0x03, 0xFF]                                                     # 白平衡一键白平衡
WB_AWB = [0x81, 0x01, 0x04, 0x35, 0x05, 0xFF]                                                   # 白平衡AWB
WB_ATW = [0x81, 0x01, 0x04, 0x35, 0x04, 0xFF]                                                   # Color_Temperature
WB_sodium_lamp = [0x81, 0x01, 0x04, 0x35, 0x0C, 0xFF]                                                   # 白平衡钠灯
WB_one_push_trigger = [0x81, 0x01, 0x04, 0x10, 0x05, 0xFF]                                                   # 白平衡one push trigger
WB_R_Gain_default = [0x81, 0x01, 0x04, 0x03, 0x00, 0xFF]                                                     # 白平衡 RGAIN恢复默认
WB_R_Gain_up= [0x81, 0x01, 0x04, 0x03, 0x02, 0xFF]                                                      # 白平衡 R增益向上调节
WB_R_Gain_down = [0x81, 0x01, 0x04, 0x03, 0x03, 0xFF]                                                     # 白平衡 R增益向下调节
WB_R_Gain_0 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x00, 0x00, 0xFF]                                   # 白平衡 R增益指定到达的位置:0
WB_R_Gain_16 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x01, 0x00, 0xFF]                                # 白平衡 R增益指定到达的位置:16
WB_R_Gain_7 = [0x81, 0x01, 0x04, 0x43, 0x00, 0x00, 0x00, 0x01, 0xFF]                                # 白平衡 R增益指定到达的位置:7
WB_R_Gain_Quire = [0x81, 0x09, 0x04, 0x43, 0xFF]                                                           # 查询红色增益值
WB_B_Gain_Quire = [0x81, 0x09, 0x04, 0x44, 0xFF]                                                           #查询蓝色增益值
WB_B_Gain_default = [0x81, 0x01, 0x04, 0x04, 0x00, 0xFF]                                                     # 白平衡 BGAIN恢复默认
WB_B_Gain_up = [0x81, 0x01, 0x04, 0x04, 0x02, 0xFF]                                                     # 白平衡 B向上调节
WB_B_Gain_down = [0x81, 0x01, 0x04, 0x04, 0x03, 0xFF]                                                     # 白平衡 B向下调节
WB_B_Gain_0 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x00, 0x00, 0xFF]                                   # 白平衡 B指定到达的位置:0
WB_B_Gain_16 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x01, 0x00, 0xFF]                                   # 白平衡 B指定到达的位置:16
WB_B_Gain_7 = [0x81, 0x01, 0x04, 0x44, 0x00, 0x00, 0x00, 0x01, 0xFF]                                   # 白平衡 B指定到达的位置:7

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


exposure_auto = [0x81, 0x01, 0x04, 0x39, 0x00, 0xFF]                                                     # 设置自动曝光模式
exposure_manual = [0x81, 0x01, 0x04, 0x39, 0x03, 0xFF]                                                     # 设置手动曝光模式
exposure_iris = [0x81, 0x01, 0x04, 0x39, 0x0B, 0xFF]                                                     # 设置光圈优先模式
exposure_shutter = [0x81, 0x01, 0x04, 0x39, 0x0A, 0xFF]                                                     # 设置快门优先模式
exposure_white_board = [0x81, 0x01, 0x04, 0x39, 0x5F, 0xFF]                                                     # 设置白板模式
# exposure_bright = [0x81, 0x01, 0x04, 0x39, 0x0D, 0xFF]                                                     # 设置亮度优先模式
exposure_Quire = [0x81, 0x09, 0x04, 0x39, 0xFF]                                                           # 曝光模式查询命令

exposure_shutter_default = [0x81, 0x01, 0x04, 0x0A, 0x00,0xFF]                                                      # 快门数值恢复默认
exposure_shutter_up = [0x81, 0x01, 0x04, 0x0A, 0x02, 0xFF]                                                     # 快门数值向上调整
exposure_shutter_down = [0x81, 0x01, 0x04, 0x0A, 0x03, 0xFF]                                                     # 快门数值向下调整
exposure_shutter_Quire = [0x81, 0x09, 0x04, 0x4A, 0xFF]                                                           #快门数值查询
exposure_shutter_1_90 = [0x81, 0x01, 0x04, 0x4A,0x00, 0x00,0x00,0x07,0xFF]                                       # 快门直接调整到：0
exposure_shutter_1_60 = [0x81, 0x01, 0x04, 0x4A,0x00, 0x00,0x00,0x06,0xFF]                                       # 快门直接调整到：0
exposure_shutter_1_10000 = [0x81, 0x01, 0x04, 0x4A,0x00, 0x00,0x00,0x00,0xFF]                                       # 快门直接调整到：0

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
exposure_bright_15 = [0x81, 0x01, 0x04, 0x4D, 0x00,0x00,0x00,0x0F,0xFF]                                       #亮度数值到指定位置：15
exposure_bright_27 = [0x81, 0x01, 0x04, 0x4D, 0x00,0x00,0x01,0x0B,0xFF]                                       #亮度数值到指定位置：27

exposure_Gain_Quire = [0x81, 0x09, 0x04, 0x4C, 0xFF]                                                             #曝光增益查询
exposure_Gain_up = [0x81, 0x01, 0x04, 0x0C, 0x02,0xFF]                                                         #曝光增益向上调整
exposure_Gain_down = [0x81, 0x01, 0x04, 0x0C, 0x03,0xFF]                                                         #曝光增益向下调整
exposure_Gain_default = [0x81, 0x01, 0x04, 0x0C, 0x00,0xFF]                                                         #曝光增益恢复默认值
exposure_Gain_0 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x00,0xFF]                                          #曝光增益数值到指定位置：0
exposure_Gain_14 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x0E,0xFF]                                          #曝光增益数值到指定位置：14
exposure_Gain_8 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x08,0xFF]                                          #曝光增益数值到指定位置：8
exposure_Gain_30 = [0x81, 0x01, 0x04, 0x4C, 0x00,0x00,0x00,0x1E,0xFF]                                          #曝光增益数值到指定位置：32

ExpComp_on= [0x81, 0x01, 0x04, 0x3E, 0x02, 0xFF]                                                        #曝光补偿打开
ExpComp_off= [0x81, 0x01, 0x04, 0x3E, 0x03, 0xFF]                                                       #曝光补偿关闭
ExpComp_default= [0x81, 0x01, 0x04, 0x0E, 0x00, 0xFF]                                                       #曝光补偿恢复默认值
ExpComp_up= [0x81, 0x01, 0x04, 0x0E, 0x02, 0xFF]                                                       #曝光补偿数值向上
ExpComp_down= [0x81, 0x01, 0x04, 0x0E, 0x03, 0xFF]                                                       #曝光补偿数值向下
ExpComp_status_quire= [0x81, 0x09, 0x04, 0x3E,0xFF]                                                              #曝光补偿状态查询
ExpComp_value_quire= [0x81, 0x09, 0x04, 0x4E,0xFF]                                                              #曝光补偿数值查询
ExpComp_value_f7= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x00,0xFF]                                     #曝光补偿数值设置为-7
ExpComp_value_0= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x07,0xFF]                                     #曝光补偿数值设置为0

ExpComp_value_7= [0x81, 0x01, 0x04, 0x4E,0x00, 0x00, 0x00, 0x04,0xFF]                                    #曝光补偿数值设置为7

BackLight_Quire= [0x81, 0x09, 0x04, 0x33, 0xFF]                                                             #背光补偿状态查询
BackLight_on= [0x81, 0x01, 0x04, 0x33, 0x02, 0xFF]                                                       #背光补偿打开
BackLight_off= [0x81, 0x01, 0x04, 0x33, 0x03, 0xFF]                                                       #背光补偿关闭
WDR_5 =[0x81, 0x01, 0x04, 0x3D, 0x05, 0xFF]                  #宽动态5
WDR_2 =[0x81, 0x01, 0x04, 0x3D, 0x02, 0xFF]                  #宽动态2
WDR_1 =[0x81, 0x01, 0x04, 0x3D, 0x01, 0xFF]                  #宽动态1
WDR_OFF =[0x81, 0x01, 0x04, 0x3D, 0x00, 0xFF]                #宽动态关闭

Sharpness_default=[0x81, 0x01, 0x04, 0x02, 0x00, 0xFF]                #锐度值恢复默认值
Sharpness_up=[0x81, 0x01, 0x04, 0x02, 0x02, 0xFF]                #锐度值增加
Sharpness_down=[0x81, 0x01, 0x04, 0x02, 0x03, 0xFF]                #锐度值减小
Sharpness_0=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x00,0xFF]                #设置锐度值0
Sharpness_1=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x01,0xFF]                #设置锐度值1
Sharpness_8=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x08,0xFF]                #设置锐度值8
Sharpness_11=[0x81, 0x01, 0x04, 0x42, 0x00, 0x00, 0x00,0x0B,0xFF]                #设置锐度值11

CAM_2DNR_Quire =[0x81, 0x09, 0x04, 0x53, 0xFF]                #2DNR值查询
CAM_2DNR_0ff =[0x81, 0x01, 0x04, 0x53, 0x00,0xFF]                #2DNR关闭
CAM_2DNR_1 =[0x81, 0x01, 0x04, 0x53, 0x01,0xFF]                #2DNR值为1
CAM_2DNR_2 =[0x81, 0x01, 0x04, 0x53, 0x02,0xFF]                #2DNR值为2
CAM_2DNR_3 =[0x81, 0x01, 0x04, 0x53, 0x03,0xFF]                #2DNR值为3

CAM_3DNR_Quire =[0x81, 0x09, 0x04, 0x54, 0xFF]                 #3DNR值查询
CAM_3DNR_0ff =[0x81, 0x01, 0x04, 0x54, 0x00,0xFF]              #3DNR关闭
CAM_3DNR_1 =[0x81, 0x01, 0x04, 0x54, 0x01,0xFF]                #3DNR值为1
CAM_3DNR_2 =[0x81, 0x01, 0x04, 0x54, 0x02,0xFF]                #3DNR值为2
CAM_3DNR_3 =[0x81, 0x01, 0x04, 0x54, 0x03,0xFF]                #3DNR值为7

clear_0 =   [0x81,0x01,0x04,0x3f,0x00,0x00,0xff]                                                       # 清除0预置位
set_0 =     [0x81,0x01,0x04,0x3f,0x01,0x00,0xff]                                                       # 设置0预置位
call_0 =    [0x81,0x01,0x04,0x3f,0x02,0x00,0xff]                                                       # 调用0预置位
clear_1 =   [0x81,0x01,0x04,0x3f,0x00,0x01,0xff]                                                       # 清除1预置位
set_1 =     [0x81,0x01,0x04,0x3f,0x01,0x01,0xff]                                                       # 设置1预置位
call_1 =    [0x81,0x01,0x04,0x3f,0x02,0x01,0xff]                                                       # 调用1预置位
clear_127 = [0x81,0x01,0x04,0x3f,0x00,0x7f,0xff]                                                       # 清除127预置位
set_127 =   [0x81,0x01,0x04,0x3f,0x01,0x7f,0xff]                                                       # 设置127预置位
call_127 =  [0x81,0x01,0x04,0x3f,0x02,0x7f,0xff]                                                       # 调用127预置位

clear_128 = [0x81,0x01,0x04,0x3f,0x10,0x00,0xff]                                                       # 清除128预置位
set_128 =   [0x81,0x01,0x04,0x3f,0x11,0x00,0xff]                                                       # 设置128预置位
call_128 =  [0x81,0x01,0x04,0x3f,0x12,0x00,0xff]                                                       # 调用128预置位
clear_255 = [0x81,0x01,0x04,0x3f,0x10,0x7f,0xff]                                                       # 清除255预置位
set_255 =   [0x81,0x01,0x04,0x3f,0x11,0x7f,0xff]                                                       # 设置255预置位
call_255 =  [0x81,0x01,0x04,0x3f,0x12,0x7f,0xff]                                                       # 调用255预置位

data_up = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x01, 0xff]  # 云台向上，速度：5，5
data_down = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x02, 0xff]  # 云台向下，速度：5，5
data_left = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x03, 0xff]  # 云台向左，速度：5，5
data_right = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x03, 0xff]  # 云台向右，速度：5，5
data_stop = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x03, 0x03, 0xff]  # 云台停止，速度：5，5
PT_UpLeft = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x01, 0xff]  # 云台左上，速度：5，5
PT_UpRight = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x01, 0xff]  # 云台右上，速度：5，5
PT_DownLeft = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x01, 0x02, 0xff]  # 云台左下，速度：5，5
PT_DownRight = [0X81, 0x01, 0x06, 0x01, 0x05, 0x05, 0x02, 0x02, 0xff]  # 云台右下，速度：5，5
PT_absolute = [0X81, 0x01, 0x06, 0x02, 0x05, 0x05, 0x00, 0x09, 0x09, 0x00, 0x00, 0x05, 0x01, 0x00, 0xff]  # 云台右下，速度：5，5
PT_relative = [0X81, 0x01, 0x06, 0x03, 0x05, 0x05, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0xff]  # 云台右下，速度：5，5

video_format_quire = [0x81, 0x09, 0x06, 0x23, 0xFF]                                                           # 视频格式查询命令
video_format_1080p60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x07, 0xFF]                                               # 视频格式设置：1080p60
video_format_1080p30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0A, 0xFF]                                               # 视频格式设置：1080p30
# video_format_1080i60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x02, 0xFF]                                               # 视频格式设置：1080i60
video_format_720p60 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0D, 0xFF]                                               # 视频格式设置：720p60
# video_format_720p30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x04, 0xFF]                                               # 视频格式设置：720p30
# video_format_4kp30 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x07, 0xFF]                                               # 视频格式设置：4kp30
video_format_1080p50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x09, 0xFF]                                               # 视频格式设置：1080p50
video_format_1080p25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0C, 0xFF]                                               # 视频格式设置：1080p25
# video_format_1080i50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0A, 0xFF]                                               # 视频格式设置：1080i50
video_format_720p50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0F, 0xFF]                                               # 视频格式设置：720p50
# video_format_720p25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0C, 0xFF]                                               # 视频格式设置：720p25
# video_format_4Kp50 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0E, 0xFF]                                               # 视频格式设置：4Kp50
# video_format_4Kp25 = [0x81, 0x01, 0x06, 0x35, 0x00, 0x0F, 0xFF]                                               # 视频格式设置：4Kp25

set_IP = [0x81, 0x01, 0x08, 0x07, 0x09,  0xFF]

set_IP_address_10_0_8_241 = [0x81, 0x01, 0x08, 0x07, 0x01, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x0f, 0x01, 0xFF]
set_IP_address_1_0_0_0 = [0x81, 0x01, 0x08, 0x07, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF]
set_IP_address_255_255_255_255 = [0x81, 0x01, 0x08, 0x07, 0x01, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xFF]
set_IP_address_10_0_8_156 = [0x81, 0x01, 0x08, 0x07, 0x01, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x09, 0x0c, 0xFF]

set_IP_mask_10_0_8_241 = [0x81, 0x01, 0x08, 0x07, 0x02, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x0f, 0x01, 0xFF]
set_IP_mask_1_0_0_0 = [0x81, 0x01, 0x08, 0x07, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF]
set_IP_mask_255_255_255_255 = [0x81, 0x01, 0x08, 0x07, 0x02, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xFF]
set_IP_mask_255_255_255_0 = [0x81, 0x01, 0x08, 0x07, 0x02, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x00, 0x00, 0xFF]

set_IP_getway_10_0_8_241 = [0x81, 0x01, 0x08, 0x07, 0x03, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x0f, 0x01, 0xFF]
set_IP_getway_1_0_0_0 = [0x81, 0x01, 0x08, 0x07, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF]
set_IP_getway_255_255_255_255 = [0x81, 0x01, 0x08, 0x07, 0x03, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0xFF]
set_IP_getway_10_0_8_1 = [0x81, 0x01, 0x08, 0x07, 0x03, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x08, 0x00, 0x01, 0xFF]

zoom_list = [(zoom_t_standard,'zoom_t_standard'),(zoom_w_standard,'zoom_w_standard'),(zoom_t_variable_0,'zoom_t_variable_0'),(zoom_t_variable_7,'zoom_t_variable_7'),(zoom_t_variable_5,'zoom_t_variable_5'),(zoom_w_variable_0,'zoom_w_variable_0'),(zoom_w_variable_7,'zoom_w_variable_7'),(zoom_w_variable_5,'zoom_w_variable_5')]
focus_list = [(focus_far_standard,'focus_far_standard'), (focus_near_standard,'focus_near_standard'), (focus_far_0,'focus_far_0'),
              (focus_far_7,'focus_far_7'), (focus_far_5,'focus_far_5'),(focus_near_0,'focus_near_0'), (focus_near_7,'focus_near_7'),
              (focus_near_5,'focus_near_5'), (focus_3bdf,'focus_3bdf'), (focus_4778,'focus_74778')]
WB_list = [WB_auto,WB_indoor,WB_outdoor,WB_one_push,WB_AWB,WB_ATW,WB_sodium_lamp]
WB_return_list = [['0x90', '0x50', '0x0', '0xff'],
                  ['0x90', '0x50', '0x1', '0xff'],
                  ['0x90', '0x50', '0x2', '0xff'],
                  ['0x90', '0x50', '0x3', '0xff'],
                  ['0x90', '0x50', '0x5', '0xff'],
                  ['0x90', '0x50', '0x4', '0xff'],
                  ['0x90', '0x50', '0xc', '0xff']
                  ]
WB_title_list = [(WB_list[0],WB_return_list[0],'WB_auto'),
                 (WB_list[1],WB_return_list[1],'WB_indoor'),
                 (WB_list[2],WB_return_list[2],'WB_outdoor'),
                 (WB_list[3],WB_return_list[3],'WB_one_push'),
                 (WB_list[4],WB_return_list[4],'WB_AWB'),
                 (WB_list[5],WB_return_list[5],'WB_ATW'),
                 (WB_list[6],WB_return_list[6],'WB_sodium_lamp')]
exposure_list = [exposure_auto,exposure_manual,exposure_iris,exposure_shutter,exposure_white_board]
exposure_return_list = [['0x90', '0x50', '0x0', '0xff'],['0x90', '0x50', '0x3', '0xff'],['0x90', '0x50', '0xb', '0xff'],['0x90', '0x50', '0xa', '0xff'],['0x90', '0x50', '0x5f', '0xff']]
video_format_return_list = [['0x90', '0x50', '0x0', '0x0', '0xff'],['0x90', '0x50', '0x0', '0x1', '0xff'],
                            ['0x90', '0x50', '0x0', '0x2', '0xff'],['0x90', '0x50', '0x0', '0x3', '0xff'],
                            ['0x90', '0x50', '0x0', '0x4', '0xff'],['0x90', '0x50', '0x0', '0x5', '0xff'],
                            ['0x90', '0x50', '0x0', '0x6', '0xff'],['0x90', '0x50', '0x0', '0x7', '0xff'],
                            ['0x90', '0x50', '0x0', '0x8', '0xff'],['0x90', '0x50', '0x0', '0x9', '0xff'],
                            ['0x90', '0x50', '0x0', '0xa', '0xff'],['0x90', '0x50', '0x0', '0xb', '0xff'],
                            ['0x90', '0x50', '0x0', '0xc', '0xff'],['0x90', '0x50', '0x0', '0xd', '0xff'],
                            ['0x90', '0x50', '0x0', '0xe', '0xff'],['0x90', '0x50', '0x0', '0xf', '0xff']
                            ]
@allure.feature("visca命令测试")

class Test_visca():

    @allure.story("电源开关测试")
    # @allure.title("电源开关测试")
    # 电源开关测试
    def test_power(self):
        power_result = PT.Visca().visca_power()
        assert power_result == True

    # @allure.story("zoom测试")
    @allure.story("zoom测试")
    @allure.title("zoom测试 -{title}")

    # zoom测试
    @pytest.mark.parametrize('zoom_value,title', zoom_list)
    def test_zoom(self,zoom_value,title):
        zoom_result = PT.Visca().visca_zoom(zoom_value)
        assert zoom_result == True

    @allure.story("数字变倍测试")

    def test_Dzoom(self):
        Dzoom_result = PT.Visca().visca_Dzoom()
        assert Dzoom_result == True

    @allure.story("zoom,focus值测试")
    def test_zoom_focus(self):
        result = PT.Visca().visca_zoom_focus()
        assert result == True

    @allure.story("focus测试")
    @allure.title("focus测试 -{title}")
    # focus测试
    @pytest.mark.parametrize('focus_value,title',focus_list)
    def test_focus(self, focus_value,title):
        focus_result = PT.Visca().visca_focus(focus_value)
        assert focus_result == True

    @allure.story("白平衡模式切换测试")
    @allure.title("白平衡模式切换测试 -{title}")
    # 白平衡模式切换测试
    @pytest.mark.parametrize('WB_value,WB_return,title',[(WB_list[0],WB_return_list[0],'WB_auto'),
                                                         (WB_list[1],WB_return_list[1],'WB_indoor'),
                                                         (WB_list[2],WB_return_list[2],'WB_outdoor'),
                                                         (WB_list[3],WB_return_list[3],'WB_one_push'),
                                                         (WB_list[4],WB_return_list[4],'WB_AWB'),
                                                         (WB_list[5],WB_return_list[5],'Color_Temperature'),
                                                         (WB_list[6],WB_return_list[6],'WB_sodium_lamp')])
    def test_WB_t(self,WB_value,WB_return,title):
        WB_result = PT.Visca().visca_WB(WB_value,WB_return)
        assert WB_result == True

    @allure.story("白平衡红色增益测试")
    @allure.title("白平衡红色增益测试 -{title}")
    # 白平衡红色增益测试
    @pytest.mark.parametrize('WB_R_Gain_value,title',[(WB_R_Gain_up,'WB_R_Gain_up'),
                                                      (WB_R_Gain_down,'WB_R_Gain_down'),
                                                      (WB_R_Gain_0,'WB_R_Gain_0'),
                                                      (WB_R_Gain_16,'WB_R_Gain_16'),
                                                      (WB_R_Gain_7,'WB_R_Gain_7')])
    def test_WB_R_Gain(self,WB_R_Gain_value,title):
        test_WB_R_Gain_reselt = PT.Visca().visca_WB_R_gian(WB_R_Gain_value)
        assert test_WB_R_Gain_reselt == True

    @allure.story("白平衡蓝色增益测试")
    @allure.title("白平衡蓝色增益测试 -{title}")
    # 白平衡蓝色增益测试
    @pytest.mark.parametrize('WB_B_Gain_value,title',[(WB_B_Gain_up,'WB_B_Gain_up'),
                                                      (WB_B_Gain_down,'WB_B_Gain_down'),
                                                      (WB_B_Gain_0,'WB_B_Gain_0'),
                                                      (WB_B_Gain_16,'WB_B_Gain_16'),
                                                      (WB_B_Gain_7,'WB_B_Gain_7')])
    def test_WB_B_Gain(self,WB_B_Gain_value,title):
        test_WB_B_Gain_reselt = PT.Visca().visca_WB_B_gian(WB_B_Gain_value)
        assert test_WB_B_Gain_reselt == True

    @allure.story("自动白平衡红色增益测试")
    def test_AWB_RGain(self):
        result = PT.Visca().AWB_RGain()
        assert result == True

    @allure.story("自动白平衡绿色增益测试")
    def test_AWB_GGain(self):
        result = PT.Visca().AWB_GGain()
        assert result == True

    @allure.story("自动白平衡蓝色增益测试")
    def test_AWB_BGain(self):
        result = PT.Visca().AWB_BGain()
        assert result == True

    @allure.story("白平衡一键触发测试")
    # @allure.title("白平衡一键触发测试 -{title}")
    # 白平衡一键触发测试
    def test_visca_WB_One_Push_Trigger(self):
        One_Push_Trigger_result = PT.Visca().visca_WB_One_Push_Trigger()
        assert One_Push_Trigger_result == True

    @allure.story("曝光模式切换测试")
    @allure.title("曝光模式切换测试 -{title}")
    # 曝光模式切换测试
    @pytest.mark.parametrize('exposure_value,exposure_return,title',[(exposure_list[0],exposure_return_list[0],'exposure_auto'),
                                                                     (exposure_list[1],exposure_return_list[1],'exposure_manual'),
                                                                     (exposure_list[2],exposure_return_list[2],'exposure_iris'),
                                                                     (exposure_list[3],exposure_return_list[3],'exposure_shutter'),
                                                                     (exposure_list[4],exposure_return_list[4],'exposure_bright')])
    def test_visca_exposure(self,exposure_value,exposure_return,title):
        test_visca_exposure_reslut = PT.Visca().visca_exposure(exposure_value,exposure_return)
        assert test_visca_exposure_reslut == True

    @allure.story("快门测试")
    @allure.title("快门测试 -{title}")
    # 快门测试
    @pytest.mark.parametrize('shutter_value,title', [(exposure_shutter_up,'exposure_shutter_up'),
                                                     (exposure_shutter_down,'exposure_shutter_down'),
                                                     (exposure_shutter_1_10000,'exposure_shutter: 1/10000'),
                                                     (exposure_shutter_1_60,'exposure_shutter: 1/60')])
    def test_visca_exposure_shutter(self,shutter_value,title):
        test_shutter_reslut = PT.Visca().visca_exposure_shutter(shutter_value)
        assert test_shutter_reslut == True

    @allure.story("光圈测试")
    @allure.title("光圈测试 -{title}")
    # 光圈测试
    @pytest.mark.parametrize('iris_value,title', [(exposure_iris_up,'exposure_iris_up'),
                                                  (exposure_iris_down,'exposure_iris_down'),
                                                  (exposure_iris_close,'exposure_iris_close'),
                                                  (exposure_iris_F1_6,'exposure_iris_F1.6')])
    def test_visca_exposure_iris(self,iris_value,title):
        test_iris_reslut = PT.Visca().visca_exposure_iris(iris_value)
        assert test_iris_reslut == True

    @allure.story("亮度测试")
    @allure.title("亮度测试 -{title}")
    # 亮度测试
    @pytest.mark.parametrize('bright_value,title', [(exposure_bright_up,'exposure_bright_up'),
                                                    (exposure_bright_down,'exposure_bright_down'),
                                                    (exposure_bright_0,'exposure_bright_0'),
                                                    (exposure_bright_15,'exposure_bright_15')])
    def test_visca_exposure_bright(self,bright_value,title):
        test_bright_reslut = PT.Visca().visca_exposure_bright(bright_value)
        assert test_bright_reslut == True

    @allure.story("曝光补偿状态测试")
    # @allure.title("曝光补偿状态测试 -{title}")
    # 曝光补偿状态测试
    def test_visca_ExpComp_status(self):
        test_reslut = PT.Visca().visca_ExpComp_status()
        assert test_reslut == True

    @allure.story("曝光补偿调节测试")
    @allure.title("曝光补偿调节测试 -{title}")
    # 曝光补偿调节测试
    @pytest.mark.parametrize('ExpComp_value,title', [(ExpComp_value_0,'ExpComp_value: 0'),
                                                     (ExpComp_value_f7,'ExpComp_value: -7'),
                                                     (ExpComp_value_7,'ExpComp_value: 7'),
                                                     (ExpComp_up,'ExpComp_up'),
                                                     (ExpComp_down,'ExpComp_down')])
    def test_visca_ExpComp(self,ExpComp_value,title):
        test_reslut = PT.Visca().visca_ExpComp(ExpComp_value)
        assert test_reslut == True

    @allure.story("曝光增益调节测试")
    @allure.title("曝光增益调节测试 -{title}")
    # 曝光增益调节测试
    @pytest.mark.parametrize('exposure_Gain,title', [(exposure_Gain_up,'exposure_Gain_up'),
                                                     (exposure_Gain_down,'exposure_Gain_down'),
                                                     (exposure_Gain_0,'exposure_Gain_0'),
                                                     (exposure_Gain_8,'exposure_Gain_8'),
                                                     (exposure_Gain_30,'exposure_Gain_30'),
                                                     (exposure_Gain_14,'exposure_Gain_14')])
    def test_visca_exposure_Gain(self, exposure_Gain,title):
        test_reslut = PT.Visca().visca_exposure_Gain(exposure_Gain)
        assert test_reslut == True

    @allure.story("背光补偿测试")
    # @allure.title("背光补偿测试 -{title}")
    # 背光补偿测试
    def test_visca_BackLight(self):
        test_reslut = PT.Visca().visca_BackLight()
        assert test_reslut == True

    @allure.story("宽动态测试")
    # @allure.title("宽动态测试 -{title}")
    # 宽动态测试
    def test_visca_WDR(self):
        test_reslut = PT.Visca().visca_WDR()
        assert test_reslut == True

    @allure.story("锐度测试")
    @allure.title("锐度测试 -{title}")
    # 锐度测试
    @pytest.mark.parametrize('Sharpness_value,title', [(Sharpness_up,'Sharpness_up'),
                                                       (Sharpness_down,'Sharpness_up'),
                                                       (Sharpness_0,'Sharpness_0'),
                                                       (Sharpness_1,'Sharpness_1'),
                                                       (Sharpness_8,'Sharpness_8'),
                                                       (Sharpness_11,'Sharpness_11')])
    def test_visca_Sharpness(self,Sharpness_value,title):
        test_reslut = PT.Visca().visca_Sharpness(Sharpness_value)
        assert test_reslut == True

    @allure.story("2D降噪测试")
    @allure.title("2D降噪测试 -{title}")
    # 2D降噪测试
    @pytest.mark.parametrize('CAM_2DNR,title',[(CAM_2DNR_1,'CAM_2DNR_1'),
                                               (CAM_2DNR_2,'CAM_2DNR_2'),
                                               (CAM_2DNR_3,'CAM_2DNR_3')])
    def test_visca_2DNR(self, CAM_2DNR,title):
        test_reslut = PT.Visca().visca_2DNR(CAM_2DNR)
        assert test_reslut == True

    @allure.story("3D降噪测试")
    @allure.title("3D降噪测试 -{title}")
    # 3D降噪测试
    @pytest.mark.parametrize('CAM_3DNR,title',[(CAM_3DNR_1,'CAM_3DNR_1'),
                                               (CAM_3DNR_2,'CAM_3DNR_2'),
                                               (CAM_3DNR_3,'CAM_3DNR_3')])
    def test_visca_3DNR(self, CAM_3DNR,title):
        test_reslut = PT.Visca().visca_3DNR(CAM_3DNR)
        assert test_reslut == True

    @allure.story("预置点设置、调用测试")
    @allure.title("预置点设置、调用测试 -{title}")
    # 预置点设置、调用测试
    @pytest.mark.parametrize('set_value,call_value,clear_value,title',[[set_0,call_0,clear_0,'设置\调用\清除预置点0'],
                                                           [set_1,call_1,clear_1,'设置\调用\清除预置点1'],
                                                           [set_127,call_127,clear_127,'设置\调用\清除预置点127'],
                                                           [set_128, call_128, clear_128, '设置\调用\清除预置点128'],
                                                           [set_255,call_255,clear_255,'设置\调用\清除预置点255']])
    def test_visca_preset(self,set_value,call_value,clear_value,title):
        test_reslut = PT.Visca().visca_preset(set_value,call_value,clear_value)
        assert test_reslut == True

    @allure.story("云台运动测试")
    @allure.title("云台运动测试 -{title}")
    # 云台运动测试
    @pytest.mark.parametrize('pt,title', [(data_up,'云台向上运动'),
                                          (data_down,'云台向下运动'),
                                          (data_left,'云台向左运动'),
                                          (data_right,'云台向右运动'),
                                          (PT_UpLeft,'云台左上运动'),
                                          (PT_UpRight,'云台右上运动'),
                                          (PT_DownLeft,'云台左下运动'),
                                          (PT_DownRight,'云台右下运动'),
                                          (PT_absolute,'云台绝对运动'),
                                          (PT_relative,'云台相对运动')
                                          ])
    def test_visca_pt(self, pt,title):
        test_reslut = PT.Visca().Visca_pt(pt)
        assert test_reslut == True



    @allure.story("红外开关测试")
    def test_IR(self):
        result = PT.Visca().Visca_IR_Receive()
        assert result == True

    @allure.story("音量测试")
    def test_audio_volume(self):
        result = PT.Visca().audio_volume()
        assert result == True

    @allure.story("动态IP开关测试")
    def test_IP_DHCP(self):
        result = PT.Visca().IP_DHCP()
        assert result == True

    @allure.story("mirror开关测试")
    def test_mirror(self):
        result = PT.Visca().mirror()
        assert result == True

    @allure.story("filp开关测试")
    def test_filp(self):
        result = PT.Visca().filp()
        assert result == True

    # @allure.story("抗闪烁开关测试")
    # def test_flicker(self):
    #     result = PT.Visca().anti_flicker()
    #     assert result == True

    @allure.story("gamma测试")
    def test_gamma(self):
        result = PT.Visca().gamma()
        assert result == True

    # @allure.story("色温调节测试")
    # def test_Color_Temperature(self):
    #     result = PT.Visca().Color_Temperature()
    #     assert result == True

    @allure.story("图像锐度调节测试")
    def test_CAM_Sharpness(self):
        result = PT.Visca().CAM_Sharpness()
        assert result == True

    @allure.story("图像亮度调节测试")
    def test_CAM_Brightness(self):
        result = PT.Visca().CAM_Brightness()
        assert result == True

    @allure.story("图像对比度调节测试")
    def test_CAM_Contrast(self):
        result = PT.Visca().CAM_Contrast()
        assert result == True

    @allure.story("图像饱和度调节测试")
    def test_CAM_Saturation(self):
        result = PT.Visca().CAM_Saturation()
        assert result == True

    @allure.story("IP地址设置测试")
    @allure.title("IP地址设置测试 -{title}")
    @pytest.mark.parametrize('value,title', [(set_IP_address_10_0_8_241, 'set_IP_address: 10.0.8.241'),
                                                (set_IP_address_1_0_0_0, 'set_IP_address: 1.0.0.0'),
                                                (set_IP_address_255_255_255_255, 'set_IP_address: 255.255.255.255'),
                                                (set_IP_address_10_0_8_156, 'set_IP_address: 10.0.8.156')
                                             ])
    def test_IP_address(self,value,title):
        result = PT.Visca().set_IP_address(value)
        assert result == True

    @allure.story("IP子网掩码设置测试")
    @allure.title("IP子网掩码设置测试 -{title}")
    @pytest.mark.parametrize('value,title', [(set_IP_mask_10_0_8_241, 'set_IP_mask: 10.0.8.241'),
                                             (set_IP_mask_1_0_0_0, 'set_IP_mask: 1.0.0.0'),
                                             (set_IP_mask_255_255_255_255, 'set_IP_mask: 255.255.255.255'),
                                             (set_IP_mask_255_255_255_0, 'set_IP_mask: 255.255.255.0')
                                             ])
    def test_IP_mask(self, value,title):
        result = PT.Visca().IP_mask(value)
        assert result == True

    @allure.story("IP网关设置测试")
    @allure.title("IP网关设置测试 -{title}")
    @pytest.mark.parametrize('value,title', [(set_IP_getway_10_0_8_241, 'set_IP_gateway: 10.0.8.241'),
                                             (set_IP_getway_1_0_0_0, 'set_IP_gateway: 1.0.0.0'),
                                             (set_IP_getway_255_255_255_255, 'set_IP_gateway: 255.255.255.255'),
                                             (set_IP_getway_10_0_8_1, 'set_IP_gateway: 10.0.8.1')
                                             ])
    def test_IP_gateway(self, value, title):
        result = PT.Visca().set_IP_gateway(value)
        assert result == True

    @allure.story("视频格式切换测试")
    @allure.title("视频格式切换测试 -{title}")
    # 视频格式切换测试
    @pytest.mark.parametrize('value,result,title', [[video_format_1080p60, video_format_return_list[7], '1080p60'],
                                                    [video_format_1080p30, video_format_return_list[10], '1080p30'],
                                                    # [video_format_1080i60, video_format_return_list[2], '1080i60'],
                                                    [video_format_720p60, video_format_return_list[13], '720p60'],
                                                    # [video_format_720p30, video_format_return_list[4], '720p30'],
                                                    # [video_format_4kp60, video_format_return_list[5], '4kp60'],
                                                    # [video_format_4kp30, video_format_return_list[6], '4kp30'],
                                                    [video_format_1080p50, video_format_return_list[9], '1080p50'],
                                                    [video_format_1080p25, video_format_return_list[12], '1080p25'],
                                                    # [video_format_1080i50, video_format_return_list[9], '1080i50'],
                                                    [video_format_720p50, video_format_return_list[15], '720p50'],
                                                    # [video_format_720p25, video_format_return_list[11], '720p25'],
                                                    # [video_format_4Kp50, video_format_return_list[12], '4Kp50'],
                                                    # [video_format_4Kp25, video_format_return_list[13], '4Kp25']
                                                    ])
    def test_visca_video_format(self, value, result, title):
        test_reslut = PT.Visca().Visca_video_format(value, result)
        assert test_reslut == True

    def methods(self):
        list_function = list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and not m.endswith("methods") and callable(getattr(self, m)),
                            dir(self)))
        return (list_function)


