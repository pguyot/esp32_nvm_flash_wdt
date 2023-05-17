from pytest_embedded import Dut
import pytest

@pytest.mark.parametrize(
    'qemu_extra_args',
    [
        '-nic user,model=open_eth',
    ],
    indirect=True,
)
def test_esp32_nvs_flash_init_wdt(dut, redirect):
     dut.expect('calling nvs_flash_init')
     dut.expect('called nvs_flash_init')
