# # # test_link_shortener.py
# # import pytest
# # from linkshorten import link_shortener, link_opener  # Import the original function

# # # Test data

# # link_to_shorten = "https://www.youtube.com/watch?v=8kIbvtCZSkU&list=RDMM&index=3"
# # shortened_link = link_shortener(link_to_shorten)

# # shortened_link2 = "https://tinyurl.com/2clqwroy"
# # original_link = link_opener(shortened_link2)



# # def test_link_shortener():
# #     assert link_shortener(link_to_shorten) == shortened_link # Ensure the link shortener function returns the expected shortened link

# # def test_link_opener(): 
# #     assert link_opener(shortened_link2) == original_link # Ensure the link opener function returns the expected original link



# # test_linkshorten.py
# import pytest
# from unittest.mock import Mock, patch
# from linkshorten import link_shortener, link_opener
# import requests

# # Test data
# TEST_LONG_URL = "https://www.example.com/very/long/url"
# TEST_SHORT_URL = "https://tinyurl.com/abc123"

# def test_link_shortener():
#     """Test the URL shortening functionality"""
#     with patch('linkshorten.pyshorteners.Shortener') as mock_shortener:
#         # Setup mock
#         mock_instance = mock_shortener.return_value
#         mock_instance.tinyurl.short.return_value = TEST_SHORT_URL
        
#         # Call function
#         result = link_shortener(TEST_LONG_URL)
        
#         # Verify results
#         assert result == TEST_SHORT_URL
#         mock_instance.tinyurl.short.assert_called_once_with(TEST_LONG_URL)

# def test_link_opener():
#     """Test the URL expanding functionality"""
#     with patch('linkshorten.requests.get') as mock_get:
#         # Setup mock response
#         mock_response = Mock()
#         mock_response.url = TEST_LONG_URL
#         mock_get.return_value = mock_response
        
#         # Call function
#         result = link_opener(TEST_SHORT_URL)
        
#         # Verify results
#         assert result == TEST_LONG_URL
#         mock_get.assert_called_once_with(
#             TEST_SHORT_URL,
#             headers={
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#                 "Accept-Language": "en-US,en;q=0.9",
#                 "Accept-Encoding": "gzip, deflate, br", 
#                 "Connection": "keep-alive"
#             },
#             allow_redirects=True
#         )

# def test_link_shortener_error_handling():
#     """Test error handling in link_shortener"""
#     with patch('linkshorten.pyshorteners.Shortener') as mock_shortener:
#         mock_instance = mock_shortener.return_value
#         mock_instance.tinyurl.short.side_effect = Exception("API Error")
        
#         result = link_shortener(TEST_LONG_URL)
#         assert result == "Something went wrong!"

# def test_link_opener_error_handling():
#     """Test error handling in link_opener"""
#     with patch('linkshorten.requests.get') as mock_get:
#         # Create a proper requests exception
#         mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        
#         result = link_opener(TEST_SHORT_URL)
#         assert "Something went wrong! Error:" in result




# from sys import exit
from Cryptodome.Util.number import long_to_bytes
# from setup import get_primes

# e = 65537

# def gen_key(k):
#     """
#     Generates RSA key with k bits
#     """
#     p,q = get_primes(k//2)
#     N = p*q
#     d = inverse(e, (p-1)*(q-1))

#     return ((N,e), d)

# def encrypt(pubkey, m):
#     N,e = pubkey
#     return pow(bytes_to_long(m.encode('utf-8')), e, N)

# def main(flag):
#     pubkey, _privkey = gen_key(1024)
#     encrypted = encrypt(pubkey, flag)
#     return (pubkey[0], encrypted)

# if __name__ == "__main__":
#     flag = open('flag.txt', 'r').read()
#     flag = flag.strip()
#     N, cypher  = main(flag)
#     print("N:", N)
#     print("e:", e)
#     print("cyphertext:", cypher)
#     exit()


# print("d:", inverse(65537, 7017759783777436124393890865599362210828546257500727953025369070343183727011411316405605662185556711993814932628766159624640209796736191682373771162566))


N = 17294741120248668746996187403163193571167507219662107805729023978840300853946215010754077199445654976005566945973527717977741275367546563385411685767652138
e = 65537
d = 8243746553175277522428763878227795046610338557380175866200298763675361374131037592824612320269203896965651552943635387367542910130259045937361729278051865


# a = "8647 370560 124334 373498 093701 581596 785583 753609 831053 902864 511989 420150 426973 107505 377038 599722 827488 002783 472986 763858 988870 637683 773281 692705 842883 826069"
# print(a.replace(" ", ""))

p = 2
q = 8647370560124334373498093701581596785583753609831053902864511989420150426973107505377038599722827488002783472986763858988870637683773281692705842883826069

N = 17294741120248668746996187403163193571167507219662107805729023978840300853946215010754077199445654976005566945973527717977741275367546563385411685767652138
e = 65537
d = 8243746553175277522428763878227795046610338557380175866200298763675361374131037592824612320269203896965651552943635387367542910130259045937361729278051865

ciphertext = 16449503542631093160207894461700027058492836243420227588152837344884124838429696910767798808109270773090232101914883537169936589541541607735669865744137615  # The encrypted flag from the program

# Decrypt the ciphertext
plaintext_long = pow(ciphertext, d, N)

# Convert the long integer to bytes, then to a string
flag = long_to_bytes(plaintext_long).decode('utf-8')

print("Decrypted Flag:", flag)
