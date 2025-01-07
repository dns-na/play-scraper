from abc import ABC, abstractmethod

PLAY_STORE_BASE_URL = "https://play.google.com"


class Format(ABC):
    @abstractmethod
    def build(self, *args):
        raise NotImplementedError

    @abstractmethod
    def build_body(self, *args):
        raise NotImplementedError


class Formats:
    class _Detail(Format):
        URL_FORMAT = (
            "{}/store/apps/details?id={{app_id}}&hl={{lang}}&gl={{country}}".format(
                PLAY_STORE_BASE_URL
            )
        )
        FALLBACK_URL_FORMAT = "{}/store/apps/details?id={{app_id}}&hl={{lang}}".format(
            PLAY_STORE_BASE_URL
        )

        def build(self, app_id: str, lang: str, country: str) -> str:
            return self.URL_FORMAT.format(app_id=app_id, lang=lang, country=country)

        def fallback_build(self, app_id: str, lang: str) -> str:
            return self.FALLBACK_URL_FORMAT.format(app_id=app_id, lang=lang)

        def build_body(self, *args):
            return None

    class _Similar(Format):
        URL_FORMAT = (
            "{}/_/PlayStoreUi/data/batchexecute?rpcids=CLXjtf%2CA6yuRe%2CWs7gDc%2CZittHe%2Cag2B9c%2Ce7uDs%2CoCPfdb&source-path=%2Fstore%2Fapps%2Fdetails&f.sid=-6820885803383552233&bl=boq_playuiserver_20241007.10_p0&hl=en-US&authuser&soc-app=121&soc-platform=1&soc-device=1&_reqid=575098&rt=c".format(
                PLAY_STORE_BASE_URL
            )
        )

        URL_SECOND_FORMAT = (
            "{}/store/apps/collection/cluster?gsr={{gsr}}".format(
                PLAY_STORE_BASE_URL
            )
        )

        def build(self) -> str:
            return self.URL_FORMAT.format()

        PAYLOAD_FORMAT = "f.req=%5B%5B%5B%22CLXjtf%22%2C%22%5B%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%221%22%5D%2C%5B%22A6yuRe%22%2C%22%5B%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%223%22%5D%2C%5B%22Ws7gDc%22%2C%22%5Bnull%2Cnull%2C%5B%5B1%2C9%2C10%2C11%2C13%2C14%2C19%2C20%2C38%2C43%2C47%2C49%2C52%2C58%2C59%2C63%2C69%2C70%2C73%2C74%2C75%2C78%2C79%2C80%2C91%2C92%2C95%2C96%2C97%2C100%2C101%2C103%2C106%2C112%2C119%2C129%2C137%2C139%2C141%2C145%2C146%2C151%2C155%2C169%5D%5D%2C%5B%5B%5B1%2Cnull%2C1%5D%2Cnull%2C%5B%5B%5B%5D%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C2%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5B%5B%5D%5D%5D%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5B%5B%5D%5D%5D%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C%5B%5B%5B%5D%5D%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B%5B%5B%5D%5D%5D%5D%2C%5B%5B%5B%5B%5D%5D%5D%5D%5D%2Cnull%2C%5B%5B%5C%22{app_id}%5C%22%2C7%5D%5D%5D%22%2Cnull%2C%225%22%5D%2C%5B%22ZittHe%22%2C%22%5B%5Bnull%2C%5B%5B3%2C%5B10%5D%5D%2Cnull%2Cnull%2C%5B184%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%5D%22%2Cnull%2C%227%22%5D%2C%5B%22ag2B9c%22%2C%22%5B%5Bnull%2C%5B%5C%22{app_id}%5C%22%2C7%5D%2Cnull%2C%5B%5B3%2C%5B6%5D%5D%2Cnull%2Cnull%2C%5B1%2C8%5D%5D%5D%2C%5B1%5D%5D%22%2Cnull%2C%229%22%5D%2C%5B%22e7uDs%22%2C%22%5B%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%2211%22%5D%2C%5B%22Ws7gDc%22%2C%22%5Bnull%2Cnull%2C%5B%5B52%5D%5D%2C%5B%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B2%5D%5D%5D%2Cnull%2C%5B%5B%5C%22{app_id}%5C%22%2C7%5D%5D%5D%22%2Cnull%2C%2213%22%5D%2C%5B%22oCPfdb%22%2C%22%5Bnull%2C%5B2%2Cnull%2C%5B20%5D%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%2215%22%5D%5D%5D&"

        def build_body(
            self,
            app_id: str
        ) -> bytes:
            result = self.PAYLOAD_FORMAT.format(app_id=app_id)
            return result.encode()

        def build_second(self,gsr: str) -> str:
            return self.URL_SECOND_FORMAT.format(gsr=gsr)


    class _Reviews(Format):
        URL_FORMAT = (
            "{}/_/PlayStoreUi/data/batchexecute?hl={{lang}}&gl={{country}}".format(
                PLAY_STORE_BASE_URL
            )
        )

        def build(self, lang: str, country: str) -> str:
            return self.URL_FORMAT.format(lang=lang, country=country)

        PAYLOAD_FORMAT_FOR_FIRST_PAGE = "f.req=%5B%5B%5B%22oCPfdb%22%2C%22%5Bnull%2C%5B2%2C{sort}%2C%5B{count}%5D%2Cnull%2C%5Bnull%2C{score}%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C{device_id}%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D%0A"
        PAYLOAD_FORMAT_FOR_PAGINATED_PAGE = "f.req=%5B%5B%5B%22oCPfdb%22%2C%22%5Bnull%2C%5B2%2C{sort}%2C%5B{count}%2Cnull%2C%5C%22{pagination_token}%5C%22%5D%2Cnull%2C%5Bnull%2C{score}%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C{device_id}%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D%0A"

        def build_body(
            self,
            app_id: str,
            sort: int,
            count: int,
            filter_score_with: int,
            filter_device_with: int,
            pagination_token: str,
        ) -> bytes:
            if pagination_token is not None:
                result = self.PAYLOAD_FORMAT_FOR_PAGINATED_PAGE.format(
                    app_id=app_id,
                    sort=sort,
                    count=count,
                    score=filter_score_with,
                    device_id=filter_device_with,
                    pagination_token=pagination_token,
                )
            else:
                result = self.PAYLOAD_FORMAT_FOR_FIRST_PAGE.format(
                    app_id=app_id,
                    sort=sort,
                    count=count,
                    score=filter_score_with,
                    device_id=filter_device_with,
                )
            return result.encode()

    class _Permissions(Format):
        URL_FORMAT = (
            "{}/_/PlayStoreUi/data/batchexecute?hl={{lang}}&gl={{country}}".format(
                PLAY_STORE_BASE_URL
            )
        )

        def build(self, lang: str, country: str) -> str:
            return self.URL_FORMAT.format(lang=lang, country=country)

        PAYLOAD_FORMAT_FOR_PERMISSION = "f.req=%5B%5B%5B%22xdSrCf%22%2C%22%5B%5Bnull%2C%5B%5C%22{app_id}%5C%22%2C7%5D%2C%5B%5D%5D%5D%22%2Cnull%2C%221%22%5D%5D%5D"

        def build_body(self, app_id: str) -> bytes:
            result = self.PAYLOAD_FORMAT_FOR_PERMISSION.format(app_id=app_id)

            return result.encode()

    class _Searchresults(Format):
        URL_FORMAT = (
            "{}/store/search?q={{query}}&c=apps&hl={{lang}}&gl={{country}}".format(
                PLAY_STORE_BASE_URL
            )
        )
        FALLBACK_URL_FORMAT = "{}/store/search?q={{query}}&c=apps&hl={{lang}}".format(
            PLAY_STORE_BASE_URL
        )

        def build(self, query: str, lang: str, country: str) -> str:
            return self.URL_FORMAT.format(query=query, lang=lang, country=country)

        def fallback_build(self, query: str, lang: str) -> str:
            return self.FALLBACK_URL_FORMAT.format(query=query, lang=lang)

        def build_body(self, *args):
            return None

    Detail = _Detail()
    Reviews = _Reviews()
    Permissions = _Permissions()
    Similar = _Similar()
    Searchresults = _Searchresults()
