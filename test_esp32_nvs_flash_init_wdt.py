from pytest_embedded import Dut
import pytest

def test_esp32_nvs_flash_init_wdt(dut, redirect):
     dut.expect('calling nvs_flash_init')
     dut.expect('called nvs_flash_init')
