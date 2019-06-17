# coding: utf-8

"""
    HEP REST API

    The REST API for HEP protocol  # noqa: E501

    OpenAPI spec version: v1
    Contact: xiawu@zeuux.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PayCacheResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dapp_key': 'str',
        'protocol': 'str',
        'version': 'str',
        'ts': 'int',
        'nonce': 'str',
        'os': 'str',
        'language': 'str',
        'dapp_signature_method': 'str',
        'dapp_signature': 'str',
        'sign_type': 'str',
        'signature': 'str',
        'uuid': 'str',
        'dapp_id': 'str',
        'action': 'str',
        'expired': 'int',
        'description': 'str',
        'price_currency': 'str',
        'total_price': 'str',
        'order_number': 'str',
        'seller': 'str',
        'customer': 'str',
        'broker': 'str'
    }

    attribute_map = {
        'dapp_key': 'dapp_key',
        'protocol': 'protocol',
        'version': 'version',
        'ts': 'ts',
        'nonce': 'nonce',
        'os': 'os',
        'language': 'language',
        'dapp_signature_method': 'dapp_signature_method',
        'dapp_signature': 'dapp_signature',
        'sign_type': 'sign_type',
        'signature': 'signature',
        'uuid': 'uuid',
        'dapp_id': 'dapp_id',
        'action': 'action',
        'expired': 'expired',
        'description': 'description',
        'price_currency': 'price_currency',
        'total_price': 'total_price',
        'order_number': 'order_number',
        'seller': 'seller',
        'customer': 'customer',
        'broker': 'broker'
    }

    def __init__(self, dapp_key=None, protocol=None, version=None, ts=None, nonce=None, os=None, language=None, dapp_signature_method=None, dapp_signature=None, sign_type=None, signature=None, uuid=None, dapp_id=None, action=None, expired=None, description=None, price_currency=None, total_price=None, order_number=None, seller=None, customer=None, broker=None):  # noqa: E501
        """PayCacheResponse - a model defined in Swagger"""  # noqa: E501
        self._dapp_key = None
        self._protocol = None
        self._version = None
        self._ts = None
        self._nonce = None
        self._os = None
        self._language = None
        self._dapp_signature_method = None
        self._dapp_signature = None
        self._sign_type = None
        self._signature = None
        self._uuid = None
        self._dapp_id = None
        self._action = None
        self._expired = None
        self._description = None
        self._price_currency = None
        self._total_price = None
        self._order_number = None
        self._seller = None
        self._customer = None
        self._broker = None
        self.discriminator = None
        self.dapp_key = dapp_key
        self.protocol = protocol
        self.version = version
        self.ts = ts
        self.nonce = nonce
        self.os = os
        self.language = language
        self.dapp_signature_method = dapp_signature_method
        self.dapp_signature = dapp_signature
        self.sign_type = sign_type
        self.signature = signature
        self.uuid = uuid
        self.dapp_id = dapp_id
        self.action = action
        self.expired = expired
        self.description = description
        self.price_currency = price_currency
        self.total_price = total_price
        self.order_number = order_number
        self.seller = seller
        self.customer = customer
        if broker is not None:
            self.broker = broker

    @property
    def dapp_key(self):
        """Gets the dapp_key of this PayCacheResponse.  # noqa: E501

        The decentralized application access key  # noqa: E501

        :return: The dapp_key of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_key

    @dapp_key.setter
    def dapp_key(self, dapp_key):
        """Sets the dapp_key of this PayCacheResponse.

        The decentralized application access key  # noqa: E501

        :param dapp_key: The dapp_key of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if dapp_key is None:
            raise ValueError("Invalid value for `dapp_key`, must not be `None`")  # noqa: E501

        self._dapp_key = dapp_key

    @property
    def protocol(self):
        """Gets the protocol of this PayCacheResponse.  # noqa: E501

        The protocol name. default is 'HEP'.  # noqa: E501

        :return: The protocol of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PayCacheResponse.

        The protocol name. default is 'HEP'.  # noqa: E501

        :param protocol: The protocol of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self):
        """Gets the version of this PayCacheResponse.  # noqa: E501

        The protocol version such as '1.0'  # noqa: E501

        :return: The version of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PayCacheResponse.

        The protocol version such as '1.0'  # noqa: E501

        :param version: The version of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def ts(self):
        """Gets the ts of this PayCacheResponse.  # noqa: E501

        The current timestamp  # noqa: E501

        :return: The ts of this PayCacheResponse.  # noqa: E501
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this PayCacheResponse.

        The current timestamp  # noqa: E501

        :param ts: The ts of this PayCacheResponse.  # noqa: E501
        :type: int
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def nonce(self):
        """Gets the nonce of this PayCacheResponse.  # noqa: E501

        The random string or auto-increment sequence  # noqa: E501

        :return: The nonce of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this PayCacheResponse.

        The random string or auto-increment sequence  # noqa: E501

        :param nonce: The nonce of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def os(self):
        """Gets the os of this PayCacheResponse.  # noqa: E501

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :return: The os of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PayCacheResponse.

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :param os: The os of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def language(self):
        """Gets the language of this PayCacheResponse.  # noqa: E501

        The i18n language code such as zh, en, etc.  # noqa: E501

        :return: The language of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PayCacheResponse.

        The i18n language code such as zh, en, etc.  # noqa: E501

        :param language: The language of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def dapp_signature_method(self):
        """Gets the dapp_signature_method of this PayCacheResponse.  # noqa: E501

        The signature method used by dapp.  # noqa: E501

        :return: The dapp_signature_method of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature_method

    @dapp_signature_method.setter
    def dapp_signature_method(self, dapp_signature_method):
        """Sets the dapp_signature_method of this PayCacheResponse.

        The signature method used by dapp.  # noqa: E501

        :param dapp_signature_method: The dapp_signature_method of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if dapp_signature_method is None:
            raise ValueError("Invalid value for `dapp_signature_method`, must not be `None`")  # noqa: E501

        self._dapp_signature_method = dapp_signature_method

    @property
    def dapp_signature(self):
        """Gets the dapp_signature of this PayCacheResponse.  # noqa: E501

        The signature generated by dapp.  # noqa: E501

        :return: The dapp_signature of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature

    @dapp_signature.setter
    def dapp_signature(self, dapp_signature):
        """Sets the dapp_signature of this PayCacheResponse.

        The signature generated by dapp.  # noqa: E501

        :param dapp_signature: The dapp_signature of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if dapp_signature is None:
            raise ValueError("Invalid value for `dapp_signature`, must not be `None`")  # noqa: E501

        self._dapp_signature = dapp_signature

    @property
    def sign_type(self):
        """Gets the sign_type of this PayCacheResponse.  # noqa: E501

        The signature Type,aka cryptographic algorithm.  # noqa: E501

        :return: The sign_type of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this PayCacheResponse.

        The signature Type,aka cryptographic algorithm.  # noqa: E501

        :param sign_type: The sign_type of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if sign_type is None:
            raise ValueError("Invalid value for `sign_type`, must not be `None`")  # noqa: E501

        self._sign_type = sign_type

    @property
    def signature(self):
        """Gets the signature of this PayCacheResponse.  # noqa: E501

        The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].  # noqa: E501

        :return: The signature of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this PayCacheResponse.

        The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].  # noqa: E501

        :param signature: The signature of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def uuid(self):
        """Gets the uuid of this PayCacheResponse.  # noqa: E501

        The request uuid  # noqa: E501

        :return: The uuid of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PayCacheResponse.

        The request uuid  # noqa: E501

        :param uuid: The uuid of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def dapp_id(self):
        """Gets the dapp_id of this PayCacheResponse.  # noqa: E501

        The decentralized application ID  # noqa: E501

        :return: The dapp_id of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_id

    @dapp_id.setter
    def dapp_id(self, dapp_id):
        """Sets the dapp_id of this PayCacheResponse.

        The decentralized application ID  # noqa: E501

        :param dapp_id: The dapp_id of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if dapp_id is None:
            raise ValueError("Invalid value for `dapp_id`, must not be `None`")  # noqa: E501

        self._dapp_id = dapp_id

    @property
    def action(self):
        """Gets the action of this PayCacheResponse.  # noqa: E501

        The action name which value is 'hep.pay.order'  # noqa: E501

        :return: The action of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PayCacheResponse.

        The action name which value is 'hep.pay.order'  # noqa: E501

        :param action: The action of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def expired(self):
        """Gets the expired of this PayCacheResponse.  # noqa: E501

        The expired timestamp  # noqa: E501

        :return: The expired of this PayCacheResponse.  # noqa: E501
        :rtype: int
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this PayCacheResponse.

        The expired timestamp  # noqa: E501

        :param expired: The expired of this PayCacheResponse.  # noqa: E501
        :type: int
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    @property
    def description(self):
        """Gets the description of this PayCacheResponse.  # noqa: E501

        The order description  # noqa: E501

        :return: The description of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PayCacheResponse.

        The order description  # noqa: E501

        :param description: The description of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def price_currency(self):
        """Gets the price_currency of this PayCacheResponse.  # noqa: E501

        The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.  # noqa: E501

        :return: The price_currency of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, price_currency):
        """Sets the price_currency of this PayCacheResponse.

        The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.  # noqa: E501

        :param price_currency: The price_currency of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if price_currency is None:
            raise ValueError("Invalid value for `price_currency`, must not be `None`")  # noqa: E501

        self._price_currency = price_currency

    @property
    def total_price(self):
        """Gets the total_price of this PayCacheResponse.  # noqa: E501

        The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.  # noqa: E501

        :return: The total_price of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this PayCacheResponse.

        The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.  # noqa: E501

        :param total_price: The total_price of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if total_price is None:
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501

        self._total_price = total_price

    @property
    def order_number(self):
        """Gets the order_number of this PayCacheResponse.  # noqa: E501

        The order number  # noqa: E501

        :return: The order_number of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this PayCacheResponse.

        The order number  # noqa: E501

        :param order_number: The order_number of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if order_number is None:
            raise ValueError("Invalid value for `order_number`, must not be `None`")  # noqa: E501

        self._order_number = order_number

    @property
    def seller(self):
        """Gets the seller of this PayCacheResponse.  # noqa: E501

        The seller's NewID  # noqa: E501

        :return: The seller of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this PayCacheResponse.

        The seller's NewID  # noqa: E501

        :param seller: The seller of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if seller is None:
            raise ValueError("Invalid value for `seller`, must not be `None`")  # noqa: E501

        self._seller = seller

    @property
    def customer(self):
        """Gets the customer of this PayCacheResponse.  # noqa: E501

        The customer's NewID  # noqa: E501

        :return: The customer of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PayCacheResponse.

        The customer's NewID  # noqa: E501

        :param customer: The customer of this PayCacheResponse.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def broker(self):
        """Gets the broker of this PayCacheResponse.  # noqa: E501

        The broker's NewID. optional.  # noqa: E501

        :return: The broker of this PayCacheResponse.  # noqa: E501
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this PayCacheResponse.

        The broker's NewID. optional.  # noqa: E501

        :param broker: The broker of this PayCacheResponse.  # noqa: E501
        :type: str
        """

        self._broker = broker

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PayCacheResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayCacheResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
