



USERNAME     = 'super.user.1'
PASSWORD     = 'X!16a99a4e'
CONSUMER_KEY = 'f3haancaj0vm4lkx2erk3uwdzy2elz00of513u5w'
TOKEN        = 'eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.Qjz0-kry1Yb7PH0Pw1PbRWrgaqsFYPbac3RHQ-eykk4'

# API server URL
BASE_URL  = "https://openlab.openbankproject.com"
API_VERSION  = "v3.0.0"
CONTENT_JSON  = { 'content-type'  : 'application/json' }
DL_TOKEN    = { 'Authorization' : f'DirectLogin token={TOKEN}' }

# # API server will redirect your browser to this URL, should be non-functional
# # You will paste the redirect location here when running the script
# CALLBACK_URI = 'http://127.0.0.1/cb'

BANKS = ['hsbc.01.hk.hsbc', 'hsbc.02.hk.hsbc', 'hsbc.01.uk.uk', 'hsbc.02.uk.uk']

# OUR_BANK     = 'gh.29.uk'

# # Our COUNTERPARTY account id (of the same currency)
# OUR_COUNTERPARTY = '8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0'
# COUNTERPARTY_BANK = 'gh.29.uk'
# # this following two fields are just used in V210
# OUR_COUNTERPARTY_ID = ''
# OUR_COUNTERPARTY_IBAN = ''


# # Our currency to use
# OUR_CURRENCY = 'GBP'

# # Our value to transfer
# # values below 1000 do not requre challenge request
# OUR_VALUE = '0.01'
# OUR_VALUE_LARGE = '1000.00'