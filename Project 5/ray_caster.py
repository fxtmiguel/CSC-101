import sys
import cast
import data
import commandline

if __name__ == '__main__':

    name = sys.argv[1]
    open_file = open(name, 'r')
    line_number = 0
    sph_list = []

    for line in open_file:
        line_number += 1
        spl_line = line.split(' ')
        try:
            data_line = [float(x) for x in spl_line]
            sph_list.append(data.Sphere(data.Point(data_line[0], data_line[1], data_line[2]),
                                        data_line[3], data.Color(data_line[4], data_line[5],
                                        data_line[6]), data.Finish(data_line[7], data_line[8],
                                        data_line[9], data_line[10])))
        except (ValueError, IndexError):
            print(f'malformed sphere on line {line_number} ... skipping')

    open_file.close()

    light = commandline.proc_light(sys.argv)
    eye_pt = commandline.proc_eye(sys.argv)
    amb = commandline.proc_amb(sys.argv)
    width = commandline.proc_view(sys.argv)[4]
    height = commandline.proc_view(sys.argv)[5]
    min_x = commandline.proc_view(sys.argv)[0]
    max_x = commandline.proc_view(sys.argv)[1]
    min_y = commandline.proc_view(sys.argv)[2]
    max_y = commandline.proc_view(sys.argv)[3]

    print('P3')
    print(width, height)
    print('255')
    cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_pt, sph_list, amb, light)
