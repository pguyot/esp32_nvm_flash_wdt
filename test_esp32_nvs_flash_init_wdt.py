from pytest_embedded import Dut
import pytest

@pytest.mark.parametrize(
    'qemu_prog_path,qemu_cli_args',
    [
        ('taskset', '-c 1 qemu-system-xtensa -nographic -machine esp32')
    ],
    indirect=True,
)
def test_esp32_nvs_flash_init_wdt(dut, redirect):
     dut.expect('calling nvs_flash_init')
     dut.expect('called nvs_flash_init')
