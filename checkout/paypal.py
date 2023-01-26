import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUPSM2s4qGRc0VzrRREIxrETgP4HwJY0LCWWQX3zIH0OTsvuiUDCd5bzYZjeu1SKhgWV90hS6AOrwX7e"
        self.client_secret = "ECpcEGlBl8PSnztBvPHSUnFht5cWr_wV6ASU4DqIaQtL3-Eg-zOpT6Cq5vNSmbZAaFtV1dYerx2-3L0U"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
