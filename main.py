import click
from PIL import Image

@click.command()
@click.option('--origin-path', help='Original image path')
@click.option('--target-path', help='Target image path')
def blend_func(origin_path, target_path):
    origin = Image.open(origin_path)
    target = Image.open(target_path)

    origin.show("Origin")
    target.show("Target")

    result = Image.alpha_composite(target, origin)
    result.show("AlphaComposite(Target,Origin)")

    result_datas = []
    origin_datas = result.getdata()
    target_datas = target.getdata()
    for index in range(len(origin_datas)):
        if origin_datas[index][0] == target_datas[index][0] and origin_datas[index][1] == target_datas[index][1] and origin_datas[index][2] == target_datas[index][2]:
            result_datas.append((0, 0, 0, 0))
        else:
            result_datas.append(target_datas[index])
    
    result = Image.new("RGBA", origin.size)
    result.putdata(result_datas)
    result.show("XOR")

if __name__ == '__main__':
    blend_func()
