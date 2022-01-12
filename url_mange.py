from anti_useragent import UserAgent
class Urlmanage(object):
    def head1(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'cache-control': 'max-age=0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': UserAgent(min_version=50, max_version=80).random,
            'cookie': 'first_visit_datetime_pc=2022-01-06+13:10:18; p_ab_id=2; p_ab_id_2=6; p_ab_d_id=2017070122; __utmz=235335808.1641442221.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); yuid_b=IYh3WFA; _fbp=fb.1.1641442226524.867865018; _ga=GA1.2.1011429997.1641442221; PHPSESSID=36658176_Ik0UZUIinN2UVDtZ36wumEICitKYpfnS; device_token=6046abf27dcad150c035e997e31999ad; c_type=21; privacy_policy_notification=0; a_type=0; b_type=0; login_ever=yes; _gcl_au=1.1.124382889.1641442357; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^6=user_id=36658176=1^9=p_ab_id=2=1^10=p_ab_id_2=6=1^11=lang=zh=1; privacy_policy_agreement=3; adr_id=FK6Oc3ZcVqzvyo46F6J3iDLM8Q2aeqVM7joFuZvcldMOmWQd; _im_vid=01FRPSTPREG77BWCGWF0TAWWHS; p_b_type=1; _im_uid.3929=b.6dd7c319e074b4f8; __utmc=235335808; tags_sended=1; categorized_tags=IVwLyT8B6k~RcahSSzeRf~_-agXPKuAQ~qiO14cZMBI; _gid=GA1.2.149545487.1641800553; __utma=235335808.1011429997.1641442221.1641800539.1641805707.10; __utmt=1; __cf_bm=IjpztpOQs3g87bPZvauxL7sWuWQHDZ4RQcR1btSMTrc-1641807660-0-AWvQ1Wgma2i2FQ9QE0bBFWUYYy5snGql/ghdkDEyKsJ7N6EE4yquIB7eXTyKo0fZFN98bgM0GY+oZbbq73jd3tmRH0dbO67Oxk6Gz9mzuSzNRpBksovwXZSkK4yxeKW3ALdaAts+aeV7Actqz0KySTbdZO2htBmpGis2m1lNq+fRzb5+Nqnx/4wTEhzEzMLjbQ==; tag_view_ranking=4TDL3X7bV9~jpIZPQ502H~fqoLWl17eh~zj9gD1HFwG~PwDMGzD6xn~vNpvefPsAB~uusOs0ipBx~yOqOtdektt~0sVgHoAwbd~qVjnJnSnAY~0xsDLqCEW6~cjsAyvz-bf~7OHNI0Gq-U~TFDu872vC0~RcahSSzeRf~FqVQndhufZ~Lt-oEicbBr~skx_-I2o4Y~WTz8QdIkZx~3cT9FM3R6t~LTW5GJcQwW~ETjPkL0e6r~qiO14cZMBI~zKLqKSPEAG~PFZpGHvD7Z~w6DOLSTOSN~faHcYIP1U0~mLrrjwTHBm~85bv9GYk84~Nqn2kKfM8q~zLYdlsj4Z9~QKeXYK2oSR~RTJMXD26Ak~iqLNss09Jd~hLeD_GxVsq~TaUYlgH_jM~JN2fNJ_Ue2~oCR2Pbz1ly~qWFESUmfEs~FySY6ZVB78~im3usT8hyU~t2ErccCFR9~jhuUT0OJva~WVrsHleeCL~tgP8r-gOe_~r_Jjn6Ua2V~ZBoVMjk2oM~dCMKBh0255~QxZFRkLR1E~2PzZzrnP0p~dqqWNpq7ul~zqe8dqUBGC~eZvMiRfsU3~LVSDGaCAdn~2-q1CV6LVL~AKT2U2P4W6~xufWQ15ZA3~F0-f08C1cg~YThJ5b-nhQ~eVxus64GZU~Cp5keYns6b~g0_XDQP_lq~YopcpQgQvo~wnGN3ZYkde~f-c_0dUV8c~VycxboLmxz~HY55MqmzzQ~QaiOjmwQnI~CrFcrMFJzz~plqXT5B4--~CiSfl_AE0h~-StjcwdYwv~X7o4FygncP~Xs-7j6fVPs~LJo91uBPz4~Jxg8TkZQdK~1LN8nwTqf_~GxEzX1Shma~A3wgamEIOQ~UdsOa6tZrT~cFYMvUloX0~0Q_7F0H35Y~klRGBoZBqU~rNs-bh_gk3~MhuNMsFpmN~Ie2c51_4Sp~5oPIfUbtd6~BtvmzyZ2Eh~zZZn32I7eS~rOnsP2Q5UN~6Bbq5MJhFe~leIwAgTj8E~bMWjDZvVht~UZootLOo57~Sbp1gmMeRy~f89C7fWBcE~MM6RXH_rlN~WLDE0_23UO~WCXA6OxHJa~6n5sWl9nNm; __utmb=235335808.10.10.1641805707; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:34'
                }
        return headers
    def head2(self):
        headers2 = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
                    'referer': '',
                    'sec-fetch-dest': 'image',
                    'sec-fetch-mode': 'no-cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': UserAgent(min_version=50, max_version=80).random,
                    'cookie': 'first_visit_datetime_pc=2022-01-06+13:10:18; p_ab_id=2; p_ab_id_2=6; p_ab_d_id=2017070122; __utmz=235335808.1641442221.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); yuid_b=IYh3WFA; _fbp=fb.1.1641442226524.867865018; _ga=GA1.2.1011429997.1641442221; PHPSESSID=36658176_Ik0UZUIinN2UVDtZ36wumEICitKYpfnS; device_token=6046abf27dcad150c035e997e31999ad; c_type=21; privacy_policy_notification=0; a_type=0; b_type=0; login_ever=yes; _gcl_au=1.1.124382889.1641442357; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^6=user_id=36658176=1^9=p_ab_id=2=1^10=p_ab_id_2=6=1^11=lang=zh=1; privacy_policy_agreement=3; adr_id=FK6Oc3ZcVqzvyo46F6J3iDLM8Q2aeqVM7joFuZvcldMOmWQd; _im_vid=01FRPSTPREG77BWCGWF0TAWWHS; p_b_type=1; _im_uid.3929=b.6dd7c319e074b4f8; __utmc=235335808; tags_sended=1; categorized_tags=IVwLyT8B6k~RcahSSzeRf~_-agXPKuAQ~qiO14cZMBI; _gid=GA1.2.149545487.1641800553; __utma=235335808.1011429997.1641442221.1641800539.1641805707.10; __utmt=1; __cf_bm=IjpztpOQs3g87bPZvauxL7sWuWQHDZ4RQcR1btSMTrc-1641807660-0-AWvQ1Wgma2i2FQ9QE0bBFWUYYy5snGql/ghdkDEyKsJ7N6EE4yquIB7eXTyKo0fZFN98bgM0GY+oZbbq73jd3tmRH0dbO67Oxk6Gz9mzuSzNRpBksovwXZSkK4yxeKW3ALdaAts+aeV7Actqz0KySTbdZO2htBmpGis2m1lNq+fRzb5+Nqnx/4wTEhzEzMLjbQ==; tag_view_ranking=4TDL3X7bV9~jpIZPQ502H~fqoLWl17eh~zj9gD1HFwG~PwDMGzD6xn~vNpvefPsAB~uusOs0ipBx~yOqOtdektt~0sVgHoAwbd~qVjnJnSnAY~0xsDLqCEW6~cjsAyvz-bf~7OHNI0Gq-U~TFDu872vC0~RcahSSzeRf~FqVQndhufZ~Lt-oEicbBr~skx_-I2o4Y~WTz8QdIkZx~3cT9FM3R6t~LTW5GJcQwW~ETjPkL0e6r~qiO14cZMBI~zKLqKSPEAG~PFZpGHvD7Z~w6DOLSTOSN~faHcYIP1U0~mLrrjwTHBm~85bv9GYk84~Nqn2kKfM8q~zLYdlsj4Z9~QKeXYK2oSR~RTJMXD26Ak~iqLNss09Jd~hLeD_GxVsq~TaUYlgH_jM~JN2fNJ_Ue2~oCR2Pbz1ly~qWFESUmfEs~FySY6ZVB78~im3usT8hyU~t2ErccCFR9~jhuUT0OJva~WVrsHleeCL~tgP8r-gOe_~r_Jjn6Ua2V~ZBoVMjk2oM~dCMKBh0255~QxZFRkLR1E~2PzZzrnP0p~dqqWNpq7ul~zqe8dqUBGC~eZvMiRfsU3~LVSDGaCAdn~2-q1CV6LVL~AKT2U2P4W6~xufWQ15ZA3~F0-f08C1cg~YThJ5b-nhQ~eVxus64GZU~Cp5keYns6b~g0_XDQP_lq~YopcpQgQvo~wnGN3ZYkde~f-c_0dUV8c~VycxboLmxz~HY55MqmzzQ~QaiOjmwQnI~CrFcrMFJzz~plqXT5B4--~CiSfl_AE0h~-StjcwdYwv~X7o4FygncP~Xs-7j6fVPs~LJo91uBPz4~Jxg8TkZQdK~1LN8nwTqf_~GxEzX1Shma~A3wgamEIOQ~UdsOa6tZrT~cFYMvUloX0~0Q_7F0H35Y~klRGBoZBqU~rNs-bh_gk3~MhuNMsFpmN~Ie2c51_4Sp~5oPIfUbtd6~BtvmzyZ2Eh~zZZn32I7eS~rOnsP2Q5UN~6Bbq5MJhFe~leIwAgTj8E~bMWjDZvVht~UZootLOo57~Sbp1gmMeRy~f89C7fWBcE~MM6RXH_rlN~WLDE0_23UO~WCXA6OxHJa~6n5sWl9nNm; __utmb=235335808.10.10.1641805707; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:34'

                    }
        return headers2





