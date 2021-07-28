# Landroid Cloud

This component has been created to be used with Home Assistant.

Landroid Cloud presents a possibility to connect your cloud connected Worx Landroid mowers to Home Assistant.

## Credit

Credit for inspiring to this component goes to [virtualzone](https://github.com/virtualzone).

### Installation:

#### HACS

- Ensure that HACS is installed.
- Search for and install the "Landroid Cloud" integration.
- Restart Home Assistant.

#### Manual installation

- Download the latest release.
- Unpack the release and copy the custom_components/landroid_cloud directory into the custom_components directory of your Home Assistant installation.
- Restart Home Assistant.

### Example entry for configuration.yaml

```
landroid_cloud:
  - email: this@example.com
    password: YourPassword
```

You can add multiple accounts like in this example:

```
landroid_cloud:
  - email: this@example.com
    password: YourPassword
  - email: another@example.com
    password: AnotherPassword
```

If you have LandXcape or Kress robots you can add `type` to the config instead of default 'worx':

```
landroid_cloud:
  - email: this@example.com
    password: YourPassword
    type: landxcape
```

### Entities & Services

Once installed, the following entities are created in Home Assistant:

```
sensor.landroid_[NAME_FROM_APP]_battery
sensor.landroid_[NAME_FROM_APP]_error
sensor.landroid_[NAME_FROM_APP]_status
```

In addition, the following services are created:

```
landroid_cloud.start
landroid_cloud.home
landroid_cloud.pause
landroid_cloud.configure (can be used to set rain delay and time extension)
```

You can simply add these to your Lovelace setup by adding an entity card. A recommended Lovelace layout is being considered for a future release.

### Known bugs

If upgrading from version lower than 1.4, please comment out the landroid_cloud section from configuration.yaml, restart Home Assistant, reinsert the landroid_cloud section and restart again.

### Other useful information
#### Services and app stopped working

You might experience being banned from Worx Landroid Cloud service.
Follow this simple guide to make it work again:
* Go to [My Landroids](https://account.worxlandroid.com/product-items)
* Unlink your Landroid(s)
* Open app on mobile device
* Add Landroid(s)

### To-do

* Add proper integration flow
* Code optimization
* Make this an official integration
* Make this vacuum compatible - might make this easier to move to a mower "domain" if/when this is made available in Home Assistant
