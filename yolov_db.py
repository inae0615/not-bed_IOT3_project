#yolov5_detect.py
#162 줄/

import time
import pymysql

 # Write results

                for *xyxy, conf, cls in reversed(det):

                    db_name = names[int(c)]
                    percent = float(conf)
#db연동/삽입
                    conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="yolov5")
                    cur = conn.cursor()
                    cur.execute("insert into detect (date, name, conf) values(default, '''{0}''', {1:0.5f})".format(db_name, percent))
                    conn.commit()
                    time.sleep(0)
                    
# 감지결과에 따른 카카오톡 전송

                    cnt = 0
                    while(1):
                        if db_name == 'np' and percent >= 0.4 and cnt == 0:
                            exec(open("app.py").read())
                            print("{0:0.3f}% 확률로 침대에 사람이 없습니다".format(percent*100))
                            cnt = 1
                        elif db_name == 'yp':
                            print("{0:0.3f}% 확률로 침대에 사람이 있습니다".format(percent*100))
                            cnt = 0
                            break
                        elif db_name == 'np' and percent < 0.4:
                            print("{0:0.3f}% 확률로 침대에 사람이 없을 수도 있습니다.".format(percent*100))
                            cnt = 0
                            break



