import ghasedakpack
import sms
import ghasedak_sms



# sms_api = ghasedakpack.Ghasedak("96ace8f39eea950aafd08c0975e1d794745ada543f8a4d28c10aef6fe7814640DKYqvoBvZpmJmctL")
# sms.verification({'receptor': '09180148821', 'type': '1', 'template': 'Ghasedak', 'code': '1234'})

import ghasedak_sms
sms_api = ghasedak_sms.Ghasedak('96ace8f39eea950aafd08c0975e1d794745ada543f8a4d28c10aef6fe7814640DKYqvoBvZpmJmctL')
response = sms_api.get_account_information()
response = sms_api.send_single_sms( receptor='09180148821', linenumber='09180148821', senddate='Ghasedak', checkid='1234')
