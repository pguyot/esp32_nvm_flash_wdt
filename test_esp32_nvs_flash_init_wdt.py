from pytest_embedded import Dut
import pytest

@pytest.mark.parametrize(
    'qemu_extra_args',
    [
        '-global driver=timer.esp32.timg,property=wdt_disable,value=true'
    ],
    indirect=True
)
def test_esp32_nvs_flash_init_wdt(dut, redirect):
     dut.expect('calling nvs_flash_init')
     dut.expect('called nvs_flash_init')
