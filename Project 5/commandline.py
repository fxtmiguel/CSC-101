import data

def proc_eye(commandline):
    eye = data.Point(0.0, 0.0, -14.0)
    try:
        if '-eye' in commandline:
            eye_flag = commandline.index('-eye')

            try:
                eye_x = float(commandline[eye_flag + 1])
            except ValueError:
                eye_x = 0.0
            try:
                eye_y = float(commandline[eye_flag + 2])
            except ValueError:
                eye_y = 0.0
            try:
                eye_z = float(commandline[eye_flag + 3])
            except ValueError:
                eye_z = -14.0

            eye = data.Point(eye_x, eye_y, eye_z)
    except IndexError:
        eye = data.Point(0.0, 0.0, -14.0)
    return eye

def proc_view(commandline):
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 512
    height = 384

    try:
        if '-view' in commandline:
            viewflag = commandline.index('-view')

            try:
                min_x = float(commandline[viewflag + 1])
            except ValueError:
                min_x = -10
            try:
                max_x = float(commandline[viewflag + 2])
            except ValueError:
                max_x = 10
            try:
                min_y = float(commandline[viewflag + 3])
            except ValueError:
                min_y = -7.5
            try:
                max_y = float(commandline[viewflag + 4])
            except ValueError:
                max_y = 7.5
            try:
                width = int(commandline[viewflag + 5])
            except ValueError:
                width = 512
            try:
                height = int(commandline[viewflag + 6])
            except ValueError:
                height = 384

    except IndexError:
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 512
        height = 384

    return [min_x, max_x, min_y, max_y, width, height]

def proc_amb(commandline):
    amb = data.Color(1.0, 1.0, 1.0)
    try:
        if '-ambient' in commandline:
            amb_flag = commandline.index('-ambient')

            try:
                amb_r = float(commandline[amb_flag + 1])
            except ValueError:
                amb_r = 1.0
            try:
                amb_g = float(commandline[amb_flag + 2])
            except ValueError:
                amb_g = 1.0
            try:
                amb_b = float(commandline[amb_flag + 3])
            except ValueError:
                amb_b = 1.0
            amb = data.Color(amb_r, amb_g, amb_b)
    except IndexError:
        amb = data.Color(1.0, 1.0, 1.0)
    return amb


def proc_light(commandline):
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    try:
        if '-light' in commandline:
            l_flag = commandline.index('-light')

            try:
                light_x = float(commandline[l_flag + 1])
            except ValueError:
                light_x = -100.0
            try:
                light_y = float(commandline[l_flag + 2])
            except ValueError:
                light_y = 100.0
            try:
                light_z = float(commandline[l_flag + 3])
            except ValueError:
                light_z = -100.0
            try:
                light_r = float(commandline[l_flag + 4])
            except ValueError:
                light_r = 1.5
            try:
                light_g = float(commandline[l_flag + 5])
            except ValueError:
                light_g = 1.5
            try:
                light_b = float(commandline[l_flag + 6])
            except ValueError:
                light_b = 1.5

            light = data.Light(data.Point(light_x, light_y, light_z), data.Color(light_r, light_g, light_b))
    except IndexError:
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    return light
