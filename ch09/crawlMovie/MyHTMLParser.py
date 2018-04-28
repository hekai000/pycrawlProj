# -*- coding: utf-8 -*-
import re
import json

class MyHTMLParser(object):

    def parser_url(self, response):
        if response is None:
            return
        pattern = re.compile(r"(http://movie.mtime.com/(\d+)/)")
        urls = pattern.findall(response)
        if urls:
            return list(set(urls))
        return None

    def parser_json(self, page_url, response):
        pattern = re.compile(r"=(.*?);")
        result = pattern.findall(response)[0]
        if result:
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print e
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, isRelease = 2)
            else:
                return self._parser_no_release(page_url, value)

    def _parser_release(self, page_url, value):
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')
            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice = boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
            ShowDays = boxOffice.get('ShowDays')

            try:
                Rank = boxOffice.get("Rank")
            except Exception as e:
                Rank = 0
            return (MovieId, movieTitle, RatingFinal, ROtherFinal,
                    RPictureFinal, RDirectorFinal, RStoryFinal,
                    Usercount, AttitudeCount, TotalBoxOffice+TotalBoxOfficeUnit,
                    TodayBoxOffice+TodayBoxOfficeUnit, Rank, ShowDays, isRelease)
        except Exception as e:
            print "parse json release occure error[%s]" % str(e)
            print "parse json release value [%s]" % str(value)
            print "parse json release url [%s]" % str(url)
            return None

    def _parser_no_release(self, page_url, value, isRelease = 0):
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            try:
                Rank = value.get("value").get("hotValue").get("Ranking")
            except Exception as e:
                Rank = 0
            return (MovieId, movieTitle, RatingFinal, ROtherFinal,
                    RPictureFinal, RDirectorFinal, RStoryFinal,
                    Usercount, AttitudeCount, u'无',u'无', Rank, 0, isRelease)
        except Exception as e:
            print "parse json release occure error[%s]" % str(e)
            print "parse json release value [%s]" % str(value)
            print "parse json release url [%s]" % str(url)
            return None


if __name__ == "__main__":
    import requests
    url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers, verify=False)
    htmlParser = MyHTMLParser()
    new_url, new_data = htmlParser.parser(url, r.text)
    print new_url
    print new_data