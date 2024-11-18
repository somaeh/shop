import ghasedakpack
import sms

sms_api = ghasedakpack.Ghasedak('96ace8f39eea950aafd08c0975e1d794745ada543f8a4d28c10aef6fe7814640DKYqvoBvZpmJmctL')
message = 'hello, world!'
my_number_1 = '09180148821'
my_number_2 = '09388772372'
linenumber = '30005088'
response = sms.send({'message': message, 'receptor': my_number_1, 'linenumber': linenumber })
