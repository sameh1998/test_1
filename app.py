import streamlit as st
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
import requests as rq
import gspread_dataframe as gd
import dataframe_image as dfi
import json
from google.oauth2.service_account import Credentials


text = st.text_input("User")
but = st.button("Apply")

def sen():
  file ={
    "type": "service_account",
    "project_id": "taager-344315",
    "private_key_id": "a193b57c858bff63e4a87841363b29398352402b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCb7xQEZcMkOnI/\nu2owGjftnnequ5bfdtHKvjzFakBeYikCsYr0XpOouaqT9ZqEKUWjaKcqH0QkLAz7\npLNs9UVmYfa1mEFJb3YGxiquyt+rJ8BTkstnlNbAcVoXQzrb3mJY4tLI92DiSLjN\neTTgMPjKUhJSlSXejr/fZdwnPKe6m2BzMckHYmemfwb9QO587hDGeXHqYtW29iZS\nDO+2t2I/LCwMXr9YvX8nTYzyb5X7uNxmnFFBwQ7FUrwZMPMenvdg6JiVO50sgRb8\n4UwY0Mu7/d6wxALEnLdfUJLw3Z+E9UwsqIdhL15w5BpMUaznf5fMVZwpDaUMqvOX\nSZcS7OZ7AgMBAAECggEAQ3DY9vfuOMaAcDkF+az1QHOXrQN6AscYgDfb/8Pu+AM7\nWntgLkWTVleKw3hnbj6NbFnQZsLkDULyEIoQwhCohdnbwnmJzxGCefaOMk/zAcrs\n/xhPmcqBQPUlckc09zAM2AWuBZYcVHIAX3nLGSWFDLgHTalNGh8iNCQRXfT5VBa/\nJkV1wNUclspwRtzAOMqVCyrGfpMewGe2bAVR7Ahg3Qx3fQEN6Tf8iLU4h59ESmVO\nedCNwgFxbgbJXLKSuZvWw0gTnYyirPQRS+9VL6l3j2xip6vBtcaR1BuRH/citw2z\nRLO6ZfiRWlUG6oRN8OZX6gKbu3iOwnFXZQcSEBZ6GQKBgQDVG1ehspelQrZoc8HW\nf9gU2uyDQsVkxhkAB9zk0PYVJrMSkajor12xvwKzA1Z8SgPm2ZqbF2EQD7tByfew\n0Kudyu0DK5lvBCQff1gQoQpEMIzjKxVbTwYJf1svXjuCXbZpVXU8QeApj1NI3O+s\n6D32Mam4I8g1qCms7YKyymjQ8wKBgQC7UdA+39LAzRNMLbKZ1mVMOBGqaY1qensR\nBcCE7AwoOD07esTEzISDm3o5oZJMSdmewl7T/y70BmtU55lA5Naz00qnJAqvOZEA\nNwrOE1dbGJODv1GtktJgxhoFAp6xmOESEF3kBfP/JdCpRBwakQ2Xk2VsRKKggv2e\nDQk3KDM2WQKBgFDzfPtYexB04hOVfVl84NkzPEq0T4VzVsXTNs7YrdHlDHsOR8pz\n6zR86YqUxwKZnxfPK1Kks+NFBo38KZHKApcDIbtlkXhBa3NnjU1rzxmOE8ardAZm\nY1WyQjIhKpvf+03R/6GvKHbBEhMIkibtZbQis2TWetQfGA2vf0lpaB2PAoGAOvoF\nUOZzmpR20PNKWjkwZ5D3runQxoeNm8xt0uvm3/rk/Ico0LV7u1wGXYLLZw2RYPTd\nmm2rwNUMkgzhKZdjKfcKeBlW69h6GNE7q6pXRK02NLLV6ophhmqY4p7yjAQQSPmy\nNgrRybGEQubY2lx1JRYZRr9NXLAhXdPI5P7ZMPECgYAsPSQGRsljwdUuNwWXy+L4\nTQ8pMJY49BP+2TiGwIsEvxhdyBrUY+xFLlYFHG6HD1jCdurS0C/TXjpsdPm7/gBh\nrEWo7ClplwS/jIYCdKopTdOwYiS4UX+qdmUbXZ0K0af2xvXAfCKFf5mL5/dYj9dC\nwKErWIM9Na+lsSnHDRv8Yg==\n-----END PRIVATE KEY-----\n",
    "client_email": "taager-1@taager-344315.iam.gserviceaccount.com",
    "client_id": "106445922971450067804",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/taager-1%40taager-344315.iam.gserviceaccount.com"
  }
  gc = gspread.service_account_from_dict(file)
  sh = gc.open_by_key('1KkxL8-h0JZqSI2u2wwV4i7CP-duIoNHU5cfBHf4s0EI')
  sheet = sh.get_worksheet(0)
  sheet.update('B1', text)
if but == True:
  sen()

