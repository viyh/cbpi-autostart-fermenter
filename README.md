# [cbpi-autostart-fermenter](https://github.com/viyh/cbpi-autostart-fermenter)

Plugin for [CraftBeerPi3](http://web.craftbeerpi.com/) [[GitHub](https://github.com/Manuel83/craftbeerpi3)] that auto starts a list of fermenters when CBPi3 starts, so that fermentation resumes where it left off before Pi restarts or power failures.

## Installation

* Clone the repo into the CBPi3 _plugins_ directory:
```
git clone https://github.com/viyh/cbpi-autostart-fermenter.git ~/craftbeerpi3/modules/plugins/AutoStartFermenter      ### CHANGE THIS TO YOUR CBPi3 DIRECTORY
```

* Restart CraftBeerPi3.
```
sudo /etc/init.d/craftbeerpiboot restart
```

## Usage
All you need to do is install the plugin and if needed, set the following parameters through the CBPi UI:

* `auto_start_fermenter_enabled` - Do you want to autostart fermenters on CBPi startup? Default: YES
* `auto_start_fermenter_list` - Autostart fermenters in this list (comma separated list) such as "1,2,5". Default: 1

## Author

* [Joe Richards](https://github.com/viyh)
