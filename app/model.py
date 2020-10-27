class ApiResponse:

    ERROR_KEY = 'error'
    ERROR_MESSAGE_EN_KEY = 'message_en'
    DATA_KEY = 'data'
    PAGINATION_KEY = 'pagination'
    NEXT_PAGE_KEY = 'next'

    def __init__(self, body):
        self.body = body

    def get_next_page(self):
        next = None
        if ApiResponse.PAGINATION_KEY in self.body:
            pagination = self.body[ApiResponse.PAGINATION_KEY]
            if pagination and ApiResponse.NEXT_PAGE_KEY in pagination:
                next = pagination[ApiResponse.NEXT_PAGE_KEY]
        return next

    def get_data(self):
        data = None
        if ApiResponse.DATA_KEY in self.body:
            data = self.body[ApiResponse.DATA_KEY]
        return data

    def get_error_msg(self):
        error_msg = None
        if ApiResponse.ERROR_KEY in self.body:
            error = self.body[ApiResponse.ERROR_KEY]
            if error and ApiResponse.ERROR_MESSAGE_EN_KEY in error:
                error_msg = error[ApiResponse.ERROR_MESSAGE_EN_KEY]
        return error_msg
