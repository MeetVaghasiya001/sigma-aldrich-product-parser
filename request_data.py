import requests as re



def price_request(json_data):
    
    cookies = {
        'language': 'en',
        'language.sig': '-goeBrIUo_00rmLK97QbPVLsLvI',
        'country': 'IN',
        'country.sig': 'efXRLjKkHxNCfg-XyKN_vNs2Qek',
        'internalUser': 'false',
        'internalUser.sig': 'emYtgbC4IagMjhR7P9-PaWfiPxw',
        'GUID': '29c8e709-702d-41e6-a966-74a624cf425b|NULL|1775195425089',
        'GUID.sig': 'HPBgSPaNcZalf_I0j2xUORE_Zvo',
        'rxVisitor': '17751954265982KK5S5HEUKIL6E7A746C4D1SAMFBD80S',
        'OptanonAlertBoxClosed': '2026-04-03T05:50:34.178Z',
        '_sfid_7064': '{%22anonymousId%22:%22501435b82aa2044a%22}',
        '_evga_05cb': '{%22uuid%22:%22501435b82aa2044a%22}',
        '_fbp': 'fb.1.1775195435083.592584197207611017',
        'zaius_js_version': '2.4.2',
        'z_idsyncs': '',
        'vtsrc': 'source%3Ddirect%7Cmedium%3Dnone',
        '_gcl_au': '1.1.545118593.1775195436',
        '_ga': 'GA1.1.1906325685.1775195436',
        '_abck': '27AFDADE3213A50A826AD311F41F7A1F~0~YAAQKhzFFxLp8EudAQAAiBIuUw+xtWRuKvoeIEiVFERSlrptHP+Q52UclCUBhDvPaSNOKBlYBJQmkhq66J49QYELd2ddtd5X50Zg20KLD5sBvKS0wWHT2jFTRqD4/GH80RnL2LLuJHPYBHDOVBDAhNLJAkDtR4z0c+kt1piL6pS+7c2ksgBvZA9HK1o+QeEITu47NGwZxVkKVzk4N/jSsq9hntSqAubO+HdG9k8yt0AmqnrJwnfl0dWlq3TFTijmq8fHQWkcsxJLFrqmRy4PVFGiW/YpbwlnmzTL0hNTT3KEh8KnIhj4gYIxUAmFd70CtEjw7U4XfqRWyj9S/YUBrXv6gU6ZjLDTHTQeTQgkD330z1smYeqvk67yEV3oOrAoqp5ikUHEM0eci0y58jzv84rnImdUhc1/wAotGCOC/ZEZbFx4ptNSWJNocsf5jsPex9b7ovw28fVuSM2xeo/9RbBv2BvFS6gsNvjHgP5FMvpW4OQuL6cCqu1JFwZqYmHRCSyRsyTOAlv5rQk20oQAnFjFmfxHOXyadj5w7pVp9b6NMZ6N2F3gtTMWX5XReIumrfGzHdmAzsWS90ImcrVVSYVkyALJRaLA8fP2IcGXX+s8nq0KnkurJsKMJz37LyH6dzVwfudXSY4Y1FJQaeJu1sQq/MMimvTPBpm4tmnnB7L/e/6S~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2fx4bxT25Sw24teR1mWcqOVCk7V7GjpH2xqhma27YZDk6JluKT2jinzas+VR9wmZQpjWVfY0DwvYqbZ6xWMXTAeTinPBKwgqwsyU+4r2AgFzGDmXZuTGaA4XlHb+QOsvsHGl+D88%3d~-1',
        'accessToken': '0a879ee1-41f1-11f1-a74d-93109d1f9ac1',
        'accessToken.sig': '-9RtEjl5vG1KrqqrZ2ZgSn8eHo8',
        'optimizelySession': '0',
        'store': 'sial',
        'QSI_SI_57sUKVKAA517cJo_intercept': 'true',
        '_clck': 'ucob04%5E2%5Eg5o%5E0%5E2284',
        'dtCookie': 'v_4_srv_21_sn_4497EE535FD788FCB95D79419FC615D9_perc_100000_ol_0_mul_1_app-3A49e38e2e60c8cd4b_1',
        'userErpType': 'ANONYMOUS',
        'ak_bmsc': '29E01ECAAAAE87806BE46FBE11B0D606~000000000000000000000000000000~YAAQt/Q3F+LIQN2dAQAAJfzX4h/Tpq0jhQwDRXGArIoybiDXDB7YhzC9yQhJbLrCJphslBNV1KVWePXjvHabQfaoepCCls8Mk+DSzFn2MES4hW4g1faxG4YKZGw5CBiEU19qTrGqAvFJlke1DUyi1LsonkM2TyTbg6JCzannl7ynnpf9FkVkUIPmecKTc04jMo8pSRJp8rWUSquAWyR7iykhPyCQdlHZRPXISSIwmEi9wElkBOAj4WULUBCLj7aUvmvsDba0FRNiyyD9JpZrLEOdipDEWWwPWunCWB59fKsI6aGnIsgoL+z/YK7vtbSEDKxG7DJuwAixCi8XXsW4OaL9LD2owdM2yS7x5yYloPHcHbRzCBlZRBXSFfHIwbUjJ5WuYm+I0YZkjFx8Th/Wdpagfqf4sNJFh6F0Jql8tNDgiPVDTP6WoJn9HgHJTTGDiI8AQSFoDF0sZEkjlxzdZ5+hpSo=',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+May+01+2026+14%3A51%3A40+GMT%2B0530+(India+Standard+Time)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d2ae1e5a-5df5-4b21-9d1d-0bbc8eee20f8&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&crTime=1775195435196&geolocation=IN%3BGJ&AwaitingReconsent=false',
        'vuid': '08c84e89-c2b0-453c-bf62-727e08a53584%7C1777627301332',
        '_rdt_uuid': '1775195434470.71eae013-200c-474c-9ed5-bd287447acdc',
        'fs_lua': '1.1777627301732',
        'fs_uid': '#15R99F#c7683fb2-677b-479a-8116-974dd6a26c2e:f7002e70-3e61-44e8-83ec-098de77e4c42:1777627301732::1###/1806731507',
        '_clsk': 'w35kso%5E1777627310596%5E3%5E0%5El.clarity.ms%2Fcollect',
        'BVImplrow': '15557_2_0',
        '_ga_BQZS3WQYGJ': 'GS2.1.s1777627301$o10$g1$t1777627315$j46$l0$h1091971600',
        '_uetsid': '2a4e7920453f11f18b8bcddcbb065c5d|17jtrhi|2|g5o|0|2308',
        '_uetvid': '08c1f5302f2111f1896e251ece595b88|i5g64s|1777627311095|3|1|bat.bing.com/p/insights/c/l',
        'profileToken': 'eyJraWQiOiIxIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwOi8vYXV0aC1zZXJ2aWNlLXN2Yy5hdXRoLXNlcnZpY2Uuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4MC9hdXRoIiwic3ViIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwiaWF0IjoxNzc3NjI3MzIyLCJleHAiOjE3Nzg5MjMzMjIsInVzZXIiOnsic0lkIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwidHlwZSI6IkdVRVNUIiwibG9jYWxlIjoiZW5fSU4iLCJjb3VudHJ5IjoiSU4ifSwibmJmIjoxNzc3NjI3MzIyfQ.X7yvEPv1EeOC8JcOLkDmypKRICFcBgszHOVhBYDjkgMHe9eWB7epw7OtLG2h2euVM1dIPD4z1BC0UaRGzVIc0BLJUEqR_3ZNEcdIX_KSvz8bFdVAkxLaZJzOpGW1B5J8FmljxwmTfAwym730mqu71uaX3qlTJqhcE8hqD1f-mSZgQhB8x3f6AyVRy_GaD77GqRTapORvQtAhqSNjW7gNNSL1ltxfal-b5horgtVzJNtrbR_QNLAEFVQqFODEjWBolwW_AIhys4EzLDPQKhT9Rob58X0FzTfJwsIXNzPAr7TM19dbZEqEHxG_GE53tflpz4KOxvmNg9gQqoB5YNh5cA',
        'profileToken.sig': 'gWlpOeQ73DUgsArA5McxzzfsAz8',
        'bm_sv': '50DCEB713A6AC8A91FA04E2A74CF5E2F~YAAQt/Q3F5XTQN2dAQAAO3PY4h8rwDyHAIzOmIIvb3a8FHbY5bCmMUuoTqh77U9Cp3Qpat2lYUSmNyyEYykXqH5UIbCnqDE/yYt+p8zoxC3mtS0t+rxTYu7IRKTWULOfdDcpfSOtpDHl7rcnsX2fF328j3GUKzVHSh5tR2dVUi0m8pqfCcddcia4qTrFE7dMP6xP8AuqSLKXw1kyeeL1oMXbpn3tzXSXBBHvzf12Q+rrprli1UEuf7E2jhhRKXecTaK9YZwRPg==~1',
        'rxvt': '1777629130787|1777627296021',
        'dtPC': '21$427324617_580h6vCDPHRJLUEEFBJCUMTADHTPGHAKPVKCLM-0e0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.sigmaaldrich.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.sigmaaldrich.com/IN/en/product/supelco/26274',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-890f2ab8db3547033624c58c701a9b3b-7035004a177e7049-01',
        'tracestate': '693b3f36-e67c5af3@dtr=1;7035004a177e7049;1;49e38e2e60c8cd4b;17751954265982KK5S5HEUKIL6E7A746C4D1SAMFBD80S;CDPHRJLUEEFBJCUMTADHTPGHAKPVKCLM-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-dtpc': '21$427324617_580h6vCDPHRJLUEEFBJCUMTADHTPGHAKPVKCLM-0e0',
        'x-gql-access-token': '0a879ee1-41f1-11f1-a74d-93109d1f9ac1',
        'x-gql-country': 'IN',
        'x-gql-guid': 'GA1.1.1906325685.1775195436',
        'x-gql-language': 'en',
        'x-gql-operation-name': 'PricingAndAvailability',
        'x-gql-profile-token': 'eyJraWQiOiIxIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwOi8vYXV0aC1zZXJ2aWNlLXN2Yy5hdXRoLXNlcnZpY2Uuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4MC9hdXRoIiwic3ViIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwiaWF0IjoxNzc3NjI3MzIyLCJleHAiOjE3Nzg5MjMzMjIsInVzZXIiOnsic0lkIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwidHlwZSI6IkdVRVNUIiwibG9jYWxlIjoiZW5fSU4iLCJjb3VudHJ5IjoiSU4ifSwibmJmIjoxNzc3NjI3MzIyfQ.X7yvEPv1EeOC8JcOLkDmypKRICFcBgszHOVhBYDjkgMHe9eWB7epw7OtLG2h2euVM1dIPD4z1BC0UaRGzVIc0BLJUEqR_3ZNEcdIX_KSvz8bFdVAkxLaZJzOpGW1B5J8FmljxwmTfAwym730mqu71uaX3qlTJqhcE8hqD1f-mSZgQhB8x3f6AyVRy_GaD77GqRTapORvQtAhqSNjW7gNNSL1ltxfal-b5horgtVzJNtrbR_QNLAEFVQqFODEjWBolwW_AIhys4EzLDPQKhT9Rob58X0FzTfJwsIXNzPAr7TM19dbZEqEHxG_GE53tflpz4KOxvmNg9gQqoB5YNh5cA',
        'x-gql-requesting-website': 'SigmaAldrich',
        'x-gql-store': 'sial',
        'x-gql-user-erp-type': 'ANONYMOUS',
        # 'cookie': 'language=en; language.sig=-goeBrIUo_00rmLK97QbPVLsLvI; country=IN; country.sig=efXRLjKkHxNCfg-XyKN_vNs2Qek; internalUser=false; internalUser.sig=emYtgbC4IagMjhR7P9-PaWfiPxw; GUID=29c8e709-702d-41e6-a966-74a624cf425b|NULL|1775195425089; GUID.sig=HPBgSPaNcZalf_I0j2xUORE_Zvo; rxVisitor=17751954265982KK5S5HEUKIL6E7A746C4D1SAMFBD80S; OptanonAlertBoxClosed=2026-04-03T05:50:34.178Z; _sfid_7064={%22anonymousId%22:%22501435b82aa2044a%22}; _evga_05cb={%22uuid%22:%22501435b82aa2044a%22}; _fbp=fb.1.1775195435083.592584197207611017; zaius_js_version=2.4.2; z_idsyncs=; vtsrc=source%3Ddirect%7Cmedium%3Dnone; _gcl_au=1.1.545118593.1775195436; _ga=GA1.1.1906325685.1775195436; _abck=27AFDADE3213A50A826AD311F41F7A1F~0~YAAQKhzFFxLp8EudAQAAiBIuUw+xtWRuKvoeIEiVFERSlrptHP+Q52UclCUBhDvPaSNOKBlYBJQmkhq66J49QYELd2ddtd5X50Zg20KLD5sBvKS0wWHT2jFTRqD4/GH80RnL2LLuJHPYBHDOVBDAhNLJAkDtR4z0c+kt1piL6pS+7c2ksgBvZA9HK1o+QeEITu47NGwZxVkKVzk4N/jSsq9hntSqAubO+HdG9k8yt0AmqnrJwnfl0dWlq3TFTijmq8fHQWkcsxJLFrqmRy4PVFGiW/YpbwlnmzTL0hNTT3KEh8KnIhj4gYIxUAmFd70CtEjw7U4XfqRWyj9S/YUBrXv6gU6ZjLDTHTQeTQgkD330z1smYeqvk67yEV3oOrAoqp5ikUHEM0eci0y58jzv84rnImdUhc1/wAotGCOC/ZEZbFx4ptNSWJNocsf5jsPex9b7ovw28fVuSM2xeo/9RbBv2BvFS6gsNvjHgP5FMvpW4OQuL6cCqu1JFwZqYmHRCSyRsyTOAlv5rQk20oQAnFjFmfxHOXyadj5w7pVp9b6NMZ6N2F3gtTMWX5XReIumrfGzHdmAzsWS90ImcrVVSYVkyALJRaLA8fP2IcGXX+s8nq0KnkurJsKMJz37LyH6dzVwfudXSY4Y1FJQaeJu1sQq/MMimvTPBpm4tmnnB7L/e/6S~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2fx4bxT25Sw24teR1mWcqOVCk7V7GjpH2xqhma27YZDk6JluKT2jinzas+VR9wmZQpjWVfY0DwvYqbZ6xWMXTAeTinPBKwgqwsyU+4r2AgFzGDmXZuTGaA4XlHb+QOsvsHGl+D88%3d~-1; accessToken=0a879ee1-41f1-11f1-a74d-93109d1f9ac1; accessToken.sig=-9RtEjl5vG1KrqqrZ2ZgSn8eHo8; optimizelySession=0; store=sial; QSI_SI_57sUKVKAA517cJo_intercept=true; _clck=ucob04%5E2%5Eg5o%5E0%5E2284; dtCookie=v_4_srv_21_sn_4497EE535FD788FCB95D79419FC615D9_perc_100000_ol_0_mul_1_app-3A49e38e2e60c8cd4b_1; userErpType=ANONYMOUS; ak_bmsc=29E01ECAAAAE87806BE46FBE11B0D606~000000000000000000000000000000~YAAQt/Q3F+LIQN2dAQAAJfzX4h/Tpq0jhQwDRXGArIoybiDXDB7YhzC9yQhJbLrCJphslBNV1KVWePXjvHabQfaoepCCls8Mk+DSzFn2MES4hW4g1faxG4YKZGw5CBiEU19qTrGqAvFJlke1DUyi1LsonkM2TyTbg6JCzannl7ynnpf9FkVkUIPmecKTc04jMo8pSRJp8rWUSquAWyR7iykhPyCQdlHZRPXISSIwmEi9wElkBOAj4WULUBCLj7aUvmvsDba0FRNiyyD9JpZrLEOdipDEWWwPWunCWB59fKsI6aGnIsgoL+z/YK7vtbSEDKxG7DJuwAixCi8XXsW4OaL9LD2owdM2yS7x5yYloPHcHbRzCBlZRBXSFfHIwbUjJ5WuYm+I0YZkjFx8Th/Wdpagfqf4sNJFh6F0Jql8tNDgiPVDTP6WoJn9HgHJTTGDiI8AQSFoDF0sZEkjlxzdZ5+hpSo=; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+01+2026+14%3A51%3A40+GMT%2B0530+(India+Standard+Time)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d2ae1e5a-5df5-4b21-9d1d-0bbc8eee20f8&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&crTime=1775195435196&geolocation=IN%3BGJ&AwaitingReconsent=false; vuid=08c84e89-c2b0-453c-bf62-727e08a53584%7C1777627301332; _rdt_uuid=1775195434470.71eae013-200c-474c-9ed5-bd287447acdc; fs_lua=1.1777627301732; fs_uid=#15R99F#c7683fb2-677b-479a-8116-974dd6a26c2e:f7002e70-3e61-44e8-83ec-098de77e4c42:1777627301732::1###/1806731507; _clsk=w35kso%5E1777627310596%5E3%5E0%5El.clarity.ms%2Fcollect; BVImplrow=15557_2_0; _ga_BQZS3WQYGJ=GS2.1.s1777627301$o10$g1$t1777627315$j46$l0$h1091971600; _uetsid=2a4e7920453f11f18b8bcddcbb065c5d|17jtrhi|2|g5o|0|2308; _uetvid=08c1f5302f2111f1896e251ece595b88|i5g64s|1777627311095|3|1|bat.bing.com/p/insights/c/l; profileToken=eyJraWQiOiIxIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwOi8vYXV0aC1zZXJ2aWNlLXN2Yy5hdXRoLXNlcnZpY2Uuc3ZjLmNsdXN0ZXIubG9jYWw6ODA4MC9hdXRoIiwic3ViIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwiaWF0IjoxNzc3NjI3MzIyLCJleHAiOjE3Nzg5MjMzMjIsInVzZXIiOnsic0lkIjoiMGE4NzllZTEtNDFmMS0xMWYxLWE3NGQtOTMxMDlkMWY5YWMxIiwidHlwZSI6IkdVRVNUIiwibG9jYWxlIjoiZW5fSU4iLCJjb3VudHJ5IjoiSU4ifSwibmJmIjoxNzc3NjI3MzIyfQ.X7yvEPv1EeOC8JcOLkDmypKRICFcBgszHOVhBYDjkgMHe9eWB7epw7OtLG2h2euVM1dIPD4z1BC0UaRGzVIc0BLJUEqR_3ZNEcdIX_KSvz8bFdVAkxLaZJzOpGW1B5J8FmljxwmTfAwym730mqu71uaX3qlTJqhcE8hqD1f-mSZgQhB8x3f6AyVRy_GaD77GqRTapORvQtAhqSNjW7gNNSL1ltxfal-b5horgtVzJNtrbR_QNLAEFVQqFODEjWBolwW_AIhys4EzLDPQKhT9Rob58X0FzTfJwsIXNzPAr7TM19dbZEqEHxG_GE53tflpz4KOxvmNg9gQqoB5YNh5cA; profileToken.sig=gWlpOeQ73DUgsArA5McxzzfsAz8; bm_sv=50DCEB713A6AC8A91FA04E2A74CF5E2F~YAAQt/Q3F5XTQN2dAQAAO3PY4h8rwDyHAIzOmIIvb3a8FHbY5bCmMUuoTqh77U9Cp3Qpat2lYUSmNyyEYykXqH5UIbCnqDE/yYt+p8zoxC3mtS0t+rxTYu7IRKTWULOfdDcpfSOtpDHl7rcnsX2fF328j3GUKzVHSh5tR2dVUi0m8pqfCcddcia4qTrFE7dMP6xP8AuqSLKXw1kyeeL1oMXbpn3tzXSXBBHvzf12Q+rrprli1UEuf7E2jhhRKXecTaK9YZwRPg==~1; rxvt=1777629130787|1777627296021; dtPC=21$427324617_580h6vCDPHRJLUEEFBJCUMTADHTPGHAKPVKCLM-0e0',
    }

    params = {
        'operation': 'PricingAndAvailability',
    }

    

    response = re.post('https://www.sigmaaldrich.com/api', params=params, cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:
        return response.text 
    else:
        print(response.status_code,response.text)
        return None





