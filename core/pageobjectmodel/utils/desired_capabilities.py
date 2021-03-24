import os


capabilities = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'emulator-5554',
    'automationName': 'UIAutomator2',
    'browserName': 'Chrome'
}


def get_desired_capabilities():
    """Get the desired capabilities to start the automation"""
    return capabilities