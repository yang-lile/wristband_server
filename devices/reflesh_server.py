import httpx
from fake_useragent import UserAgent
# import time
# import logging
# from datetime import datetime
# import sched


class data_collection:
    curTimestamp: int
    baseUrl: str = "http://yunxin.device.guangbao-uni.com:61101/"

    def checkDeviceList(self):
        # 获取设备列表
        response = httpx.get("{}/clients".format(self.baseUrl),
                             headers={"User-Agent": UserAgent().random}, follow_redirects=True,)

        if response.status_code == 200:
            # print(response.text)
            return response.text

    def deviceState(self, uid):
        # 
        respone = httpx.get("{}/client/state/{}".format(self.baseUrl, uid),
                            headers={"User-Agent": UserAgent().random}, follow_redirects=True,)

        if respone.status_code == 200:
            return respone.text

    def deviceHeartRate(self, uid):
        respone = httpx.get("{}/client/heartrate/{}".format(self.baseUrl, uid),
                                  headers={"User-Agent": UserAgent().random}, follow_redirects=True, timeout=60,)

        if respone.status_code == 200:
            return respone.text

    def deviceBlood(self, uid):
        respone = httpx.get("{}/client/blood/{}".format(self.baseUrl, uid),
                                  headers={"User-Agent": UserAgent().random}, follow_redirects=True, timeout=60,)

        if respone.status_code == 200:
            return respone.text

    def deviceOxStart(self, uid):
        respone = httpx.get("{}/client/oxstart/{}".format(self.baseUrl, uid),
                                  headers={"User-Agent": UserAgent().random}, follow_redirects=True, timeout=60,)

        if respone.status_code == 200:
            return respone.text

    def deviceLocation(self, uid):
        pass

    # def startLoop(self):
    #     s = sched.scheduler(time.time, time.sleep)
    #     s.enter(5, 1, self.checkDeviceList, ())
    #     s.run()
