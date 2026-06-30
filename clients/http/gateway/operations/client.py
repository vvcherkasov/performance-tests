from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsSummaryResponseSchema,
    GetOperationResponseSchema,
    GetOperationsResponseSchema,
    GetOperationsQuerySchema,
    GetOperationReceiptResponseSchema,
    GetOperationsSummaryQuerySchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakePurchaseOperationRequestSchema
)

class OperationsGatewayHTTPClient(HTTPClient):
    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            '/api/v1/operations',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета

        :param query: Словарь с параметрами запроса
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            '/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными для операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-fee-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными для операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-top-up-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с данными для операции кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-cashback-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными для операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-transfer-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с данными для операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-purchase-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными для операции оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-bill-payment-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с данными для операции снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-cash-withdrawal-operation',
            json=request.model_dump(by_alias=True)
        )

    def get_operation(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operations(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            cardId= card_id,
            accountId= account_id
        )
        response = self.make_fee_operation_api(request=request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request=request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request=request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request=request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_purchase_operation_api(request=request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request=request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request=request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())