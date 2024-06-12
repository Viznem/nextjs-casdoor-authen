import os
from dotenv import load_dotenv

load_dotenv()

from casdoor import CasdoorSDK


async def get_casdoor_sdk():

    sdk = CasdoorSDK(
        endpoint=os.environ["CASDOOR_SDK"],
        client_id=os.environ["CASDOOR_CLIENT_ID"],
        client_secret=os.environ["CASDOOR_CLIENT_SECRET"],
        certificate=os.environ["CASDOOR_CLIENT_CERTIFICATE"],
        org_name=os.environ["CASDOOR_CLIENT_ORG_NAME"],
        application_name=os.environ["CASDOOR_CLIENT_APPLICATION_NAME"],
    )

    return sdk
