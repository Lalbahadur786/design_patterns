
# Main concrete class
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None
        self.power_supply = None
        self.cooling = None
        self.rgb_lights = None
    
    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, gpu={self.gpu}, storage={self.storage},\
            power_supply={self.power_supply}, cooling={self.cooling}, rgb_lights={self.rgb_lights})"


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_power_supply(self, power_supply):
        self.computer.power_supply = power_supply
        return self
    
    def set_cooling(self, cooling):
        self.computer.cooling = cooling
        return self
    
    def set_rgb_lights(self, rgb):
        self.computer.rgb_lights = rgb
        return self
    
    def build(self):
        return self.computer

class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def build_office_computer(self):
        return ( self.builder
                .set_cpu('Intel')
                .set_ram('16 GB DDR5')
                .set_gpu('Intel 2 GB')
                .set_storage('500 GB SSD')
                .set_power_supply('500W')
                .build() )
    
    def build_gaming_computer(self):
        return (self.builder
                .set_cpu('AMD')
                .set_ram('64 GB DDR5')
                .set_gpu('NVIDIA GTX 8050')
                .set_storage('500 GB SSD')
                .set_power_supply('1000W')
                .set_cooling('AIO liquid cooler')
                .set_rgb_lights('RGB panels')
                .build())

if __name__ == "__main__":
    builder = ComputerBuilder()
    computer_director = ComputerDirector(builder)
    make_gaming_pc = computer_director.build_gaming_computer()
    print(f"Building gaming pc with: {make_gaming_pc}")

