import argparse

parser = argparse.ArgumentParser(description='Расчитаем зарплату')
parser.add_argument('hours', metavar='hours', type=int,
                    help='часы выработки')
parser.add_argument('rate', metavar='rate', type=int,
                    help='ставка')
parser.add_argument('bonus', metavar='bonus', type=int,
                    help='премия')

# args = parser.parse_args(['1', '2', '3'])
args = parser.parse_args()
print(args.hours*args.rate + args.bonus)
