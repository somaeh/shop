import ghasedakpack
import sms
def send_otp_code(phone_number, code):
    pass
    # sms_api = ghasedak_sms.Ghasedak('96ace8f39eea950aafd08c0975e1d794745ada543f8a4d28c10aef6fe7814640DKYqvoBvZpmJmctL')
    # params = {
    #     'sender': '',
    #     'receptor': 'phone_number',
    #     'message': f'{code}:کد تاییدشما '
    # }
    # response = sms_api.send_bulk_sms(params)

    # print(response)
    sms_api = ghasedakpack.Ghasedak('96ace8f39eea950aafd08c0975e1d794745ada543f8a4d28c10aef6fe7814640DKYqvoBvZpmJmctL')
   
    sms_api.verification({'receptor': 'phone_number', 'type': '1', 'template': 'Ghasedak', 'param1': '1234'})
    