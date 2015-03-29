__author__ = 'vladymyr'
 # coding=utf8


import unittest
from CompArcLab1 import MyXmlParser
from CompArcLab1 import conf
import xml.etree.ElementTree as ET

test_file_path = "/home/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/UnitTest/Test.py"



class MyTest(unittest.TestCase):
    def test_getUrlPath(self):
        str = conf.getUrlPath()
        self.assertEqual(str, '/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/source/urls_uk.xml')

    def test_InfoPath(self):
        str = conf.getInfoPath()
        self.assertEqual(str, '/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/gns/data_uk.txt')


    def test_getDirectChildrenTagText(self):
        xmlParser = MyXmlParser.myXMLParser('/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/source/urls_uk.xml')
        urlList = xmlParser.getDirectChildrenTagText("url")
        self.assertEqual(len(urlList), 6)
        self.assertEqual(urlList[0], ('http://www.npr.org/rss/rss.php?id=1004', 'npr'))

    def test_searchForInfo(self):
        xmlParser = MyXmlParser.myXMLParser('/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/source/urls_uk.xml')
        file = open('MyTestRSS.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , True)

        xmlParser = MyXmlParser.myXMLParser('/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/source/urls_uk.xml')
        file = open('MyTestRSS2.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , False)


    def test_findWholeWord(self):
        xmlParser = MyXmlParser.myXMLParser('/home/roman/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/source/urls_uk.xml')
        res = xmlParser.findWholeWord('word')('one ttt word')
        res = xmlParser.findWholeWord(u'Крым')(u'Крым')
        self.assertTrue(xmlParser.findWholeWord('word')('one ttt word'))
        self.assertFalse(xmlParser.findWholeWord(u'Крым')(u'one ttt word'))
        self.assertTrue(xmlParser.findWholeWord(u'Крым')(u'one Крым word'))
        self.assertFalse(xmlParser.findWholeWord('word')('one ttt '))

