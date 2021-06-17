
import argparse,sys

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='Elije el primer numero para copiar')
    parser.add_argument('--y', type=float, default=1.0, help='Elije el segundo numero para copiar')
    parser.add_argument('--operation', type=str, default='add', help='Elije el primer numero para copiar')
    args = parser.parse_args()
    sys.stdout.write(str(calcular(args)))

def calcular(args):
    if args.operation == 'add':
        resultado=args.x + args.y
    return resultado


if __name__=='__main__':
    main()