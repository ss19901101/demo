# coding: utf-8

"""
    demo

    this is a demo for device manager  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Device(object):
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
        'id': 'int',
        'esn': 'int',
        'device_name': 'str',
        'device_type': 'int',
        'status': 'int',
        'interfaces': 'list[Interface]'
    }

    attribute_map = {
        'id': 'id',
        'esn': 'esn',
        'device_name': 'device_name',
        'device_type': 'device_type',
        'status': 'status',
        'interfaces': 'interfaces'
    }

    def __init__(self, id=None, esn=None, device_name=None, device_type=None, status=None, interfaces=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._esn = None
        self._device_name = None
        self._device_type = None
        self._status = None
        self._interfaces = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if esn is not None:
            self.esn = esn
        if device_name is not None:
            self.device_name = device_name
        if device_type is not None:
            self.device_type = device_type
        if status is not None:
            self.status = status
        if interfaces is not None:
            self.interfaces = interfaces

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def esn(self):
        """Gets the esn of this Device.  # noqa: E501


        :return: The esn of this Device.  # noqa: E501
        :rtype: int
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this Device.


        :param esn: The esn of this Device.  # noqa: E501
        :type: int
        """

        self._esn = esn

    @property
    def device_name(self):
        """Gets the device_name of this Device.  # noqa: E501


        :return: The device_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this Device.


        :param device_name: The device_name of this Device.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def device_type(self):
        """Gets the device_type of this Device.  # noqa: E501


        :return: The device_type of this Device.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Device.


        :param device_type: The device_type of this Device.  # noqa: E501
        :type: int
        """

        self._device_type = device_type

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501


        :return: The status of this Device.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.


        :param status: The status of this Device.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def interfaces(self):
        """Gets the interfaces of this Device.  # noqa: E501


        :return: The interfaces of this Device.  # noqa: E501
        :rtype: list[Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this Device.


        :param interfaces: The interfaces of this Device.  # noqa: E501
        :type: list[Interface]
        """

        self._interfaces = interfaces

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
