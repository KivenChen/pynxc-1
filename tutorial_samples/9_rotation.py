def main():


    SetSensor(IN_1, SENSOR_ROTATION); ClearSensor(IN_1)
    SetSensor(IN_3, SENSOR_ROTATION); ClearSensor(IN_3)
    
    while True:
        if SENSOR_1 < SENSOR_3:
            OnFwd(OUT_A, 75)
            Float(OUT_C)
        elif SENSOR_1 > SENSOR_3:
            OnFwd(OUT_C, 75)
            Float(OUT_A)
        else:
            OnFwd(OUT_AC, 75)
            

