import click

from mix import calculate


@ click.command()
@ click.option('--n', required=True, prompt='Whats your desired N ratio?', type=int)
@ click.option('--p', required=True, prompt='Whats your desired P ratio?', type=int)
@ click.option('--k', required=True, prompt='Whats your desired K ratio?', type=int)
@ click.option('--fn', required=True, prompt='Your fertilizer N content?', type=int)
@ click.option('--fp', required=True, prompt='Your fertilizer P content?', type=int)
@ click.option('--fk', required=True, prompt='Your fertilizer K content?', type=int)
@ click.option('--coverage', required=True, prompt='What\'s your nitrogen coverage in pounds per 1,000 ft square?', type=float)
@ click.option('--area', required=True, prompt='Coverage area in square feet?', type=int, default=1000)
def cli(n, p, k, fn, fp, fk, coverage, area):
    click.echo(f"Desired ratio {n}-{p}-{k}")
    click.echo(
        (f"Fertilizer content:\n\tNitrogen={fn}\n\tPhosphorus={fp}\n\tPotassium={fk}"))
    click.echo(f"Coverage is {coverage} lbs per 1,000 square feet")

    coverages = calculate(n, p, k, fn, fp, fk, coverage, area)
    nc = round(coverages[0], 3)
    pc = round(coverages[1], 3)
    kc = round(coverages[2], 3)

    click.echo(
        f"Coverages in pounds for {area} square feet.\n\tNitrogen: {nc} lbs\n\tPhosphorus: {pc} lbs\n\tPotassium: {kc} lbs")


if __name__ == '__main__':
    cli()
    # calculate(4, 1, 2, 45, 20, 60, .9, 5000)
