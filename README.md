# Demo Holidaycheck - very simple Page Object Model usage

Testing popular holiday website using [Appium](https://www.appium.io) test framework and Python.

## Android device only supported

# Quick setup
First install dependencies for python
```bash
pip install -r requirements
```

In order to use real or emulated device edit `desired_capabilities.py` file and change values in dictionary:
```python
capabilities = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'emulator-5554',
    'automationName': 'UIAutomator2',
    'browserName': 'Chrome'
}
```

## Launch test case
Execute `pytest` command in main directory.

## Use case
1. Navigate to homepage of http://www.holidaycheck.de
2. Click search
3. Input "Berlin" and select first suggested result
4. Confirm that all search result contain "Berlin" in the result title