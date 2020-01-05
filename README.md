# cbpi-autostart-fermenter
Plugin for CraftBeerPi3 that auto starts a list of fermenters when CBPi3 starts, so that fermentation resumes where it left off before Pi restarts or power failures.

## Usage

All you need to do is install the plugin and if needed, set the following parameters through the CBPi UI:

* `auto_start_fermenter_enabled` - Do you want to autostart fermenters on CBPi startup? Default: YES
* `auto_start_fermenter_list` - Autostart fermenters in this list (comma separated list) such as "1,2,5". Default: 1
