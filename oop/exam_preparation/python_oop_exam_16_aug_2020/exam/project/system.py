from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        software_memory_consumption = sum([s.memory_consumption for s in System._software])
        hardware_total_memory = sum([h.memory for h in System._hardware])
        software_capacity_consumption = sum([s.capacity_consumption for s in System._software])
        hardware_total_capacity = sum([h.capacity for h in System._hardware])
        output_str = [
            "System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
            f"Total Operational Memory: {software_memory_consumption} / {hardware_total_memory}",
            f"Total Capacity Taken: {software_capacity_consumption} / {hardware_total_capacity}"
        ]
        return '\n'.join(output_str)

    @staticmethod
    def system_split():
        output_str = []

        for hardware in System._hardware:
            number_express_software = len([s for s in hardware.software_components if type(s).__name__ == 'ExpressSoftware'])
            number_light_software = len([s for s in hardware.software_components if type(s).__name__ == 'LightSoftware'])
            software_memory_consumption = sum(s.memory_consumption for s in hardware.software_components)
            software_capacity_consumption = sum(s.capacity_consumption for s in hardware.software_components)
            software_components = [s.name for s in hardware.software_components]
            hardware_type = 'Heavy' if type(hardware).__name__ == 'HeavyHardware' else 'Power'

            if not software_components:
                software_components = 'None'
            hardware_output = [
                f"Hardware Component - {hardware.name}",
                f"Express Software Components: {number_express_software}",
                f"Light Software Components: {number_light_software}",
                f"Memory Usage: {software_memory_consumption} / {hardware.memory}",
                f"Capacity Usage: {software_capacity_consumption} / {hardware.capacity}",
                f"Type: {hardware_type}",
                f"Software Components: {', '.join(software_components)}"
            ]
            output_str.extend(hardware_output)

        return '\n'.join(output_str)







