from __future__ import print_function
import time
import argparse

from heat import init_fields, iterate, write_field

try:
    from heat import iterate as itarate_py
    from heat_cy import iterate as iterate_cy
except ImportError as e:
    print(e)


def main(input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=200, image_interval=4000, program='python'):

    # Initialise the temperature field
    field, field0 = init_fields(input_file)

    print("Heat equation solver")
    print("Diffusion constant: {}".format(a))
    print("Input file: {}".format(input_file))
    print("Parameters")
    print("----------")
    print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1], dx, dy))
    print("  time steps={}  image interval={}".format(timesteps, image_interval))
    print("  program={}".format(program))

    iterate = iterate_cy if program == 'cython' else itarate_py
    
    # Plot/save initial field
    write_field(input_file, field, 0)
    # Iterate
    t0 = time.time()
    iterate(field, field0, a, dx, dy, timesteps)
    t1 = time.time()
    # Plot/save final field
    write_field(input_file, field, timesteps)

    print("Simulation finished in {0} s".format(t1-t0))
    return t1 - t0

if __name__ == '__main__':

    # Process command line arguments
    parser = argparse.ArgumentParser(description='Heat equation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-dx', type=float, default=0.01,
                        help='grid spacing in x-direction')
    parser.add_argument('-dy', type=float, default=0.01,
                        help='grid spacing in y-direction')
    parser.add_argument('-a', type=float, default=0.5,
                        help='diffusion constant')
    parser.add_argument('-n', type=int, default=200,
                        help='number of time steps')
    parser.add_argument('-i', type=int, default=4000,
                        help='image interval')
    parser.add_argument('-f', type=str, default='./data/bottle.dat', 
                        help='input file')
    parser.add_argument('-p', type=str, default='python',
                        help='program to use', choices=['python', 'cython'])

    args = parser.parse_args()

    main(args.f, args.a, args.dx, args.dy, args.n, args.i, args.p)

