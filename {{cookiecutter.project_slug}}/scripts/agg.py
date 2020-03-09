import click

# Placeholder test to combine multiple files

@click.command()
@click.argument('out_file', nargs=1)
@click.argument('in_file', nargs=-1)
def rec(out_file, in_file):
    # print("Agg")
    print(in_file)
    print(out_file)
    with open(out_file, 'w') as f:
        for l in in_file:
            f.write(l+'\n')

if __name__ == '__main__':
    rec()
