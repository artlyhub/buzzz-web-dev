
from datetime import datetime
from selenium import webdriver
import pyautogui
import os
from bs4 import BeautifulSoup
import requests
import time


class KRX:
    def __init__(self):
        self.driver = webdriver.Firefox()
    #사이트 접속
    def accessToKRX(self):
        self.driver.get('http://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage')
        time.sleep(4)

    #코스피/코스닥 항목 검색
    def search(self, btn_id):
        btn = self.driver.find_element_by_id(btn_id)
        btn.click()
        self.driver.execute_script('fnSearchWithoutIndex();') #검색 버튼
        time.sleep(3)

    #코스피 엑셀 파일 다운로드
    def downloadKospi(self):
        self.driver.execute_script('fnDownload();')
        time.sleep(4)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
    #코스닥 엑셀 파일 다운로드
    def downloadKosdaq(self):
        self.driver.execute_script('fnDownload();')
        time.sleep(4)
        pyautogui.press('enter')


class GetEvents():

    #다운로드 폴더로 이동
    def moveToFileDirection(self):
        os.chdir(self.downLoadPath)

    #xls -> txt 변환
    def changeToTxt(self, fileName):
        if (os.path.isfile(fileName) and fileName == "상장법인목록.xls" ):
            os.rename(fileName, 'KOSPI.txt')
        elif (os.path.isfile(fileName) and fileName == "상장법인목록(1).xls"):
            os.rename(fileName, 'KOSDAQ.txt')

    #파일 열기
    def openFile(self, fileName):
        self.kospiDoc = open(fileName, "r")
        self.kospiSoup = BeautifulSoup(self.kospiDoc, "html.parser")
    #파일 닫기
    def closeFile(self):
        self.kospiDoc.close()
    #파일 지우기
    def deleteFile(self, fileName):
        os.remove(fileName)

    #회사코드 찾기
    def findCompanyCode(self):
        return self.kospiSoup.select('td[style*="@"]')


class GetKos():
    #회사 정보 가져와서 저장
    def companies(self, date, companyCode, market):
        for i in range(len(companyCode)):
        #save in sqlite
            company = companyCode[i].find_previous_sibling('td').string
            code = companyCode[i].string

def main():

    #오늘의 날짜
    date = datetime.now().strftime('%Y%m%d')


    #코스피, 코스닥 excel 파일 다운로드
    krx = KRX()
    krx.accessToKRX()
    krx.search('rWertpapier')
    krx.downloadKospi()
    krx.search('rKosdaq')
    krx.downloadKosdaq()


    #객체 생성
    event = GetEvents("C:\\Users\\SeheeKim\\Downloads", "C:\\Users\\SeheeKim\\Desktop\\Project\\Project1\\Stock.db")
    kos = GetKos("C:\\Users\\SeheeKim\\Downloads", "C:\\Users\\SeheeKim\\Desktop\\Project\\Project1\\Stock.db")
    yearlyPerformance = GetPerformance("C:\\Users\\SeheeKim\\Downloads", "C:\\Users\\SeheeKim\\Desktop\\Project\\Project1\\Stock.db")
    #다운로드 폴더로 이동
    event.moveToFileDirection()




    ###코스피
    event.changeToTxt('상장법인목록.xls')
    event.openFile('KOSPI.txt')

    #종목별 코드 찾기
    kospiCompanyCode = event.findCompanyCode()

    #코스피 회사명, 회사코드, 종목 저장
    kos.companies(date, kospiCompanyCode, "KP")



    ###코스닥
    event.changeToTxt('상장법인목록(1).xls')
    event.openFile('KOSDAQ.txt')

    #종목별 코드 찾기
    kosdaqCompanyCode = event.findCompanyCode()

    #코스닥 회사명, 회사코드, 종목 저장
    kos.companies(date, kosdaqCompanyCode, "KD")

    #오늘 쓴 파일 지우기
    event.deleteFile('KOSPI.txt')
    event.deleteFile('KOSDAQ.txt')


if __name__=="__main__":
    main()
