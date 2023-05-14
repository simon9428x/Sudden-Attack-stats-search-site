import requests


class SA:
    """
    서든어택 조회 모듈 SA
    """

    def clan_search(self, clanname):
        """
        서든어택 클랜 조회
        """

        try:
            url = f"https://barracks.sa.nexon.com/api/Search/GetSearchClanAll/{clanname}/1"
            req = requests.post(url=url)
        except Exception as e: 
            return {"result" : False, "reason" : f"{e}"}

        if req.status_code != 200:
            return {"result" : False, "reason" : f"{req.status_code} 에러"}
        
        req = req.json()

        if req['result']['total_cnt'] == 0:
            return {"result" : False, "reason" : "존재하지 않는 클랜명 입니다."}

        req = req['result']['clanInfo'][0]['clan_id']

        try:
            url = f"https://barracks.sa.nexon.com/api/ClanHome/GetClanInfo"
            data = {"clan_id": req}
            reqs = requests.post(url=url,json=data)
        except Exception as e: 
            return {"result" : False, "reason" : f"{e}"}
        
        reqs = reqs.json()
        
        return { "result" : True, "ClanInfo" : reqs['resultClanInfo']}

    def name_search(self, username):
        """
        서든어택 닉네임 조회
        """

        try:
            url =  f'https://barracks.sa.nexon.com/api/Search/GetSearchAll/{username}/1'
            req = requests.post(url=url)
        except Exception as e: 
            return {"result" : False, "reason" : f"{e}"}

        if req.status_code != 200:
            return {"result" : False, "reason" : f"{req.status_code} 에러"}

        try:
            req = req.json()['result']['characterInfo'][0]['user_nexon_sn']
        except:
            return {"result" : False, "reason" : "존재하지 않는 닉네임 입니다."}

        response = requests.post(f'https://barracks.sa.nexon.com/api/Profile/GetProfileMain/{str(req)}')
        response = response.json()

        return { "result" : True, "characterInfo" : response['result']}





