#include <stdio.h>
#include <nvs_flash.h>

void app_main(void)
{
    printf("calling nvs_flash_init\n");
    nvs_flash_init();
    printf("called nvs_flash_init\n");
}
