from requests import Session

from bynder_sdk.util import SessionMixin, UA_HEADER


class PermanentTokenSession(SessionMixin, Session):
    def __init__(self, bynder_domain, permanent_token):
        super().__init__()

        self.bynder_domain = bynder_domain
        self.headers.update({
            'Authorization': 'Bearer {}'.format(permanent_token),
        })

        self._set_ua_header()
